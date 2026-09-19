import urllib.request
import urllib.parse
import urllib.error
import json
import ssl
import time
import jwt
from datetime import datetime

_TRACCAR_LOCK = False

@service
def process_traccar_activity():
    global _TRACCAR_LOCK
    
    if _TRACCAR_LOCK:
        log.warning("Debounce active: Activity upload already in progress.")
        return
        
    _TRACCAR_LOCK = True

    try:
        # --- LOAD SECRETS (Injected via Infisical -> secrets.yaml) ---
        import yaml as _yaml
        with open("/config/secrets.yaml", "r") as _sf:
            _secrets = _yaml.safe_load(_sf)
            
        # 1. Fetch UI States
        act_type = state.get("input_select.traccar_log_type")
        harley_behavior = state.get("input_select.traccar_log_harley_behavior")
        loot_found = state.get("input_boolean.traccar_log_loot_found") == "on"
        act_notes = state.get("input_text.traccar_log_notes")
        start_time = state.get("input_datetime.traccar_log_start")
        end_time = state.get("input_datetime.traccar_log_end")

        # Format times for Traccar API using Alberta MDT offset (-06:00)
        start_iso = start_time.replace(" ", "T") + "-06:00"
        end_iso = end_time.replace(" ", "T") + "-06:00"

        # 2. Extract Route Data from Traccar (Raw string injection to bypass urlencode colon stripping)
        traccar_url = f"https://traccar.sythsaz.ca/api/reports/route?deviceId=1&from={start_iso}&to={end_iso}"
        
        # Read Traccar API token from injected secrets
        TRACCAR_TOKEN = _secrets.get("traccar_api_token", "")
        
        req = urllib.request.Request(traccar_url, headers={
            "Authorization": f"Bearer {TRACCAR_TOKEN}", 
            "Accept": "application/json"
        })
        
        ctx = ssl._create_unverified_context()
        
        try:
            response = task.executor(urllib.request.urlopen, req, context=ctx)
            route_data = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            # Send a persistent notification to HA so you can see the exact error text
            error_body = e.read().decode("utf-8")
            err_msg = f"HTTP {e.code}: {error_body}"
            log.error(f"Traccar Fetch Failed: {err_msg} | URL: {traccar_url}")
            service.call("persistent_notification", "create", title="Traccar Fetch Error", message=err_msg)
            return
        except Exception as e:
            log.error(f"Traccar Fetch Failed (Generic): {e}")
            return
            
        # 3. Generate Basic GPX Payload
        gpx_output = '<?xml version="1.0" encoding="UTF-8"?>\n<gpx version="1.1" creator="HomeAssistant Pyscript">\n<trk>\n<trkseg>\n'
        max_speed = 0
        
        for point in route_data:
            lat = point.get("latitude", 0)
            lon = point.get("longitude", 0)
            speed = point.get("speed", 0) * 1.852
            if speed > max_speed: max_speed = speed
            gpx_output += f'<trkpt lat="{lat}" lon="{lon}"></trkpt>\n'
            
        gpx_output += '</trkseg>\n</trk>\n</gpx>'

        # 4. Authenticate & Upload to Google Drive
        folder_map = {
            "Walk": "1LBcvMLfGrPK9oAM_FxeUmNAdIVHlFWxp", 
            "Field Agent": "15gvchdC_PbPDFk-SS0_j2Y_AmwnvPVD1"
        }
        target_folder_id = folder_map.get(act_type, "1vVR9O-pXPyWOBHsY6ydTErFi5UWG9ViX") 
        file_name = f"Traccar_{act_type.replace(' ', '_')}_{start_time.split(' ')[0]}.gpx"
        
        drive_token = None
        
        # --- SERVICE ACCOUNT CREDENTIALS ---
        CLIENT_EMAIL = _secrets.get("gcp_traccar_client_email", "")
        PRIVATE_KEY = _secrets.get("gcp_traccar_private_key", "").replace("\\n", "\n")
        
        # Build & Sign JWT Payload - FORCED FULL DRIVE SCOPE
        payload = {
            "iss": CLIENT_EMAIL,
            "scope": "https://www.googleapis.com/auth/drive",
            "aud": "https://oauth2.googleapis.com/token",
            "iat": int(time.time()),
            "exp": int(time.time()) + 3600
        }
        
        try:
            signed_jwt = jwt.encode(payload, PRIVATE_KEY, algorithm="RS256")
            token_data = urllib.parse.urlencode({
                "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
                "assertion": signed_jwt
            }).encode("utf-8")
            
            token_req = urllib.request.Request("https://oauth2.googleapis.com/token", data=token_data, method="POST")
            token_res = task.executor(urllib.request.urlopen, token_req, context=ctx)
            drive_token = json.loads(token_res.read().decode("utf-8")).get("access_token")
        except Exception as e:
            log.error(f"JWT Token Exchange Failed: {e}")
            return

        if not drive_token:
            log.error("Failed to acquire Google Drive access token.")
            return

        # Execute multipart upload with active Bearer token
        boundary = "gpx_upload_boundary_string"
        metadata = {
            "name": file_name,
            "parents": [target_folder_id]
        }
        
        body = (
            f"--{boundary}\r\n"
            f"Content-Type: application/json; charset=UTF-8\r\n\r\n"
            f"{json.dumps(metadata)}\r\n"
            f"--{boundary}\r\n"
            f"Content-Type: application/gpx+xml\r\n\r\n"
            f"{gpx_output}\r\n"
            f"--{boundary}--\r\n"
        )
        
        drive_req = urllib.request.Request(
            "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
            data=body.encode("utf-8"),
            headers={
                "Authorization": f"Bearer {drive_token}",
                "Content-Type": f"multipart/related; boundary={boundary}"
            },
            method="POST"
        )
        
        try:
            drive_res = task.executor(urllib.request.urlopen, drive_req, context=ctx)
            drive_data = json.loads(drive_res.read().decode("utf-8"))
            uploaded_file_id = drive_data.get("id")
            drive_url = f"https://drive.google.com/open?id={uploaded_file_id}"
        except urllib.error.HTTPError as e:
            # Extract exact Google API JSON error
            error_body = e.read().decode("utf-8")
            err_msg = f"HTTP {e.code}: {error_body}"
            log.error(f"Google Drive Upload Failed: {err_msg}")
            service.call("persistent_notification", "create", title="Drive Upload Error", message=err_msg)
            return
        except Exception as e:
            log.error(f"Google Drive Upload Failed (Generic): {e}")
            return

        # 5. Append to Google Sheets
        service.call("google_sheets", "append_sheet", 
            config_entry="01M0XDDEPPZXEMRZDT022XRQQE",
            worksheet="Activity_Logs",
            data={
                "Date": start_time.split(" ")[0],
                "Start": start_time.split(" ")[1],
                "End": end_time.split(" ")[1],
                "Type": act_type,
                "Harley Behavior": harley_behavior,
                "Found Items": loot_found,
                "Notes": act_notes,
                "Max Speed (km/h)": round(max_speed, 2),
                "GPS File": drive_url
            }
        )
        
        # 6. Reset UI
        service.call("input_text", "set_value", entity_id="input_text.traccar_log_notes", value="")
        service.call("input_select", "select_option", entity_id="input_select.traccar_log_harley_behavior", option="N/A")
        service.call("input_boolean", "turn_off", entity_id="input_boolean.traccar_log_loot_found")
        log.info(f"Activity processed. Drive URL: {drive_url}")
        
    finally:
        task.sleep(5)
        _TRACCAR_LOCK = False