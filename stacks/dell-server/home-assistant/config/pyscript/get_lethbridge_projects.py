import requests

URLS = {
    "projects": "https://services6.arcgis.com/u9bqNg4TWfrgrRVV/arcgis/rest/services/PRD_CityProjects_202504_View_LethProjects/FeatureServer/0/query?where=1%3D1&outFields=*&f=json",
    "areas": "https://services6.arcgis.com/u9bqNg4TWfrgrRVV/arcgis/rest/services/PRD_CityProjectAreas_202504_View_LethProjects/FeatureServer/0/query?where=1%3D1&outFields=*&f=json"
}

# This trigger runs the script every hour on the hour, and once when Home Assistant starts up.
@time_trigger("startup", "cron(0 * * * *)")
def fetch_lethbridge_projects():
    for category, url in URLS.items():
        try:
            # PyScript runs in an async loop. We MUST use task.executor for blocking requests like requests.get()
            response = task.executor(requests.get, url)
            data = response.json()
            
            for feature in data.get('features', []):
                attributes = feature.get('attributes', {})
                
                object_id = attributes.get('OBJECTID')
                if not object_id:
                    continue
                    
                project_name = attributes.get('PROJECT_NAME', f"Project {object_id}")
                
                # Construct the Home Assistant entity ID
                entity_id = f"sensor.lethbridge_{category}_{object_id}"
                
                # Set the main state (you can change 'STATUS' to whichever key you prefer)
                main_state = attributes.get('STATUS', 'Unknown')
                
                # Inject standard Home Assistant UI attributes into our data payload
                attributes['friendly_name'] = f"Lethbridge {category.title()}: {project_name}"
                attributes['icon'] = "mdi:crane"
                
                # PyScript Magic: This directly creates or updates the sensor in Home Assistant
                state.set(entity_id, value=main_state, new_attributes=attributes)
                
            log.info(f"PyScript: Successfully processed {len(data.get('features', []))} Lethbridge {category}.")
            
        except Exception as e:
            log.error(f"PyScript: Error fetching Lethbridge {category} - {e}")