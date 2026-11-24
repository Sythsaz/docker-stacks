import aiohttp

@service
async def publish_to_wordpress(title=None, content=None, status="draft"):
    """
    Publishes a post to the WordPress REST API.
    
    Args:
        title (str): The title of the blog post.
        content (str): The HTML or text content of the post.
        status (str): The post status (e.g., 'publish', 'draft', 'private').
    """
    # 1. Input Validation
    if not title or not content:
        log.warning("WordPress Publish aborted: Title or content missing.")
        return

    # 2. Secure Configuration Retrieval
    config = pyscript.app_config
    if not config:
        log.error("WordPress Publish failed: PyScript app configuration missing.")
        return

    wp_url = config.get("wp_url")
    wp_user = config.get("wp_user")
    wp_pass = config.get("wp_pass")

    if not all([wp_url, wp_user, wp_pass]):
        log.error("WordPress Publish failed: Missing credentials in configuration.")
        return

    # 3. Payload Construction
    payload = {
        "title": str(title),
        "content": str(content),
        "status": str(status)
    }

    # 4. Asynchronous API Request
    try:
        auth = aiohttp.BasicAuth(wp_user, wp_pass)
        
        # Using aiohttp ensures Home Assistant's event loop is not blocked
        async with aiohttp.ClientSession() as session:
            async with session.post(wp_url, auth=auth, json=payload, ssl=True) as response:
                
                # Catch 4xx and 5xx HTTP errors automatically
                response.raise_for_status() 
                
                data = await response.json()
                post_id = data.get("id")
                
                log.info(f"Successfully published to WordPress. Post ID: {post_id}")
                
                # Optional: Broadcast a custom event back to Home Assistant upon success
                event.fire("wordpress_post_success", post_id=post_id, title=title)
                
    except aiohttp.ClientResponseError as e:
        log.error(f"WordPress API HTTP Error {e.status}: {e.message}")
    except Exception as e:
        log.error(f"Unexpected error during WordPress publish: {e}")