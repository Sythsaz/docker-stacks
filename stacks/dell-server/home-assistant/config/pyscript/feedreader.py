import sys
from pathlib import Path
import re
import json
import os
from datetime import datetime  # Ensure datetime is available

if "/pyscript/modules" not in sys.path:
    sys.path.append("/pyscript/modules")

# Feed sensors
FEED_SENSORS = {
    "event.alberta_emergency_alert_full_atom_feed": "config/alberta_emergency_alert_full_atom_feed.json",
    "event.alberta_king_s_printer_all_legislative_publications_rss_feeds": "config/alberta_king_s_printer_all_legislative_publications_rss_feeds.json",
    "event.all_feeds_alberta_king_s_printer_legislation_updates": "config/all_feeds_alberta_king_s_printer_legislation_updates.json",
    "event.aeso_rss_feed": "config/aeso_rss_feed.json",
    "event.agriculture_and_food_news_for_all_audiences": "config/agriculture_and_food_news_for_all_audiences.json",
    "event.calgary": "config/calgary.json",
    "event.calgary_tech": "config/calgary_tech.json",
    "event.city_of_lethbridge_weather_alert_environment_canada": "config/city_of_lethbridge_weather_alert_environment_canada.json",
    "event.lethbridge": "config/lethbridge.json",
    "event.national_news": "config/national_news.json",
    "event.repair": "config/repair.json",
    "event.rss_from_apa": "config/rss_from_apa.json",
}

NOTIFICATION_SERVICE = "telegram_bot.send_message"


def get_secret_from_file(key: str) -> str | None:
    p = Path("/config/secrets.yaml")  # adjust if your HA config path differs
    if not p.exists():
        log.error("secrets.yaml not found at /config/secrets.yaml")
        return None
    text = p.read_text(encoding="utf-8")
    # Simple YAML single-line scalar extractor (won't handle multiline secrets, complex YAML)
    m = re.search(
        r"^\s*" + re.escape(key) + r'\s*:\s*(["\']?)(.+?)\1\s*$',
        text,
        flags=re.MULTILINE,
    )
    return m.group(2).strip() if m else None


def load_feed_alerts(feed_file):
    """Load tracked alerts for a specific feed from its JSON file."""
    if not Path(feed_file).exists():
        return []
    with open(feed_file, "r") as f:
        return json.load(f)


def save_feed_alerts(feed_file, alerts):
    """Save tracked alerts for a specific feed to its JSON file."""
    with open(feed_file, "w") as f:
        json.dump(alerts, f, indent=4)


@service
def check_feed(feed_entity_id=None):
    """Check for new entries in a specific feed."""
    if not feed_entity_id:
        log.debug("No feed_entity_id provided.")
        return

    # Get the feed file for the given entity ID
    feed_file = FEED_SENSORS.get(feed_entity_id)
    if not feed_file:
        log.debug(f"Feed entity ID {feed_entity_id} is not defined in FEED_SENSORS.")
        return

    # Load tracked alerts for this feed
    tracked_alerts = load_feed_alerts(feed_file)

    # Get the state and attributes of the feed sensor
    if feed_entity_id not in state:
        log.debug(f"Sensor {feed_entity_id} is not available.")
        return

    feed_state = state[feed_entity_id]
    feed_attributes = feed_state.attributes

    # Extract necessary attributes
    alert_title = feed_attributes.get("title")
    alert_link = feed_attributes.get("link")
    alert_description = feed_attributes.get("description")

    if not alert_title or not alert_link or not alert_description:
        log.debug(f"Sensor {feed_entity_id} has no title, link, or description.")
        return

    # Check if the alert link, title, and description are already in the tracked list
    existing_alerts = {
        (alert["link"], alert["title"], alert["description"])
        for alert in tracked_alerts
    }
    if (alert_link, alert_title, alert_description) not in existing_alerts:
        # Send a notification for the new alert
        message = f"Description: {alert_description}\nLink: {alert_link}"
        chat_id = get_secret_from_file("telegram_chat_id")
        if chat_id:
            service.call(
                "script.send_message_telegram",
                message=message,
                message_target=chat_id,
                message_title=alert_title,
            )
        else:
            log.error("telegram_chat_id not found in secrets.yaml")

        # Add the new alert to the tracked alerts
        tracked_alerts.append(
            {
                "link": alert_link,
                "title": alert_title,
                "description": alert_description,
                "timestamp": datetime.now().isoformat(),
            }
        )

        # Save updated tracked alerts
        save_feed_alerts(feed_file, tracked_alerts)
    else:
        log.debug(
            f"Alert already sent for feed: {feed_entity_id}, title: {alert_title}"
        )
