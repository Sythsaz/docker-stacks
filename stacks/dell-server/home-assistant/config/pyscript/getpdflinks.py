import asyncio
import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone

# ─── 1) Define your “scrape jobs” ────────────────────────────────────────
BYPAGE = "https://www.lethbridge.ca/bylaws-animal-services/bylaws/"
JOBS = [
    #
    # Nuisance bylaws
    # Note: All these are on the same page, so we can reuse the same URL
    {
        # Animal Care and Control Bylaw
        "link_text":  "Animal Care and Control Bylaw",
        "sensor":    "sensor.pdf_link_animal_care_and_control_bylaw",
        "friendly":  "PDF Link – Animal Care and Control Bylaw",
    },
    {
        # Graffiti Bylaw
        "link_text":  "Graffiti Bylaw",
        "sensor":    "sensor.pdf_link_graffiti_bylaw",
        "friendly":  "PDF Link – Graffiti Bylaw",
    },
    {
        # Minimum Property Standards Bylaw
        "link_text":  "Minimum Property Standards Bylaw",
        "sensor":    "sensor.pdf_link_minimum_property_standards_bylaw",
        "friendly":  "PDF Link – Minimum Property Standards Bylaw",
    },
    {
        # Noise Bylaw
        "link_text":  "Noise Bylaw",
        "sensor":    "sensor.pdf_link_noise_bylaw",
        "friendly":  "PDF Link – Noise Bylaw",
    },
    {
        # Open Burning Bylaw
        "link_text":  "Open Burning Bylaw",
        "sensor":    "sensor.pdf_link_open_burning_bylaw",
        "friendly":  "PDF Link – Open Burning Bylaw",
    },
    {
        # Smoking Bylaw
        "link_text":  "Smoking Bylaw",
        "sensor":    "sensor.pdf_link_smoking_bylaw",
        "friendly":  "PDF Link – Smoking Bylaw",
    },
    {
        # Unsightly Property Bylaw
        "link_text":  "Unsightly Property Bylaw",
        "sensor":    "sensor.pdf_link_unsightly_property_bylaw",
        "friendly":  "PDF Link – Unsightly Property Bylaw",
    },
    {
        # Weed Control Bylaw
        "link_text":  "Weed Control Bylaw",
        "sensor":    "sensor.pdf_link_weed_control_bylaw",
        "friendly":  "PDF Link – Weed Control Bylaw",
    },
    #
    # Parks bylaws
    # Note: This is a separate section on the same page, so we reuse the same page URL
    {
        # Parks Bylaw
        "link_text":  "Parks Bylaw",
        "sensor":    "sensor.pdf_link_parks_bylaw",
        "friendly":  "PDF Link – Parks Bylaw",
    },
    #
    # Streets and Roads bylaws
    # Note: This is another section on the same page, so we reuse the same page URL
    {
        # Bicycle Bylaw
        "link_text": "Bicycle Bylaw",
        "sensor":    "sensor.pdf_link_bicycle_bylaw",
        "friendly":  "PDF Link – Bicycle Bylaw",
    },
    {
        # Closing of Certain Roads Bylaw
        "link_text":  "Closing of Certain Roads Bylaw",
        "sensor":    "sensor.pdf_link_closing_of_certain_roads_bylaw",
        "friendly":  "PDF Link – Closing of Certain Roads Bylaw",
    },
    {
        # Conduct of Passengers on Buses Bylaw
        "link_text":  "Conduct of Passengers on Buses Bylaw",
        "sensor":    "sensor.pdf_link_conduct_of_passengers_on_buses_bylaw",
        "friendly":  "PDF Link – Conduct of Passengers on Buses Bylaw",
    },
    {
        # Drainage Bylaw
        "link_text":  "Drainage Bylaw",
        "sensor":    "sensor.pdf_link_drainage_bylaw",
        "friendly":  "PDF Link – Drainage Bylaw",
    },
    {
        # Snow Removal Bylaw
        "link_text":  "Snow Removal Bylaw",
        "sensor":    "sensor.pdf_link_snow_removal_bylaw",
        "friendly":  "PDF Link – Snow Removal Bylaw",
    },
    {
        # Streets Bylaw
        "link_text":  "Streets Bylaw",
        "sensor":    "sensor.pdf_link_streets_bylaw",
        "friendly":  "PDF Link – Streets Bylaw",
    },
    {
        # Traffic Bylaw

        "link_text":  "Traffic Bylaw",
        "sensor":    "sensor.pdf_link_traffic_bylaw",
        "friendly":  "PDF Link – Traffic Bylaw",
    },
    {
        # Transportation System Bylaw
        "link_text":  "Transportation System Bylaw",
        "sensor":    "sensor.pdf_link_transportation_system_bylaw",
        "friendly":  "PDF Link – Transportation System Bylaw",
    }
]

BASE_URL = "https://www.lethbridge.ca"

@service # type: ignore
async def scrape_multiple_bylaw_pdfs():
    # 1) fetch the index page once
    try:
        resp = await asyncio.to_thread(requests.get, BYPAGE, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
    except Exception as e:
        log.error(f"[ALL] Could not fetch bylaws index: {e}") # type: ignore
        return

    # 2) loop through each job
    for job in JOBS:
        name = job["friendly"]
        want_lower = job["link_text"].lower() 

        # 1) grab ALL <a> whose text contains your title (case-insensitive)
        #    we bind `want` into the lambda via a default argument `w=want_lower`
        candidates = soup.find_all(
            "a",
            href=True,
            string=lambda s, w=want_lower: (
                s is not None and
                w in s.strip().lower()
            )
        )

        # pick the first one whose href ends in ".pdf"
        pdf_link = None
        for a in candidates:
            href = a["href"].strip().lower()
            if href.endswith(".pdf"):
                pdf_link = a
                break

        if not pdf_link:
            log.error(f"[{job['friendly']}] Could not find a PDF <a> containing '{job['link_text']}'") # type: ignore
            hass.bus.fire("bylaw_update_link", { # type: ignore
            "name": name,
            "success":  False,
            "link": full,
            "sensor": job["sensor"],
            "reason": "Could not find a PDF <a>"
            })
            continue

        rel = pdf_link["href"]
        full = rel if rel.startswith("http") else BASE_URL + rel
        ts   = datetime.now(timezone.utc).isoformat()

        hass.states.async_set( # type: ignore
            job["sensor"],
            full,
            {
                "friendly_name": name,
                "attribution":   "City of Lethbridge Bylaw PDF Link",
                "last_scraped":  ts,
            }
        )
        log.info(f"[{name}] → {full}") # type: ignore
        hass.bus.fire("bylaw_update_link", { # type: ignore
            "name": name,
            "success":  True,
            "link": full,
            "sensor": job["sensor"]
        })