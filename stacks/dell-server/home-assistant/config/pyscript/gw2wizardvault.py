# pyscript/gw2wizardvault/update_gw2_objectives.py

import logging
from homeassistant.helpers.aiohttp_client import async_get_clientsession

log = logging.getLogger(__name__)

@service
async def update_gw2_objectives():
    """Fetch GW2 Wizards Vault objectives and update a sensor."""
    session = async_get_clientsession(hass)        # pass in hass
    url = "https://api.guildwars2.com/v2/wizardsvault/objectives"

    try:
        resp = await session.get(url, timeout=10)
        resp.raise_for_status()
        data = await resp.json()                   # your list of ints
    except Exception as e:
        log.error(f"Failed to fetch GW2 API: {e}")
        return

    # Async set the sensor state + attributes
    hass.states.async_set(
        "sensor.gw2_wizards_vault_objectives",
        len(data),
        {
            "raw": data,
            "friendly_name": "GW2 Wizards Vault Objectives"
        }
    )
    log.info(f"Updated GW2 objectives: {len(data)} items")

@service
async def update_gw2_objectives_all():
    """Fetch all Wizards Vault objectives in one batch and store them as attributes."""
    session = async_get_clientsession(hass)
    url = "https://api.guildwars2.com/v2/wizardsvault/objectives?ids=all"

    try:
        resp = await session.get(url, timeout=10)
        resp.raise_for_status()
        data = await resp.json()  # this is a list of objects, each with id, name, etc.
    except Exception as e:
        log.error(f"Failed to fetch GW2 full objectives list: {e}")
        return

    # Push into a single sensor
    hass.states.async_set(
        "sensor.gw2_wizards_vault_objectives_full",
        len(data),
        {
            "objectives": data,
            "friendly_name": "GW2 Wizards Vault Objectives (Full)"
        }
    )
    log.info(f"Fetched and stored {len(data)} objectives")