from pathlib import Path
import asyncio
from datetime import datetime, timezone
import requests

# Your "watch list":
PDFS = [
    {
        # Animal Care and Control Bylaw
        "url_sensor": "sensor.pdf_link_animal_care_and_control_bylaw",
        "local_path": "/pdfs/bylaws/animal_care_and_control_bylaw.pdf",
        "lm_sensor":  "sensor.pdf_lastmod_animal_care_and_control_bylaw",
    },
    {
        # Graffiti Bylaw
        "url_sensor": "sensor.pdf_link_graffiti_bylaw",
        "local_path": "/pdfs/bylaws/graffiti_bylaw.pdf",
        "lm_sensor":  "sensor.pdf_lastmod_graffiti_bylaw",
    },
    {
        # Minimum Property Standards Bylaw
        "url_sensor": "sensor.pdf_link_minimum_property_standards_bylaw",
        "local_path": "/pdfs/bylaws/minimum_property_standards_bylaw.pdf",
        "lm_sensor":  "sensor.pdf_lastmod_minimum_property_standards_bylaw",
    },
    {
        # Noise Bylaw
        "url_sensor": "sensor.pdf_link_noise_bylaw",
        "local_path": "/pdfs/bylaws/noise_bylaw.pdf",
        "lm_sensor":  "sensor.pdf_lastmod_noise_bylaw",
    },
    {
        # Open Burning Bylaw
        "url_sensor": "sensor.pdf_link_open_burning_bylaw",
        "local_path": "/pdfs/bylaws/open_burning_bylaw.pdf",
        "lm_sensor":  "sensor.pdf_lastmod_open_burning_bylaw",
    },
    {
        # Smoking Bylaw
        "url_sensor": "sensor.pdf_link_smoking_bylaw",
        "local_path": "/pdfs/bylaws/smoking_bylaw.pdf",
        "lm_sensor":  "sensor.pdf_lastmod_smoking_bylaw",
    },
    {
        # Unsightly Property Bylaw
        "url_sensor": "sensor.pdf_link_unsightly_property_bylaw",
        "local_path": "/pdfs/bylaws/unsightly_property_bylaw.pdf",
        "lm_sensor":  "sensor.pdf_lastmod_unsightly_property_bylaw",
    },
    {
        # Weed Control Bylaw
        "url_sensor": "sensor.pdf_link_weed_control_bylaw",
        "local_path": "/pdfs/bylaws/weed_control_bylaw.pdf",
        "lm_sensor":  "sensor.pdf_lastmod_weed_control_bylaw",
    },
    {
        # Parks Bylaw
        "url_sensor": "sensor.pdf_link_parks_bylaw",
        "local_path": "/pdfs/bylaws/parks_bylaw.pdf",
        "lm_sensor":  "sensor.pdf_lastmod_parks_bylaw",
    },
    {
        # Bicycle Bylaw
        "url_sensor": "sensor.pdf_link_bicycle_bylaw",
        "local_path": "/pdfs/bylaws/bicycle_bylaw.pdf",
        "lm_sensor":  "sensor.pdf_lastmod_bicycle_bylaw",
    },
    {
        # Closing of Certain Roads Bylaw
        "url_sensor": "sensor.pdf_link_closing_of_certain_roads_bylaw",
        "local_path": "/pdfs/bylaws/closing_of_certain_roads_bylaw.pdf",
        "lm_sensor":  "sensor.pdf_lastmod_closing_of_certain_roads_bylaw",
    },
    {
        # Conduct of Passengers on Buses Bylaw
        "url_sensor": "sensor.pdf_link_conduct_of_passengers_on_buses_bylaw",
        "local_path": "/pdfs/bylaws/conduct_of_passengers_on_buses_bylaw.pdf",
        "lm_sensor":  "sensor.pdf_lastmod_conduct_of_passengers_on_buses_bylaw",
    },
    {
        # Drainage Bylaw
        "url_sensor": "sensor.pdf_link_drainage_bylaw",
        "local_path": "/pdfs/bylaws/drainage_bylaw.pdf",
        "lm_sensor":  "sensor.pdf_lastmod_drainage_bylaw",
    },
    {
        # Snow Removal Bylaw
        "url_sensor": "sensor.pdf_link_snow_removal_bylaw",
        "local_path": "/pdfs/bylaws/snow_removal_bylaw.pdf",
        "lm_sensor":  "sensor.pdf_lastmod_snow_removal_bylaw",
    },
    {
        # Streets Bylaw
        "url_sensor": "sensor.pdf_link_streets_bylaw",
        "local_path": "/pdfs/bylaws/streets_bylaw.pdf",
        "lm_sensor":  "sensor.pdf_lastmod_streets_bylaw",
    },
    {
        # Traffic Bylaw
        "url_sensor": "sensor.pdf_link_traffic_bylaw",
        "local_path": "/pdfs/bylaws/traffic_bylaw.pdf",
        "lm_sensor":  "sensor.pdf_lastmod_traffic_bylaw",
    },
    {
        # Transportation System Bylaw
        "url_sensor": "sensor.pdf_link_transportation_system_bylaw",
        "local_path": "/pdfs/bylaws/transportation_system_bylaw.pdf",
        "lm_sensor":  "sensor.pdf_lastmod_transportation_system_bylaw",
    }
]

DOWNLOAD_ROOT = Path("/share/downloads")

