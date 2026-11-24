import aiohttp
import xml.etree.ElementTree as ET

def extract_release_data(xml_text):
    try:
        root = ET.fromstring(xml_text)
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        entry = root.find('atom:entry', ns)
        if entry is None:
            return None
        title = entry.find('atom:title', ns).text
        link = entry.find('atom:link', ns).attrib.get('href')
        
        # The magic addition: grabbing the actual HTML content of the post
        content_elem = entry.find('atom:content', ns)
        content = content_elem.text if content_elem is not None else ""
        
        return {"title": title, "link": link, "content": content}
    except Exception as e:
        return {"error": str(e)}

@service
async def monitor_ha_releases(**kwargs):
    # Send a notification to the UI
    persistent_notification.create(
        title="HA Release Monitor", 
        message="1. Script started successfully!"
    )
    
    feed_url = "https://www.home-assistant.io/atom.xml"
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(feed_url, ssl=True) as response:
                response.raise_for_status()
                text = await response.text()
    except Exception as e:
        persistent_notification.create(
            title="HA Release Monitor Error", 
            message=f"Failed to fetch feed: {e}"
        )
        return

    # THE FIX: Call the function directly instead of using task.executor!
    latest_post = extract_release_data(text)
    
    if not latest_post:
        persistent_notification.create(
            title="HA Release Monitor", 
            message="Feed was empty or failed to parse."
        )
        return
    if "error" in latest_post:
        persistent_notification.create(
            title="HA Release Monitor", 
            message=f"Error parsing XML: {latest_post['error']}"
        )
        return
        
    title = latest_post.get("title", "")
    link = latest_post.get("link", "")
    
    persistent_notification.create(
        title="HA Release Monitor", 
        message=f"2. Found latest post: '{title}'"
    )
    
    # 1. Filter Check
    # if "Release" not in title and "Core" not in title:
        # persistent_notification.create(
            # title="HA Release Monitor", 
            # message=f"3. Exiting. '{title}' is not a Core Release."
        # )
        # return 

    # 2. Duplicate Check
    last_processed = state.get("input_text.last_ha_release_url")
    if link == last_processed:
        persistent_notification.create(
            title="HA Release Monitor", 
            message=f"3. Exiting. We already processed this URL before!"
        )
        return 

    persistent_notification.create(
        title="HA Release Monitor", 
        message="4. Passed all filters! Pushing to WordPress..."
    )

    final_payload = f"""
    <!-- wp:paragraph -->
    <p><strong>A new Home Assistant update is available!</strong></p>
    <!-- /wp:paragraph -->
    
    <!-- wp:paragraph -->
    <p>Title: {title}</p>
    <!-- /wp:paragraph -->

    <!-- wp:paragraph -->
    <p>Read the full release notes and breaking changes here: <br>
    <a href="{link}" target="_blank" rel="noopener">{link}</a></p>
    <!-- /wp:paragraph -->
    
    <!-- wp:separator -->
    <hr class="wp-block-separator has-alpha-channel-opacity"/>
    <!-- /wp:separator -->
    """

    try:
        await pyscript.publish_to_wordpress(
            title=f"HA Update: {title}",
            content=final_payload,
            status="draft" 
        )
        # Save the URL so we don't process it again
        state.set("input_text.last_ha_release_url", link)
        persistent_notification.create(
            title="HA Release Monitor SUCCESS", 
            message=f"Draft created successfully for {link}!"
        )
        
    except Exception as e:
        persistent_notification.create(
            title="HA Release Monitor", 
            message=f"Failed to push to WP: {e}"
        )