@service  # type: ignore
async def check_all_bylaw_pdfs():
    log.debug("Starting check_all_bylaw_pdfs")  # type: ignore
    log.debug(f"DOWNLOAD_ROOT = {DOWNLOAD_ROOT!r}")  # type: ignore
    log.debug(f"DOWNLOAD_ROOT.exists()? {DOWNLOAD_ROOT.exists()}")  # type: ignore
    if DOWNLOAD_ROOT.exists():
        try:
            # list the first level of files for sanity
            files = [p.name for p in DOWNLOAD_ROOT.iterdir()]
            log.debug(f"Top‑level entries under DOWNLOAD_ROOT: {files}")  # type: ignore
        except Exception as e:
            log.error(f"Could not list DOWNLOAD_ROOT: {e}")  # type: ignore
    for job in PDFS:
        p        = Path(job["local_path"].lstrip("/"))
        subdir   = p.parent
        filename = p.name
        local_dir  = DOWNLOAD_ROOT / subdir
        local_file = local_dir / filename

        log.debug(f"→ subdir        = {subdir!r}")        # type: ignore
        log.debug(f"→ filename      = {filename!r}")      # type: ignore
        log.debug(f"→ local_dir     = {local_dir!r}")     # type: ignore
        log.debug(f"  exists?        {local_dir.exists()}")  # type: ignore
        if local_dir.exists():
            try:
                log.debug(f"  contains: {[x.name for x in local_dir.iterdir()]}")  # type: ignore
            except Exception as e:
                log.error(f"  couldn't list {local_dir}: {e}")  # type: ignore

        log.debug(f"→ local_file    = {local_file!r}")    # type: ignore
        log.debug(f"  exists?        {local_file.exists()}") # type: ignore
        url = state.get(job["url_sensor"])  # type: ignore
        lm_sensor = job["lm_sensor"]
        st = hass.states.get(lm_sensor)  # type: ignore
        prev_mod = st.state if st else ""
        log.debug(f"Checking {url!r} — previous Last‑Modified: {prev_mod!r}")  # type: ignore

        # HEAD
        try:
            resp_head = await asyncio.to_thread(requests.head, url, timeout=10)
            resp_head.raise_for_status()
        except Exception as e:
            log.error(f"HEAD failed for {url}: {e}")  # type: ignore
            hass.bus.fire("bylaw_download_update", { # type: ignore
                "name": url,
                "sensor": lm_sensor,
                "success": False,
                "url": url,
                "filename": filename,
                "error": f"HEAD failed: {e}"
            })
            continue

        last_mod = resp_head.headers.get("Last-Modified", "")
        log.debug(f"Remote Last‑Modified: {last_mod!r}")  # type: ignore

        # parse timestamp
        remote_ts = None
        if last_mod:
            try:
                remote_ts = datetime.strptime(last_mod, "%a, %d %b %Y %H:%M:%S %Z")
            except Exception as e:
                log.error(f"Could not parse Last-Modified header: {e}")  # type: ignore
                hass.bus.fire("bylaw_download_update", { # type: ignore
                "name": url,
                "sensor": lm_sensor,
                "success": False,
                "url": url,
                "filename": filename,
                "error": f"Could not parse Last-Modified header: {e}"
            })

        # decide to download
        log.debug(f"Polling for downloaded file at {local_file}")  # type: ignore

        # decide if we need to download
        need_download = (
            not local_file.exists()
            or (remote_ts and remote_ts.timestamp() > local_file.stat().st_mtime)
        )
        if need_download:
            log.debug(f"Starting download of {url} → {local_file}")  # type: ignore
            log.debug(f"Downloader args subdir={subdir!r}, filename={filename!r}")  # type: ignore
            
            # 3) fire off your retrying download script
            await hass.services.async_call( # type: ignore
                "script",
                "download_a_file_with_retries",
                {
                    "url":       url,
                    "subdir":    str(subdir),
                    "filename":  filename,
                    "max_tries": 3,
                    "delay_sec": 5,
                },
                blocking=True,
            )

            # 4) now poll that exact path for up to 30s
            for _ in range(30):
                if local_file.exists():
                    log.debug(f"{filename} appeared on disk")  # type: ignore
                    break
                await asyncio.sleep(1)
            else:
                log.error(f"Timed out waiting for {filename} at {local_file}")  # type: ignore
                hass.bus.fire("bylaw_download_update", { # type: ignore
                "name": url,
                "sensor": lm_sensor,
                "success": False,
                "url": url,
                "filename": filename,
                "error": f"Timed out waiting for {filename} at {local_file}"
                })
                continue  # skip updating the sensor, move on

            # 5) update sensor state
            timestamp     = datetime.now(timezone.utc).isoformat()
            downloaded_at = datetime.fromtimestamp(
                local_file.stat().st_mtime, tz=timezone.utc
            ).isoformat()

            hass.states.async_set(  # type: ignore
                lm_sensor,
                last_mod,
                {
                    "friendly_name": f"Last‑Modified ({lm_sensor})",
                    "attribution":   "City of Lethbridge Bylaw PDF",
                    "last_checked":  timestamp,
                    "downloaded_at": downloaded_at,
                },
            )
            log.debug(f"Updated sensor {lm_sensor} to {last_mod!r}")  # type: ignore
            hass.bus.fire("bylaw_download_update", { # type: ignore
                "name": url,
                "sensor": lm_sensor,
                "success": True,
                "url": url,
                "filename": filename,
                "last_modified": last_mod
            })

        else:
            log.debug("No update needed.")  # type: ignore
            hass.bus.fire("bylaw_download_update", { # type: ignore
                "name": url,
                "sensor": lm_sensor,
                "success": True,
                "url": url,
                "filename": filename,
            })

    log.debug("Finished check_all_bylaw_pdfs")  # type: ignore