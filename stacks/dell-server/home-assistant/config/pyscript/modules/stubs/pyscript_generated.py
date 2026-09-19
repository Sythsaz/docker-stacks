from typing import Any, Literal
from datetime import datetime
from pyscript_builtins import StateVal

class adaptive_lighting:

    @staticmethod
    def apply(*, entity_id: str | None=None, lights: str | None=None, transition: str | None=None, adapt_brightness: bool | None=None, adapt_color: bool | None=None, prefer_rgb_color: bool | None=None, turn_on_lights: bool | None=None):
        """Applies the current Adaptive Lighting settings to lights.

        Args:
            entity_id: The `entity_id` of the switch with the settings to apply. 📝
            lights: A light (or list of lights) to apply the settings to. 💡
            transition: Duration of transition when lights change, in seconds. 🕑 Example: 10
            adapt_brightness: Whether to adapt the brightness of the light. 🌞 Example: True
            adapt_color: Whether to adapt the color on supporting lights. 🌈 Example: True
            prefer_rgb_color: Whether to prefer RGB color adjustment over light color temperature when possible. 🌈
            turn_on_lights: Whether to turn on lights that are currently off. 🔆"""
        ...

    @staticmethod
    def set_manual_control(*, entity_id: str | None=None, lights: str | None=None, manual_control: bool=True):
        """Mark whether a light is 'manually controlled'.

        Args:
            entity_id: The `entity_id` of the switch in which to (un)mark the light as being `manually controlled`. 📝
            lights: entity_id(s) of lights, if not specified, all lights in the switch are selected. 💡
            manual_control: Whether to add ("true") or remove ("false") all adapted attributes of the light from the "manual_control" list, or the name of an attribute for selective addition. 🔒 Example: True"""
        ...

    @staticmethod
    def change_switch_settings(*, entity_id: str, use_defaults: Literal['', 'current', 'configuration', 'factory']='current', include_config_in_attributes: bool | None=None, turn_on_lights: bool | None=None, initial_transition: str | None=None, sleep_transition: str | None=None, max_brightness: str | None=None, max_color_temp: str | None=None, min_brightness: str | None=None, min_color_temp: str | None=None, only_once: bool | None=None, prefer_rgb_color: bool | None=None, separate_turn_on_commands: bool | None=None, send_split_delay: bool | None=None, sleep_brightness: str | None=None, sleep_rgb_or_color_temp: Literal['', 'rgb_color', 'color_temp'] | None=None, sleep_rgb_color: tuple[int, int, int] | None=None, sleep_color_temp: str | None=None, sunrise_offset: int | None=None, sunrise_time: str | None=None, sunset_offset: int | None=None, sunset_time: str | None=None, max_sunrise_time: str | None=None, min_sunset_time: str | None=None, take_over_control: bool | None=None, take_over_control_mode: Literal['', 'pause_all', 'pause_changed'] | None=None, detect_non_ha_changes: bool | None=None, transition: str | None=None, adapt_delay: str | None=None, autoreset_control_seconds: str | None=None):
        """Change any settings you'd like in the switch. All options here are the same as in the config flow.

        Args:
            entity_id: Entity ID of the switch. 📝
            use_defaults: Sets the default values not specified in this service call. Options: "current" (default, retains current values), "factory" (resets to documented defaults), or "configuration" (reverts to switch config defaults). ⚙️ Example: current
            include_config_in_attributes: Show all options as attributes on the switch in Home Assistant when set to `true`. 📝
            turn_on_lights: Whether to turn on lights that are currently off. 🔆
            initial_transition: Duration of the first transition when lights turn from `off` to `on` in seconds. ⏲️ Example: 1
            sleep_transition: Duration of transition when "sleep mode" is toggled in seconds. 😴 Example: 1
            max_brightness: Maximum brightness percentage. 💡 Example: 100
            max_color_temp: Coldest color temperature in Kelvin. ❄️ Example: 5500
            min_brightness: Minimum brightness percentage. 💡 Example: 1
            min_color_temp: Warmest color temperature in Kelvin. 🔥 Example: 2000
            only_once: Adapt lights only when they are turned on (`true`) or keep adapting them (`false`). 🔄
            prefer_rgb_color: Whether to prefer RGB color adjustment over light color temperature when possible. 🌈
            separate_turn_on_commands: Use separate `light.turn_on` calls for color and brightness, needed for some light types. 🔀
            send_split_delay: Delay (ms) between `separate_turn_on_commands` for lights that don't support simultaneous brightness and color setting. ⏲️
            sleep_brightness: Brightness percentage of lights in sleep mode. 😴 Example: 1
            sleep_rgb_or_color_temp: Use either `"rgb_color"` or `"color_temp"` in sleep mode. 🌙 Example: color_temp
            sleep_rgb_color: RGB color in sleep mode (used when `sleep_rgb_or_color_temp` is "rgb_color"). 🌈
            sleep_color_temp: Color temperature in sleep mode (used when `sleep_rgb_or_color_temp` is `color_temp`) in Kelvin. 😴 Example: 1000
            sunrise_offset: Adjust sunrise time with a positive or negative offset in seconds. ⏰
            sunrise_time: Set a fixed time (HH:MM:SS) for sunrise. 🌅
            sunset_offset: Adjust sunset time with a positive or negative offset in seconds. ⏰
            sunset_time: Set a fixed time (HH:MM:SS) for sunset. 🌇
            max_sunrise_time: Set the latest virtual sunrise time (HH:MM:SS), allowing for earlier sunrises. 🌅
            min_sunset_time: Set the earliest virtual sunset time (HH:MM:SS), allowing for later sunsets. 🌇
            take_over_control: Pause adaptation of individual lights and hand over (manual) control to other sources that issue `light.turn_on` calls for lights that are on. 🔒 Example: True
            take_over_control_mode: The adaptation pausing mode when other sources change brightness and/or color of lights. `pause_all` always pauses both brightness and color adaptation. `pause_changed` pauses the adaptation of only the changed attributes and continues adapting unchanged attributes, e.g., continues color adaptation when only brightness was changed. Example: pause_changed
            detect_non_ha_changes: Detects and halts adaptations for non-`light.turn_on` state changes. Needs `take_over_control` enabled. 🕵️ Caution: ⚠️ Some lights might falsely indicate an 'on' state, which could result in lights turning on unexpectedly. Note that this calls `homeassistant.update_entity` every `interval`! Disable this feature if you encounter such issues.
            transition: Duration of transition when lights change, in seconds. 🕑 Example: 45
            adapt_delay: Wait time (seconds) between light turn on and Adaptive Lighting applying changes. Might help to avoid flickering. ⏲️
            autoreset_control_seconds: Automatically reset the manual control after a number of seconds. Set to 0 to disable. ⏲️"""
        ...

class _ai_task_state(StateVal):
    supported_features: int

class ai_task:
    google_ai_task: _ai_task_state

    @staticmethod
    def generate_data(*, task_name: str, instructions: str, entity_id: str | None=None, structure: Any | None=None, attachments=None) -> dict[str, Any]:
        """

        Args:
            task_name:  Example: home summary
            instructions:  Example: Generate a funny notification that the garage door was left open
            structure:  Example: { "name": { "selector": { "text": }, "description": "Name of the user", "required": "True" } } }, "age": { "selector": { "number": }, "description": "Age of the user" } }"""
        ...

    @staticmethod
    def generate_image(*, task_name: str, instructions: str, entity_id: str, attachments=None) -> dict[str, Any]:
        """

        Args:
            task_name:  Example: picture of a dog
            instructions:  Example: Generate a high quality square image of a dog on transparent background"""
        ...

class alarm_control_panel:

    @staticmethod
    def alarm_disarm(*, entity_id: str, code: str | None=None):
        """

        Args:
            entity_id: Entity ID
            code:  Example: 1234"""
        ...

    @staticmethod
    def alarm_arm_home(*, entity_id: str, code: str | None=None):
        """

        Args:
            entity_id: Entity ID
            code:  Example: 1234"""
        ...

    @staticmethod
    def alarm_arm_away(*, entity_id: str, code: str | None=None):
        """

        Args:
            entity_id: Entity ID
            code:  Example: 1234"""
        ...

    @staticmethod
    def alarm_arm_night(*, entity_id: str, code: str | None=None):
        """

        Args:
            entity_id: Entity ID
            code:  Example: 1234"""
        ...

    @staticmethod
    def alarm_arm_vacation(*, entity_id: str, code: str | None=None):
        """

        Args:
            entity_id: Entity ID
            code:  Example: 1234"""
        ...

    @staticmethod
    def alarm_arm_custom_bypass(*, entity_id: str, code: str | None=None):
        """

        Args:
            entity_id: Entity ID
            code:  Example: 1234"""
        ...

    @staticmethod
    def alarm_trigger(*, entity_id: str, code: str | None=None):
        """

        Args:
            entity_id: Entity ID
            code:  Example: 1234"""
        ...

class assist_satellite:

    @staticmethod
    def announce(*, entity_id: str, message: str='', media_id=None, preannounce: bool=True, preannounce_media_id=None):
        """

        Args:
            entity_id: Entity ID
            message:  Example: Time to wake up!"""
        ...

    @staticmethod
    def start_conversation(*, entity_id: str, start_message: str='', start_media_id=None, extra_system_prompt: str | None=None, preannounce: bool=True, preannounce_media_id=None):
        """

        Args:
            entity_id: Entity ID
            start_message:  Example: You left the lights on in the living room. Turn them off?"""
        ...

    @staticmethod
    def ask_question(*, entity_id: str, question: str='', question_media_id=None, preannounce: bool=True, preannounce_media_id=None, answers: Any | None=None) -> dict[str, Any]:
        """

        Args:
            question:  Example: What kind of music would you like to play?"""
        ...

class _automation_state(StateVal):
    current: int
    id: str
    last_triggered: datetime
    max: int
    mode: str
    restored: bool
    supported_features: int

    def trigger(self, skip_condition: bool):
        ...

    def toggle(self):
        ...

    def turn_on(self):
        ...

    def turn_off(self, stop_actions: bool):
        ...

class automation:
    furnace_room_door_closed: _automation_state
    bedroom_closet_off: _automation_state
    env_can_adv_notification_telegram: _automation_state
    iphone_cell_state_change_notification: _automation_state
    syth_zone_system: _automation_state
    ashton_leave_home: _automation_state
    full_moon_notification: _automation_state
    external_ip_monitor: _automation_state
    outside_light_helper_toggle: _automation_state
    alberta_alert_rss: _automation_state
    ha_start_stop: _automation_state
    telegram_bot_commands: _automation_state
    accuweather_pressure_automation_telegram: _automation_state
    a_j_personal_ashton_home: _automation_state
    aurora_notification_telegram_boyz: _automation_state
    update_notifications: _automation_state
    telegram_bot_filtering: _automation_state
    livingtv_buffering_notification: _automation_state
    arduino_uno: _automation_state
    mqtt_webhook: _automation_state
    sunset_outside_light: _automation_state
    justices_external_ip_address: _automation_state
    server_fan_restart: _automation_state
    ape_junk_live_tts: _automation_state
    open_weather_tts: _automation_state
    justice_spotify_notification: _automation_state
    aurora_tts_notification: _automation_state
    home_assistant_high_temp: _automation_state
    youtube_video_notification: _automation_state
    waste_reminders: _automation_state
    justice_calendar_notification: _automation_state
    justice_s_waste_notificatons: _automation_state
    understairs_closet: _automation_state
    send_harley_s_food: _automation_state
    sync_home_calendar_to_kit_ashton: _automation_state
    change_detection_io_notification: _automation_state
    electricity_maps_fossil_fuel_notification: _automation_state
    discord_notifications: _automation_state
    download_traffic_camera_photos: _automation_state
    door_sensors_offline: _automation_state
    discord_notifications_2: _automation_state
    internet: _automation_state
    changedetection_io_notifications: _automation_state
    streamer_bot_tts: _automation_state
    weekly_tts_cache_cleanup: _automation_state
    sir_flop_s_puzzles_list_to_helper: _automation_state
    notify_when_qbittorrent_completes: _automation_state
    iphone_steps_notification: _automation_state
    iphone_storage_notification: _automation_state
    harley_s_food_order_to_google_calendar: _automation_state
    coulee_vet_email_notifications: _automation_state
    opnsense_interface_errors: _automation_state
    opnsense_system_notifications: _automation_state
    update_bylaw_links_pdfs: _automation_state
    bylaw_pdf_update_notifications: _automation_state
    iphone_zone_state_lights: _automation_state
    breaker_box_mic: _automation_state
    furnace_room_lights_lock: _automation_state
    bedroom_closet_lights_lock: _automation_state
    ps4_fan: _automation_state
    bread_timer: _automation_state
    internet_bandwidth_notifications: _automation_state
    start_adjustable_timer_from_input_text_with_validation: _automation_state
    space_weather_aurora_alert: _automation_state
    space_weather_hf_aviation_alert: _automation_state
    space_weather_satellite_drag_alert: _automation_state
    space_weather_aurora_alert_lethbridge_tuned: _automation_state
    space_weather_hf_aviation_alert_lethbridge_tuned: _automation_state
    space_weather_satellite_drag_alert_lethbridge_tuned: _automation_state
    discord_status_notifications: _automation_state
    astroweather_notify_when_good_for_deep_sky_backyard: _automation_state
    hourly_updates: _automation_state
    calendar_notifications_actions_birthdays: _automation_state
    calendar_notifications_actions_canadian_holidays: _automation_state
    camera_snapshot_ai_notification_on_motion: _automation_state
    frigate_notification_0_10_0: _automation_state
    piper_stop: _automation_state
    toggle_adaptive_lighting: _automation_state
    file_reloading: _automation_state
    error_log_monitoring: _automation_state
    check_gemini_time: _automation_state
    docker_container_status: _automation_state
    error_log_counter_no_notify: _automation_state
    update_clock_seconds: _automation_state
    generative_ai_max_tokens: _automation_state
    hacs_restart_required_send_actionable_mobile_notification: _automation_state
    aeso_new_grid_alert_notifier: _automation_state
    aea_emergency_alert_notifier: _automation_state
    grafana_alerts: _automation_state
    frigate_notification_0_10_0_ipad: _automation_state
    github_releases: _automation_state
    github_commits: _automation_state
    post_status_update: _automation_state
    spotify_jusparr_started_new_track_stopped: _automation_state
    speak_statement: _automation_state
    open_weather_tts_2: _automation_state
    download_traffic_camera_photos_2: _automation_state
    syth_iphone_location_state_monitor: _automation_state
    telegram_bot_commands_2: _automation_state
    new_telegram_message: _automation_state
    outside_light_power: _automation_state
    send_data_from_ha_to_wordpress: _automation_state
    save_radar_gif: _automation_state
    giveaway_bot_update_notifications: _automation_state
    github_sponsors_notifications: _automation_state
    irl_stream_1_min_battery_poll: _automation_state
    full_moon_notifications: _automation_state
    streamer_bot_stream_webhook: _automation_state
    system_whisper_memory_usage_alert: _automation_state
    environment_lethbridge_high_wind_alert: _automation_state

    @staticmethod
    def trigger(*, entity_id: str, skip_condition: bool=True):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_on(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_off(*, entity_id: str, stop_actions: bool=True):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def reload():
        ...

class backup:

    @staticmethod
    def create():
        ...

    @staticmethod
    def create_automatic():
        ...

class battery_notes:

    @staticmethod
    def set_battery_replaced(*, device_id=None, source_entity_id: str | None=None, datetime_replaced: datetime | None=None):
        """Set the battery last replaced.

        Args:
            device_id: Device that has had its battery replaced.
            source_entity_id: Entity that has had its battery replaced (only used for entity associated battery notes).
            datetime_replaced: Date replaced."""
        ...

    @staticmethod
    def check_battery_last_reported(*, days_last_reported: float, raise_events: bool=True) -> dict[str, Any]:
        """Get or raise events for devices that haven't reported their battery level.

        Args:
            days_last_reported: Number of days since a device last reported its battery level.
            raise_events: Raise events for use in automation triggers."""
        ...

    @staticmethod
    def check_battery_last_replaced(*, days_last_replaced: float, raise_events: bool=True) -> dict[str, Any]:
        """Get or raise events for devices that haven't had their battery replaced."

        Args:
            days_last_replaced: Number of days since a device last had its battery replaced.
            raise_events: Raise events for use in automation triggers."""
        ...

    @staticmethod
    def check_battery_low(*, raise_events: bool=True) -> dict[str, Any]:
        """Get or raise events for devices that have a low battery.

        Args:
            raise_events: Raise events for use in automation triggers."""
        ...

class _binary_sensor_state(StateVal):
    activityType: str
    airdate: str
    attribution: str
    battery_last_replaced: datetime
    battery_low_threshold: int
    battery_quantity: int
    battery_type: str
    battery_type_and_quantity: str
    bio: str
    box_art_url: str
    browserID: str
    connection_type: str
    data: str
    days_offset: int
    deep_link: str
    device_id: str
    device_name: str
    device_type: str
    display_name: str
    end_time: datetime
    end_uv: float
    entity_picture: str
    excludes: list
    fanart: str
    genres: str
    icons: list
    ignoring_battery_optimizations: bool
    interval_type: str
    interval_value: int
    last_performed: str
    last_pypi_update_old_version: str
    last_pypi_update_package_name: str
    last_pypi_update_package_url: str
    last_pypi_update_version: str
    location: str
    manufacturer: str
    manufacturer_url: str
    markdown: str
    model_description: str
    model_name: str
    model_number: str
    model_url: str
    next_due: str
    normal_price: str
    pending_notices: list
    percent_off: int
    poster: str
    presentation_url: str
    price: str
    rating: str
    real_name: str
    release: str
    restored: bool
    review_desc: str
    reviews_percent: int
    reviews_total: int
    sale_price: str
    serial_number: str
    source_entity_id: str
    start_time: datetime
    start_uv: float
    steam_id: str
    supported_features: int
    title: str
    type: str
    udn: str
    upc: str
    updates: list
    url: str
    workdays: list

class binary_sensor:
    openuv_protection_window: _binary_sensor_state
    debian_hp_client: _binary_sensor_state
    debian_hp_key_expiry_disabled: _binary_sensor_state
    debian_hp_supports_hairpinning: _binary_sensor_state
    debian_hp_supports_ipv6: _binary_sensor_state
    debian_hp_supports_pcp: _binary_sensor_state
    debian_hp_supports_nat_pmp: _binary_sensor_state
    debian_hp_supports_udp: _binary_sensor_state
    debian_hp_supports_upnp: _binary_sensor_state
    debian_r_client: _binary_sensor_state
    debian_r_key_expiry_disabled: _binary_sensor_state
    debian_r_supports_hairpinning: _binary_sensor_state
    debian_r_supports_ipv6: _binary_sensor_state
    debian_r_supports_pcp: _binary_sensor_state
    debian_r_supports_nat_pmp: _binary_sensor_state
    debian_r_supports_udp: _binary_sensor_state
    debian_r_supports_upnp: _binary_sensor_state
    desk_j_client: _binary_sensor_state
    desk_j_key_expiry_disabled: _binary_sensor_state
    desk_j_supports_hairpinning: _binary_sensor_state
    desk_j_supports_ipv6: _binary_sensor_state
    desk_j_supports_pcp: _binary_sensor_state
    desk_j_supports_nat_pmp: _binary_sensor_state
    desk_j_supports_udp: _binary_sensor_state
    desk_j_supports_upnp: _binary_sensor_state
    desktop_3tursll_client: _binary_sensor_state
    desktop_3tursll_key_expiry_disabled: _binary_sensor_state
    desktop_3tursll_supports_hairpinning: _binary_sensor_state
    desktop_3tursll_supports_ipv6: _binary_sensor_state
    desktop_3tursll_supports_pcp: _binary_sensor_state
    desktop_3tursll_supports_nat_pmp: _binary_sensor_state
    desktop_3tursll_supports_udp: _binary_sensor_state
    desktop_3tursll_supports_upnp: _binary_sensor_state
    desktop_bcdiv5f_client: _binary_sensor_state
    desktop_bcdiv5f_key_expiry_disabled: _binary_sensor_state
    desktop_bcdiv5f_supports_hairpinning: _binary_sensor_state
    desktop_bcdiv5f_supports_ipv6: _binary_sensor_state
    desktop_bcdiv5f_supports_pcp: _binary_sensor_state
    desktop_bcdiv5f_supports_nat_pmp: _binary_sensor_state
    desktop_bcdiv5f_supports_udp: _binary_sensor_state
    desktop_bcdiv5f_supports_upnp: _binary_sensor_state
    google_chromecast_1_client: _binary_sensor_state
    google_chromecast_1_key_expiry_disabled: _binary_sensor_state
    google_chromecast_1_supports_hairpinning: _binary_sensor_state
    google_chromecast_1_supports_ipv6: _binary_sensor_state
    google_chromecast_1_supports_pcp: _binary_sensor_state
    google_chromecast_1_supports_nat_pmp: _binary_sensor_state
    google_chromecast_1_supports_udp: _binary_sensor_state
    google_chromecast_1_supports_upnp: _binary_sensor_state
    homeassistant_j_1_client: _binary_sensor_state
    homeassistant_j_1_key_expiry_disabled: _binary_sensor_state
    homeassistant_j_1_supports_hairpinning: _binary_sensor_state
    homeassistant_j_1_supports_ipv6: _binary_sensor_state
    homeassistant_j_1_supports_pcp: _binary_sensor_state
    homeassistant_j_1_supports_nat_pmp: _binary_sensor_state
    homeassistant_j_1_supports_udp: _binary_sensor_state
    homeassistant_j_1_supports_upnp: _binary_sensor_state
    homeassistant_t_1_client: _binary_sensor_state
    homeassistant_t_1_key_expiry_disabled: _binary_sensor_state
    homeassistant_t_1_supports_hairpinning: _binary_sensor_state
    homeassistant_t_1_supports_ipv6: _binary_sensor_state
    homeassistant_t_1_supports_pcp: _binary_sensor_state
    homeassistant_t_1_supports_nat_pmp: _binary_sensor_state
    homeassistant_t_1_supports_udp: _binary_sensor_state
    homeassistant_t_1_supports_upnp: _binary_sensor_state
    ipad_gen_6_client: _binary_sensor_state
    ipad_gen_6_key_expiry_disabled: _binary_sensor_state
    ipad_gen_6_supports_hairpinning: _binary_sensor_state
    ipad_gen_6_supports_ipv6: _binary_sensor_state
    ipad_gen_6_supports_pcp: _binary_sensor_state
    ipad_gen_6_supports_nat_pmp: _binary_sensor_state
    ipad_gen_6_supports_udp: _binary_sensor_state
    ipad_gen_6_supports_upnp: _binary_sensor_state
    iphone_11_pro_max_client: _binary_sensor_state
    iphone_11_pro_max_key_expiry_disabled: _binary_sensor_state
    iphone_11_pro_max_supports_hairpinning: _binary_sensor_state
    iphone_11_pro_max_supports_ipv6: _binary_sensor_state
    iphone_11_pro_max_supports_pcp: _binary_sensor_state
    iphone_11_pro_max_supports_nat_pmp: _binary_sensor_state
    iphone_11_pro_max_supports_udp: _binary_sensor_state
    iphone_11_pro_max_supports_upnp: _binary_sensor_state
    laptop_client: _binary_sensor_state
    laptop_key_expiry_disabled: _binary_sensor_state
    laptop_supports_hairpinning: _binary_sensor_state
    laptop_supports_ipv6: _binary_sensor_state
    laptop_supports_pcp: _binary_sensor_state
    laptop_supports_nat_pmp: _binary_sensor_state
    laptop_supports_udp: _binary_sensor_state
    laptop_supports_upnp: _binary_sensor_state
    opnsense_1_client: _binary_sensor_state
    opnsense_1_key_expiry_disabled: _binary_sensor_state
    opnsense_1_supports_hairpinning: _binary_sensor_state
    opnsense_1_supports_ipv6: _binary_sensor_state
    opnsense_1_supports_pcp: _binary_sensor_state
    opnsense_1_supports_nat_pmp: _binary_sensor_state
    opnsense_1_supports_udp: _binary_sensor_state
    opnsense_1_supports_upnp: _binary_sensor_state
    raspberrypi_client: _binary_sensor_state
    raspberrypi_key_expiry_disabled: _binary_sensor_state
    raspberrypi_supports_hairpinning: _binary_sensor_state
    raspberrypi_supports_ipv6: _binary_sensor_state
    raspberrypi_supports_pcp: _binary_sensor_state
    raspberrypi_supports_nat_pmp: _binary_sensor_state
    raspberrypi_supports_udp: _binary_sensor_state
    raspberrypi_supports_upnp: _binary_sensor_state
    samsung_sm_a136w_1_client: _binary_sensor_state
    samsung_sm_a136w_1_key_expiry_disabled: _binary_sensor_state
    samsung_sm_a136w_1_supports_hairpinning: _binary_sensor_state
    samsung_sm_a136w_1_supports_ipv6: _binary_sensor_state
    samsung_sm_a136w_1_supports_pcp: _binary_sensor_state
    samsung_sm_a136w_1_supports_nat_pmp: _binary_sensor_state
    samsung_sm_a136w_1_supports_udp: _binary_sensor_state
    samsung_sm_a136w_1_supports_upnp: _binary_sensor_state
    samsung_sm_a136w_client: _binary_sensor_state
    samsung_sm_a136w_key_expiry_disabled: _binary_sensor_state
    samsung_sm_a136w_supports_hairpinning: _binary_sensor_state
    samsung_sm_a136w_supports_ipv6: _binary_sensor_state
    samsung_sm_a136w_supports_pcp: _binary_sensor_state
    samsung_sm_a136w_supports_nat_pmp: _binary_sensor_state
    samsung_sm_a136w_supports_udp: _binary_sensor_state
    samsung_sm_a136w_supports_upnp: _binary_sensor_state
    samsung_sm_g960w_client: _binary_sensor_state
    samsung_sm_g960w_key_expiry_disabled: _binary_sensor_state
    samsung_sm_g960w_supports_hairpinning: _binary_sensor_state
    samsung_sm_g960w_supports_ipv6: _binary_sensor_state
    samsung_sm_g960w_supports_pcp: _binary_sensor_state
    samsung_sm_g960w_supports_nat_pmp: _binary_sensor_state
    samsung_sm_g960w_supports_udp: _binary_sensor_state
    samsung_sm_g960w_supports_upnp: _binary_sensor_state
    workday_sensor: _binary_sensor_state
    home_assistant_versions_update_available: _binary_sensor_state
    home_assistant_website_update_available: _binary_sensor_state
    docker_hub_update_available: _binary_sensor_state
    python_package_index_pypi_update_available: _binary_sensor_state
    syth_focus: _binary_sensor_state
    pet_lost: _binary_sensor_state
    security_keys_lost: _binary_sensor_state
    spare_keys_lost: _binary_sensor_state
    keys_lost: _binary_sensor_state
    iphone_lost: _binary_sensor_state
    opnsense_client: _binary_sensor_state
    opnsense_key_expiry_disabled: _binary_sensor_state
    opnsense_supports_hairpinning: _binary_sensor_state
    opnsense_supports_ipv6: _binary_sensor_state
    opnsense_supports_pcp: _binary_sensor_state
    opnsense_supports_nat_pmp: _binary_sensor_state
    opnsense_supports_udp: _binary_sensor_state
    opnsense_supports_upnp: _binary_sensor_state
    home_home_assistant: _binary_sensor_state
    freebsd_router: _binary_sensor_state
    laptop_ashton: _binary_sensor_state
    desktop_u5e7nrv_ashtonparrott_hotmail_com: _binary_sensor_state
    desktop_u5e7nrv_client: _binary_sensor_state
    desktop_u5e7nrv_key_expiry_disabled: _binary_sensor_state
    desktop_u5e7nrv_supports_hairpinning: _binary_sensor_state
    desktop_u5e7nrv_supports_ipv6: _binary_sensor_state
    desktop_u5e7nrv_supports_pcp: _binary_sensor_state
    desktop_u5e7nrv_supports_nat_pmp: _binary_sensor_state
    desktop_u5e7nrv_supports_udp: _binary_sensor_state
    desktop_u5e7nrv_supports_upnp: _binary_sensor_state
    plex_media_server_home_assistant: _binary_sensor_state
    system_monitor_process_nmap: _binary_sensor_state
    system_monitor_process_python3: _binary_sensor_state
    aurora_visibility_alert: _binary_sensor_state
    debian_dell_client: _binary_sensor_state
    debian_dell_key_expiry_disabled: _binary_sensor_state
    debian_dell_supports_hairpinning: _binary_sensor_state
    debian_dell_supports_ipv6: _binary_sensor_state
    debian_dell_supports_pcp: _binary_sensor_state
    debian_dell_supports_nat_pmp: _binary_sensor_state
    debian_dell_supports_udp: _binary_sensor_state
    debian_dell_supports_upnp: _binary_sensor_state
    opnsense_pending_notices_present: _binary_sensor_state
    home_assistant: _binary_sensor_state
    sun_solar_rising: _binary_sensor_state
    steam_wishlist_76561198025675241_arma_3: _binary_sensor_state
    steam_wishlist_76561198025675241_galaxy_on_fire_2tm_full_hd: _binary_sensor_state
    steam_wishlist_76561198025675241_ftl_faster_than_light: _binary_sensor_state
    steam_wishlist_76561198025675241_don_t_starve: _binary_sensor_state
    steam_wishlist_76561198025675241_towns: _binary_sensor_state
    steam_wishlist_76561198025675241_reus: _binary_sensor_state
    steam_wishlist_76561198025675241_octodad_dadliest_catch: _binary_sensor_state
    steam_wishlist_76561198025675241_wreckfest: _binary_sensor_state
    steam_wishlist_76561198025675241_deadfall_adventures: _binary_sensor_state
    steam_wishlist_76561198025675241_knights_of_pen_and_paper_1_edition: _binary_sensor_state
    steam_wishlist_76561198025675241_naruto_shippuden_ultimate_ninja_storm_3_full_burst_hd: _binary_sensor_state
    steam_wishlist_76561198025675241_metal_gear_rising_revengeance: _binary_sensor_state
    steam_wishlist_76561198025675241_middle_earthtm_shadow_of_mordortm: _binary_sensor_state
    steam_wishlist_76561198025675241_the_forest: _binary_sensor_state
    steam_wishlist_76561198025675241_banished: _binary_sensor_state
    steam_wishlist_76561198025675241_assetto_corsa: _binary_sensor_state
    steam_wishlist_76561198025675241_space_engineers: _binary_sensor_state
    steam_wishlist_76561198025675241_artemis_spaceship_bridge_simulator: _binary_sensor_state
    steam_wishlist_76561198025675241_7_days_to_die: _binary_sensor_state
    steam_wishlist_76561198025675241_yaiba_ninja_gaiden_z: _binary_sensor_state
    steam_wishlist_76561198025675241_x_plane_11: _binary_sensor_state
    steam_wishlist_76561198025675241_astebreed_definitive_edition: _binary_sensor_state
    steam_wishlist_76561198025675241_wildlife_park_3: _binary_sensor_state
    steam_wishlist_76561198025675241_metal_gear_solid_v_the_phantom_pain: _binary_sensor_state
    steam_wishlist_76561198025675241_life_is_feudal_your_own: _binary_sensor_state
    steam_wishlist_76561198025675241_valkyria_chroniclestm: _binary_sensor_state
    steam_wishlist_76561198025675241_wildlife_park_2: _binary_sensor_state
    steam_wishlist_76561198025675241_the_elder_scrolls_r_online: _binary_sensor_state
    steam_wishlist_76561198025675241_wildlife_park: _binary_sensor_state
    steam_wishlist_76561198025675241_spaceengine: _binary_sensor_state
    steam_wishlist_76561198025675241_frostpunk: _binary_sensor_state
    steam_wishlist_76561198025675241_rise_to_ruins: _binary_sensor_state
    steam_wishlist_76561198025675241_besiege: _binary_sensor_state
    steam_wishlist_76561198025675241_factorio: _binary_sensor_state
    steam_wishlist_76561198025675241_wallpaper_engine: _binary_sensor_state
    steam_wishlist_76561198025675241_surviving_mars: _binary_sensor_state
    steam_wishlist_76561198025675241_the_pedestrian: _binary_sensor_state
    steam_wishlist_76561198025675241_hackmud: _binary_sensor_state
    steam_wishlist_76561198025675241_human_fall_flat: _binary_sensor_state
    steam_wishlist_76561198025675241_uboat: _binary_sensor_state
    steam_wishlist_76561198025675241_totally_accurate_battle_simulator: _binary_sensor_state
    steam_wishlist_76561198025675241_half_life_alyx: _binary_sensor_state
    steam_wishlist_76561198025675241_warhammer_vermintide_2: _binary_sensor_state
    steam_wishlist_76561198025675241_far_cry_r_5: _binary_sensor_state
    steam_wishlist_76561198025675241_world_of_final_fantasy_r: _binary_sensor_state
    steam_wishlist_76561198025675241_danganronpa_v3_killing_harmony: _binary_sensor_state
    steam_wishlist_76561198025675241_stormworks_build_and_rescue: _binary_sensor_state
    steam_wishlist_76561198025675241_monster_hunter_world: _binary_sensor_state
    steam_wishlist_76561198025675241_barotrauma: _binary_sensor_state
    steam_wishlist_76561198025675241_accel_world_vs_sword_art_online_deluxe_edition: _binary_sensor_state
    steam_wishlist_76561198025675241_rec_center_tycoon_management_simulator: _binary_sensor_state
    steam_wishlist_76561198025675241_blade_and_sorcery: _binary_sensor_state
    steam_wishlist_76561198025675241_mordhau: _binary_sensor_state
    steam_wishlist_76561198025675241_devil_may_cry_hd_collection: _binary_sensor_state
    steam_wishlist_76561198025675241_pathfinder_kingmaker_enhanced_plus_edition: _binary_sensor_state
    steam_wishlist_76561198025675241_stream_avatars: _binary_sensor_state
    steam_wishlist_76561198025675241_rise_of_industry: _binary_sensor_state
    steam_wishlist_76561198025675241_code_vein: _binary_sensor_state
    steam_wishlist_76561198025675241_hell_let_loose: _binary_sensor_state
    steam_wishlist_76561198025675241_overcrowd_a_commute_em_up: _binary_sensor_state
    steam_wishlist_76561198025675241_temtem: _binary_sensor_state
    steam_wishlist_76561198025675241_contraband_police: _binary_sensor_state
    steam_wishlist_76561198025675241_smalland_survive_the_wilds: _binary_sensor_state
    steam_wishlist_76561198025675241_total_war_three_kingdoms: _binary_sensor_state
    steam_wishlist_76561198025675241_workers_resources_soviet_republic: _binary_sensor_state
    steam_wishlist_76561198025675241_phoenix_wright_ace_attorney_trilogy: _binary_sensor_state
    steam_wishlist_76561198025675241_valkyria_chronicles_4_complete_edition: _binary_sensor_state
    steam_wishlist_76561198025675241_plane_mechanic_simulator: _binary_sensor_state
    steam_wishlist_76561198025675241_cliff_empire: _binary_sensor_state
    steam_wishlist_76561198025675241_shortest_trip_to_earth: _binary_sensor_state
    steam_wishlist_76561198025675241_assassin_s_creed_r_odyssey: _binary_sensor_state
    steam_wishlist_76561198025675241_animal_well: _binary_sensor_state
    steam_wishlist_76561198025675241_warriors_orochi_4: _binary_sensor_state
    steam_wishlist_76561198025675241_sword_art_online_lost_song: _binary_sensor_state
    steam_wishlist_76561198025675241_dragon_ball_z_kakarot: _binary_sensor_state
    steam_wishlist_76561198025675241_bum_simulator: _binary_sensor_state
    steam_wishlist_76561198025675241_dawn_of_man: _binary_sensor_state
    steam_wishlist_76561198025675241_factory_town: _binary_sensor_state
    steam_wishlist_76561198025675241_songs_of_conquest: _binary_sensor_state
    steam_wishlist_76561198025675241_granblue_fantasy_relink: _binary_sensor_state
    steam_wishlist_76561198025675241_autonomica: _binary_sensor_state
    steam_wishlist_76561198025675241_spellcaster_university: _binary_sensor_state
    steam_wishlist_76561198025675241_kubifaktorium: _binary_sensor_state
    steam_wishlist_76561198025675241_meeple_station: _binary_sensor_state
    steam_wishlist_76561198025675241_wrench: _binary_sensor_state
    steam_wishlist_76561198025675241_among_us: _binary_sensor_state
    steam_wishlist_76561198025675241_cities_skylines_ii: _binary_sensor_state
    steam_wishlist_76561198025675241_volcanoids: _binary_sensor_state
    steam_wishlist_76561198025675241_resident_evil_3: _binary_sensor_state
    steam_wishlist_76561198025675241_grounded: _binary_sensor_state
    steam_wishlist_76561198025675241_foundry: _binary_sensor_state
    steam_wishlist_76561198025675241_hogwarts_legacy: _binary_sensor_state
    steam_wishlist_76561198025675241_kebab_chefs_restaurant_simulator: _binary_sensor_state
    steam_wishlist_76561198025675241_through_the_darkest_of_times: _binary_sensor_state
    steam_wishlist_76561198025675241_unrailed: _binary_sensor_state
    steam_wishlist_76561198025675241_going_medieval: _binary_sensor_state
    steam_wishlist_76561198025675241_crime_scene_cleaner: _binary_sensor_state
    steam_wishlist_76561198025675241_booze_masters_freezing_moonshine: _binary_sensor_state
    steam_wishlist_76561198025675241_this_land_is_my_land: _binary_sensor_state
    steam_wishlist_76561198025675241_dragon_quest_builderstm_2: _binary_sensor_state
    steam_wishlist_76561198025675241_baldur_s_gate_3: _binary_sensor_state
    steam_wishlist_76561198025675241_car_mechanic_simulator_vr: _binary_sensor_state
    steam_wishlist_76561198025675241_rebel_inc_escalation: _binary_sensor_state
    steam_wishlist_76561198025675241_cyberpunk_2077: _binary_sensor_state
    steam_wishlist_76561198025675241_florence: _binary_sensor_state
    steam_wishlist_76561198025675241_founders_fortune: _binary_sensor_state
    steam_wishlist_76561198025675241_outbrk: _binary_sensor_state
    steam_wishlist_76561198025675241_bot_studio_for_discord: _binary_sensor_state
    steam_wishlist_76561198025675241_stationflow: _binary_sensor_state
    steam_wishlist_76561198025675241_mindustry: _binary_sensor_state
    steam_wishlist_76561198025675241_hades_ii: _binary_sensor_state
    steam_wishlist_76561198025675241_not_for_broadcast: _binary_sensor_state
    steam_wishlist_76561198025675241_horizon_zero_dawntm_complete_edition: _binary_sensor_state
    steam_wishlist_76561198025675241_master_of_pottery: _binary_sensor_state
    steam_wishlist_76561198025675241_daemon_x_machina: _binary_sensor_state
    steam_wishlist_76561198025675241_star_wars_jedi_fallen_ordertm: _binary_sensor_state
    steam_wishlist_76561198025675241_dune_awakening: _binary_sensor_state
    steam_wishlist_76561198025675241_little_kitty_big_city: _binary_sensor_state
    steam_wishlist_76561198025675241_meet_your_maker: _binary_sensor_state
    steam_wishlist_76561198025675241_elden_ring: _binary_sensor_state
    steam_wishlist_76561198025675241_ships_at_sea: _binary_sensor_state
    steam_wishlist_76561198025675241_the_planet_crafter: _binary_sensor_state
    steam_wishlist_76561198025675241_tiny_tina_s_wonderlands: _binary_sensor_state
    steam_wishlist_76561198025675241_powerwash_simulator: _binary_sensor_state
    steam_wishlist_76561198025675241_cult_of_the_lamb: _binary_sensor_state
    steam_wishlist_76561198025675241_risk_of_rain_returns: _binary_sensor_state
    steam_wishlist_76561198025675241_manor_lords: _binary_sensor_state
    steam_wishlist_76561198025675241_audiotheory_grids: _binary_sensor_state
    steam_wishlist_76561198025675241_myth_of_empires: _binary_sensor_state
    steam_wishlist_76561198025675241_naval_action_navy_connection: _binary_sensor_state
    steam_wishlist_76561198025675241_sand: _binary_sensor_state
    steam_wishlist_76561198025675241_junxions: _binary_sensor_state
    steam_wishlist_76561198025675241_pacific_drive: _binary_sensor_state
    steam_wishlist_76561198025675241_snowrunner: _binary_sensor_state
    steam_wishlist_76561198025675241_the_crust: _binary_sensor_state
    steam_wishlist_76561198025675241_seablip: _binary_sensor_state
    steam_wishlist_76561198025675241_monsters_briefcase_and_road: _binary_sensor_state
    steam_wishlist_76561198025675241_depersonalization: _binary_sensor_state
    steam_wishlist_76561198025675241_sker_ritual: _binary_sensor_state
    steam_wishlist_76561198025675241_wartales: _binary_sensor_state
    steam_wishlist_76561198025675241_echoes_of_the_plum_grove: _binary_sensor_state
    steam_wishlist_76561198025675241_outpost_infinity_siege: _binary_sensor_state
    steam_wishlist_76561198025675241_dread_delusion: _binary_sensor_state
    steam_wishlist_76561198025675241_v_rising: _binary_sensor_state
    steam_wishlist_76561198025675241_warno: _binary_sensor_state
    steam_wishlist_76561198025675241_still_wakes_the_deep: _binary_sensor_state
    steam_wishlist_76561198025675241_love_ghostie: _binary_sensor_state
    steam_wishlist_76561198025675241_nine_sols: _binary_sensor_state
    steam_wishlist_76561198025675241_bellwright: _binary_sensor_state
    steam_wishlist_76561198025675241_hi_fi_rush: _binary_sensor_state
    steam_wishlist_76561198025675241_death_stranding_director_s_cut: _binary_sensor_state
    steam_wishlist_76561198025675241_norland: _binary_sensor_state
    steam_wishlist_76561198025675241_dave_the_diver: _binary_sensor_state
    steam_wishlist_76561198025675241_reus_2: _binary_sensor_state
    steam_wishlist_76561198025675241_jujutsu_kaisen_cursed_clash: _binary_sensor_state
    steam_wishlist_76561198025675241_aska: _binary_sensor_state
    steam_wishlist_76561198025675241_nightingale: _binary_sensor_state
    steam_wishlist_76561198025675241_nobody_wants_to_die: _binary_sensor_state
    steam_wishlist_76561198025675241_dungeons_of_hinterberg: _binary_sensor_state
    steam_wishlist_76561198025675241_call_of_duty_r_black_ops_cold_war: _binary_sensor_state
    steam_wishlist_76561198025675241_pax_dei: _binary_sensor_state
    steam_wishlist_76561198025675241_roadcraft: _binary_sensor_state
    steam_wishlist_76561198025675241_fields_of_mistria: _binary_sensor_state
    steam_wishlist_76561198025675241_granblue_fantasy_versus_rising: _binary_sensor_state
    steam_wishlist_76561198025675241_persona_3_reload: _binary_sensor_state
    steam_wishlist_76561198025675241_warhammer_40000_space_marine_2: _binary_sensor_state
    steam_wishlist_76561198025675241_warhammer_40000_rogue_trader: _binary_sensor_state
    steam_wishlist_76561198025675241_tiny_terry_s_turbo_trip: _binary_sensor_state
    steam_wishlist_76561198025675241_monster_hunter_wilds: _binary_sensor_state
    steam_wishlist_76561198025675241_metropolis_1998: _binary_sensor_state
    steam_wishlist_76561198025675241_mini_airways: _binary_sensor_state
    steam_wishlist_76561198025675241_farming_simulator_25: _binary_sensor_state
    steam_wishlist_76561198025675241_destiny_2_the_final_shape: _binary_sensor_state
    steam_wishlist_76561198025675241_black_myth_wukong: _binary_sensor_state
    steam_wishlist_76561198025675241_far_cry_r_6: _binary_sensor_state
    steam_wishlist_76561198025675241_solo_leveling_arise_overdrive: _binary_sensor_state
    steam_wishlist_76561198025675241_like_a_dragon_gaiden_the_man_who_erased_his_name: _binary_sensor_state
    steam_wishlist_76561198025675241_tony_hawk_stm_pro_skatertm_1_2: _binary_sensor_state
    steam_wishlist_76561198025675241_bodycam: _binary_sensor_state
    steam_wishlist_76561198025675241_horizon_forbidden_westtm_complete_edition: _binary_sensor_state
    steam_wishlist_76561198025675241_inzoi: _binary_sensor_state
    steam_wishlist_76561198025675241_senuas_saga_hellblade_ii: _binary_sensor_state
    steam_wishlist_76561198025675241_expeditions_a_mudrunner_game: _binary_sensor_state
    steam_wishlist_76561198025675241_gray_zone_warfare: _binary_sensor_state
    steam_wishlist_76561198025675241_f1_r_24: _binary_sensor_state
    steam_wishlist_76561198025675241_little_known_galaxy: _binary_sensor_state
    steam_wishlist_76561198025675241_eden_crafters: _binary_sensor_state
    steam_wishlist_76561198025675241_duck_detective_the_secret_salami: _binary_sensor_state
    steam_wishlist_76561198025675241_five_nights_at_freddy_s_into_the_pit: _binary_sensor_state
    steam_wishlist_76561198025675241_soulmask: _binary_sensor_state
    steam_wishlist_76561198025675241_sam_max_the_devil_s_playhouse: _binary_sensor_state
    steam_wishlist_76561198025675241_marvel_s_spider_man_2: _binary_sensor_state
    steam_wishlist_76561198025675241_supermarket_simulator: _binary_sensor_state
    steam_wishlist_76561198025675241_contractville: _binary_sensor_state
    steam_wishlist_76561198025675241_the_crew_motorfest: _binary_sensor_state
    steam_wishlist_76561198025675241_rooftops_alleys_the_parkour_game: _binary_sensor_state
    steam_wishlist_76561198025675241_mad_island: _binary_sensor_state
    steam_wishlist_76561198025675241_tavern_manager_simulator: _binary_sensor_state
    steam_wishlist_76561198025675241_lockdown_protocol: _binary_sensor_state
    steam_wishlist_76561198025675241_avatar_frontiers_of_pandoratm: _binary_sensor_state
    steam_wishlist_76561198025675241_content_warning: _binary_sensor_state
    steam_wishlist_76561198025675241_grocery_store_simulator: _binary_sensor_state
    steam_wishlist_76561198025675241_pilgrim: _binary_sensor_state
    steam_wishlist_76561198025675241_doom_the_dark_ages: _binary_sensor_state
    steam_wishlist_76561198025675241_crosswind: _binary_sensor_state
    steam_wishlist_76561198025675241_schedule_i: _binary_sensor_state
    steam_wishlist_76561198025675241_paradise: _binary_sensor_state
    steam_wishlist_76561198025675241_the_hidden_ones: _binary_sensor_state
    steam_wishlist_76561198025675241_the_seven_deadly_sins_origin: _binary_sensor_state
    ythsaz_subscribed_to_playstation_plus: _binary_sensor_state
    syth_local_browser_fullykiosk: _binary_sensor_state
    syth_local_browser_dark_mode: _binary_sensor_state
    syth_local: _binary_sensor_state
    desktop_browser_fullykiosk: _binary_sensor_state
    desktop_browser_dark_mode: _binary_sensor_state
    desktop: _binary_sensor_state
    laptop_browser_fullykiosk: _binary_sensor_state
    laptop_browser_dark_mode: _binary_sensor_state
    laptop: _binary_sensor_state
    syth_tailscale_browser_fullykiosk: _binary_sensor_state
    syth_tailscale_browser_dark_mode: _binary_sensor_state
    syth_tailscale: _binary_sensor_state
    steam_wishlist_76561198025675241_crisisx: _binary_sensor_state
    steam_wishlist_76561198025675241_caravanners_co_op_open_world_camping: _binary_sensor_state
    steam_wishlist_76561198025675241_drug_schedule: _binary_sensor_state
    steam_wishlist_76561198025675241_openfront: _binary_sensor_state
    back_alley_all_occupancy: _binary_sensor_state
    backyard_all_occupancy: _binary_sensor_state
    backyard_fence_person_occupancy: _binary_sensor_state
    alley_speed_person_occupancy: _binary_sensor_state
    parking_pad_person_occupancy: _binary_sensor_state
    backyard_camera_hq_person_occupancy: _binary_sensor_state
    back_alley_person_occupancy: _binary_sensor_state
    backyard_person_occupancy: _binary_sensor_state
    backyard_fence_all_occupancy: _binary_sensor_state
    parking_pad_all_occupancy: _binary_sensor_state
    alley_speed_all_occupancy: _binary_sensor_state
    backyard_camera_hq_all_occupancy: _binary_sensor_state
    backyard_camera_hq_shatter_sound: _binary_sensor_state
    backyard_camera_hq_bark_sound: _binary_sensor_state
    backyard_camera_hq_smoke_detector_sound: _binary_sensor_state
    backyard_camera_hq_glass_sound: _binary_sensor_state
    backyard_camera_hq_yell_sound: _binary_sensor_state
    backyard_camera_hq_scream_sound: _binary_sensor_state
    backyard_camera_hq_fire_alarm_sound: _binary_sensor_state
    backyard_camera_hq_speech_sound: _binary_sensor_state
    backyard_camera_hq_motion: _binary_sensor_state
    plex_media_server_debian_dell: _binary_sensor_state
    sound_forge_audio_studio_14_steam_wishlist_edition: _binary_sensor_state
    system_monitor_process_go2rtc: _binary_sensor_state
    astroweather_backyard_deep_sky_view: _binary_sensor_state
    astroweather_backyard_moon_rises_during_darkness: _binary_sensor_state
    astroweather_backyard_moon_sets_during_darkness: _binary_sensor_state
    astroweather_backyard_moon_always_up_during_darkness: _binary_sensor_state
    astroweather_backyard_moon_always_down_during_darkness: _binary_sensor_state
    moon_astro_none: _binary_sensor_state
    pypi_none: _binary_sensor_state
    backyard_fence_dog_occupancy: _binary_sensor_state
    alley_speed_dog_occupancy: _binary_sensor_state
    back_alley_cat_occupancy: _binary_sensor_state
    backyard_camera_hq_motorcycle_occupancy: _binary_sensor_state
    backyard_camera_hq_car_occupancy: _binary_sensor_state
    parking_pad_motorcycle_occupancy: _binary_sensor_state
    backyard_cat_occupancy: _binary_sensor_state
    parking_pad_car_occupancy: _binary_sensor_state
    back_alley_motorcycle_occupancy: _binary_sensor_state
    back_alley_car_occupancy: _binary_sensor_state
    backyard_fence_cat_occupancy: _binary_sensor_state
    alley_speed_cat_occupancy: _binary_sensor_state
    backyard_fence_bicycle_occupancy: _binary_sensor_state
    backyard_motorcycle_occupancy: _binary_sensor_state
    backyard_camera_hq_bicycle_occupancy: _binary_sensor_state
    parking_pad_bicycle_occupancy: _binary_sensor_state
    backyard_car_occupancy: _binary_sensor_state
    backyard_camera_hq_dog_occupancy: _binary_sensor_state
    back_alley_bicycle_occupancy: _binary_sensor_state
    parking_pad_dog_occupancy: _binary_sensor_state
    alley_speed_car_occupancy: _binary_sensor_state
    backyard_fence_motorcycle_occupancy: _binary_sensor_state
    alley_speed_motorcycle_occupancy: _binary_sensor_state
    backyard_fence_car_occupancy: _binary_sensor_state
    back_alley_dog_occupancy: _binary_sensor_state
    backyard_bicycle_occupancy: _binary_sensor_state
    backyard_camera_hq_cat_occupancy: _binary_sensor_state
    backyard_dog_occupancy: _binary_sensor_state
    parking_pad_cat_occupancy: _binary_sensor_state
    alley_speed_bicycle_occupancy: _binary_sensor_state
    ipad_local_browser_fullykiosk: _binary_sensor_state
    ipad_local_browser_dark_mode: _binary_sensor_state
    ipad_local: _binary_sensor_state
    ipad_focus: _binary_sensor_state
    local_status: _binary_sensor_state
    plex_status: _binary_sensor_state
    frigate_status: _binary_sensor_state
    portainer_status: _binary_sensor_state
    whisper_status: _binary_sensor_state
    esphome_status: _binary_sensor_state
    tasmoadmin_status: _binary_sensor_state
    watchtower_status: _binary_sensor_state
    piper_status: _binary_sensor_state
    music_assistant_status: _binary_sensor_state
    nodered_status: _binary_sensor_state
    homeassistant_status: _binary_sensor_state
    scrutiny_status: _binary_sensor_state
    bedroom_closet_door_opening: _binary_sensor_state
    furnace_room_door_opening: _binary_sensor_state
    timescaledb_poc_status: _binary_sensor_state
    opnsense_exporter_status: _binary_sensor_state
    postgres_exporter_status: _binary_sensor_state
    prometheus_status: _binary_sensor_state
    grafana_status: _binary_sensor_state
    core_ha_dev_1_status: _binary_sensor_state
    system_monitor_process_docker: _binary_sensor_state
    bedroom_closet_door_battery_plus_low: _binary_sensor_state
    furnace_room_door_battery_plus_low: _binary_sensor_state
    ipad_battery_plus_low: _binary_sensor_state
    s9_battery_plus_low: _binary_sensor_state
    syth_battery_plus_low: _binary_sensor_state
    telegram_client_zashtys_restricted: _binary_sensor_state
    telegram_client_zashtys_premium: _binary_sensor_state
    steam_wishlist_76561198025675241_animula_nook: _binary_sensor_state
    wordpress_wordpress_1_status: _binary_sensor_state
    wordpress_db_1_status: _binary_sensor_state
    mailcowdockerized_watchdog_mailcow_1_status: _binary_sensor_state
    mailcowdockerized_acme_mailcow_1_status: _binary_sensor_state
    mailcowdockerized_nginx_mailcow_1_status: _binary_sensor_state
    mailcowdockerized_rspamd_mailcow_1_status: _binary_sensor_state
    mailcowdockerized_ofelia_mailcow_1_status: _binary_sensor_state
    mailcowdockerized_php_fpm_mailcow_1_status: _binary_sensor_state
    mailcowdockerized_dovecot_mailcow_1_status: _binary_sensor_state
    mailcowdockerized_postfix_mailcow_1_status: _binary_sensor_state
    mailcowdockerized_mysql_mailcow_1_status: _binary_sensor_state
    mailcowdockerized_clamd_mailcow_1_status: _binary_sensor_state
    mailcowdockerized_redis_mailcow_1_status: _binary_sensor_state
    mailcowdockerized_postfix_tlspol_mailcow_1_status: _binary_sensor_state
    mailcowdockerized_sogo_mailcow_1_status: _binary_sensor_state
    mailcowdockerized_olefy_mailcow_1_status: _binary_sensor_state
    mailcowdockerized_netfilter_mailcow_1_status: _binary_sensor_state
    mailcowdockerized_portainer_mailcow_1_status: _binary_sensor_state
    mailcowdockerized_memcached_mailcow_1_status: _binary_sensor_state
    mailcowdockerized_unbound_mailcow_1_status: _binary_sensor_state
    mailcowdockerized_dockerapi_mailcow_1_status: _binary_sensor_state
    steam_wishlist_76561198025675241_sand_raiders_of_sophie: _binary_sensor_state
    steam_wishlist_76561198025675241_caravanners: _binary_sensor_state
    system_monitor_process_s6_ipcserverd: _binary_sensor_state
    system_monitor_process_s6_svscan: _binary_sensor_state
    zashtys: _binary_sensor_state
    zashtys_in_game: _binary_sensor_state
    zashtys_subscribed_to_xbox_game_pass: _binary_sensor_state
    steam_wishlist_76561198025675241_windrose: _binary_sensor_state
    steam_wishlist_76561198025675241_timberborn: _binary_sensor_state
    steam_wishlist_76561198025675241_nier_replicanttm_ver_1_22474487139: _binary_sensor_state
    steam_wishlist_76561198025675241_clair_obscur_expedition_33: _binary_sensor_state
    steam_wishlist_76561198025675241_two_point_museum: _binary_sensor_state
    steam_wishlist_76561198025675241_dispatch: _binary_sensor_state
    steam_wishlist_76561198025675241_enginefall: _binary_sensor_state
    steam_wishlist_76561198025675241_kingdom_come_deliverance_ii: _binary_sensor_state
    steam_wishlist_76561198025675241_peak: _binary_sensor_state
    steam_wishlist_76561198025675241_the_witcher_3_wild_hunt: _binary_sensor_state
    steam_wishlist_76561198025675241_waterpark_simulator: _binary_sensor_state
    steam_wishlist_76561198025675241_powerwash_simulator_2: _binary_sensor_state
    steam_wishlist_76561198025675241_construction_simulator: _binary_sensor_state
    steam_wishlist_76561198025675241_voyagers_of_nera: _binary_sensor_state
    steam_wishlist_76561198025675241_is_this_seat_taken: _binary_sensor_state
    steam_wishlist_76561198025675241_a_little_to_the_left: _binary_sensor_state
    steam_wishlist_76561198025675241_rv_there_yet: _binary_sensor_state
    steam_wishlist_76561198025675241_battlefieldtm_6: _binary_sensor_state
    steam_wishlist_76561198025675241_elden_ring_nightreign: _binary_sensor_state
    steam_wishlist_76561198025675241_hollow_knight_silksong: _binary_sensor_state
    steam_wishlist_76561198025675241_final_fantasy_tactics_the_ivalice_chronicles: _binary_sensor_state
    steam_wishlist_76561198025675241_the_outer_worlds_2: _binary_sensor_state
    steam_wishlist_76561198025675241_megabonk: _binary_sensor_state
    steam_wishlist_76561198025675241_blue_prince: _binary_sensor_state
    steam_wishlist_76561198025675241_ancient_farm: _binary_sensor_state
    steam_wishlist_76561198025675241_dunecrawl: _binary_sensor_state
    steam_wishlist_76561198025675241_quarantine_zone_the_last_check: _binary_sensor_state
    steam_wishlist_76561198025675241_craftlings: _binary_sensor_state
    steam_wishlist_76561198025675241_earth_of_oryn: _binary_sensor_state
    steam_wishlist_76561198025675241_factory_planner: _binary_sensor_state
    steam_wishlist_76561198025675241_tailside_cozy_cafe_sim: _binary_sensor_state
    steam_wishlist_76561198025675241_nova_roma: _binary_sensor_state
    steam_wishlist_76561198025675241_bladesong: _binary_sensor_state
    steam_wishlist_76561198025675241_the_gold_river_project: _binary_sensor_state
    steam_wishlist_76561198025675241_escape_from_ever_after: _binary_sensor_state
    steam_wishlist_76561198025675241_adaptory: _binary_sensor_state
    steam_wishlist_76561198025675241_car_service_together: _binary_sensor_state
    steam_wishlist_76561198025675241_code_vein_ii: _binary_sensor_state
    steam_wishlist_76561198025675241_cairn: _binary_sensor_state
    steam_wishlist_76561198025675241_pax_autocratica: _binary_sensor_state
    steam_wishlist_76561198025675241_mewgenics: _binary_sensor_state
    steam_wishlist_76561198025675241_lost_and_found_co: _binary_sensor_state
    steam_wishlist_76561198025675241_chromagun_2_dye_hard: _binary_sensor_state
    steam_wishlist_76561198025675241_astrobotanica: _binary_sensor_state
    steam_wishlist_76561198025675241_office_simulator: _binary_sensor_state
    steam_wishlist_76561198025675241_food_processing_simulator: _binary_sensor_state
    steam_wishlist_76561198025675241_big_hops: _binary_sensor_state
    steam_wishlist_76561198025675241_magic_forge_tycoon: _binary_sensor_state
    steam_wishlist_76561198025675241_isekai_adventurer_guild: _binary_sensor_state
    steam_wishlist_76561198025675241_moving_simulator: _binary_sensor_state
    steam_wishlist_76561198025675241_apocalypse_factory: _binary_sensor_state
    steam_wishlist_76561198025675241_exotica_2_pet_shop_simulator: _binary_sensor_state
    steam_wishlist_76561198025675241_rogue_factory: _binary_sensor_state
    steam_wishlist_76561198025675241_gridle: _binary_sensor_state
    steam_wishlist_76561198025675241_my_tiny_garden: _binary_sensor_state
    steam_wishlist_76561198025675241_unemployment_simulator_2018: _binary_sensor_state
    steam_wishlist_76561198025675241_scaling_up: _binary_sensor_state
    steam_wishlist_76561198025675241_fields_of_fortune: _binary_sensor_state
    steam_wishlist_76561198025675241_the_jackbox_party_pack_11: _binary_sensor_state
    steam_wishlist_76561198025675241_minemogul: _binary_sensor_state
    steam_wishlist_76561198025675241_jurassic_world_evolution_3: _binary_sensor_state
    steam_wishlist_76561198025675241_dying_light_the_beast: _binary_sensor_state
    steam_wishlist_76561198025675241_digimon_story_time_stranger: _binary_sensor_state
    steam_wishlist_76561198025675241_path_of_exile_2: _binary_sensor_state
    steam_wishlist_76561198025675241_the_last_caretaker: _binary_sensor_state
    steam_wishlist_76561198025675241_anno_117_pax_romana: _binary_sensor_state
    steam_wishlist_76561198025675241_silent_hill_f: _binary_sensor_state
    jusparr: _binary_sensor_state
    jusparr_in_game: _binary_sensor_state
    jusparr_subscribed_to_xbox_game_pass: _binary_sensor_state
    sig1325: _binary_sensor_state
    sig1325_subscribed_to_xbox_game_pass: _binary_sensor_state
    mrcolvan1: _binary_sensor_state
    mrcolvan1_in_game: _binary_sensor_state
    mrcolvan1_subscribed_to_xbox_game_pass: _binary_sensor_state
    maxdeath397: _binary_sensor_state
    maxdeath397_in_game: _binary_sensor_state
    maxdeath397_subscribed_to_xbox_game_pass: _binary_sensor_state
    steam_wishlist_76561198025675241_autonomica_survival_automation: _binary_sensor_state
    steam_wishlist_76561198025675241_the_settlers_r_new_allies: _binary_sensor_state
    steam_wishlist_76561198025675241_eco: _binary_sensor_state
    mastodon_sythsaz_mastodon_social_bot: _binary_sensor_state
    mastodon_sythsaz_mastodon_social_discoverable: _binary_sensor_state
    mastodon_sythsaz_mastodon_social_locked: _binary_sensor_state
    mastodon_sythsaz_mastodon_social_moved: _binary_sensor_state
    steam_wishlist_76561198025675241_project_rebearth: _binary_sensor_state
    psn_api_key_for_ha_expiration: _binary_sensor_state
    jusparr_docker_status: _binary_sensor_state
    portainer_agent_status: _binary_sensor_state
    ha_esphome_1_status: _binary_sensor_state
    ha_watchtower_1_status: _binary_sensor_state
    ha_whisper_1_status: _binary_sensor_state
    ha_piper_1_status: _binary_sensor_state
    ha_aircast_1_status: _binary_sensor_state
    ha_scrutiny_1_status: _binary_sensor_state
    mediamtx_status: _binary_sensor_state
    opnsense_wan_status: _binary_sensor_state
    ha_nodered_1_status: _binary_sensor_state
    s9_plus_android_auto: _binary_sensor_state
    s9_plus_app_inactive: _binary_sensor_state
    s9_plus_headphones: _binary_sensor_state
    s9_plus_mic_muted: _binary_sensor_state
    s9_plus_speakerphone: _binary_sensor_state
    s9_plus_music_active: _binary_sensor_state
    s9_plus_is_charging: _binary_sensor_state
    s9_plus_bluetooth_state: _binary_sensor_state
    s9_plus_work_profile: _binary_sensor_state
    s9_plus_device_locked: _binary_sensor_state
    s9_plus_device_secure: _binary_sensor_state
    s9_plus_keyguard_locked: _binary_sensor_state
    s9_plus_keyguard_secure: _binary_sensor_state
    s9_plus_high_accuracy_mode: _binary_sensor_state
    s9_plus_mobile_data: _binary_sensor_state
    s9_plus_mobile_data_roaming: _binary_sensor_state
    s9_plus_wi_fi_state: _binary_sensor_state
    s9_plus_hotspot_state: _binary_sensor_state
    s9_plus_nfc_state: _binary_sensor_state
    s9_plus_interactive: _binary_sensor_state
    s9_plus_doze_mode: _binary_sensor_state
    s9_plus_power_save: _binary_sensor_state
    samsung_sm_g991w_client: _binary_sensor_state
    samsung_sm_g991w_key_expiry_disabled: _binary_sensor_state
    samsung_sm_g991w_supports_ipv6: _binary_sensor_state
    samsung_sm_g991w_supports_pcp: _binary_sensor_state
    samsung_sm_g991w_supports_nat_pmp: _binary_sensor_state
    samsung_sm_g991w_supports_udp: _binary_sensor_state
    samsung_sm_g991w_supports_upnp: _binary_sensor_state
    browser_mod_c9a5c39b_a64fa6bd_browser_fullykiosk: _binary_sensor_state
    browser_mod_c9a5c39b_a64fa6bd_browser_dark_mode: _binary_sensor_state
    browser_mod_c9a5c39b_a64fa6bd: _binary_sensor_state
    zashtys_satellite_rpi_mqtt_monitor: _binary_sensor_state
    mediamtx_status_2: _binary_sensor_state
    wordpress_wordpress_1_status_2: _binary_sensor_state
    homeassistant_status_2: _binary_sensor_state
    plex_status_2: _binary_sensor_state
    aircast_status_2: _binary_sensor_state
    wordpress_db_1_status_2: _binary_sensor_state
    music_assistant_status_2: _binary_sensor_state
    tasmoadmin_status_2: _binary_sensor_state
    nodered_status_2: _binary_sensor_state
    esphome_status_2: _binary_sensor_state
    frigate_status_2: _binary_sensor_state
    portainer_status_2: _binary_sensor_state
    watchtower_status_2: _binary_sensor_state
    scrutiny_status_2: _binary_sensor_state
    piper_status_2: _binary_sensor_state
    whisper_status_2: _binary_sensor_state
    ha_aircast_1_status_2: _binary_sensor_state
    ha_nodered_1_status_2: _binary_sensor_state
    ha_esphome_1_status_2: _binary_sensor_state
    portainer_agent_status_2: _binary_sensor_state
    ha_watchtower_1_status_2: _binary_sensor_state
    ha_whisper_1_status_2: _binary_sensor_state
    ha_piper_1_status_2: _binary_sensor_state
    ha_scrutiny_1_status_2: _binary_sensor_state
    home_assistant_main_status: _binary_sensor_state
    timescale_db_status: _binary_sensor_state
    wordpress_status: _binary_sensor_state
    rtmp_relay_status: _binary_sensor_state
    rtmp_relay_status_2: _binary_sensor_state
    steam_wishlist_76561198025675241_dying_light_the_beast_restored_land: _binary_sensor_state

class blueprint:
    ...

class bluesky:

    @staticmethod
    def post(*, message):
        """Post a message to Bluesky

        Args:
            message: The message to post to Bluesky Example: Hello, Bluesky!"""
        ...

class browser_mod:

    @staticmethod
    def sequence(*, browser_id=None, user_id: str | None=None, sequence: Any | None=None):
        """Run a sequence of services

        Args:
            sequence: List of services to run"""
        ...

    @staticmethod
    def delay(*, browser_id=None, user_id: str | None=None, time: float | None=None):
        """Wait for a time

        Args:
            time: Time to wait (ms)"""
        ...

    @staticmethod
    def popup(*, content: Any, browser_id=None, user_id: str | None=None, popup_card_id: str | None=None, title: str | None=None, adaptive: bool | None=None, adaptive_allow_mode_change: bool | None=None, adaptive_force_bottom_sheet: bool | None=None, initial_style: Literal['', 'normal', 'classic', 'wide', 'fullscreen'] | None=None, style_sequence: Literal['', 'initial', 'normal', 'classic', 'wide', 'fullscreen'] | None=None, popup_styles: Any | None=None, right_button: str | None=None, right_button_variant: Literal['', 'brand', 'neutral', 'danger', 'warning', 'success'] | None=None, right_button_appearance: Literal['', 'accent', 'filled', 'outlined', 'plain'] | None=None, right_button_action: Any | None=None, left_button: str | None=None, left_button_variant: Literal['', 'brand', 'neutral', 'danger', 'warning', 'success'] | None=None, left_button_appearance: Literal['', 'accent', 'filled', 'outlined', 'plain'] | None=None, left_button_action: Any | None=None, dismissable: bool=True, dismiss_action: Any | None=None, autoclose: bool=False, timeout: float | None=None, timeout_action: Any | None=None, timeout_hide_progress: bool | None=None, tag: str | None=None):
        """Display a popup

        Args:
            content: Popup content (Text or lovelace card configuration)
            popup_card_id: ID of the popup-card to use as a template for the popup
            title: Popup title
            adaptive: Use adaptive dialog instead of standard dialog.
            adaptive_allow_mode_change: Allow adaptive dialog to continually change between standard and adaptive mode based on screen size instead of only on open. This can be used to make the popup responsive to screen size changes while open but may cause issues with content or styles.
            adaptive_force_bottom_sheet: Force the popup to always open as a bottom sheet when in adaptive mode.
            initial_style: Initial style to apply to the popup
            style_sequence: Sequence of styles to cycle through when user taps the title or with browser_mod.set_popup_style service
            popup_styles: Popup styles to apply. Use 'all' to always apply the style. You can add to standard styles or create your own
            right_button: Text of the right button
            right_button_variant: Variant of the right button
            right_button_appearance: Appearance of the right button
            right_button_action: Action to perform when the right button is pressed
            left_button: Text of the left button
            left_button_variant: Variant of the left button
            left_button_appearance: Appearance of the left button
            left_button_action: Action to perform when left button is pressed
            dismissable: Whether the popup can be closed by the user without action
            dismiss_action: Action to perform when popup is dismissed
            autoclose: Close the popup automatically on mouse, pointer or keyboard activity
            timeout: Time before closing (ms)
            timeout_action: Action to perform when popup is closed by timeout
            timeout_hide_progress: Hide timeout progress bar
            tag: Tag for managing multiple popups"""
        ...

    @staticmethod
    def more_info(*, browser_id=None, user_id: str | None=None, entity: str | None=None, view: Literal['', 'info', 'history', 'settings', 'related'] | None=None, large: bool=False, ignore_popup_card: bool=False, close: bool=False):
        """Show more-info dialog

        Args:
            view: More-info view to show
            close: Close the more-info dialog if open"""
        ...

    @staticmethod
    def close_popup(*, browser_id=None, user_id: str | None=None, all: bool=False, tag: str | None=None):
        """Close a popup

        Args:
            all: Close all Browser Mod popups on the browser
            tag: Tag for popup to close when using multiple popups"""
        ...

    @staticmethod
    def set_popup_style(*, browser_id=None, user_id: str | None=None, all: bool=False, tag: str | None=None, style: Literal['', 'normal', 'classic', 'wide', 'fullscreen'] | None=None, direction: Literal['', 'forward', 'back'] | None=None):
        """Set the style of a popup

        Args:
            all: Set style for all open Browser Mod popups on the browser
            tag: Tag for popup to set style for when using multiple popups
            style: Style to apply to the popup
            direction: Direction to cycle through style sequence"""
        ...

    @staticmethod
    def notification(*, message: str, browser_id=None, user_id: str | None=None, duration: float | None=None, action_text: str | None=None, action: Any | None=None):
        """Display a short notification

        Args:
            message: Message to display
            duration: Time before closing (ms)
            action_text: Text of optional action button
            action: Action to perform when the action button is pressed"""
        ...

    @staticmethod
    def navigate(*, browser_id=None, user_id: str | None=None, path: str | None=None):
        """Navigate browser to a different page

        Args:
            path: Target path"""
        ...

    @staticmethod
    def refresh(*, browser_id=None, user_id: str | None=None):
        """Refresh page"""
        ...

    @staticmethod
    def change_browser_id(*, current_browser_id=None, new_browser_id: str | None=None, register: bool | None=None, refresh: bool=True):
        """Change browser ID

        Args:
            current_browser_id: Current Browser ID of the browser to change
            new_browser_id: New Browser ID for the browser
            register: Register the browser
            refresh: Refresh the browser after changing the ID"""
        ...

    @staticmethod
    def set_theme(*, browser_id=None, user_id: str | None=None, theme: str | None=None, dark: Literal['', 'auto', 'light', 'dark'] | None=None, primaryColor: tuple[int, int, int] | None=None, accentColor: tuple[int, int, int] | None=None):
        """Change the current theme

        Args:
            theme: Name of theme or 'auto'
            dark: Dark/light mode
            primaryColor: Primary theme color
            accentColor: Accent theme color"""
        ...

    @staticmethod
    def console(*, browser_id=None, user_id: str | None=None, message: str | None=None):
        """Print text to browser console

        Args:
            message: Text to print"""
        ...

    @staticmethod
    def javascript(*, browser_id=None, user_id: str | None=None, code: Any | None=None):
        """Run arbitrary JavaScript code

        Args:
            code: JavaScript code to run"""
        ...

    @staticmethod
    def deregister_browser(*, browser_id=None, browser_id_exclude=None, area_id_exclude=None):
        """Deregister a browser. Include at leaset one paremeter. Calling wiith either exclude parameter will deregister all browsers except those excluded.

        Args:
            browser_id_exclude: Exclude browser from deregister
            area_id_exclude: Exclude browsers in area from deregister"""
        ...

class _button_state(StateVal):
    restored: bool
    supported_features: int

    def press(self):
        ...

class button:
    homeassistant_restart: _button_state
    homeassistant_reload: _button_state
    ignore_all_issues: _button_state
    unignore_all_issues: _button_state
    clear_additional_tracked: _button_state
    wake_on_lan_b8_ca_3a_93_bf_d3: _button_state
    reboot: _button_state
    reboot_2: _button_state
    restart_wifi: _button_state
    debian_dell_scan_clients: _button_state
    desktop_wake_on_lan: _button_state
    bedroom_speaker_favorite_current_song: _button_state
    bathroom_favorite_current_song: _button_state
    bed_and_bath_favorite_current_song: _button_state
    two_normal_favorite_current_song: _button_state
    speakers_favorite_current_song: _button_state
    living_room_favorite_current_song: _button_state
    bedroom_closet_door_identify: _button_state
    furnace_room_door_identify: _button_state
    bedroom_closet_door_battery_replaced: _button_state
    furnace_room_door_battery_replaced: _button_state
    ipad_battery_replaced: _button_state
    s9_battery_replaced: _button_state
    syth_battery_replaced: _button_state
    piper_restart_container: _button_state
    homeassistant_restart_container: _button_state
    whisper_restart_container: _button_state
    wordpress_wordpress_1_restart_container: _button_state
    esphome_restart_container: _button_state
    portainer_restart_container: _button_state
    music_assistant_restart_container: _button_state
    prometheus_restart_container: _button_state
    mailcowdockerized_watchdog_mailcow_1_restart_container: _button_state
    mailcowdockerized_acme_mailcow_1_restart_container: _button_state
    mailcowdockerized_nginx_mailcow_1_restart_container: _button_state
    mailcowdockerized_ofelia_mailcow_1_restart_container: _button_state
    mailcowdockerized_rspamd_mailcow_1_restart_container: _button_state
    mailcowdockerized_postfix_mailcow_1_restart_container: _button_state
    mailcowdockerized_dovecot_mailcow_1_restart_container: _button_state
    mailcowdockerized_php_fpm_mailcow_1_restart_container: _button_state
    mailcowdockerized_mysql_mailcow_1_restart_container: _button_state
    mailcowdockerized_clamd_mailcow_1_restart_container: _button_state
    mailcowdockerized_postfix_tlspol_mailcow_1_restart_container: _button_state
    mailcowdockerized_redis_mailcow_1_restart_container: _button_state
    mailcowdockerized_sogo_mailcow_1_restart_container: _button_state
    mailcowdockerized_dockerapi_mailcow_1_restart_container: _button_state
    mailcowdockerized_olefy_mailcow_1_restart_container: _button_state
    mailcowdockerized_memcached_mailcow_1_restart_container: _button_state
    mailcowdockerized_unbound_mailcow_1_restart_container: _button_state
    mailcowdockerized_netfilter_mailcow_1_restart_container: _button_state
    plex_restart_container: _button_state
    frigate_restart_container: _button_state
    wordpress_db_1_restart_container: _button_state
    watchtower_restart_container: _button_state
    tasmoadmin_restart_container: _button_state
    scrutiny_restart_container: _button_state
    opnsense_exporter_restart_container: _button_state
    nodered_restart_container: _button_state
    grafana_restart_container: _button_state
    timescaledb_poc_restart_container: _button_state
    postgres_exporter_restart_container: _button_state
    local_prune_unused_images: _button_state
    jusparr_docker_prune_unused_images: _button_state
    portainer_agent_restart_container: _button_state
    ha_esphome_1_restart_container: _button_state
    ha_nodered_1_restart_container: _button_state
    ha_watchtower_1_restart_container: _button_state
    ha_whisper_1_restart_container: _button_state
    ha_piper_1_restart_container: _button_state
    ha_aircast_1_restart_container: _button_state
    ha_scrutiny_1_restart_container: _button_state
    mediamtx_restart_container: _button_state
    zashtys_satellite_system_restart: _button_state
    zashtys_satellite_system_shutdown: _button_state
    zashtys_satellite_monitor_on: _button_state
    zashtys_satellite_monitor_off: _button_state
    mediamtx_restart_container_2: _button_state
    wordpress_wordpress_1_restart_container_2: _button_state
    homeassistant_restart_container_2: _button_state
    plex_restart_container_2: _button_state
    aircast_restart_container_2: _button_state
    wordpress_db_1_restart_container_2: _button_state
    music_assistant_restart_container_2: _button_state
    tasmoadmin_restart_container_2: _button_state
    nodered_restart_container_2: _button_state
    esphome_restart_container_2: _button_state
    frigate_restart_container_2: _button_state
    portainer_restart_container_2: _button_state
    watchtower_restart_container_2: _button_state
    scrutiny_restart_container_2: _button_state
    piper_restart_container_2: _button_state
    whisper_restart_container_2: _button_state
    prometheus_restart_container_2: _button_state
    opnsense_exporter_restart_container_2: _button_state
    grafana_restart_container_2: _button_state
    timescaledb_poc_restart_container_2: _button_state
    postgres_exporter_restart_container_2: _button_state
    ha_aircast_1_restart_container_2: _button_state
    ha_nodered_1_restart_container_2: _button_state
    ha_esphome_1_restart_container_2: _button_state
    portainer_agent_restart_container_2: _button_state
    ha_watchtower_1_restart_container_2: _button_state
    ha_whisper_1_restart_container_2: _button_state
    ha_piper_1_restart_container_2: _button_state
    ha_scrutiny_1_restart_container_2: _button_state
    livingroom_tv_favorite_current_song: _button_state
    tv_group_favorite_current_song: _button_state
    bedroom_speaker_favorite_current_song_3: _button_state
    bedroom_speaker_favorite_current_song_2: _button_state
    bathroom_favorite_current_song_2: _button_state
    tv_group_favorite_current_song_2: _button_state
    two_normal_favorite_current_song_2: _button_state
    bed_and_bath_favorite_current_song_2: _button_state
    livingroom_tv_airplay_favorite_current_song: _button_state
    speakers_favorite_current_song_2: _button_state
    tv_group_airplay_favorite_current_song: _button_state
    two_normal_airplay_favorite_current_song: _button_state
    bed_and_bath_airplay_favorite_current_song: _button_state
    homeassistant_pause_container: _button_state
    homeassistant_resume_container: _button_state
    mediamtx_pause_container: _button_state
    mediamtx_resume_container: _button_state
    plex_pause_container: _button_state
    plex_resume_container: _button_state
    aircast_pause_container: _button_state
    aircast_resume_container: _button_state
    music_assistant_pause_container: _button_state
    music_assistant_resume_container: _button_state
    nodered_pause_container: _button_state
    nodered_resume_container: _button_state
    esphome_pause_container: _button_state
    esphome_resume_container: _button_state
    frigate_pause_container: _button_state
    frigate_resume_container: _button_state
    wordpress_db_1_pause_container: _button_state
    wordpress_db_1_resume_container: _button_state
    portainer_pause_container: _button_state
    portainer_resume_container: _button_state
    wordpress_wordpress_1_pause_container: _button_state
    wordpress_wordpress_1_resume_container: _button_state
    tasmoadmin_pause_container: _button_state
    tasmoadmin_resume_container: _button_state
    watchtower_pause_container: _button_state
    watchtower_resume_container: _button_state
    scrutiny_pause_container: _button_state
    scrutiny_resume_container: _button_state
    piper_pause_container: _button_state
    piper_resume_container: _button_state
    whisper_pause_container: _button_state
    whisper_resume_container: _button_state
    prometheus_pause_container: _button_state
    prometheus_resume_container: _button_state
    opnsense_exporter_pause_container: _button_state
    opnsense_exporter_resume_container: _button_state
    grafana_pause_container: _button_state
    grafana_resume_container: _button_state
    timescaledb_poc_pause_container: _button_state
    timescaledb_poc_resume_container: _button_state
    postgres_exporter_pause_container: _button_state
    postgres_exporter_resume_container: _button_state
    ha_aircast_1_pause_container: _button_state
    ha_aircast_1_resume_container: _button_state
    ha_nodered_1_pause_container: _button_state
    ha_nodered_1_resume_container: _button_state
    ha_esphome_1_pause_container: _button_state
    ha_esphome_1_resume_container: _button_state
    portainer_agent_pause_container: _button_state
    portainer_agent_resume_container: _button_state
    ha_watchtower_1_pause_container: _button_state
    ha_watchtower_1_resume_container: _button_state
    ha_whisper_1_pause_container: _button_state
    ha_whisper_1_resume_container: _button_state
    ha_piper_1_pause_container: _button_state
    ha_piper_1_resume_container: _button_state
    ha_scrutiny_1_pause_container: _button_state
    ha_scrutiny_1_resume_container: _button_state
    duolingo_force_scrape: _button_state

    @staticmethod
    def press(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

class _calendar_state(StateVal):
    all_day: bool
    all_tasks: list
    description: str
    due_today: bool
    end_time: str
    labels: list
    location: str
    message: str
    offset_reached: bool
    overdue: bool
    priority: int
    restored: bool
    start_time: str
    supported_features: int

    def create_event(self, *, summary: str, description: str | None=None, start_date_time: datetime | None=None, end_date_time: datetime | None=None, start_date: datetime | None=None, end_date: datetime | None=None, location: str | None=None):
        """

        Args:
            summary:  Example: Department Party
            description:  Example: Meeting to provide technical review for 'Phoenix' design.
            start_date_time:  Example: 2022-03-22 20:00:00
            end_date_time:  Example: 2022-03-22 22:00:00
            start_date:  Example: 2022-03-22
            end_date:  Example: 2022-03-23
            location:  Example: Conference Room - F123, Bldg. 002"""
        ...

    def get_events(self, *, start_date_time: datetime | None=None, end_date_time: datetime | None=None, duration=None) -> dict[str, Any]:
        """

        Args:
            start_date_time:  Example: 2022-03-22 20:00:00
            end_date_time:  Example: 2022-03-22 22:00:00"""
        ...

class calendar:
    canada_ab: _calendar_state
    ashton_s_work: _calendar_state
    phases_of_the_moon: _calendar_state
    holidays_in_japan: _calendar_state
    holidays_in_canada: _calendar_state
    family: _calendar_state
    kit_ashton: _calendar_state
    ashtons_ipad: _calendar_state
    harley: _calendar_state
    ashtonparrott_gmail_com: _calendar_state
    hindu_holidays: _calendar_state
    holidays_in_united_states: _calendar_state
    christian_holidays: _calendar_state
    orthodox_holidays: _calendar_state
    jewish_holidays: _calendar_state
    field_agent: _calendar_state
    streaming: _calendar_state
    justiceparrott_outlook_com: _calendar_state
    muslim_holidays: _calendar_state
    working_location: _calendar_state
    eventbrite: _calendar_state
    home: _calendar_state
    kantor: _calendar_state
    birthdays_2: _calendar_state
    inbox: _calendar_state
    home_2: _calendar_state
    my_work: _calendar_state
    city_of_lethbridge_waste: _calendar_state
    city_of_lethbridge_justice: _calendar_state
    workday_sensor_calendar: _calendar_state
    last_day_to_book_fall_leaf_collection: _calendar_state
    last_day_to_book_fall_leaf_collection_2: _calendar_state
    seasonal_changeover: _calendar_state
    inbox_2: _calendar_state
    home_3: _calendar_state
    my_work_2: _calendar_state
    personal_streaming: _calendar_state
    llm_vision_timeline: _calendar_state

    @staticmethod
    def create_event(*, entity_id: str, summary: str, description: str | None=None, start_date_time: datetime | None=None, end_date_time: datetime | None=None, start_date: datetime | None=None, end_date: datetime | None=None, location: str | None=None):
        """

        Args:
            entity_id: Entity ID
            summary:  Example: Department Party
            description:  Example: Meeting to provide technical review for 'Phoenix' design.
            start_date_time:  Example: 2022-03-22 20:00:00
            end_date_time:  Example: 2022-03-22 22:00:00
            start_date:  Example: 2022-03-22
            end_date:  Example: 2022-03-23
            location:  Example: Conference Room - F123, Bldg. 002"""
        ...

    @staticmethod
    def get_events(*, entity_id: str, start_date_time: datetime | None=None, end_date_time: datetime | None=None, duration=None) -> dict[str, Any]:
        """

        Args:
            entity_id: Entity ID
            start_date_time:  Example: 2022-03-22 20:00:00
            end_date_time:  Example: 2022-03-22 22:00:00"""
        ...

class _camera_state(StateVal):
    access_token: str
    attribution: str
    browserID: str
    camera_name: str
    client_id: str
    entity_picture: str
    file_path: str
    motion_detection: bool
    observation_time: Any
    restored: bool
    supported_features: int
    type: str

    def enable_motion_detection(self):
        ...

    def disable_motion_detection(self):
        ...

    def turn_off(self):
        ...

    def turn_on(self):
        ...

    def snapshot(self, filename: str):
        """

        Args:
            filename:  Example: /tmp/snapshot_{{ entity_id.name }}.jpg"""
        ...

    def play_stream(self, *, media_player: str, format: Literal['', 'hls']='hls'):
        ...

    def record(self, *, filename: str, duration: int=30, lookback: int=0):
        """

        Args:
            filename:  Example: /tmp/snapshot_{{ entity_id.name }}.mp4"""
        ...

class camera:
    env_can_radar: _camera_state
    highway_3_gif: _camera_state
    whoop_up_west_gif: _camera_state
    whoop_up_east_gif: _camera_state
    scenic_whoop_up: _camera_state
    whoop_up_west_east: _camera_state
    syth_local: _camera_state
    desktop: _camera_state
    laptop: _camera_state
    syth_tailscale: _camera_state
    backyard_camera_hq: _camera_state
    ipad_local: _camera_state

    @staticmethod
    def enable_motion_detection(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def disable_motion_detection(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_off(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_on(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def snapshot(*, entity_id: str, filename: str):
        """

        Args:
            entity_id: Entity ID
            filename:  Example: /tmp/snapshot_{{ entity_id.name }}.jpg"""
        ...

    @staticmethod
    def play_stream(*, entity_id: str, media_player: str, format: Literal['', 'hls']='hls'):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def record(*, entity_id: str, filename: str, duration: int=30, lookback: int=0):
        """

        Args:
            entity_id: Entity ID
            filename:  Example: /tmp/snapshot_{{ entity_id.name }}.mp4"""
        ...

class cast:

    @staticmethod
    def show_lovelace_view(*, entity_id: str, view_path: str, dashboard_path: str | None=None):
        """

        Args:
            view_path:  Example: downstairs
            dashboard_path:  Example: lovelace-cast"""
        ...

class climate:

    @staticmethod
    def turn_on(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_off(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_hvac_mode(*, entity_id: str, hvac_mode: str | None=None):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_preset_mode(*, entity_id: str, preset_mode: str):
        """

        Args:
            entity_id: Entity ID
            preset_mode:  Example: away"""
        ...

    @staticmethod
    def set_temperature(*, entity_id: str, temperature: float | None=None, target_temp_high: float | None=None, target_temp_low: float | None=None, hvac_mode: str | None=None):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_humidity(*, entity_id: str, humidity: int):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_fan_mode(*, entity_id: str, fan_mode: str):
        """

        Args:
            entity_id: Entity ID
            fan_mode:  Example: low"""
        ...

    @staticmethod
    def set_swing_mode(*, entity_id: str, swing_mode: str):
        """

        Args:
            entity_id: Entity ID
            swing_mode:  Example: on"""
        ...

    @staticmethod
    def set_swing_horizontal_mode(*, entity_id: str, swing_horizontal_mode: str):
        """

        Args:
            entity_id: Entity ID
            swing_horizontal_mode:  Example: on"""
        ...

class cloud:

    @staticmethod
    def remote_connect():
        ...

    @staticmethod
    def remote_disconnect():
        ...

class color_extractor:

    @staticmethod
    def turn_on(*, entity_id: str, color_extract_url: str | None=None, color_extract_path: str | None=None):
        """

        Args:
            entity_id: Entity ID
            color_extract_url:  Example: https://www.example.com/images/logo.png
            color_extract_path:  Example: /opt/images/logo.png"""
        ...

class command_line:

    @staticmethod
    def reload():
        ...

class _conversation_state(StateVal):
    supported_features: int

class conversation:
    google_generative_ai: _conversation_state

    @staticmethod
    def process(*, text: str, language: str | None=None, agent_id=None, conversation_id: str | None=None) -> dict[str, Any]:
        """

        Args:
            text:  Example: Turn all lights on
            language:  Example: NL
            agent_id:  Example: homeassistant
            conversation_id:  Example: my_conversation_1"""
        ...

    @staticmethod
    def reload(*, language: str | None=None, agent_id=None):
        """

        Args:
            language:  Example: NL
            agent_id:  Example: homeassistant"""
        ...

class _counter_state(StateVal):
    editable: bool
    initial: int
    minimum: int
    step: int

    def increment(self):
        ...

    def decrement(self):
        ...

    def reset(self):
        ...

    def set_value(self, value: float):
        ...

class counter:
    ha_error_log: _counter_state
    ha_warning_log: _counter_state

    @staticmethod
    def increment(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def decrement(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def reset(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_value(*, entity_id: str, value: float):
        """

        Args:
            entity_id: Entity ID"""
        ...

class cover:

    @staticmethod
    def open_cover(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def close_cover(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_cover_position(*, entity_id: str, position: int):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def stop_cover(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def open_cover_tilt(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def close_cover_tilt(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def stop_cover_tilt(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_cover_tilt_position(*, entity_id: str, tilt_position: int):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle_cover_tilt(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

class date:

    @staticmethod
    def set_value(*, entity_id: str, date: datetime):
        """

        Args:
            entity_id: Entity ID
            date:  Example: 2022/11/01"""
        ...

class datetime:

    @staticmethod
    def set_value(*, entity_id: str, datetime: datetime):
        """

        Args:
            entity_id: Entity ID
            datetime:  Example: 2023-10-07T21:35:22"""
        ...

class _device_tracker_state(StateVal):
    alert: str
    altitude: float
    apple_account: str
    away_time_zone_offset: str
    band: str
    battery_level: int
    calc_distance: float
    connection: str
    course: int
    device_status: str
    distance_to: str
    down_speed: int
    event_log_version: str
    expires: datetime | str
    from_zone: str
    gps: str
    gps_accuracy: int | float
    home_distance: float
    host_name: str
    icloud3_devices: str
    icloud3_directory: str
    icloud3_version: str
    integration: str
    interface: str
    ip: str
    is_lost: bool
    last_known_connected_time: datetime
    last_known_ip: str
    last_lost_timestamp: datetime
    last_time_reachable: str
    last_timestamp: datetime | str
    last_zone: str
    latitude: float
    located: str
    location_source: str
    longitude: float
    mac: str
    max_distance: float
    mobile_app: str
    name: str
    next_update: str
    online_time: float
    packets_received: int
    packets_sent: int
    picture_file: str
    primary_home_zone: str
    reason: str
    restored: bool
    ring_state: str
    rx_rate: int
    signal: int
    source_type: str
    speed: int
    supported_features: int
    track_from_zones: str
    traffic_usage: int
    trigger: str
    tx_rate: int
    type: str
    up_speed: int
    vertical_accuracy: int
    voip_state: str
    waze_distance: float
    zone: str
    zone_changed: str
    zone_distance: float

class device_tracker:
    syth: _device_tracker_state
    s9: _device_tracker_state
    ipad: _device_tracker_state
    wiz_connected_lighting_company_limited_89_45_8e: _device_tracker_state
    google_68_e1_4a: _device_tracker_state
    google_a8_e3_e4: _device_tracker_state
    hewlett_packard_98_ce_b5: _device_tracker_state
    chicony_electronics_d9_41_12: _device_tracker_state
    tp_link_technologies_18_16_8c: _device_tracker_state
    google_2c_d3_65: _device_tracker_state
    apple_51_be_79: _device_tracker_state
    google_16_61_63: _device_tracker_state
    compal_information_kunshan_b3_e1_77: _device_tracker_state
    asustek_computer_9b_a7_8f: _device_tracker_state
    murata_manufacturing_7d_d4_74: _device_tracker_state
    pet: _device_tracker_state
    security_keys: _device_tracker_state
    spare_keys: _device_tracker_state
    keys: _device_tracker_state
    iphone: _device_tracker_state
    syth_iphone_icloud: _device_tracker_state
    syth_ipad: _device_tracker_state
    iphone_tracker_syth: _device_tracker_state
    flightradar24: _device_tracker_state
    wiz_iot_company_limited_be_1f_2f: _device_tracker_state
    wiz_iot_company_limited_bc_af_9b: _device_tracker_state
    wiz_connected_lighting_company_limited_17_4b_40: _device_tracker_state
    wiz_iot_company_limited_fc_22_fb: _device_tracker_state
    wiz_iot_company_limited_be_a3_09: _device_tracker_state
    wiz_connected_lighting_company_limited_14_bd_c7: _device_tracker_state
    opnsense_opnsense: _device_tracker_state
    opnsense_d2_e9_08_a3_ad_6c: _device_tracker_state
    opnsense_cc_f4_11_a8_e3_e4: _device_tracker_state
    opnsense_30_fd_38_68_e1_4a: _device_tracker_state
    opnsense_b0_c0_90_d9_41_12: _device_tracker_state
    opnsense_bc_dd_c2_97_5d_46: _device_tracker_state
    opnsense_b0_a7_b9_3c_d4_df: _device_tracker_state
    opnsense_7c_a1_ae_51_be_79: _device_tracker_state
    opnsense_20_df_b9_16_61_63: _device_tracker_state
    opnsense_1c_75_08_b3_e1_77: _device_tracker_state
    opnsense_30_85_a9_9b_a7_8f: _device_tracker_state
    opnsense_ac_e2_d3_f8_ca_7a: _device_tracker_state
    opnsense_d0_bf_9c_98_ce_b5: _device_tracker_state
    opnsense_6c_29_90_14_bd_c7: _device_tracker_state
    opnsense_6c_29_90_89_45_8e: _device_tracker_state
    opnsense_a8_bb_50_be_a3_09: _device_tracker_state
    opnsense_a8_bb_50_bc_af_9b: _device_tracker_state
    opnsense_a8_bb_50_be_1f_2f: _device_tracker_state
    opnsense_cc_32_e5_18_16_8c: _device_tracker_state
    opnsense_d142_59_111_36_abhsia_telus_net: _device_tracker_state
    opnsense_d142_59_111_190_abhsia_telus_net: _device_tracker_state
    opnsense_30_10_e4_7f_0f_8b: _device_tracker_state
    opnsense_a8_bb_50_be_a5_37: _device_tracker_state
    opnsense_d8_8c_79_2c_d3_65: _device_tracker_state
    opnsense_laptop: _device_tracker_state
    opnsense_6c_29_90_17_4b_40: _device_tracker_state
    opnsense_a8_bb_50_fc_22_fb: _device_tracker_state
    google: _device_tracker_state
    desktop_u5e7nrv: _device_tracker_state
    sunrich: _device_tracker_state
    apple: _device_tracker_state
    google_2: _device_tracker_state
    tp_link: _device_tracker_state
    debian_r: _device_tracker_state
    google_3: _device_tracker_state
    laptop: _device_tracker_state
    desktop_3pnv5bo: _device_tracker_state
    ashtons_galaxy_s9: _device_tracker_state
    syth_2: _device_tracker_state
    google_4: _device_tracker_state
    ipad_2: _device_tracker_state
    sunrich_2: _device_tracker_state
    tp_link_corporation_limited: _device_tracker_state
    google_5: _device_tracker_state
    debian_r_2: _device_tracker_state
    desktop_3pnv5bo_2: _device_tracker_state
    desktop_u5e7nrv_2: _device_tracker_state
    murata_manufacturing: _device_tracker_state
    syth_3: _device_tracker_state
    apple_2: _device_tracker_state
    laptop_2: _device_tracker_state
    debian_dell_2: _device_tracker_state
    google_home_mini: _device_tracker_state
    wiz_bea309: _device_tracker_state
    google_home: _device_tracker_state
    wiz_174b40: _device_tracker_state
    ipad_k_2: _device_tracker_state
    wiz_bea537: _device_tracker_state
    google_nest_mini: _device_tracker_state
    hpf8ca7a: _device_tracker_state
    chicony: _device_tracker_state
    wiz_fc22fb: _device_tracker_state
    server_fan: _device_tracker_state
    printer: _device_tracker_state
    wiz_bcaf9b: _device_tracker_state
    wiz_14bdc7: _device_tracker_state
    wiz_be1f2f: _device_tracker_state
    wiz_89458e: _device_tracker_state
    b6_f7_37_89_0c_50: _device_tracker_state
    jeff_s_s23_fe: _device_tracker_state
    chicony_2: _device_tracker_state
    network_device: _device_tracker_state
    wiz_iot: _device_tracker_state
    wiz_iot_2: _device_tracker_state
    espressif: _device_tracker_state
    nintendo_3ds: _device_tracker_state
    living_room_wifi: _device_tracker_state
    breaker_box: _device_tracker_state
    sony_interactive_entertainment: _device_tracker_state
    opnsense_7c_9e_bd_62_37_88: _device_tracker_state
    ps4_693253: _device_tracker_state
    network_device_2: _device_tracker_state
    kobo: _device_tracker_state
    hpace2d3f8ca7a_1839: _device_tracker_state
    wiz_iot_3: _device_tracker_state
    network_device_3: _device_tracker_state
    kit_s_ipad: _device_tracker_state
    my_ipad: _device_tracker_state
    f2_d2_5f_bb_75_7c: _device_tracker_state
    black_phone: _device_tracker_state
    backyard_camera: _device_tracker_state
    backyard_camera_2: _device_tracker_state
    backyard_camera_3: _device_tracker_state
    backyard_camera_4: _device_tracker_state
    debian_dell_3: _device_tracker_state
    debian_dell_2_2: _device_tracker_state
    sunrich_technology_limited_3b_c2_7e: _device_tracker_state
    ps4: _device_tracker_state
    server_fan_2: _device_tracker_state
    wiz_iot_4: _device_tracker_state
    network_device_4: _device_tracker_state
    iphone_2: _device_tracker_state
    iphone_3: _device_tracker_state
    network_device_5: _device_tracker_state
    d0_df_9a_8a_a7_8a: _device_tracker_state
    win_818skdv8i0p: _device_tracker_state
    iphone_4: _device_tracker_state
    laptop_3: _device_tracker_state
    wiz_iot_5: _device_tracker_state
    samsung_electro_mechanics_thailand_e9_a4_cc: _device_tracker_state
    samsung_electro_mechanics: _device_tracker_state
    quanta_computer_98_85_f6: _device_tracker_state
    quanta_computer: _device_tracker_state
    zashtys_satellite: _device_tracker_state
    desktop_9tdjp21: _device_tracker_state
    hp_15_laptop: _device_tracker_state
    hewlett_packard: _device_tracker_state
    hon_hai_precision_ind: _device_tracker_state
    jeff_s_s23_fe_2: _device_tracker_state
    network_device_6: _device_tracker_state
    network_device_7: _device_tracker_state
    network_device_8: _device_tracker_state

    @staticmethod
    def see(*, mac: str | None=None, dev_id: str | None=None, host_name: str | None=None, location_name: str | None=None, gps: Any | None=None, gps_accuracy: float | None=None, battery: int | None=None):
        """

        Args:
            mac:  Example: FF:FF:FF:FF:FF:FF
            dev_id:  Example: phonedave
            host_name:  Example: Dave
            location_name:  Example: home
            gps:  Example: [51.509802, -0.086692]"""
        ...

class downloader:

    @staticmethod
    def download_file(*, url: str, subdir: str | None=None, filename: str | None=None, overwrite: bool=False, headers: Any | None=None):
        """

        Args:
            url:  Example: http://example.org/myfile
            subdir:  Example: download_dir
            filename:  Example: my_file_name
            headers:  Example: {'Accept': 'application/json'}"""
        ...

class environment_canada:

    @staticmethod
    def set_radar_type(*, entity_id: str, radar_type: Literal['', 'Auto', 'Rain', 'Snow']):
        """

        Args:
            entity_id: Entity ID
            radar_type:  Example: Snow"""
        ...

    @staticmethod
    def get_forecasts(*, entity_id: str) -> dict[str, Any]:
        """

        Args:
            entity_id: Entity ID"""
        ...

class _event_state(StateVal):
    backup_stage: Any
    bot: dict
    chat_id: int
    domain: str
    event_type: str
    event_types: list
    failed_reason: Any
    file: str
    folder: str
    issue_id: str
    message_id: int
    path: str

class event:
    repair: _event_state
    backup_automatic_backup: _event_state
    folder_watcher_config_www_downloads: _event_state
    folder_watcher_config: _event_state
    folder_watcher_config_pyscript: _event_state
    folder_watcher_config_python_scripts: _event_state
    folder_watcher_config_media: _event_state
    folder_watcher_config_automations: _event_state
    folder_watcher_config_scripts: _event_state
    folder_watcher_config_feedreader: _event_state
    zashtys_update_event: _event_state

class fan:

    @staticmethod
    def turn_on(*, entity_id: str, percentage: int | None=None, preset_mode: str | None=None):
        """

        Args:
            entity_id: Entity ID
            preset_mode:  Example: auto"""
        ...

    @staticmethod
    def turn_off(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def increase_speed(*, entity_id: str, percentage_step: int | None=None):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def decrease_speed(*, entity_id: str, percentage_step: int | None=None):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def oscillate(*, entity_id: str, oscillating: bool):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_direction(*, entity_id: str, direction: Literal['', 'forward', 'reverse']):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_percentage(*, entity_id: str, percentage: int):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_preset_mode(*, entity_id: str, preset_mode: str):
        """

        Args:
            entity_id: Entity ID
            preset_mode:  Example: auto"""
        ...

class ffmpeg:

    @staticmethod
    def start(*, entity_id: str | None=None):
        ...

    @staticmethod
    def stop(*, entity_id: str | None=None):
        ...

    @staticmethod
    def restart(*, entity_id: str | None=None):
        ...

class file:

    @staticmethod
    def read_file(*, file_name: str | None=None, file_encoding: Literal['', 'JSON', 'YAML'] | None=None) -> dict[str, Any]:
        """

        Args:
            file_name:  Example: www/my_file.json
            file_encoding:  Example: JSON"""
        ...

class frigate:

    @staticmethod
    def export_recording(*, entity_id: str, playback_factor: Literal['', 'realtime', 'timelapse_25x']='realtime', start_time: datetime, end_time: datetime, name: str | None=None):
        """Export a custom recording or timelapse.

        Args:
            entity_id: Entity ID
            playback_factor: Playback factor for recordings Example: realtime
            start_time: Start time of exported recording
            end_time: End time of exported recording
            name: Optional name for the exported recording. If not provided, the API will generate one.
                """
        ...

    @staticmethod
    def favorite_event(*, entity_id: str, event_id: str='', favorite: bool=True):
        """Favorites or unfavorites an event. Favorited events are retained indefinitely.

        Args:
            entity_id: Entity ID
            event_id: ID of the event to favorite or unfavorite. Example: 1656510950.19548-ihtjj7
            favorite: If the event should be favorited or unfavorited. Enable to favorite, disable to unfavorite.
                 Example: True"""
        ...

    @staticmethod
    def ptz(*, entity_id: str, action: Literal['', 'move', 'preset', 'stop', 'zoom']='move', argument: str=''):
        """Pan / Tilt, Zoom, or move a camera to a preset

        Args:
            entity_id: Entity ID
            action: Type of PTZ action Example: move
            argument: left, right, up, down for move; in, out for zoom; name of preset
                 Example: down"""
        ...

    @staticmethod
    def create_event(*, entity_id: str, label: str='', sub_label: str | None=None, duration: int=30, include_recording: bool=True) -> dict[str, Any]:
        """Create a manual event with a given label for a camera.

        Args:
            entity_id: Entity ID
            label: Label for the event Example: Doorbell press
            sub_label: Sub label for the event Example: Front door
            duration: Predetermined length of event. Default is 30 seconds. Use 0 for indefinite.
                 Example: 30
            include_recording: Whether the event should save recordings along with the snapshot that is taken.
                 Example: True"""
        ...

    @staticmethod
    def end_event(*, entity_id: str, event_id: str='') -> dict[str, Any]:
        """End a manual event with a given id for a camera.

        Args:
            entity_id: Entity ID
            event_id: ID of the event to end. Example: 1656510950.19548-ihtjj7"""
        ...

    @staticmethod
    def review_summarize(*, start_time: datetime, end_time: datetime) -> dict[str, Any]:
        """Get a summary of review items for a specified time period. Only available in Frigate 0.17+.

        Args:
            start_time: Start time for the review period
            end_time: End time for the review period"""
        ...

class frontend:

    @staticmethod
    def set_theme(*, name=None, name_dark=None):
        """

        Args:
            name:  Example: default
            name_dark:  Example: default"""
        ...

    @staticmethod
    def reload_themes():
        ...

class gasbuddy:

    @staticmethod
    def lookup_gps(*, entity_id: str) -> dict[str, Any]:
        """List gas prices based on GPS coordinates of device tracker.

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def lookup_zip(*, zipcode: str) -> dict[str, Any]:
        """List gas prices based on entered ZIP code."""
        ...

    @staticmethod
    def clear_cache(*, entity_id: str):
        """Clear library cache file.

        Args:
            entity_id: Entity ID"""
        ...

class genius_lyrics:

    @staticmethod
    def register_card_resources():
        """Re-register the built-in Genius Lyrics card resource in Lovelace."""
        ...

    @staticmethod
    def search_lyrics(*, entity_id='', media_artist='', media_title='') -> dict[str, Any]:
        """

        Args:
            entity_id:  Example: sensor.foobar_lyrics
            media_artist:  Example: Protoje
            media_title:  Example: Mind of a King"""
        ...

class gif:

    @staticmethod
    def create_gif(*, images, output_path, fps=10, loop=True):
        """Create a GIF from a list of images

        Args:
            images: List of image file paths Example: ['/config/images/image1.jpg', '/config/images/image2.jpg']
            output_path: Path to save the GIF Example: /config/gifs/output.gif
            fps: Frames per second for the GIF Example: 10
            loop: Whether the GIF should loop Example: True"""
        ...

class google:

    @staticmethod
    def create_event(*, entity_id: str, summary: str, description: str | None=None, start_date_time: str | None=None, end_date_time: str | None=None, start_date: str | None=None, end_date: str | None=None, location: str | None=None):
        """

        Args:
            entity_id: Entity ID
            summary:  Example: Bowling
            description:  Example: Birthday bowling
            start_date_time:  Example: 2022-03-22 20:00:00
            end_date_time:  Example: 2022-03-22 22:00:00
            start_date:  Example: 2022-03-10
            end_date:  Example: 2022-03-11
            location:  Example: Conference Room - F123, Bldg. 002"""
        ...

class google_generative_ai_conversation:

    @staticmethod
    def generate_content(*, prompt: str, filenames: str | None=None) -> dict[str, Any]:
        ...

class google_home:

    @staticmethod
    def delete_alarm(*, entity_id: str, alarm_id: str, skip_refresh: bool=False):
        """

        Args:
            entity_id:  Example: sensor.kitchen_alarms
            alarm_id:  Example: alarm/6ed06a56-8a58-c6e3-a7d4-03f92c9d8a51
            skip_refresh:  Example: True"""
        ...

    @staticmethod
    def delete_timer(*, entity_id: str, timer_id: str, skip_refresh: bool=False):
        """

        Args:
            entity_id:  Example: sensor.kitchen_timers
            timer_id:  Example: timer/6ed06a56-8a58-c6e3-a7d4-03f92c9d8a51
            skip_refresh:  Example: True"""
        ...

    @staticmethod
    def reboot_device(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def refresh_devices():
        ...

class google_mail:

    @staticmethod
    def set_vacation(*, entity_id: str, enabled: bool=True, message: str, title: str | None=None, plain_text: bool=True, restrict_contacts: bool | None=None, restrict_domain: bool | None=None, start: datetime | None=None, end: datetime | None=None):
        """

        Args:
            entity_id: Entity ID"""
        ...

class google_sheets:

    @staticmethod
    def append_sheet(*, config_entry: str, data: Any, worksheet: str | None=None, add_created_column: bool=True):
        """

        Args:
            data:  Example: {"hello": world, "cool": True, "count": 5}
            worksheet:  Example: Sheet1"""
        ...

    @staticmethod
    def get_sheet(*, config_entry: str, rows: float, worksheet: str | None=None) -> dict[str, Any]:
        """

        Args:
            rows:  Example: 2
            worksheet:  Example: Sheet1"""
        ...

class group:

    @staticmethod
    def reload():
        ...

    @staticmethod
    def set(*, object_id: str, name: str | None=None, icon: str | None=None, entities: str | None=None, add_entities: str | None=None, remove_entities: str | None=None, all: bool | None=None):
        """

        Args:
            object_id:  Example: test_group
            name:  Example: My test group
            icon:  Example: mdi:camera
            entities:  Example: domain.entity_id1, domain.entity_id2
            add_entities:  Example: domain.entity_id1, domain.entity_id2
            remove_entities:  Example: domain.entity_id1, domain.entity_id2"""
        ...

    @staticmethod
    def remove(*, object_id: Any):
        """

        Args:
            object_id:  Example: test_group"""
        ...

class home_maintenance:

    @staticmethod
    def reset_last_performed(*, entity_id: str, performed_date: datetime | None=None):
        """Resets the 'last_performed' date for a maintenance task entity, and updates the 'next_due' date based on the interval.

        Args:
            entity_id: The ID of the task entity to reset.
            performed_date: Optionally specify the date the task was last performed. Example: 2025-06-01"""
        ...

class homeassistant:

    @staticmethod
    def save_persistent_states():
        ...

    @staticmethod
    def turn_off(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_on(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def stop():
        ...

    @staticmethod
    def check_config():
        ...

    @staticmethod
    def update_entity(*, entity_id: str):
        ...

    @staticmethod
    def reload_core_config():
        ...

    @staticmethod
    def set_location(*, latitude: float, longitude: float, elevation: float | None=None):
        """

        Args:
            latitude:  Example: 32.87336
            longitude:  Example: 117.22743
            elevation:  Example: 120"""
        ...

    @staticmethod
    def reload_custom_templates():
        ...

    @staticmethod
    def reload_config_entry(*, entity_id: str, entry_id: str | None=None):
        """

        Args:
            entity_id: Entity ID
            entry_id:  Example: 8955375327824e14ba89e4b29cc3ec9a"""
        ...

    @staticmethod
    def reload_all():
        ...

    @staticmethod
    def remove_alias_from_area(*, area_id, alias: Any):
        """Removes an alias from an area.

        Args:
            area_id: The ID of the area to remove the alias from.
            alias: The alias (or list of aliasses) to remove from the area."""
        ...

    @staticmethod
    def delete_all_orphaned_entities():
        """Deletes all orphaned entities that no longer have an integration that claim/provide them. Please note, if the integration was just removed, it might need a restart for Home Assistant to realize they are orphaned.
        **WARNING** Entities might have been marked orphaned because an integration is offline or not working since Home Assistant started. Calling this action will delete those entities as well."""
        ...

    @staticmethod
    def remove_area_from_floor(*, area_id):
        """Removes an area from a floor. As an area can only be on one floor, this call doesn't need to specify the floor.

        Args:
            area_id: The ID of the area to remove the floor from."""
        ...

    @staticmethod
    def remove_label_from_device(*, label_id, device_id):
        """Removes a label from a device. If multiple labels or multiple devices are provided, all combinations will be removed.

        Args:
            label_id: The ID(s) of the label(s) to remove from the device(s).
            device_id: The ID(s) of the device(s) to remove the label(s) from."""
        ...

    @staticmethod
    def remove_entity_from_area(*, entity_id: str):
        """Removes an entity from an area. As an entity can only be in one area, this call doesn't need to specify the area. Please note, the entity will still be in the area of the device that provides it after this call.

        Args:
            entity_id: The ID of the entity (or entities) to remove the area from."""
        ...

    @staticmethod
    def add_alias_to_area(*, area_id, alias: Any):
        """Adds an alias to an area.

        Args:
            area_id: The ID of the area to add the alias to.
            alias: The alias (or list of aliasses) to add to the area."""
        ...

    @staticmethod
    def disable_device(*, device_id):
        """Disables a device on the fly.

        Args:
            device_id: The device(s) to disable."""
        ...

    @staticmethod
    def unhide_entity(*, entity_id: str):
        """Unhides an entity (or entities) on the fly.

        Args:
            entity_id: The entity/entities to unhide."""
        ...

    @staticmethod
    def hide_entity(*, entity_id: str):
        """Hides an entity (or entities) on the fly.

        Args:
            entity_id: The entity/entities to hide."""
        ...

    @staticmethod
    def remove_label_from_area(*, label_id, area_id):
        """Removes a label to an area. If multiple labels or multiple areas are provided, all combinations will be removed.

        Args:
            label_id: The ID(s) of the label(s) to remove from the area(s).
            area_id: The ID(s) of the area(s) to remove the label(s) from."""
        ...

    @staticmethod
    def remove_label_from_entity(*, label_id, entity_id: str):
        """Removes a label from an entity. If multiple labels or multiple entities are provided, all combinations will be removed.

        Args:
            label_id: The ID(s) of the label(s) to remove from the entity/entities.
            entity_id: The ID(s) of the entity/entities to remove the label(s) from."""
        ...

    @staticmethod
    def set_area_aliases(*, area_id, aliases: Any):
        """Sets aliases for an area. Overwrite and removed any existing aliases, fully replacing them with the new ones.

        Args:
            area_id: The ID of the area to set the aliases for.
            aliases: The aliases to set for the area."""
        ...

    @staticmethod
    def disable_entity(*, entity_id: str):
        """Disables an entity (or entities) on the fly.

        Args:
            entity_id: The entity/entities to disable."""
        ...

    @staticmethod
    def disable_config_entry(*, config_entry_id: str):
        """Disables an integration configuration entry.

        Args:
            config_entry_id: The integration configuration entry to disable."""
        ...

    @staticmethod
    def add_area_to_floor(*, floor_id, area_id):
        """Adds an area to a floor. Please note, if the area is already on a floor, it will be removed from the previous floor.

        Args:
            floor_id: The ID of the floor to add the area on.
            area_id: The ID of the area(s) to add to the floor."""
        ...

    @staticmethod
    def add_label_to_device(*, label_id, device_id):
        """Adds a label to a device. If multiple labels or multiple devices are provided, all combinations will be added.

        Args:
            label_id: The ID(s) of the label(s) to add the device(s).
            device_id: The ID(s) of the device(s) to add the label(s) to."""
        ...

    @staticmethod
    def enable_polling(*, config_entry_id: str):
        """Enables polling for updates for an integration configuration entry.

        Args:
            config_entry_id: The integration configuration entry to enable polling for."""
        ...

    @staticmethod
    def add_label_to_area(*, label_id, area_id):
        """Adds a label to an area. If multiple labels or multiple areas are provided, all combinations will be added.

        Args:
            label_id: The ID(s) of the label(s) to add the area(s).
            area_id: The ID(s) of the area(s) to add the label(s) to."""
        ...

    @staticmethod
    def create_label(*, name: str, description: str, icon: str | None=None, color: Literal['', 'primary', 'accent', 'disabled', 'red', 'pink', 'purple', 'deep_purple', 'indigo', 'blue', 'light_blue', 'cyan', 'teal', 'green', 'light_green', 'lime', 'yellow', 'orange', 'deep_orange', 'brown', 'grey', 'blue_grey', 'black', 'white'] | None=None):
        """Creates a new label on the fly.

        Args:
            name: The name of the label to create.
            description: Description for the label.
            icon: Icon to use for the label.
            color: Color to use for the label. Can be a color name from the list, or a hex color code (like #FF0000)."""
        ...

    @staticmethod
    def add_label_to_entity(*, label_id, entity_id: str):
        """Adds a label to an entity. If multiple labels or multiple entities are provided, all combinations will be added.

        Args:
            label_id: The ID(s) of the label(s) to add the entity/entities.
            entity_id: The ID(s) of the entity/entities to add the label(s) to."""
        ...

    @staticmethod
    def enable_device(*, device_id):
        """Enables a device on the fly.

        Args:
            device_id: The device(s) to enable."""
        ...

    @staticmethod
    def create_floor(*, name: str, icon: str | None=None, level: float | None=None, aliases: Any | None=None):
        """Creates a new floor on the fly.

        Args:
            name: The name of the floor to create.
            icon: Icon to use for the floor.
            level: The level the floor is on in your home.
            aliases: A list of aliases for the floor. This is useful if you want to use the floor in a different language or different nickname."""
        ...

    @staticmethod
    def add_alias_to_floor(*, floor_id, alias: Any):
        """Adds an alias to a floor.

        Args:
            floor_id: The ID of the floor to add the alias to.
            alias: The alias (or list of aliasses) to add to the floor."""
        ...

    @staticmethod
    def rename_entity(*, entity_id: str, name: str):
        """Renames an entity (or entities) on the fly.

        Args:
            entity_id: The entity/entities to rename.
            name: The new name for the entity/entities."""
        ...

    @staticmethod
    def add_device_to_area(*, area_id, device_id):
        """Adds an device to an area. Please note, if the device is already in an area, it will be removed from the previous area.

        Args:
            area_id: The ID of the area to add the device to.
            device_id: The ID of the device(s) to add to the area."""
        ...

    @staticmethod
    def enable_config_entry(*, config_entry_id: str):
        """Enables an integration configuration entry.

        Args:
            config_entry_id: The integration configuration entry to enable."""
        ...

    @staticmethod
    def set_floor_aliases(*, floor_id, aliases: Any):
        """Sets aliases for a floor. Overwrite and removed any existing aliases, fully replacing them with the new ones.

        Args:
            floor_id: The ID of the floor to set the aliases for.
            aliases: The aliases to set for the floor."""
        ...

    @staticmethod
    def list_orphaned_database_entities() -> dict[str, Any]:
        """Lists all orphaned database entities unclaimed by any integration."""
        ...

    @staticmethod
    def remove_alias_from_floor(*, floor_id, alias: Any):
        """Removes an alias from a floor.

        Args:
            floor_id: The ID of the floor to remove the alias from.
            alias: The alias (or list of aliasses) to remove from the floor."""
        ...

    @staticmethod
    def add_entity_to_area(*, area_id, entity_id: str):
        """Adds an entity to an area. Please note, if the enity is already in an area, it will be removed from the previous area. This will override the area the device, that provides this entity, is in.

        Args:
            area_id: The ID of the area to add the entity to.
            entity_id: The ID of the entity (or entities) to add to the area."""
        ...

    @staticmethod
    def delete_floor(*, floor_id):
        """Deletes a floor on the fly.

        Args:
            floor_id: The ID of the floor to delete."""
        ...

    @staticmethod
    def enable_entity(*, entity_id: str):
        """Enables an entity (or entities) on the fly.

        Args:
            entity_id: The entity/entities to enable."""
        ...

    @staticmethod
    def delete_label(*, label_id):
        """Deletes a label on the fly.

        Args:
            label_id: The ID of the label to delete."""
        ...

    @staticmethod
    def update_entity_id(*, entity_id: str, new_entity_id: str):
        """Updates an entity's ID on the fly.

        Args:
            entity_id: The entity/entities to update.
            new_entity_id: The new ID for the entity"""
        ...

    @staticmethod
    def disable_polling(*, config_entry_id: str):
        """Disables polling for updates for an integration configuration entry.

        Args:
            config_entry_id: The integration configuration entry to disable polling for."""
        ...

    @staticmethod
    def remove_device_from_area(*, device_id):
        """Removes a device from an area. As a device can only be in one area, this call doesn't need to specify the area.

        Args:
            device_id: The ID of the device to remove the area from."""
        ...

    @staticmethod
    def create_area(*, name: str, icon: str | None=None, aliases: Any | None=None):
        """Creates a new area on the fly.

        Args:
            name: The name of the area to create.
            icon: Icon to use for the area.
            aliases: A list of aliases for the area. This is useful if you want to use the area in a different language or different nickname."""
        ...

    @staticmethod
    def ignore_all_discovered(*, domain: str | None=None):
        """Ignore all currently discovered devices that are shown on the integrations dashboard. This will not ignore devices that are discovered after this.

        Args:
            domain: The integration domain to ignore all discovered devices for. If not provided, all domains will be considered to be ignored."""
        ...

    @staticmethod
    def restart(*, safe_mode: bool | None=None, force: bool | None=None):
        """Restart the Home Assistant action.

        Args:
            safe_mode: If the restart should be done in safe mode. This will disable all custom integrations and frontend modules.
            force: Force the restart. WARNING! This will not gracefully shutdown Home Assistant, it will skip configuration checks and ignore running database migrations. Only use this if you know what you are doing."""
        ...

    @staticmethod
    def delete_area(*, area_id):
        """Deletes a new area on the fly.

        Args:
            area_id: The ID of the area to delete."""
        ...

class html5:

    @staticmethod
    def dismiss(*, target: Any | None=None, data: Any | None=None):
        """

        Args:
            target:  Example: ['my_phone', 'my_tablet']
            data:  Example: { "tag": "tagname" }"""
        ...

class humidifier:

    @staticmethod
    def turn_on(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_off(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_mode(*, entity_id: str, mode: str):
        """

        Args:
            entity_id: Entity ID
            mode:  Example: away"""
        ...

    @staticmethod
    def set_humidity(*, entity_id: str, humidity: int):
        """

        Args:
            entity_id: Entity ID"""
        ...

class icloud3:

    @staticmethod
    def action(*, command: Literal['', 'Restart iCloud3', 'Pause Tracking', 'Resume Tracking', 'Locate Device(s) using iCloud', 'Send Locate Request to Mobile App'], device_name=None):
        """This service will send operational commands to iCloud3

        Args:
            command: (Required) The action to be performed Example: pause
            device_name: (Optional) Apply all devices or only apply to the selected device Example: Gary (gary_iphone)"""
        ...

    @staticmethod
    def update():
        """The Update service has been replaced by the Action service"""
        ...

    @staticmethod
    def restart():
        """This service will restart iCloud3"""
        ...

    @staticmethod
    def find_iphone_alert(*, device_name):
        """This service will send an alert tone to the device that you want to find

        Args:
            device_name: Device the alert should be sent to Example: Gary (gary_iphone)"""
        ...

    @staticmethod
    def lost_device_alert(*, device_name, number: str, message: str):
        """This service will send a Message and Phone number to the lost iPhone

        Args:
            device_name: Device the Find iPhone Alert and Message should be sent to Example: Gary (gary_iphone)
            number: The phone number to send the message to Example: 123-456-7890
            message: The message to be sent Example: This Phone has been lost. Please call this number to report it found."""
        ...

    @staticmethod
    def display_message_alert(*, device_name, message: str, sounds: str):
        """This service will display a message on the device and can also play an alert tone

        Args:
            device_name: Device the message should be displayed on Example: Duncan (duncan_iphone)
            message: The message to be sent Example: Back door is unlocked
            sounds: If a sound is to be played along with message Example: True"""
        ...

class _image_state(StateVal):
    access_token: str
    background_color: str
    border: int
    color: str
    entity_picture: str
    error_correction: str
    restored: bool
    scale: int
    supported_features: int
    text: str

    def snapshot(self, filename: str):
        """

        Args:
            filename:  Example: /tmp/image_snapshot.jpg"""
        ...

class image:
    ythsaz_share_profile: _image_state
    ythsaz_avatar: _image_state
    ythsaz_now_playing: _image_state
    russell117045_avatar: _image_state
    russell117045_now_playing: _image_state
    howler4522_avatar: _image_state
    howler4522_now_playing: _image_state
    toxiccrumble_avatar: _image_state
    toxiccrumble_now_playing: _image_state
    jusparr_avatar: _image_state
    jusparr_now_playing: _image_state
    backyard_camera_hq_person: _image_state
    shawex: _image_state
    backyard_camera_hq_dog: _image_state
    backyard_camera_hq_motorcycle: _image_state
    backyard_camera_hq_cat: _image_state
    backyard_camera_hq_car: _image_state
    backyard_camera_hq_bicycle: _image_state
    shaw2ex2_4: _image_state
    shaw2ex5_2: _image_state
    bing_wallpaper_picture_bing_wallpaper: _image_state
    zashtys_gamerpic: _image_state
    zashtys_now_playing: _image_state
    zashtys_avatar: _image_state
    jusparr_gamerpic: _image_state
    jusparr_now_playing_2: _image_state
    jusparr_avatar_2: _image_state
    sig1325_gamerpic: _image_state
    sig1325_now_playing: _image_state
    sig1325_avatar: _image_state
    mrcolvan1_gamerpic: _image_state
    mrcolvan1_now_playing: _image_state
    mrcolvan1_avatar: _image_state
    maxdeath397_gamerpic: _image_state
    maxdeath397_now_playing: _image_state
    maxdeath397_avatar: _image_state

    @staticmethod
    def snapshot(*, entity_id: str, filename: str):
        """

        Args:
            entity_id: Entity ID
            filename:  Example: /tmp/image_snapshot.jpg"""
        ...

class image_processing:

    @staticmethod
    def scan(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

class imap:

    @staticmethod
    def seen(*, entry: str, uid: str):
        """

        Args:
            uid:  Example: 12"""
        ...

    @staticmethod
    def move(*, entry: str, uid: str, target_folder: str, seen: bool | None=None):
        """

        Args:
            uid:  Example: 12
            target_folder:  Example: INBOX.Trash"""
        ...

    @staticmethod
    def delete(*, entry: str, uid: str):
        """

        Args:
            uid:  Example: 12"""
        ...

    @staticmethod
    def fetch(*, entry: str, uid: str) -> dict[str, Any]:
        """

        Args:
            uid:  Example: 12"""
        ...

    @staticmethod
    def fetch_part(*, entry: str, uid: str, part: str) -> dict[str, Any]:
        """

        Args:
            uid:  Example: 12
            part:  Example: 0,1"""
        ...

class _input_boolean_state(StateVal):
    editable: bool

    def turn_on(self):
        ...

    def turn_off(self):
        ...

    def toggle(self):
        ...

class _input_button_state(StateVal):
    editable: bool

    def press(self):
        ...

class _input_datetime_state(StateVal):
    day: int
    editable: bool
    has_date: bool
    has_time: bool
    hour: int
    minute: int
    month: int
    second: int
    timestamp: int | float
    year: int

    def set_datetime(self, *, date: str | None=None, time: str | None=None, datetime: str | None=None, timestamp: float | None=None):
        '''

        Args:
            date:  Example: "2019-04-20"
            time:  Example: "05:04:20"
            datetime:  Example: "2019-04-20 05:04:20"'''
        ...

class _input_number_state(StateVal):
    editable: bool
    initial: Any
    max: float
    min: float
    mode: str
    step: float
    unit_of_measurement: str

    def set_value(self, value: float):
        ...

    def decrement(self, amount: float | None):
        """Decrease an input number entity value by a certain amount.

        Args:
            amount: The amount to decrease the input number with. If not provided, the step of the number entity will be used."""
        ...

    def increment(self, amount: float | None):
        """Increase an input number entity value by a certain amount.

        Args:
            amount: The amount to increase the input number with. If not provided, the step of the number entity will be used."""
        ...

    def min(self):
        """Set an input number entity to its minimum value."""
        ...

    def max(self):
        """Set an input number entity to its maximum value."""
        ...

class _input_text_state(StateVal):
    editable: bool
    max: int
    min: int
    mode: str
    pattern: Any

    def set_value(self, value: str):
        """

        Args:
            value:  Example: This is an example text"""
        ...

class input_boolean:
    outside_light_stay_on: _input_boolean_state
    a_j_personal_ashton_home_toggle: _input_boolean_state
    ac_running: _input_boolean_state
    furnace_room_light_lock: _input_boolean_state
    bedroom_closet_light_lock: _input_boolean_state
    quetiapinetaken: _input_boolean_state
    pregabalin_taken: _input_boolean_state
    duloxetine_taken: _input_boolean_state
    outing_today: _input_boolean_state
    wrist_brace: _input_boolean_state
    knee_brace: _input_boolean_state
    flair_today: _input_boolean_state
    woke_up_overnight: _input_boolean_state
    lay_down_today: _input_boolean_state
    water_drank: _input_boolean_state
    meals_eaten_breakfast: _input_boolean_state
    meals_eaten_lunch: _input_boolean_state
    meals_eaten_dinner: _input_boolean_state
    caffeine_1: _input_boolean_state
    caffeine_2: _input_boolean_state
    caffeine_3: _input_boolean_state
    caffeine_4: _input_boolean_state
    gemini_max_tokens: _input_boolean_state
    disable_iphone_light_change: _input_boolean_state

    @staticmethod
    def reload():
        ...

    @staticmethod
    def turn_on(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_off(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

class input_button:
    send_email_for_harley_s_food_renewal: _input_button_state
    say_weather: _input_button_state
    generate_tts: _input_button_state
    start_bread_timer: _input_button_state
    start_adjustable_timer: _input_button_state
    toggle_adaptive_lighting: _input_button_state
    post_status_update: _input_button_state
    speak_statement: _input_button_state

    @staticmethod
    def reload():
        ...

    @staticmethod
    def press(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

class input_datetime:
    bed_time: _input_datetime_state
    wake_time: _input_datetime_state
    outing_start: _input_datetime_state
    outing_end: _input_datetime_state
    wrist_brace_start: _input_datetime_state
    wrist_brace_end: _input_datetime_state
    knee_brace_start: _input_datetime_state
    knee_brace_end: _input_datetime_state
    last_tracker_sent: _input_datetime_state
    woke_up_overnight_wake_time: _input_datetime_state
    woke_up_overnight_sleep_time: _input_datetime_state
    lay_down_today_start: _input_datetime_state
    lay_down_today_end: _input_datetime_state
    meals_eaten_breakfast_time: _input_datetime_state
    meals_eaten_lunch_time: _input_datetime_state
    meals_eaten_dinner_time: _input_datetime_state
    pregabalin_taken_time: _input_datetime_state
    quetiapine_taken_time: _input_datetime_state
    other_meds_taken_time: _input_datetime_state
    eye_drops_use_time: _input_datetime_state
    flair_today_time: _input_datetime_state
    instability_events_time: _input_datetime_state
    duloxetine_taken_time: _input_datetime_state
    caffeine_time_1: _input_datetime_state
    caffeine_time_2: _input_datetime_state
    caffeine_time_3: _input_datetime_state
    caffeine_time_4: _input_datetime_state

    @staticmethod
    def reload():
        ...

    @staticmethod
    def set_datetime(*, entity_id: str, date: str | None=None, time: str | None=None, datetime: str | None=None, timestamp: float | None=None):
        '''

        Args:
            entity_id: Entity ID
            date:  Example: "2019-04-20"
            time:  Example: "05:04:20"
            datetime:  Example: "2019-04-20 05:04:20"'''
        ...

class input_number:
    living_room_volume_day: _input_number_state
    living_room_volume_night: _input_number_state
    bedroom_volume_day: _input_number_state
    bedroom_volume_night: _input_number_state
    bathroom_volume_day: _input_number_state
    bathroom_volume_night: _input_number_state
    living_room_volume_ac: _input_number_state
    isp_download: _input_number_state
    isp_upload: _input_number_state
    lan_bandwidth: _input_number_state
    sleep_quality: _input_number_state
    pain_morning: _input_number_state
    pain_afternoon: _input_number_state
    pain_evening: _input_number_state
    eye_pan_morning: _input_number_state
    eye_pain_afternoon: _input_number_state
    eye_pain_evening: _input_number_state
    activity_duration_minutes: _input_number_state
    outing_excursion: _input_number_state
    brace_comfort: _input_number_state
    outing_pain: _input_number_state
    outing_fatuige: _input_number_state
    recovery_days: _input_number_state
    worst_pain_today: _input_number_state
    anxiety_score_morning: _input_number_state
    depression_score_morning: _input_number_state
    anxiety_score_afternoon: _input_number_state
    anxiety_score_evening: _input_number_state
    depression_score_afternoon: _input_number_state
    depression_score_evening: _input_number_state
    fatuige_score_morning: _input_number_state
    fatuige_score_afternoon: _input_number_state
    fatuige_acore_evening: _input_number_state
    syth_steps_yesterday: _input_number_state

    @staticmethod
    def reload():
        ...

    @staticmethod
    def set_value(*, entity_id: str, value: float):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def decrement(*, entity_id: str, amount: float | None=None):
        """Decrease an input number entity value by a certain amount.

        Args:
            entity_id: Entity ID
            amount: The amount to decrease the input number with. If not provided, the step of the number entity will be used."""
        ...

    @staticmethod
    def increment(*, entity_id: str, amount: float | None=None):
        """Increase an input number entity value by a certain amount.

        Args:
            entity_id: Entity ID
            amount: The amount to increase the input number with. If not provided, the step of the number entity will be used."""
        ...

    @staticmethod
    def min(*, entity_id: str):
        """Set an input number entity to its minimum value.

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def max(*, entity_id: str):
        """Set an input number entity to its maximum value.

        Args:
            entity_id: Entity ID"""
        ...

class input_select:

    @staticmethod
    def reload():
        ...

    @staticmethod
    def select_first(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def select_last(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def select_next(*, entity_id: str, cycle: bool=True):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def select_option(*, entity_id: str, option: str):
        '''

        Args:
            entity_id: Entity ID
            option:  Example: "Item A"'''
        ...

    @staticmethod
    def select_previous(*, entity_id: str, cycle: bool=True):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_options(*, entity_id: str, options: str):
        """

        Args:
            entity_id: Entity ID
            options:  Example: ["Item A", "Item B", "Item C"]"""
        ...

    @staticmethod
    def random(*, entity_id: str, options: Any | None=None):
        """Select an random option for an input_select entity.

        Args:
            entity_id: Entity ID
            options: Limits the options to select from. If not provided, all options will be considered."""
        ...

    @staticmethod
    def shuffle(*, entity_id: str):
        """Shuffles the list of selectable options for an `input_select` entity. This is not persistent and will be undone once reloaded or Home Assistant restarts.

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def sort(*, entity_id: str):
        """Sorts the list of selectable options for an `input_select` entity. This is not persistent and will be undone once reloaded or Home Assistant restarts.

        Args:
            entity_id: Entity ID"""
        ...

class input_text:
    external_ip: _input_text_state
    env_can_summary_store: _input_text_state
    justices_external_ip: _input_text_state
    last_precipitation_kind: _input_text_state
    next_payment_message: _input_text_state
    opnsense_wan_last_status: _input_text_state
    last_precipitation_amount: _input_text_state
    last_alert_aea_updated: _input_text_state
    last_alert_aeso_updated: _input_text_state
    weather_url: _input_text_state
    syth_iphone_last_state: _input_text_state
    other_meds_taken: _input_text_state
    missed_meds: _input_text_state
    meds_side_effect: _input_text_state
    pain_type: _input_text_state
    fibromyalgia_notes: _input_text_state
    joint_pain: _input_text_state
    instability_events: _input_text_state
    paresthesia: _input_text_state
    eye_drops_use: _input_text_state
    eye_symptoms: _input_text_state
    outing_type: _input_text_state
    sensory_excursion: _input_text_state
    other_supports: _input_text_state
    alcohol: _input_text_state
    meals_skipped: _input_text_state
    weather_notes: _input_text_state
    recovery_actions: _input_text_state
    clinician_notes: _input_text_state
    triggers_morning: _input_text_state
    triggers_afternoon: _input_text_state
    triggers_evening: _input_text_state
    water_drank_amount: _input_text_state
    meals_eaten_type_breakfast: _input_text_state
    meals_eaten_type_lunch: _input_text_state
    meals_eaten_type_dinner: _input_text_state
    caffeine_type_1: _input_text_state
    caffeine_type_2: _input_text_state
    caffeine_type_3: _input_text_state
    caffeine_type_4: _input_text_state
    last_weather_condition: _input_text_state
    set_adjustable_timer_hr_min: _input_text_state
    clock_seconds: _input_text_state
    post_status_text: _input_text_state
    post_status_update_file_name: _input_text_state
    statement_to_speak: _input_text_state
    env_can_last_advisory_state: _input_text_state
    env_can_last_warning_state: _input_text_state
    env_can_last_watches_state: _input_text_state
    discord_last_status: _input_text_state
    discord_last_status_justice: _input_text_state
    discord_last_game: _input_text_state
    discord_last_game_justice: _input_text_state
    discord_last_attributes: _input_text_state
    discord_last_attributes_justice: _input_text_state

    @staticmethod
    def reload():
        ...

    @staticmethod
    def set_value(*, entity_id: str, value: str):
        """

        Args:
            entity_id: Entity ID
            value:  Example: This is an example text"""
        ...

class lawn_mower:

    @staticmethod
    def start_mowing(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def pause(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def dock(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

class _light_state(StateVal):
    brightness: int
    browserID: str
    color_mode: str
    color_temp_kelvin: int
    effect: Any
    effect_list: list
    hs_color: tuple
    max_color_temp_kelvin: int
    min_color_temp_kelvin: int
    restored: bool
    rgb_color: tuple
    rgbw_color: Any
    supported_color_modes: list
    supported_features: int
    type: str
    xy_color: tuple

    def turn_on(self, *, transition: int | None=None, rgb_color: tuple[int, int, int] | None=None, color_temp_kelvin: int | None=None, brightness_pct: int | None=None, brightness_step_pct: int | None=None, effect: str | None=None, rgbw_color: Any | None=None, rgbww_color: Any | None=None, color_name: Literal['', 'homeassistant', 'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'goldenrod', 'gray', 'green', 'greenyellow', 'grey', 'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightslategrey', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'navy', 'navyblue', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver', 'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'white', 'whitesmoke', 'yellow', 'yellowgreen'] | None=None, hs_color: Any | None=None, xy_color: Any | None=None, brightness: int | None=None, brightness_step: int | None=None, white=None, profile: str | None=None, flash: Literal['', 'long', 'short'] | None=None):
        """

        Args:
            rgb_color:  Example: [255, 100, 100]
            rgbw_color:  Example: [255, 100, 100, 50]
            rgbww_color:  Example: [255, 100, 100, 50, 70]
            hs_color:  Example: [300, 70]
            xy_color:  Example: [0.52, 0.43]
            profile:  Example: relax"""
        ...

    def turn_off(self, *, transition: int | None=None, flash: Literal['', 'long', 'short'] | None=None):
        ...

    def toggle(self, *, transition: int | None=None, rgb_color: tuple[int, int, int] | None=None, color_temp_kelvin: int | None=None, brightness_pct: int | None=None, effect: str | None=None, rgbw_color: Any | None=None, rgbww_color: Any | None=None, color_name: Literal['', 'homeassistant', 'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'goldenrod', 'gray', 'green', 'greenyellow', 'grey', 'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightslategrey', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'navy', 'navyblue', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver', 'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'white', 'whitesmoke', 'yellow', 'yellowgreen'] | None=None, hs_color: Any | None=None, xy_color: Any | None=None, brightness: int | None=None, white=None, profile: str | None=None, flash: Literal['', 'long', 'short'] | None=None):
        """

        Args:
            rgb_color:  Example: [255, 100, 100]
            rgbw_color:  Example: [255, 100, 100, 50]
            rgbww_color:  Example: [255, 100, 100, 50, 70]
            hs_color:  Example: [300, 70]
            xy_color:  Example: [0.52, 0.43]
            profile:  Example: relax"""
        ...

class light:
    k_bedside_lamp: _light_state
    bedroom_lights: _light_state
    furnace_room_lights: _light_state
    stovetop: _light_state
    furnace_room_1: _light_state
    understairs_closet: _light_state
    furnace_room_2: _light_state
    bedside_lamp: _light_state
    bedroom_closet: _light_state
    outside: _light_state
    syth_local_screen: _light_state
    desktop_screen: _light_state
    laptop_screen: _light_state
    syth_tailscale_screen: _light_state
    ipad_local_screen: _light_state
    browser_mod_c9a5c39b_a64fa6bd_screen: _light_state

    @staticmethod
    def turn_on(*, entity_id: str, transition: int | None=None, rgb_color: tuple[int, int, int] | None=None, color_temp_kelvin: int | None=None, brightness_pct: int | None=None, brightness_step_pct: int | None=None, effect: str | None=None, rgbw_color: Any | None=None, rgbww_color: Any | None=None, color_name: Literal['', 'homeassistant', 'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'goldenrod', 'gray', 'green', 'greenyellow', 'grey', 'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightslategrey', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'navy', 'navyblue', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver', 'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'white', 'whitesmoke', 'yellow', 'yellowgreen'] | None=None, hs_color: Any | None=None, xy_color: Any | None=None, brightness: int | None=None, brightness_step: int | None=None, white=None, profile: str | None=None, flash: Literal['', 'long', 'short'] | None=None):
        """

        Args:
            entity_id: Entity ID
            rgb_color:  Example: [255, 100, 100]
            rgbw_color:  Example: [255, 100, 100, 50]
            rgbww_color:  Example: [255, 100, 100, 50, 70]
            hs_color:  Example: [300, 70]
            xy_color:  Example: [0.52, 0.43]
            profile:  Example: relax"""
        ...

    @staticmethod
    def turn_off(*, entity_id: str, transition: int | None=None, flash: Literal['', 'long', 'short'] | None=None):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str, transition: int | None=None, rgb_color: tuple[int, int, int] | None=None, color_temp_kelvin: int | None=None, brightness_pct: int | None=None, effect: str | None=None, rgbw_color: Any | None=None, rgbww_color: Any | None=None, color_name: Literal['', 'homeassistant', 'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'goldenrod', 'gray', 'green', 'greenyellow', 'grey', 'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightslategrey', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'navy', 'navyblue', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver', 'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'white', 'whitesmoke', 'yellow', 'yellowgreen'] | None=None, hs_color: Any | None=None, xy_color: Any | None=None, brightness: int | None=None, white=None, profile: str | None=None, flash: Literal['', 'long', 'short'] | None=None):
        """

        Args:
            entity_id: Entity ID
            rgb_color:  Example: [255, 100, 100]
            rgbw_color:  Example: [255, 100, 100, 50]
            rgbww_color:  Example: [255, 100, 100, 50, 70]
            hs_color:  Example: [300, 70]
            xy_color:  Example: [0.52, 0.43]
            profile:  Example: relax"""
        ...

class llmvision:

    @staticmethod
    def image_analyzer(*, provider: str, message: str, include_filename: bool=False, model: str | None=None, store_in_timeline: bool=False, use_memory: bool=False, image_file: str | None=None, image_entity: str | None=None, target_width: int=1280, max_tokens: float=3000, generate_title: bool=False, expose_images: bool=False, response_format: Literal['', 'text', 'json']='text', structure: str | None=None, title_field: str='title', description_field: str='description') -> dict[str, Any]:
        """Analyze an image with AI

        Args:
            provider: Configuration to use
            message: Model prompt Example: Describe the image
            include_filename: Include filename in the request
            model: Model to use. Uncheck for default. Example: gpt-4o-mini
            store_in_timeline: Create a new event in the timeline for this detection. Example: True
            use_memory: Use information stored in memory to provide additional context. Memory must be set up. Example: True
            image_file: Local path to image Example: /config/www/tmp/front_door.jpg
            image_entity: Image or camera entity to analyze Example: image.front_door_person
            target_width: Width in pixels to downscale Example: 1280
            max_tokens: Maximum number of tokens to generate Example: 3000
            generate_title: Generate a title. (Used for notifications and events)
            expose_images: Save the key frame. This will save analyzed frames in /media/llmvision/snapshots so they can be used for notifications. The file path will be included in the response.
            response_format: Format of the response - text for natural language or json for structured data Example: json
            structure: JSON schema defining the expected response structure (only used when response_format is json). To enable automatic title generation for timeline events, include a field in your schema for the title (e.g., "title": {"type": "string", "description": "Event title"}) and specify the field names below. Example: {"type": "object", "properties": {"title": {"type": "string", "description": "Event title"}, "description": {"type": "string", "description": "Event description"}, "confidence": {"type": "number", "minimum": 0, "maximum": 100}}, "required": ["title", "description", "confidence"], "additionalProperties": false}
            title_field: Name of the field in your JSON schema that contains the event title (used for timeline). Leave empty to use fallback title "Motion detected". Example: title
            description_field: Name of the field in your JSON schema that contains the event description (used for timeline). Example: description"""
        ...

    @staticmethod
    def video_analyzer(*, provider: str, message: str, include_filename: bool=False, model: str | None=None, store_in_timeline: bool=False, use_memory: bool=False, video_file: str | None=None, event_id: str | None=None, max_frames: int=3, target_width: int=1280, max_tokens: float=3000, generate_title: bool=False, expose_images: bool=False, response_format: Literal['', 'text', 'json']='text', structure: str | None=None, title_field: str='title', description_field: str='description') -> dict[str, Any]:
        """Analyze video with AI

        Args:
            provider: Configuration to use
            message: Model prompt Example: Describe what happens in the video
            include_filename: Include filename in the request
            model: Model to use. Uncheck for default. Example: gpt-4o-mini
            store_in_timeline: Create a new event in the timeline for this detection. Example: True
            use_memory: Use information stored in memory to provide additional context. Memory must be set up. Example: True
            video_file: One or multiple local paths or URLs to video. Use a new line to separate multiple entries. Example: /config/www/recordings/front_door.mp4
            event_id: Frigate Event ID Example: 1712108310.968815-r28cdt
            max_frames: How many frames to analyze. Picks frames with the most movement. Example: 3
            target_width: Width in pixels to downscale Example: 1280
            max_tokens: Maximum number of tokens to generate Example: 3000
            generate_title: Generate a title. (Used for notifications and events)
            expose_images: Save the key frame. This will save analyzed frames in /media/llmvision/snapshots so they can be used for notifications. The file path will be included in the response.
            response_format: Format of the response - text for natural language or json for structured data Example: json
            structure: JSON schema defining the expected response structure (only used when response_format is json). To enable automatic title generation for timeline events, include a field in your schema for the title (e.g., "title": {"type": "string", "description": "Event title"}) and specify the field names below. Example: {"type": "object", "properties": {"title": {"type": "string", "description": "Event title"}, "description": {"type": "string", "description": "Event description"}, "confidence": {"type": "number", "minimum": 0, "maximum": 100}}, "required": ["title", "description", "confidence"], "additionalProperties": false}
            title_field: Name of the field in your JSON schema that contains the event title (used for timeline). Leave empty to use fallback title "Motion detected". Example: title
            description_field: Name of the field in your JSON schema that contains the event description (used for timeline). Example: description"""
        ...

    @staticmethod
    def stream_analyzer(*, provider: str, message: str, image_entity: str, duration: int=5, include_filename: bool=False, model: str | None=None, store_in_timeline: bool=False, use_memory: bool=False, max_frames: int=3, target_width: int=1280, max_tokens: float=3000, generate_title: bool=False, expose_images: bool=False, response_format: Literal['', 'text', 'json']='text', structure: str | None=None, title_field: str='title', description_field: str='description') -> dict[str, Any]:
        """Analyze a live camera stream with AI

        Args:
            provider: Configuration to use
            message: Model prompt Example: Describe what happens in the camera feed
            image_entity: Camera entity to stream Example: camera.front_door
            duration: How long to record in seconds Example: 5
            include_filename: Include camera name in request
            model: Model to use. Uncheck for default. Example: gpt-4o-mini
            store_in_timeline: Create a new event in the timeline for this detection. Example: True
            use_memory: Use information stored in memory to provide additional context. Memory must be set up. Example: True
            max_frames: How many frames to analyze. Picks frames with the most movement. Example: 3
            target_width: Width in pixels to downscale Example: 1280
            max_tokens: Maximum number of tokens to generate Example: 3000
            generate_title: Generate a title. (Used for notifications and events)
            expose_images: Save the key frame. This will save analyzed frames in /media/llmvision/snapshots so they can be used for notifications. The file path will be included in the response.
            response_format: Format of the response - text for natural language or json for structured data Example: json
            structure: JSON schema defining the expected response structure (only used when response_format is json). To enable automatic title generation for timeline events, include a field in your schema for the title (e.g., "title": {"type": "string", "description": "Event title"}) and specify the field names below. Example: {"type": "object", "properties": {"title": {"type": "string", "description": "Event title"}, "description": {"type": "string", "description": "Event description"}, "confidence": {"type": "number", "minimum": 0, "maximum": 100}}, "required": ["title", "description", "confidence"], "additionalProperties": false}
            title_field: Name of the field in your JSON schema that contains the event title (used for timeline). Leave empty to use fallback title "Motion detected". Example: title
            description_field: Name of the field in your JSON schema that contains the event description (used for timeline). Example: description"""
        ...

    @staticmethod
    def data_analyzer(*, provider: str, message: str='How many cars are parked?', sensor_entity: str, include_filename: bool=False, model: str | None=None, store_in_timeline: bool=False, use_memory: bool=False, image_file: str | None=None, image_entity: str | None=None, target_width: int=1280, max_tokens: float=3000, generate_title: bool=False, expose_images: bool=False) -> dict[str, Any]:
        """Update sensors with data extracted from images (Beta)

        Args:
            provider: Configuration to use
            message: Describe what should be extracted from the image. Data types and available options will be recognized automatically based the provided sensor. Example: How many cars are parked?
            sensor_entity: The sensor to update
            include_filename: Include filename in the request
            model: Model to use. Uncheck for default. Example: gpt-4o-mini
            store_in_timeline: Create a new event in the timeline for this detection. Example: True
            use_memory: Use information stored in memory to provide additional context. Memory must be set up. Example: True
            image_file: Local path to image Example: /config/www/tmp/front_door.jpg
            image_entity: Image or camera entity to analyze Example: image.front_door_person
            target_width: Width in pixels to downscale Example: 1280
            max_tokens: Maximum number of tokens to generate Example: 3000
            generate_title: Generate a title. (Used for notifications and events)
            expose_images: Save the key frame. This will save analyzed frames in /media/llmvision/snapshots so they can be used for notifications. The file path will be included in the response."""
        ...

    @staticmethod
    def create_event(*, title: str, description: str, label: Literal['', 'Alarm', 'Bike', 'Bird', 'Bus', 'Camera', 'Car', 'Cat', 'Dog', 'Door', 'Key', 'Light', 'Lock', 'Motorcycle', 'Package', 'Person', 'Plant', 'Sensor', 'Tree', 'Truck', 'Van'] | None=None, image_path: str | None=None, camera_entity: str | None=None, start_time: datetime | None=None, end_time: datetime | None=None):
        """Creates a new event in the LLM Vision Timeline

        Args:
            title: Event Title Example: Car seen
            description: Event Description Example: A car was seen pulling into a driveway
            label: Label to assign the event to Example: Car
            image_path: Image of the event. Must be stored in "/media/llmvision/snapshots/" Example: /media/llmvision/snapshots/example.jpg
            camera_entity: Camera that recorded the event. Example: camera.front_door
            start_time: Time and date the event started. Set to now if left blank. Format: (YYYY-MM-DD HH:MM:SS) Example: 2022-02-22 13:30:00
            end_time: Time and date the event ended. Set to one minute after start if left blank. Format: (YYYY-MM-DD HH:MM:SS) Example: 2022-02-22 13:30:00"""
        ...

class local_file:

    @staticmethod
    def update_file_path(*, entity_id: str, file_path: str):
        """

        Args:
            entity_id: Entity ID
            file_path:  Example: /config/www/images/image.jpg"""
        ...

class lock:

    @staticmethod
    def unlock(*, entity_id: str, code: str | None=None):
        """

        Args:
            entity_id: Entity ID
            code:  Example: 1234"""
        ...

    @staticmethod
    def lock(*, entity_id: str, code: str | None=None):
        """

        Args:
            entity_id: Entity ID
            code:  Example: 1234"""
        ...

    @staticmethod
    def open(*, entity_id: str, code: str | None=None):
        """

        Args:
            entity_id: Entity ID
            code:  Example: 1234"""
        ...

class logbook:

    @staticmethod
    def log(*, name: str, message: str, entity_id: str | None=None, domain: str | None=None):
        """

        Args:
            name:  Example: Kitchen
            message:  Example: is being used
            domain:  Example: light"""
        ...

class logger:

    @staticmethod
    def set_default_level(*, level: Literal['', 'debug', 'info', 'warning', 'error', 'fatal', 'critical'] | None=None):
        ...

    @staticmethod
    def set_level():
        ...

class mass_queue:

    @staticmethod
    def get_queue_items(*, entity: str, limit: int | None=None, offset: int | None=None, limit_before: int=5, limit_after: int=100) -> dict[str, Any]:
        """

        Args:
            entity: Music Assistant Media Player Entity
            limit: Limit on the number of items in queue to return Example: 500
            offset: Location in queue to start where zero equals the first item in queue, not the current item. Example: 50
            limit_before: Number of items to pull before current active item in queue. Example: 5
            limit_after: Number of items to pull after current active item in queue. Example: 50"""
        ...

    @staticmethod
    def move_queue_item_down(*, queue_item_id: str, entity: str):
        """

        Args:
            entity: Music Assistant Media Player Entity"""
        ...

    @staticmethod
    def move_queue_item_next(*, queue_item_id: str, entity: str):
        """

        Args:
            entity: Music Assistant Media Player Entity"""
        ...

    @staticmethod
    def move_queue_item_up(*, queue_item_id: str, entity: str):
        """

        Args:
            entity: Music Assistant Media Player Entity"""
        ...

    @staticmethod
    def play_queue_item(*, queue_item_id: str, entity: str):
        """

        Args:
            entity: Music Assistant Media Player Entity"""
        ...

    @staticmethod
    def remove_queue_item(*, queue_item_id: str, entity: str):
        """

        Args:
            entity: Music Assistant Media Player Entity"""
        ...

    @staticmethod
    def send_command(*, command: str, config_entry_id: str, data: Any | None=None) -> dict[str, Any]:
        """

        Args:
            command: Command to send to Music Assistant
            data: Command data to send"""
        ...

    @staticmethod
    def unfavorite_current_item(*, entity: str):
        """

        Args:
            entity: Music Assistant Media Player Entity"""
        ...

    @staticmethod
    def get_recommendations(*, entity: str, providers: str | None=None) -> dict[str, Any]:
        """

        Args:
            entity: Music Assistant Media Player Entity
            providers: Limit recommendations to the specified providers."""
        ...

    @staticmethod
    def get_group_volume(*, entity: str) -> dict[str, Any]:
        """

        Args:
            entity: Music Assistant Media Player Entity"""
        ...

    @staticmethod
    def set_group_volume(*, entity: str, volume_level: int):
        """

        Args:
            entity: Music Assistant Media Player Entity
            volume_level: Volume level to set the player to."""
        ...

    @staticmethod
    def clear_queue_from_here(*, entity: str):
        """

        Args:
            entity: Music Assistant Media Player Entity"""
        ...

    @staticmethod
    def get_playlist_tracks(*, config_entry_id: str, uri: str, page: float | None=None) -> dict[str, Any]:
        """

        Args:
            uri: URI for the playlist Example: library://playlist/12"""
        ...

    @staticmethod
    def get_album_tracks(*, config_entry_id: str, uri: str, page: float | None=None) -> dict[str, Any]:
        """

        Args:
            uri: URI for the album Example: library://album/12"""
        ...

    @staticmethod
    def get_artist_tracks(*, config_entry_id: str, uri: str, page: float | None=None) -> dict[str, Any]:
        """

        Args:
            uri: URI for the artist Example: library://artist/12"""
        ...

    @staticmethod
    def get_podcast_episodes(*, config_entry_id: str, uri: str) -> dict[str, Any]:
        """

        Args:
            uri: URI for the podcast Example: library://podcast/12"""
        ...

    @staticmethod
    def get_album(*, config_entry_id: str, uri: str) -> dict[str, Any]:
        """

        Args:
            uri: URI for the Album Example: library://album/12"""
        ...

    @staticmethod
    def get_artist(*, config_entry_id: str, uri: str) -> dict[str, Any]:
        """

        Args:
            uri: URI for the artist Example: library://artist/12"""
        ...

    @staticmethod
    def get_playlist(*, config_entry_id: str, uri: str) -> dict[str, Any]:
        """

        Args:
            uri: URI for the playlist Example: library://playlist/12"""
        ...

    @staticmethod
    def get_podcast(*, config_entry_id: str, uri: str) -> dict[str, Any]:
        """

        Args:
            uri: URI for the podcast Example: library://podcast/12"""
        ...

    @staticmethod
    def remove_playlist_tracks(*, config_entry_id: str, playlist_id: str, positions_to_remove: str):
        ...

class mastodon:

    @staticmethod
    def get_account(*, config_entry_id: str, account_name: str) -> dict[str, Any]:
        ...

    @staticmethod
    def mute_account(*, config_entry_id: str, account_name: str, duration=None, hide_notifications: bool=True):
        ...

    @staticmethod
    def unmute_account(*, config_entry_id: str, account_name: str):
        ...

    @staticmethod
    def post(*, config_entry_id: str, status: str, media_warning: bool, visibility: Literal['', 'public', 'unlisted', 'private', 'direct'] | None=None, idempotency_key: str | None=None, content_warning: str | None=None, language=None, media: str | None=None, media_description: str | None=None):
        ...

class _media_player_state(StateVal):
    active_queue: str
    app_id: str
    app_name: str
    assumed_state: bool
    audio_interaction_required: bool
    browserID: str
    entity_picture_local: Any
    group_members: list
    is_volume_muted: bool
    mass_player_type: str
    media_content_type: str
    media_position: float
    media_position_updated_at: datetime
    repeat: str
    restored: bool
    shuffle: bool
    source: str
    source_list: list
    supported_features: int
    type: str
    video_interaction_required: bool
    volume_level: float

    def turn_on(self):
        ...

    def turn_off(self):
        ...

    def toggle(self):
        ...

    def volume_up(self):
        ...

    def volume_down(self):
        ...

    def media_play_pause(self):
        ...

    def media_play(self):
        ...

    def media_pause(self):
        ...

    def media_stop(self):
        ...

    def media_next_track(self):
        ...

    def media_previous_track(self):
        ...

    def clear_playlist(self):
        ...

    def volume_set(self, volume_level: int):
        ...

    def volume_mute(self, is_volume_muted: bool):
        ...

    def media_seek(self, seek_position: float):
        ...

    def join(self, group_members: str):
        """

        Args:
            group_members:  Example: - media_player.multiroom_player2
                - media_player.multiroom_player3
                """
        ...

    def select_source(self, source: str):
        """

        Args:
            source:  Example: video1"""
        ...

    def select_sound_mode(self, sound_mode: str | None):
        """

        Args:
            sound_mode:  Example: Music"""
        ...

    def play_media(self, *, media, enqueue: Literal['', 'play', 'next', 'add', 'replace'] | None=None, announce: bool | None=None):
        """

        Args:
            media:  Example: {"media_content_id": "https://home-assistant.io/images/cast/splash.png", "media_content_type": "music"}
            announce:  Example: true"""
        ...

    def browse_media(self, *, media_content_type: str | None=None, media_content_id: str | None=None) -> dict[str, Any]:
        """

        Args:
            media_content_type:  Example: music
            media_content_id:  Example: A:ALBUMARTIST/Beatles"""
        ...

    def search_media(self, *, search_query: str, media_content_type: str | None=None, media_content_id: str | None=None, media_filter_classes: str | None=None) -> dict[str, Any]:
        """

        Args:
            search_query:  Example: Beatles
            media_content_type:  Example: music
            media_content_id:  Example: A:ALBUMARTIST/Beatles
            media_filter_classes:  Example: ['album', 'artist']"""
        ...

    def shuffle_set(self, shuffle: bool):
        ...

    def unjoin(self):
        ...

    def repeat_set(self, repeat: Literal['', 'off', 'all', 'one']):
        ...

class media_extractor:

    @staticmethod
    def extract_media_url(*, url: str, format_query: str | None=None) -> dict[str, Any]:
        """

        Args:
            url:  Example: https://www.youtube.com/watch?v=dQw4w9WgXcQ
            format_query:  Example: best"""
        ...

    @staticmethod
    def play_media(*, entity_id: str, media_content_id: str, media_content_type: Literal['', 'CHANNEL', 'EPISODE', 'PLAYLIST MUSIC', 'MUSIC', 'TVSHOW', 'VIDEO']):
        """

        Args:
            entity_id: Entity ID
            media_content_id:  Example: https://soundcloud.com/bruttoband/brutto-11"""
        ...

class media_player:
    bedroom_tv: _media_player_state
    tv_group: _media_player_state
    bedroom_speaker: _media_player_state
    living_room_tv: _media_player_state
    bathroom: _media_player_state
    two_normal: _media_player_state
    speakers: _media_player_state
    living_room: _media_player_state
    living_room_tv_2: _media_player_state
    spotify_ashton_parrott: _media_player_state
    bed_and_bath: _media_player_state
    spotify_jusparr: _media_player_state
    playstation_4: _media_player_state
    laptop: _media_player_state
    playstation_4_2: _media_player_state
    syth_local: _media_player_state
    desktop: _media_player_state
    laptop_2: _media_player_state
    syth_tailscale: _media_player_state
    plex_plex_for_android_tv_chromecast_google_tv: _media_player_state
    plex_plex_web_chrome_windows: _media_player_state
    bedroom_speaker_2: _media_player_state
    bathroom_2: _media_player_state
    bed_and_bath_2: _media_player_state
    two_normal_2: _media_player_state
    speakers_2: _media_player_state
    living_room_2: _media_player_state
    ipad_local: _media_player_state
    plex_plex_web_chrome_windows_2: _media_player_state
    plex_plex_for_playstation_4_ps4_200: _media_player_state
    plex_justice_parrott_jusparr_plex_for_android_tv_chromecast_google_tv_hd: _media_player_state
    plex_plex_for_ios_iphone: _media_player_state
    plex_justice_parrott_jusparr_plex_web_firefox_windows: _media_player_state
    browser_mod_c9a5c39b_a64fa6bd: _media_player_state
    livingroom_tv: _media_player_state
    tv_group_2: _media_player_state
    bedroom_speaker_4: _media_player_state
    plex_plex_web_chrome_windows_3: _media_player_state
    bedroom_speaker_3: _media_player_state
    bathroom_3: _media_player_state
    tv_group_3: _media_player_state
    two_normal_3: _media_player_state
    bed_and_bath_3: _media_player_state
    livingroom_tv_airplay: _media_player_state
    speakers_3: _media_player_state
    tv_group_airplay: _media_player_state
    two_normal_airplay: _media_player_state
    bed_and_bath_airplay: _media_player_state

    @staticmethod
    def turn_on(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_off(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def volume_up(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def volume_down(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def media_play_pause(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def media_play(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def media_pause(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def media_stop(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def media_next_track(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def media_previous_track(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def clear_playlist(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def volume_set(*, entity_id: str, volume_level: int):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def volume_mute(*, entity_id: str, is_volume_muted: bool):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def media_seek(*, entity_id: str, seek_position: float):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def join(*, entity_id: str, group_members: str):
        """

        Args:
            entity_id: Entity ID
            group_members:  Example: - media_player.multiroom_player2
                - media_player.multiroom_player3
                """
        ...

    @staticmethod
    def select_source(*, entity_id: str, source: str):
        """

        Args:
            entity_id: Entity ID
            source:  Example: video1"""
        ...

    @staticmethod
    def select_sound_mode(*, entity_id: str, sound_mode: str | None=None):
        """

        Args:
            entity_id: Entity ID
            sound_mode:  Example: Music"""
        ...

    @staticmethod
    def play_media(*, entity_id: str, media, enqueue: Literal['', 'play', 'next', 'add', 'replace'] | None=None, announce: bool | None=None):
        """

        Args:
            entity_id: Entity ID
            media:  Example: {"media_content_id": "https://home-assistant.io/images/cast/splash.png", "media_content_type": "music"}
            announce:  Example: true"""
        ...

    @staticmethod
    def browse_media(*, entity_id: str, media_content_type: str | None=None, media_content_id: str | None=None) -> dict[str, Any]:
        """

        Args:
            entity_id: Entity ID
            media_content_type:  Example: music
            media_content_id:  Example: A:ALBUMARTIST/Beatles"""
        ...

    @staticmethod
    def search_media(*, entity_id: str, search_query: str, media_content_type: str | None=None, media_content_id: str | None=None, media_filter_classes: str | None=None) -> dict[str, Any]:
        """

        Args:
            entity_id: Entity ID
            search_query:  Example: Beatles
            media_content_type:  Example: music
            media_content_id:  Example: A:ALBUMARTIST/Beatles
            media_filter_classes:  Example: ['album', 'artist']"""
        ...

    @staticmethod
    def shuffle_set(*, entity_id: str, shuffle: bool):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def unjoin(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def repeat_set(*, entity_id: str, repeat: Literal['', 'off', 'all', 'one']):
        """

        Args:
            entity_id: Entity ID"""
        ...

class mqtt:

    @staticmethod
    def publish(*, topic: str, payload=None, evaluate_payload: bool=False, qos: Literal['', '0', '1', '2']=0, retain: bool=False):
        """

        Args:
            topic:  Example: /homeassistant/hello
            payload:  Example: The temperature is {{ states('sensor.temperature') }}"""
        ...

    @staticmethod
    def dump(*, topic: str | None=None, duration: int=5):
        """

        Args:
            topic:  Example: OpenZWave/#"""
        ...

    @staticmethod
    def reload():
        ...

class music_assistant:

    @staticmethod
    def search(*, config_entry_id: str, name: str, media_type: Literal['', 'artist', 'album', 'audiobook', 'playlist', 'podcast', 'track', 'radio'] | None=None, artist: str | None=None, album: str | None=None, limit: int=5, library_only: bool=False) -> dict[str, Any]:
        """

        Args:
            name:  Example: We Are The Champions
            media_type:  Example: playlist
            artist:  Example: Queen
            album:  Example: News of the world
            limit:  Example: 25
            library_only:  Example: true"""
        ...

    @staticmethod
    def get_library(*, config_entry_id: str, media_type: Literal['', 'artist', 'album', 'audiobook', 'playlist', 'podcast', 'track', 'radio'], favorite: bool=False, search: str | None=None, limit: int=25, offset: int=0, order_by: Literal['', 'name', 'name_desc', 'sort_name', 'sort_name_desc', 'timestamp_added', 'timestamp_added_desc', 'last_played', 'last_played_desc', 'play_count', 'play_count_desc', 'year', 'year_desc', 'position', 'position_desc', 'artist_name', 'artist_name_desc', 'random', 'random_play_count'] | None=None, album_type: Literal['', 'album', 'single', 'compilation', 'ep', 'unknown'] | None=None, album_artists_only: bool=False) -> dict[str, Any]:
        """

        Args:
            media_type:  Example: playlist
            favorite:  Example: true
            search:  Example: We Are The Champions
            limit:  Example: 25
            offset:  Example: 25
            order_by:  Example: random
            album_type:  Example: single
            album_artists_only:  Example: true"""
        ...

    @staticmethod
    def play_media(*, entity_id: str, media_id: Any, media_type: Literal['', 'artist', 'album', 'audiobook', 'folder', 'playlist', 'podcast', 'track', 'radio'] | None=None, artist: str | None=None, album: str | None=None, enqueue: Literal['', 'play', 'replace', 'next', 'replace_next', 'add'] | None=None, radio_mode: bool | None=None):
        """

        Args:
            entity_id: Entity ID
            media_id:  Example: spotify://playlist/aabbccddeeff
            media_type:  Example: playlist
            artist:  Example: Queen
            album:  Example: News of the world"""
        ...

    @staticmethod
    def play_announcement(*, entity_id: str, url: str, use_pre_announce: bool | None=None, pre_announce_url: str | None=None, announce_volume: int | None=None):
        """

        Args:
            entity_id: Entity ID
            url:  Example: http://someremotesite.com/doorbell.mp3
            use_pre_announce:  Example: true
            pre_announce_url:  Example: http://someremotesite.com/chime.mp3
            announce_volume:  Example: 75"""
        ...

    @staticmethod
    def transfer_queue(*, entity_id: str, source_player: str | None=None, auto_play: bool | None=None):
        """

        Args:
            entity_id: Entity ID
            auto_play:  Example: true"""
        ...

    @staticmethod
    def get_queue(*, entity_id: str) -> dict[str, Any]:
        """

        Args:
            entity_id: Entity ID"""
        ...

class nodered:

    @staticmethod
    def trigger(*, entity_id: str, output_path: str='0', message: Any | None=None):
        """

        Args:
            entity_id: Entity ID
            output_path:  Example: 1,2"""
        ...

class _notify_state(StateVal):
    supported_features: int

    def send_message(self, *, message: str, title: str | None=None):
        ...

class notify:
    ythsaz_group_kirito_3972: _notify_state
    telegram_bot_1112301530_1025100466: _notify_state
    telegram_bot_1112301530_5256494429: _notify_state
    telegram_bot_1112301530_1001888460290: _notify_state
    ythsaz_direct_message_jusparr: _notify_state
    ythsaz_direct_message_russell117045: _notify_state
    ythsaz_direct_message_toxiccrumble: _notify_state
    ythsaz_direct_message_howler4522: _notify_state
    telegram_bot_1112301530_1002895905903: _notify_state
    telegram_bot_1112301530_1002009033814: _notify_state
    telegram_bot_1112301530_1087968824: _notify_state

    @staticmethod
    def send_message(*, entity_id: str, message: str, title: str | None=None):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def persistent_notification(*, message: str, title: str | None=None, data: Any | None=None):
        """

        Args:
            message:  Example: The garage door has been open for 10 minutes.
            title:  Example: Your Garage Door Friend
            data:  Example: platform specific"""
        ...

    @staticmethod
    def sythsaz_twitter(*, message: str, title: str | None=None, target: Any | None=None, data: Any | None=None):
        """Sends a notification message using the sythsaz_twitter service.

        Args:
            message:  Example: The garage door has been open for 10 minutes.
            title:  Example: Your Garage Door Friend
            target:  Example: platform specific
            data:  Example: platform specific"""
        ...

    @staticmethod
    def mobile_app_syth(*, message: str, title: str | None=None, target: Any | None=None, data: Any | None=None):
        """Sends a notification message using the mobile_app_syth integration.

        Args:
            message:  Example: The garage door has been open for 10 minutes.
            title:  Example: Your Garage Door Friend
            target:  Example: platform specific
            data:  Example: platform specific"""
        ...

    @staticmethod
    def mobile_app_ipad(*, message: str, title: str | None=None, target: Any | None=None, data: Any | None=None):
        """Sends a notification message using the mobile_app_ipad integration.

        Args:
            message:  Example: The garage door has been open for 10 minutes.
            title:  Example: Your Garage Door Friend
            target:  Example: platform specific
            data:  Example: platform specific"""
        ...

    @staticmethod
    def mobile_app_s9_plus(*, message: str, title: str | None=None, target: Any | None=None, data: Any | None=None):
        """Sends a notification message using the mobile_app_s9_plus integration.

        Args:
            message:  Example: The garage door has been open for 10 minutes.
            title:  Example: Your Garage Door Friend
            target:  Example: platform specific
            data:  Example: platform specific"""
        ...

    @staticmethod
    def notify(*, message: str, title: str | None=None, target: Any | None=None, data: Any | None=None):
        """Sends a notification message using the notify service.

        Args:
            message:  Example: The garage door has been open for 10 minutes.
            title:  Example: Your Garage Door Friend
            target:  Example: platform specific
            data:  Example: platform specific"""
        ...

    @staticmethod
    def auto_from_ha(*, message: str, title: str | None=None, target: Any | None=None, data: Any | None=None):
        """Sends a notification message using the auto_from_ha service.

        Args:
            message:  Example: The garage door has been open for 10 minutes.
            title:  Example: Your Garage Door Friend
            target:  Example: platform specific
            data:  Example: platform specific"""
        ...

    @staticmethod
    def html5(*, message: str, title: str | None=None, target: Any | None=None, data: Any | None=None):
        """Sends a notification message using the html5 service.

        Args:
            message:  Example: The garage door has been open for 10 minutes.
            title:  Example: Your Garage Door Friend
            target:  Example: platform specific
            data:  Example: platform specific"""
        ...

    @staticmethod
    def ashtonparrott_gmail_com(*, message: str, title: str | None=None, target: Any | None=None, data: Any | None=None):
        """Sends a notification message using the ashtonparrott_gmail_com service.

        Args:
            message:  Example: The garage door has been open for 10 minutes.
            title:  Example: Your Garage Door Friend
            target:  Example: platform specific
            data:  Example: platform specific"""
        ...

class _number_state(StateVal):
    max: int | float
    min: int | float
    mode: str
    restored: bool
    step: int | float
    supported_features: int
    unit_of_measurement: str

    def set_value(self, value: str):
        """

        Args:
            value:  Example: 42"""
        ...

    def decrement(self, amount: float | None):
        """Decrease a number entity value by a certain amount.

        Args:
            amount: The amount to decrease the number with. If not provided, the step of the number entity will be used."""
        ...

    def increment(self, amount: float | None):
        """Increase a number entity value by a certain amount.

        Args:
            amount: The amount to increase the number with. If not provided, the step of the number entity will be used."""
        ...

    def min(self):
        """Set a number entity to its minimum value."""
        ...

    def max(self):
        """Set a number entity to its maximum value."""
        ...

class number:
    k_s_bedside_lamp_effect_speed: _number_state
    stovetop_effect_speed: _number_state
    furnace_room_1_effect_speed: _number_state
    understairs_closet_effect_speed: _number_state
    furnace_room_2_effect_speed: _number_state
    bedside_lamp_effect_speed: _number_state
    bedroom_closet_effect_speed: _number_state
    outside_effect_speed: _number_state
    living_room_alarm_volume: _number_state
    bathroom_alarm_volume: _number_state
    bedroom_speaker_alarm_volume: _number_state
    breaker_box_mic_sensitivity: _number_state
    backyard_camera_hq_contour_area: _number_state
    backyard_camera_hq_threshold: _number_state

    @staticmethod
    def set_value(*, entity_id: str, value: str):
        """

        Args:
            entity_id: Entity ID
            value:  Example: 42"""
        ...

    @staticmethod
    def decrement(*, entity_id: str, amount: float | None=None):
        """Decrease a number entity value by a certain amount.

        Args:
            entity_id: Entity ID
            amount: The amount to decrease the number with. If not provided, the step of the number entity will be used."""
        ...

    @staticmethod
    def increment(*, entity_id: str, amount: float | None=None):
        """Increase a number entity value by a certain amount.

        Args:
            entity_id: Entity ID
            amount: The amount to increase the number with. If not provided, the step of the number entity will be used."""
        ...

    @staticmethod
    def min(*, entity_id: str):
        """Set a number entity to its minimum value.

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def max(*, entity_id: str):
        """Set a number entity to its maximum value.

        Args:
            entity_id: Entity ID"""
        ...

class openweathermap:

    @staticmethod
    def get_minute_forecast(*, entity_id: str) -> dict[str, Any]:
        """

        Args:
            entity_id: Entity ID"""
        ...

class opnsense:

    @staticmethod
    def close_notice(*, id: str='all', multiple_opnsense=None):
        """

        Args:
            id:  Example: all"""
        ...

    @staticmethod
    def start_service(*, service_id: str | None=None, multiple_opnsense=None):
        ...

    @staticmethod
    def stop_service(*, service_id: str | None=None, multiple_opnsense=None):
        ...

    @staticmethod
    def restart_service(*, only_if_running: bool=False, service_id: str | None=None, multiple_opnsense=None):
        ...

    @staticmethod
    def system_halt(*, device_id=None, entity_id: str | None=None):
        """

        Args:
            entity_id:  Example: sensor.opnsense_interface_lan_status"""
        ...

    @staticmethod
    def system_reboot(*, device_id=None, entity_id: str | None=None):
        """

        Args:
            entity_id:  Example: sensor.opnsense_interface_lan_status"""
        ...

    @staticmethod
    def send_wol(*, interface: str, mac: str, multiple_opnsense=None):
        ...

    @staticmethod
    def reload_interface(*, interface: str, multiple_opnsense=None):
        ...

    @staticmethod
    def generate_vouchers(*, validity: Literal['', '14400', '28800', '86400', '172800', '259200', '345600', '432000', '518400', '604800', '1209600']='14400', expirytime: Literal['', '0', '21600', '43200', '86400', '172800', '259200', '345600', '432000', '518400', '604800', '1209600', '1814400', '2419200', '4838400', '7257600']='0', count: float=1, vouchergroup: str='Home Assistant', voucher_server: str | None=None, multiple_opnsense=None) -> dict[str, Any]:
        ...

    @staticmethod
    def kill_states(*, ip_addr: str, multiple_opnsense=None) -> dict[str, Any]:
        """

        Args:
            ip_addr:  Example: 192.168.0.100"""
        ...

    @staticmethod
    def run_speedtest(*, multiple_opnsense=None) -> dict[str, Any]:
        ...

    @staticmethod
    def get_vnstat_metrics(*, period: Literal['', 'hourly', 'daily', 'monthly', 'yearly']='hourly', multiple_opnsense=None) -> dict[str, Any]:
        ...

    @staticmethod
    def toggle_alias(*, alias: str, toggle_on_off: Literal['', 'toggle', 'on', 'off']='toggle', multiple_opnsense=None):
        """

        Args:
            alias:  Example: iphones"""
        ...

class persistent_notification:

    @staticmethod
    def create(*, message: str, title: str | None=None, notification_id: str | None=None):
        """

        Args:
            message:  Example: Please check your configuration.yaml.
            title:  Example: Test notification
            notification_id:  Example: 1234"""
        ...

    @staticmethod
    def dismiss(*, notification_id: str):
        """

        Args:
            notification_id:  Example: 1234"""
        ...

    @staticmethod
    def dismiss_all():
        ...

class _person_state(StateVal):
    device_trackers: list
    editable: bool
    gps_accuracy: int
    id: str
    latitude: float
    longitude: float
    source: str
    user_id: str

class person:
    ashton: _person_state
    kit: _person_state

    @staticmethod
    def reload():
        ...

    @staticmethod
    def add_device_tracker(*, entity_id: str, device_tracker: str):
        """Add a device tracker to a person.

        Args:
            entity_id: The person entity ID to add the device tracker to.
            device_tracker: The device tracker entity ID to add to the person."""
        ...

    @staticmethod
    def remove_device_tracker(*, entity_id: str, device_tracker: str):
        """Remove a device tracker from a person.

        Args:
            entity_id: The person entity ID to remove the device tracker from.
            device_tracker: The device tracker entity ID to remove from the person."""
        ...

class plex:

    @staticmethod
    def refresh_library(*, library_name: str, server_name: str | None=None):
        """

        Args:
            library_name:  Example: TV Shows
            server_name:  Example: My Plex Server"""
        ...

class portainer:

    @staticmethod
    def prune_images(*, device_id, until=None, dangling: bool | None=None):
        ...

class ps4:

    @staticmethod
    def send_command(*, entity_id: str, command: Literal['', 'back', 'down', 'enter', 'left', 'option', 'ps_hold', 'ps', 'right', 'up']):
        ...

class pypi_updates:

    @staticmethod
    def update():
        ...

    @staticmethod
    def reset():
        ...

class pyscript:

    @staticmethod
    def check_all_bylaw_pdfs():
        """pyscript function check_all_bylaw_pdfs()"""
        ...

    @staticmethod
    def check_feed(*, feed_entity_id=None):
        """Check for new entries in a specific feed.

        Args:
            feed_entity_id: argument feed_entity_id"""
        ...

    @staticmethod
    def scrape_multiple_bylaw_pdfs():
        """pyscript function scrape_multiple_bylaw_pdfs()"""
        ...

    @staticmethod
    def update_gw2_objectives():
        """Fetch GW2 Wizards Vault objectives and update a sensor."""
        ...

    @staticmethod
    def update_gw2_objectives_all():
        """Fetch all Wizards Vault objectives in one batch and store them as attributes."""
        ...

    @staticmethod
    def reload(*, global_ctx: str | None=None):
        """Reloads all available pyscripts and restart triggers

        Args:
            global_ctx: Only reload this specific global context (file or app) Example: file.example"""
        ...

    @staticmethod
    def generate_stubs() -> dict[str, Any]:
        """Build a stub files combining builtin helpers with discovered entities and services."""
        ...

    @staticmethod
    def jupyter_kernel_start(*, key: str, kernel_name: str='pyscript', shell_port: int | None=None, iopub_port: int | None=None, stdin_port: int | None=None, control_port: int | None=None, hb_port: int | None=None, ip: str='127.0.0.1', transport: Literal['', 'tcp', 'udp']='tcp', signature_scheme: Literal['', 'hmac-sha256']='hmac-sha256'):
        """Starts a jupyter kernel for interactive use; Called by Jupyter front end and should generally not be used by users

        Args:
            key: Used for signing Example: 012345678-9abcdef023456789abcdef
            kernel_name: Kernel name Example: pyscript
            shell_port: Shell port number Example: 63599
            iopub_port: IOPub port number Example: 63598
            stdin_port: Stdin port number Example: 63597
            control_port: Control port number Example: 63596
            hb_port: Heartbeat port number Example: 63595
            ip: IP address to connect to Jupyter front end Example: 127.0.0.1
            transport: Transport type Example: tcp
            signature_scheme: Signing algorithm Example: hmac-sha256"""
        ...

class python_script:

    @staticmethod
    def reload():
        ...

    @staticmethod
    def next_payment_date() -> dict[str, Any]:
        ...

class qr_generator:

    @staticmethod
    def save(*, entity_id: str, filename: str):
        """Save the current image to a path

        Args:
            entity_id: Identifier of the image entity. Example: image.qr_code
            filename: Target filename. Example: /tmp/snapshot_{{ entity_id.name }}.mp4"""
        ...

class readme:

    @staticmethod
    def generate():
        """Generates the README.md file"""
        ...

class recorder:

    @staticmethod
    def purge(*, keep_days: int | None=None, repack: bool=False, apply_filter: bool=False):
        ...

    @staticmethod
    def purge_entities(*, entity_id: str | None=None, domains: Any | None=None, entity_globs: Any | None=None, keep_days: int=0):
        """

        Args:
            domains:  Example: sun
            entity_globs:  Example: domain*.object_id*"""
        ...

    @staticmethod
    def enable():
        ...

    @staticmethod
    def disable():
        ...

    @staticmethod
    def get_statistics(*, start_time: datetime, statistic_ids, period: Literal['', '5minute', 'hour', 'day', 'week', 'month', 'year'], types: Literal['', 'change', 'last_reset', 'max', 'mean', 'min', 'state', 'sum'], end_time: datetime | None=None, units: Any | None=None) -> dict[str, Any]:
        """

        Args:
            start_time:  Example: 2025-01-01 00:00:00
            statistic_ids:  Example: ['sensor.energy_consumption', 'sensor.temperature']
            period:  Example: hour
            types:  Example: ['mean', 'sum']
            end_time:  Example: 2025-01-02 00:00:00
            units:  Example: {'energy': 'kWh', 'temperature': '°C'}"""
        ...

    @staticmethod
    def import_statistics(*, statistic_id: str, source: str, has_mean: bool, has_sum: bool, stats: Any, name: str | None=None, unit_of_measurement: str | None=None):
        """Import long-term statistics.

        Args:
            statistic_id: The statistics ID (entity ID) to import for.
            source: The source of the statistics data.
            has_mean: If the statistics has a mean value.
            has_sum: If the statistics has a sum value.
            stats: A list of mappings/dictionaries with statistics to import. The dictionaries must contain a "start" key with a datetime string other valid options are "mean", "sum", "min", "max", "last_reset", and "state". All of those are optional and either an integer or a float, except for "last_reset" which is a datetime string.
            name: The name of the statistics.
            unit_of_measurement: The unit of measurement of the statistics."""
        ...

class _remote_state(StateVal):
    activity_list: list
    current_activity: str
    supported_features: int

    def turn_off(self):
        ...

    def turn_on(self, activity: str | None):
        """

        Args:
            activity:  Example: BedroomTV"""
        ...

    def toggle(self):
        ...

    def send_command(self, *, command: Any, device: str | None=None, num_repeats: int=1, delay_secs: int=0.4, hold_secs: int=0):
        """

        Args:
            command:  Example: Play
            device:  Example: 32756745"""
        ...

    def learn_command(self, *, device: str | None=None, command: Any | None=None, command_type: Literal['', 'ir', 'rf']='ir', alternative: bool | None=None, timeout: int | None=None):
        """

        Args:
            device:  Example: television
            command:  Example: Turn on"""
        ...

    def delete_command(self, *, command: Any, device: str | None=None):
        """

        Args:
            command:  Example: Mute
            device:  Example: television"""
        ...

class remote:
    living_room_tv: _remote_state

    @staticmethod
    def turn_off(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_on(*, entity_id: str, activity: str | None=None):
        """

        Args:
            entity_id: Entity ID
            activity:  Example: BedroomTV"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def send_command(*, entity_id: str, command: Any, device: str | None=None, num_repeats: int=1, delay_secs: int=0.4, hold_secs: int=0):
        """

        Args:
            entity_id: Entity ID
            command:  Example: Play
            device:  Example: 32756745"""
        ...

    @staticmethod
    def learn_command(*, entity_id: str, device: str | None=None, command: Any | None=None, command_type: Literal['', 'ir', 'rf']='ir', alternative: bool | None=None, timeout: int | None=None):
        """

        Args:
            entity_id: Entity ID
            device:  Example: television
            command:  Example: Turn on"""
        ...

    @staticmethod
    def delete_command(*, entity_id: str, command: Any, device: str | None=None):
        """

        Args:
            entity_id: Entity ID
            command:  Example: Mute
            device:  Example: television"""
        ...

class repairs:

    @staticmethod
    def remove(*, issue_id: str):
        """Removes a manually created Home Assistant repairs issue. This action can only remove issues created with the `repairs_create` action.

        Args:
            issue_id: The issue ID to remove."""
        ...

    @staticmethod
    def ignore_all():
        """Ignore all issues currently raised in Home Assistant Repairs."""
        ...

    @staticmethod
    def unignore_all():
        """Unignore all issues currently raised in Home Assistant Repairs."""
        ...

    @staticmethod
    def create(*, title: str, description: str, issue_id: str | None=None, domain: str | None=None, severity: Literal['', 'warning', 'error', 'critical'] | None=None, persistent: bool | None=None):
        """Manually create and raise a issue in Home Assistant repairs.

        Args:
            title: The title of the issue.
            description: The description of the issue. Supports Markdown.
            issue_id: The issue can have an identifier, which allows you to cancel it later with that ID if needed. It also prevent duplicate issues to be created. If not provided, a random ID will be generated.
            domain: This field can be used to set the domain of the issue. For example, by default (if not set), it will use "spook". This causes Spook to be shown in the logo/image of the issue. If you set it to "homeassistant", the Home Assistant logo will be used, or use "hue", "zwave_js", "mqtt", etc. to use the logo of that integration.
            severity: The severity of the issue. This will be used to determine the priority of the issue. If not set, "warning" will be used
            persistent: If the issue should be persistent, which means it will survive restarts of Home Assistant. By default, issues are not persistent."""
        ...

class rest_command:

    @staticmethod
    def twitter_laptop() -> dict[str, Any]:
        ...

    @staticmethod
    def send_whatsapp_message() -> dict[str, Any]:
        ...

    @staticmethod
    def reload():
        ...

class _scene_state(StateVal):
    id: str

    def delete(self):
        ...

    def turn_on(self, transition: int | None):
        ...

class scene:
    arrive_home: _scene_state
    leave_home_day: _scene_state
    all_leave_home_night: _scene_state
    make_bed: _scene_state
    sleep: _scene_state

    @staticmethod
    def reload():
        ...

    @staticmethod
    def apply(*, entities: Any, transition: int | None=None):
        """

        Args:
            entities:  Example: light.kitchen: "on"
                light.ceiling:
                  state: "on"
                  brightness: 80
                """
        ...

    @staticmethod
    def create(*, scene_id: str, entities: Any | None=None, snapshot_entities: str | None=None):
        """

        Args:
            scene_id:  Example: all_lights
            entities:  Example: light.tv_back_light: "on"
                light.ceiling:
                  state: "on"
                  brightness: 200
                
            snapshot_entities:  Example: - light.ceiling
                - light.kitchen
                """
        ...

    @staticmethod
    def delete(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_on(*, entity_id: str, transition: int | None=None):
        """

        Args:
            entity_id: Entity ID"""
        ...

class schedule:

    @staticmethod
    def reload():
        ...

    @staticmethod
    def get_schedule(*, entity_id: str) -> dict[str, Any]:
        """

        Args:
            entity_id: Entity ID"""
        ...

class _script_state(StateVal):
    current: int
    last_triggered: datetime
    max: int
    mode: str
    restored: bool
    supported_features: int

    def turn_on(self):
        ...

    def turn_off(self):
        ...

    def toggle(self):
        ...

class script:
    do_not_disturb_on: _script_state
    do_not_disturb_off: _script_state
    sleep_mode_on: _script_state
    sleep_mode_off: _script_state
    download_a_file_with_retries: _script_state
    send_message_telegram: _script_state
    send_document_message_telegram: _script_state
    send_harleys_food_email: _script_state
    send_voice_message_telegram_2: _script_state
    send_discord_message: _script_state
    speak_var: _script_state
    notify_devices: _script_state
    send_message_telegram_2: _script_state
    download_a_file_with_retries_2: _script_state
    send_voice_message_telegram_3: _script_state
    send_harley_s_food_email: _script_state
    send_document_telegram: _script_state
    discord_notification_engine_comprehensive: _script_state

    @staticmethod
    def speak_var(*, speak_var=None, cache=None, bypass=None, caller=None) -> dict[str, Any]:
        """Optimized for Docker CPU/IO bottlenecks. Returns a response variable 'response' indicating status."""
        ...

    @staticmethod
    def notify_devices(*, target_device: str | None=None, message: str | None=None, media=None, mobile: bool=True, browser_mod: bool | None=None, home_assistant: bool | None=None, message_title: str | None=None, media_toggle: bool | None=None, action: str | None=None, send_action: bool | None=None, action_title: str | None=None) -> dict[str, Any]:
        """Sends a notification to one or more specified devices, ensuring that targets are valid.

        Args:
            media: The media to send to the Target Device
            media_toggle: Turn on if media is being sent
            send_action: Whether or not to send up to two actions to a mobile device."""
        ...

    @staticmethod
    def send_message_telegram_2(*, message: str, message_target: str, message_tag: str | None=None, message_title: str | None=None, message_inline: str | None=None, parse_mode: str='MarkdownV2', inline_keyboard: bool=False) -> dict[str, Any]:
        """Send a message (optionally with tag, title, inline keyboard, parse_mode)

        Args:
            message: The message to send
            message_target: Telegram chat ID
            message_tag: A tag for the message
            message_title: The title of the message
            message_inline: Comma-separated buttons for an inline keyboard
            parse_mode: e.g. "MarkdownV2" or "HTML"
            inline_keyboard: Whether to include an inline keyboard"""
        ...

    @staticmethod
    def download_a_file_with_retries_2(*, url: str, subdir: str, max_tries: int=3, delay_sec: int=5, filename: str | None=None) -> dict[str, Any]:
        """Download a URL into a subdir, retrying up to {{ max_tries }} times

        Args:
            url: The full URL to download
            subdir: The downloader subdir to use
            filename: Name for file to be downloaded"""
        ...

    @staticmethod
    def send_voice_message_telegram_3(*, file_url: str, username_id: str, message_tag: str | None=None) -> dict[str, Any]:
        """

        Args:
            file_url: http://YOUR_HA:8123/api/tts_proxy/abcdef1234567890_piper.mp3
            username_id: The User id of the user to send the telegram message to
            message_tag: The tag of the message"""
        ...

    @staticmethod
    def send_harley_s_food_email() -> dict[str, Any]:
        """Send Harley’s food request email to the vet"""
        ...

    @staticmethod
    def send_document_telegram(*, file_url: str, username_id: str, document_tag: str | None=None, document_caption: str | None=None) -> dict[str, Any]:
        """Sends a document to a Telegram user, optionally including a message tag and caption.

        Args:
            file_url: The full file path to send via telegram
            username_id: The User id of the user to send the telegram message to
            document_tag: The tag of the message
            document_caption: The caption of the file to send"""
        ...

    @staticmethod
    def discord_notification_engine_comprehensive(*, target: str | None=None, message: str | None=None, title: str | None=None, description: str | None=None, link: str | None=None, color: str | None=None, image_url: str | None=None, thumbnail_url: str | None=None, author_name: str | None=None, author_url: str | None=None, author_icon: str | None=None, footer_text: str | None=None, footer_icon: str | None=None, embed_fields: str | None=None, images: str | None=None, attachment_urls: str | None=None, verify_ssl: bool=True) -> dict[str, Any]:
        """Sends a notification to Discord with full support for Embeds, Attachments, and Fields.

        Args:
            target: List of Channel or User IDs. (Required) Example: ['1469444151593406700']
            message: The main body text. Required by Discord even if empty. Example: Update detected!
            title: Bold title at the top of the embed.
            description: Main text inside the embed.
            link: URL opened when clicking the title.
            color: Color of the left border (Integer, e.g., 3066993 for Green).
            image_url: Large image displayed inside the embed.
            thumbnail_url: Small square image in the top-right.
            author_name: Name of the author at the top.
            author_url: Link when clicking the author name.
            author_icon: Small avatar next to author name.
            footer_text: Small text at the very bottom.
            footer_icon: Tiny icon next to footer text.
            embed_fields: A list of field objects: [{name: 'Name', value: 'Val', inline: true}] Example: [{'name': 'Version', 'value': '1.0', 'inline': true}]
            images: List of LOCAL file paths to upload. Example: ['/config/www/snapshot.jpg']
            attachment_urls: List of REMOTE URLs to download and attach. Example: ['http://google.com/image.png']
            verify_ssl: Default True"""
        ...

    @staticmethod
    def reload():
        ...

    @staticmethod
    def turn_on(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_off(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

class select:

    @staticmethod
    def select_first(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def select_last(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def select_next(*, entity_id: str, cycle: bool=True):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def select_option(*, entity_id: str, option: str):
        '''

        Args:
            entity_id: Entity ID
            option:  Example: "Item A"'''
        ...

    @staticmethod
    def select_previous(*, entity_id: str, cycle: bool=True):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def random(*, entity_id: str, options: Any | None=None):
        """Select an random option for a select entity.

        Args:
            entity_id: Entity ID
            options: Limits the options to select from. If not provided, all options will be considered."""
        ...

class _sensor_state(StateVal):
    ADIST: int | float
    Argument_of_perihelion_wrt_ecliptic: int | float
    Available: str
    BuildDateTime: str
    Confidence: str
    Country: str
    Ecliptic: int | float
    Epoch: int | float
    Hostname: str
    IPAddress: str
    Inclination_wrt_ecliptic: int | float
    Label: str
    LoadAvg: int
    Locality: str
    Location: list
    Longitude_of_ascending_node_wrt_ecliptic: int | float
    Magnitude: int | float
    Mean_motion: int | float
    MqttCount: int
    Name: str
    Neo_Watcher_Orbit_Viewer_URL: str
    Ocean: str
    Perihelion: int | float
    Perihelion_Julian_Day: int | float
    RSSI: str
    RestartReason: str
    Thoroughfare: str
    Tier: int
    Total: str
    Types: list
    Uptime: str
    Version: str
    Zones: list
    absolute_magnitude_h: float
    achieved: Any
    achievements: Any
    administrative_area: str
    age_coverage_ratio: float
    alarm_volume: int
    alarms: list
    albums: int
    alert: str
    alert_count: int
    alert_monitored: str
    alert_startup: str
    alert_tracked: str
    alerts: str
    arch: str
    artists: int
    attribution: str
    audio: str
    auth_token: str
    automatic: bool
    available: str | bool
    avatar: str
    battery_last_replaced: datetime
    battery_last_reported: datetime
    battery_last_reported_level: float
    battery_low: bool
    battery_low_threshold: int
    battery_quantity: int
    battery_type: str
    battery_type_and_quantity: str
    bio: str
    blocks: str
    blue_hour: bool
    board: str
    bodies: list
    brand: str
    browserID: str
    buffer_usage_ratio: float
    bytes_received: int
    bytes_sent: int
    channel: str
    channel_picture: str
    city: str
    cli: str
    close_approach_date: str
    close_approach_date_full: str
    comets: list
    command_set: str
    connected_not_paired_devices: list
    connected_paired_devices: list
    country: str
    country_code: str
    created: Any
    cron_jobs: str
    current: float
    current_latitude: float
    current_longitude: float
    daily_goal: int
    data: list
    daylight: bool
    developer: Any
    device: str
    device_id: str
    device_name: str
    devicename: str
    devicetracker_entityid: str
    devicetracker_zone: str
    devicetracker_zone_name: str
    direction_of_travel: str
    display_name: str
    display_options: str
    distance_from_home_km: float
    distance_from_home_m: float
    distance_from_home_mi: float
    distance_traveled_m: float
    distance_traveled_mi: float
    dns: str
    element: str
    enabled: bool
    end: int | str
    entity_picture: str
    estimated_diameter_max_km: float
    estimated_diameter_max_mi: float
    estimated_diameter_min_km: float
    estimated_diameter_min_mi: float
    evlog_url_list: dict
    expires: str
    extended_today: bool
    filtername: str
    flights: list
    fname: str
    fnames: dict
    followers: int
    following: bool
    following_since: datetime
    formatted_address: str
    free_external_storage: str
    free_memory: float
    fullUrlPath: str
    fullname: str
    game: str
    gamerscore: Any
    gateways: list
    gems: int
    genres: Any
    ghz_advertised: float
    golden_hour: bool
    gps_accuracy: float
    home_latitude: float
    home_longitude: float
    home_zone: str
    horizon_url: str
    house_angle: float
    id: str
    idle: str
    illumination_fraction: float
    image: str
    in_daylight_time: bool
    in_vehicle: int
    info: str
    integration: str
    interface: str
    interrupt: str
    ip6_addresses: list
    ip_address: str
    ip_addresses: list
    ipv4: str
    ipv6: str
    is_hidden: bool
    is_potentially_hazardous_asteroid: bool
    iso_country_code: str
    language: str
    languages: list
    last_added_item: str
    last_added_timestamp: datetime
    last_extended: str
    last_online: datetime
    last_place_name: str
    lat: str
    latitude: float
    learning_language: str
    length: int
    level: int
    light: int
    locality: str
    location: str | list
    log_level_debug: str
    logs: str
    long: str
    longitude: float
    mac: str
    map_link: str
    marker_high_level: int
    marker_low_level: int
    marker_type: str
    max: int
    max_value: str
    media: str
    media_artist: Any
    media_image: Any
    media_lyrics: Any
    media_pyong_count: Any
    media_stats_hot: Any
    media_title: Any
    message_text: str
    metered: bool
    min: int
    min_age: Any
    min_value: str
    miss_distance_km: str
    miss_distance_mi: str
    modality: str
    moon_age: float
    moon_altitude_deg: float
    moon_altitude_radians: float
    moon_azimuth_deg: float
    moon_azimuth_radians: float
    moon_distance_km: float
    moon_high: datetime
    moon_parallactic_angle: float
    moon_parallactic_angle_deg: float
    moonrise: datetime
    moonset: datetime
    motion: int
    mountpoint: str
    multicast: str
    name: str
    name_servers: str
    name_urlencoded: str
    names: str
    nasa_jpl_url: str
    neighbourhood: str
    next_alarm_status: str
    next_change: datetime
    next_first_quarter: datetime
    next_full_moon: datetime
    next_new_moon: datetime
    next_phase: str
    next_phase_date: datetime
    next_third_quarter: datetime
    next_timer_status: str
    next_update: datetime
    nice: str
    number: int
    objects: list
    observer: str
    on_foot: int
    on_sale: list
    openPopups: list
    options: list
    orbiting_body: str
    os: str
    osm_details_dict: dict
    osm_dict: dict
    osm_id: str
    osm_type: str
    paired_devices: list
    panelComponentName: str
    panelIcon: str
    panelNarrow: bool
    panelRequireAdmin: bool
    panelTitle: str
    panelUrlPath: str
    pathSegments: list
    person: str
    phone: str
    place_type: str
    platform: Any
    popupOpen: bool
    postal_code: str
    premises: str
    previous_latitude: float
    previous_longitude: float
    progress: Any
    published_at: datetime
    publisher: Any
    querytype: str
    records: int
    registrar: str
    relative_velocity_km_per_h: str
    relative_velocity_km_per_s: str
    relative_velocity_mi_per_h: str
    release_date: str
    release_description: str
    release_notes: str
    release_title: str
    resolver: str
    restored: bool
    rising: bool
    routes: list
    run_mode: str
    seasons: int
    sensor_updated: str
    serial: str
    server_country: str
    server_id: str
    server_name: str
    sha: str
    short_description: Any
    shows: int
    source: str
    source_entity_id: str
    source_value_valid: bool
    start: int | str
    started_at: datetime
    state_abbr: str
    state_class: str
    state_message: str
    state_province: str
    state_reason: Any
    station: str
    station_id: str
    status: str
    still: int
    street: str
    street_number: str
    sub_administrative_area: str
    sub_locality: str
    sub_thoroughfare: str
    subscribed: bool
    subscription_is_gifted: bool
    subscription_tier: int
    sun_azimuth: float
    sun_elevation: float
    supervisor: str
    supported_features: int
    system: str
    tag: str
    thoroughfare: str
    time: datetime
    time_zone_id: str
    time_zone_short: str
    timers: list
    timestamp: int
    title: str
    today: datetime | float
    today_hms: str
    tomorrow: datetime | float
    tomorrow_hms: str
    total_external_storage: str
    total_memory: float
    total_xp: int
    type: str
    unit_of_measurement: str
    unknown: int
    update_time: str
    updated: str
    uri_supported: str
    url: str
    used: str
    user: str
    userAgent: str
    userData: dict
    user_message: str
    username: str
    uses_daylight_time: bool
    utc_offset: int
    versionEvLog: str
    version_evlog: str
    version_ic3: str
    video_id: str
    viewNarrow: bool
    viewTitle: str
    viewUrlPath: str
    viewers: int
    voltage: float
    walking: int
    wall: str
    xp: int
    xp_goal: int
    yesterday: datetime | float
    yesterday_hms: str

class sensor:
    iss: _sensor_state
    openuv_current_ozone_level: _sensor_state
    openuv_current_uv_index: _sensor_state
    openuv_current_uv_level: _sensor_state
    openuv_max_uv_index: _sensor_state
    openuv_skin_type_1_safe_exposure_time: _sensor_state
    openuv_skin_type_2_safe_exposure_time: _sensor_state
    openuv_skin_type_3_safe_exposure_time: _sensor_state
    openuv_skin_type_4_safe_exposure_time: _sensor_state
    openuv_skin_type_5_safe_exposure_time: _sensor_state
    openuv_skin_type_6_safe_exposure_time: _sensor_state
    k_s_bedside_lamp_power: _sensor_state
    k_s_bedside_lamp_signal_strength: _sensor_state
    season: _sensor_state
    speedtest_ping: _sensor_state
    speedtest_download: _sensor_state
    speedtest_upload: _sensor_state
    env_can_advisory: _sensor_state
    env_can_aqhi: _sensor_state
    env_can_barometric_pressure: _sensor_state
    env_can_chance_of_precipitation: _sensor_state
    env_can_current_condition: _sensor_state
    env_can_dew_point: _sensor_state
    env_can_endings: _sensor_state
    env_can_high_temperature: _sensor_state
    env_can_humidex: _sensor_state
    env_can_humidity: _sensor_state
    env_can_icon_code: _sensor_state
    env_can_low_temperature: _sensor_state
    env_can_normal_high_temperature: _sensor_state
    env_can_normal_low_temperature: _sensor_state
    env_can_observation_time: _sensor_state
    env_can_statements: _sensor_state
    env_can_summary: _sensor_state
    env_can_temperature: _sensor_state
    env_can_tendency: _sensor_state
    env_can_uv_index: _sensor_state
    env_can_visibility: _sensor_state
    env_can_warnings: _sensor_state
    env_can_watches: _sensor_state
    env_can_wind_bearing: _sensor_state
    env_can_wind_chill: _sensor_state
    env_can_wind_direction: _sensor_state
    env_can_wind_gust: _sensor_state
    env_can_wind_speed: _sensor_state
    phone_pressures: _sensor_state
    outside_pressures: _sensor_state
    cpu_speed: _sensor_state
    hp_envy_4510_series_uptime: _sensor_state
    hp_envy_4510_series_black_ink: _sensor_state
    hp_envy_4510_series_tri_color_ink: _sensor_state
    hp_envy_4510_series: _sensor_state
    home_assistant_analytics_insights_accuweather: _sensor_state
    home_assistant_analytics_insights_analytics: _sensor_state
    home_assistant_analytics_insights_android_debug_bridge: _sensor_state
    home_assistant_analytics_insights_android_ip_webcam: _sensor_state
    home_assistant_analytics_insights_android_tv_remote: _sensor_state
    home_assistant_analytics_insights_apc_ups_daemon: _sensor_state
    home_assistant_analytics_insights_apple_itunes: _sensor_state
    home_assistant_analytics_insights_backup: _sensor_state
    home_assistant_analytics_insights_bluetooth: _sensor_state
    home_assistant_analytics_insights_bluetooth_adapters: _sensor_state
    home_assistant_analytics_insights_automation: _sensor_state
    home_assistant_analytics_insights_bluetooth_le_tracker: _sensor_state
    home_assistant_analytics_insights_bluetooth_tracker: _sensor_state
    home_assistant_analytics_insights_browser: _sensor_state
    home_assistant_analytics_insights_camera_proxy: _sensor_state
    home_assistant_analytics_insights_counter: _sensor_state
    home_assistant_analytics_insights_auth: _sensor_state
    home_assistant_analytics_insights_aurora: _sensor_state
    home_assistant_analytics_insights_command_line: _sensor_state
    home_assistant_analytics_insights_cpu_speed: _sensor_state
    home_assistant_analytics_insights_configuration: _sensor_state
    home_assistant_analytics_insights_diagnostics: _sensor_state
    home_assistant_analytics_insights_certificate_expiry: _sensor_state
    home_assistant_analytics_insights_change_device_type_of_a_switch: _sensor_state
    home_assistant_analytics_insights_custom_panel: _sensor_state
    home_assistant_analytics_insights_default_config: _sensor_state
    home_assistant_analytics_insights_environment_canada: _sensor_state
    home_assistant_analytics_insights_esphome: _sensor_state
    home_assistant_analytics_insights_google_calendar: _sensor_state
    home_assistant_analytics_insights_google_cast: _sensor_state
    home_assistant_analytics_insights_generic_camera: _sensor_state
    home_assistant_analytics_insights_google_mail: _sensor_state
    home_assistant_analytics_insights_google_maps: _sensor_state
    home_assistant_analytics_insights_google_sheets: _sensor_state
    home_assistant_analytics_insights_google_tasks: _sensor_state
    home_assistant_analytics_insights_history: _sensor_state
    home_assistant_analytics_insights_hardware: _sensor_state
    home_assistant_analytics_insights_holiday: _sensor_state
    home_assistant_analytics_insights_home_assistant_alerts: _sensor_state
    home_assistant_analytics_insights_home_assistant_analytics_insights: _sensor_state
    home_assistant_analytics_insights_home_assistant_api: _sensor_state
    home_assistant_analytics_insights_home_assistant_cloud: _sensor_state
    home_assistant_analytics_insights_home_assistant_core_integration: _sensor_state
    home_assistant_analytics_insights_home_assistant_frontend: _sensor_state
    home_assistant_analytics_insights_home_assistant_green: _sensor_state
    home_assistant_analytics_insights_home_assistant_hardware: _sensor_state
    home_assistant_analytics_insights_home_assistant_ios: _sensor_state
    home_assistant_analytics_insights_home_assistant_onboarding: _sensor_state
    home_assistant_analytics_insights_home_assistant_supervisor: _sensor_state
    home_assistant_analytics_insights_home_assistant_websocket_api: _sensor_state
    home_assistant_analytics_insights_home_assistant_yellow: _sensor_state
    home_assistant_analytics_insights_my_home_assistant: _sensor_state
    home_assistant_analytics_insights_homekit_bridge: _sensor_state
    home_assistant_analytics_insights_homekit_device: _sensor_state
    home_assistant_analytics_insights_http: _sensor_state
    home_assistant_analytics_insights_history_stats: _sensor_state
    home_assistant_analytics_insights_iframe_panel: _sensor_state
    home_assistant_analytics_insights_ifttt: _sensor_state
    home_assistant_analytics_insights_logbook: _sensor_state
    home_assistant_analytics_insights_local_calendar: _sensor_state
    home_assistant_analytics_insights_local_file: _sensor_state
    home_assistant_analytics_insights_local_ip_address: _sensor_state
    home_assistant_analytics_insights_local_to_do: _sensor_state
    home_assistant_analytics_insights_html5_push_notifications: _sensor_state
    home_assistant_analytics_insights_moon: _sensor_state
    home_assistant_analytics_insights_influxdb: _sensor_state
    home_assistant_analytics_insights_imap: _sensor_state
    home_assistant_analytics_insights_input_boolean: _sensor_state
    home_assistant_analytics_insights_input_button: _sensor_state
    home_assistant_analytics_insights_input_datetime: _sensor_state
    home_assistant_analytics_insights_input_number: _sensor_state
    home_assistant_analytics_insights_input_select: _sensor_state
    home_assistant_analytics_insights_input_text: _sensor_state
    home_assistant_analytics_insights_logentries: _sensor_state
    home_assistant_analytics_insights_logger: _sensor_state
    home_assistant_analytics_insights_min_max: _sensor_state
    home_assistant_analytics_insights_minecraft_server: _sensor_state
    home_assistant_analytics_insights_mqtt: _sensor_state
    home_assistant_analytics_insights_manual_mqtt_alarm_control_panel: _sensor_state
    home_assistant_analytics_insights_mqtt_eventstream: _sensor_state
    home_assistant_analytics_insights_mqtt_json: _sensor_state
    home_assistant_analytics_insights_mqtt_room_presence: _sensor_state
    home_assistant_analytics_insights_mqtt_statestream: _sensor_state
    home_assistant_analytics_insights_onvif: _sensor_state
    home_assistant_analytics_insights_dlna_digital_media_renderer: _sensor_state
    home_assistant_analytics_insights_dlna_digital_media_server: _sensor_state
    home_assistant_analytics_insights_media_extractor: _sensor_state
    home_assistant_analytics_insights_media_source: _sensor_state
    home_assistant_analytics_insights_universal_media_player: _sensor_state
    home_assistant_analytics_insights_vlc_media_player: _sensor_state
    home_assistant_analytics_insights_vlc_media_player_via_telnet: _sensor_state
    home_assistant_analytics_insights_openuv: _sensor_state
    home_assistant_analytics_insights_openweathermap: _sensor_state
    home_assistant_analytics_insights_person: _sensor_state
    home_assistant_analytics_insights_persistent_notification: _sensor_state
    home_assistant_analytics_insights_phone_modem: _sensor_state
    home_assistant_analytics_insights_pi_hole: _sensor_state
    home_assistant_analytics_insights_random: _sensor_state
    home_assistant_analytics_insights_qr_code: _sensor_state
    home_assistant_analytics_insights_network_configuration: _sensor_state
    home_assistant_analytics_insights_qbittorrent: _sensor_state
    home_assistant_analytics_insights_scrape: _sensor_state
    home_assistant_analytics_insights_python_scripts: _sensor_state
    home_assistant_analytics_insights_scripts: _sensor_state
    home_assistant_analytics_insights_schedule: _sensor_state
    home_assistant_analytics_insights_search: _sensor_state
    home_assistant_analytics_insights_season: _sensor_state
    home_assistant_analytics_insights_steam: _sensor_state
    home_assistant_analytics_insights_stream: _sensor_state
    home_assistant_analytics_insights_smartthings: _sensor_state
    home_assistant_analytics_insights_snmp: _sensor_state
    home_assistant_analytics_insights_speedtest_net: _sensor_state
    home_assistant_analytics_insights_serial: _sensor_state
    home_assistant_analytics_insights_streamlabs: _sensor_state
    home_assistant_analytics_insights_mjpeg_ip_camera: _sensor_state
    home_assistant_analytics_insights_plant_monitor: _sensor_state
    home_assistant_analytics_insights_plex_media_server: _sensor_state
    home_assistant_analytics_insights_raspberry_pi_camera: _sensor_state
    home_assistant_analytics_insights_radio_browser: _sensor_state
    home_assistant_analytics_insights_folder: _sensor_state
    home_assistant_analytics_insights_folder_watcher: _sensor_state
    home_assistant_analytics_insights_repairs: _sensor_state
    home_assistant_analytics_insights_recovery_mode: _sensor_state
    home_assistant_analytics_insights_reddit: _sensor_state
    home_assistant_analytics_insights_sun: _sensor_state
    home_assistant_analytics_insights_zone: _sensor_state
    home_assistant_analytics_insights_zodiac: _sensor_state
    home_assistant_analytics_insights_telegram: _sensor_state
    home_assistant_analytics_insights_telegram_bot: _sensor_state
    home_assistant_analytics_insights_system_bridge: _sensor_state
    home_assistant_analytics_insights_global_disaster_alert_and_coordination_system_gdacs: _sensor_state
    home_assistant_analytics_insights_system_health: _sensor_state
    home_assistant_analytics_insights_system_log: _sensor_state
    home_assistant_analytics_insights_system_monitor: _sensor_state
    home_assistant_analytics_insights_syslog: _sensor_state
    home_assistant_analytics_insights_uptime: _sensor_state
    home_assistant_analytics_insights_usb_discovery: _sensor_state
    home_assistant_analytics_insights_opnsense: _sensor_state
    home_assistant_analytics_insights_opensensemap: _sensor_state
    home_assistant_analytics_insights_open_hardware_monitor: _sensor_state
    home_assistant_analytics_insights_adaptive_cover_custom: _sensor_state
    home_assistant_analytics_insights_adaptive_lighting_custom: _sensor_state
    home_assistant_analytics_insights_androidtv_custom: _sensor_state
    home_assistant_analytics_insights_androidtv_remote_custom: _sensor_state
    home_assistant_analytics_insights_opnsense_custom: _sensor_state
    home_sun_solar_midnight: _sensor_state
    home_sun_astronomical_dawn: _sensor_state
    home_sun_nautical_dawn: _sensor_state
    home_sun_dawn: _sensor_state
    home_sun_rising: _sensor_state
    home_sun_solar_noon: _sensor_state
    home_sun_setting: _sensor_state
    home_sun_dusk: _sensor_state
    home_sun_nautical_dusk: _sensor_state
    home_sun_astronomical_dusk: _sensor_state
    home_sun_daylight: _sensor_state
    home_sun_civil_daylight: _sensor_state
    home_sun_nautical_daylight: _sensor_state
    home_sun_astronomical_daylight: _sensor_state
    home_sun_night: _sensor_state
    home_sun_civil_night: _sensor_state
    home_sun_nautical_night: _sensor_state
    home_sun_astronomical_night: _sensor_state
    home_sun_minimum_elevation: _sensor_state
    home_sun_maximum_elevation: _sensor_state
    home_sun_azimuth: _sensor_state
    home_sun_elevation: _sensor_state
    home_sun_phase: _sensor_state
    home_sun_deconz_daylight: _sensor_state
    home_sun_rising_azimuth: _sensor_state
    home_sun_setting_azimuth: _sensor_state
    esphome_esphome_discussions: _sensor_state
    home_assistant_core_discussions: _sensor_state
    home_assistant_frontend_discussions: _sensor_state
    home_assistant_operating_system_discussions: _sensor_state
    home_assistant_supervisor_discussions: _sensor_state
    internetarchive_openlibrary_client_discussions: _sensor_state
    khoih_prog_wifinina_generic_discussions: _sensor_state
    marc_romu_home_assistant_blueprints_discussions: _sensor_state
    nabucasa_hass_nabucasa_discussions: _sensor_state
    rdavydov_twitch_channel_points_miner_v2_discussions: _sensor_state
    shaked6540_youtubeplaylistdownloader_discussions: _sensor_state
    sherlock_project_sherlock_discussions: _sensor_state
    thomasnordquist_mqtt_explorer_discussions: _sensor_state
    travisghansen_hass_opnsense_discussions: _sensor_state
    vova_sh_termux_api_discussions: _sensor_state
    esphome_esphome_stars: _sensor_state
    home_assistant_core_stars: _sensor_state
    home_assistant_frontend_stars: _sensor_state
    home_assistant_operating_system_stars: _sensor_state
    home_assistant_supervisor_stars: _sensor_state
    internetarchive_openlibrary_client_stars: _sensor_state
    khoih_prog_wifinina_generic_stars: _sensor_state
    marc_romu_home_assistant_blueprints_stars: _sensor_state
    nabucasa_hass_nabucasa_stars: _sensor_state
    rdavydov_twitch_channel_points_miner_v2_stars: _sensor_state
    shaked6540_youtubeplaylistdownloader_stars: _sensor_state
    sherlock_project_sherlock_stars: _sensor_state
    thomasnordquist_mqtt_explorer_stars: _sensor_state
    travisghansen_hass_opnsense_stars: _sensor_state
    vova_sh_termux_api_stars: _sensor_state
    esphome_esphome_watchers: _sensor_state
    home_assistant_core_watchers: _sensor_state
    home_assistant_frontend_watchers: _sensor_state
    home_assistant_operating_system_watchers: _sensor_state
    home_assistant_supervisor_watchers: _sensor_state
    internetarchive_openlibrary_client_watchers: _sensor_state
    khoih_prog_wifinina_generic_watchers: _sensor_state
    marc_romu_home_assistant_blueprints_watchers: _sensor_state
    nabucasa_hass_nabucasa_watchers: _sensor_state
    rdavydov_twitch_channel_points_miner_v2_watchers: _sensor_state
    shaked6540_youtubeplaylistdownloader_watchers: _sensor_state
    sherlock_project_sherlock_watchers: _sensor_state
    thomasnordquist_mqtt_explorer_watchers: _sensor_state
    travisghansen_hass_opnsense_watchers: _sensor_state
    vova_sh_termux_api_watchers: _sensor_state
    esphome_esphome_forks: _sensor_state
    home_assistant_core_forks: _sensor_state
    home_assistant_frontend_forks: _sensor_state
    home_assistant_operating_system_forks: _sensor_state
    home_assistant_supervisor_forks: _sensor_state
    internetarchive_openlibrary_client_forks: _sensor_state
    khoih_prog_wifinina_generic_forks: _sensor_state
    marc_romu_home_assistant_blueprints_forks: _sensor_state
    nabucasa_hass_nabucasa_forks: _sensor_state
    rdavydov_twitch_channel_points_miner_v2_forks: _sensor_state
    shaked6540_youtubeplaylistdownloader_forks: _sensor_state
    sherlock_project_sherlock_forks: _sensor_state
    thomasnordquist_mqtt_explorer_forks: _sensor_state
    travisghansen_hass_opnsense_forks: _sensor_state
    vova_sh_termux_api_forks: _sensor_state
    esphome_esphome_issues: _sensor_state
    home_assistant_core_issues: _sensor_state
    home_assistant_frontend_issues: _sensor_state
    home_assistant_operating_system_issues: _sensor_state
    home_assistant_supervisor_issues: _sensor_state
    internetarchive_openlibrary_client_issues: _sensor_state
    khoih_prog_wifinina_generic_issues: _sensor_state
    marc_romu_home_assistant_blueprints_issues: _sensor_state
    nabucasa_hass_nabucasa_issues: _sensor_state
    rdavydov_twitch_channel_points_miner_v2_issues: _sensor_state
    shaked6540_youtubeplaylistdownloader_issues: _sensor_state
    sherlock_project_sherlock_issues: _sensor_state
    thomasnordquist_mqtt_explorer_issues: _sensor_state
    travisghansen_hass_opnsense_issues: _sensor_state
    vova_sh_termux_api_issues: _sensor_state
    esphome_esphome_pull_requests: _sensor_state
    home_assistant_core_pull_requests: _sensor_state
    home_assistant_frontend_pull_requests: _sensor_state
    home_assistant_operating_system_pull_requests: _sensor_state
    home_assistant_supervisor_pull_requests: _sensor_state
    internetarchive_openlibrary_client_pull_requests: _sensor_state
    khoih_prog_wifinina_generic_pull_requests: _sensor_state
    marc_romu_home_assistant_blueprints_pull_requests: _sensor_state
    nabucasa_hass_nabucasa_pull_requests: _sensor_state
    rdavydov_twitch_channel_points_miner_v2_pull_requests: _sensor_state
    shaked6540_youtubeplaylistdownloader_pull_requests: _sensor_state
    sherlock_project_sherlock_pull_requests: _sensor_state
    thomasnordquist_mqtt_explorer_pull_requests: _sensor_state
    travisghansen_hass_opnsense_pull_requests: _sensor_state
    vova_sh_termux_api_pull_requests: _sensor_state
    esphome_esphome_latest_commit: _sensor_state
    home_assistant_core_latest_commit: _sensor_state
    home_assistant_frontend_latest_commit: _sensor_state
    home_assistant_operating_system_latest_commit: _sensor_state
    home_assistant_supervisor_latest_commit: _sensor_state
    internetarchive_openlibrary_client_latest_commit: _sensor_state
    khoih_prog_wifinina_generic_latest_commit: _sensor_state
    marc_romu_home_assistant_blueprints_latest_commit: _sensor_state
    nabucasa_hass_nabucasa_latest_commit: _sensor_state
    rdavydov_twitch_channel_points_miner_v2_latest_commit: _sensor_state
    shaked6540_youtubeplaylistdownloader_latest_commit: _sensor_state
    sherlock_project_sherlock_latest_commit: _sensor_state
    thomasnordquist_mqtt_explorer_latest_commit: _sensor_state
    travisghansen_hass_opnsense_latest_commit: _sensor_state
    vova_sh_termux_api_latest_commit: _sensor_state
    esphome_esphome_latest_discussion: _sensor_state
    home_assistant_core_latest_discussion: _sensor_state
    home_assistant_frontend_latest_discussion: _sensor_state
    home_assistant_operating_system_latest_discussion: _sensor_state
    home_assistant_supervisor_latest_discussion: _sensor_state
    internetarchive_openlibrary_client_latest_discussion: _sensor_state
    khoih_prog_wifinina_generic_latest_discussion: _sensor_state
    marc_romu_home_assistant_blueprints_latest_discussion: _sensor_state
    nabucasa_hass_nabucasa_latest_discussion: _sensor_state
    rdavydov_twitch_channel_points_miner_v2_latest_discussion: _sensor_state
    shaked6540_youtubeplaylistdownloader_latest_discussion: _sensor_state
    sherlock_project_sherlock_latest_discussion: _sensor_state
    thomasnordquist_mqtt_explorer_latest_discussion: _sensor_state
    travisghansen_hass_opnsense_latest_discussion: _sensor_state
    vova_sh_termux_api_latest_discussion: _sensor_state
    esphome_esphome_latest_release: _sensor_state
    home_assistant_core_latest_release: _sensor_state
    home_assistant_frontend_latest_release: _sensor_state
    home_assistant_operating_system_latest_release: _sensor_state
    home_assistant_supervisor_latest_release: _sensor_state
    internetarchive_openlibrary_client_latest_release: _sensor_state
    khoih_prog_wifinina_generic_latest_release: _sensor_state
    marc_romu_home_assistant_blueprints_latest_release: _sensor_state
    nabucasa_hass_nabucasa_latest_release: _sensor_state
    rdavydov_twitch_channel_points_miner_v2_latest_release: _sensor_state
    shaked6540_youtubeplaylistdownloader_latest_release: _sensor_state
    sherlock_project_sherlock_latest_release: _sensor_state
    thomasnordquist_mqtt_explorer_latest_release: _sensor_state
    travisghansen_hass_opnsense_latest_release: _sensor_state
    vova_sh_termux_api_latest_release: _sensor_state
    esphome_esphome_latest_issue: _sensor_state
    home_assistant_core_latest_issue: _sensor_state
    home_assistant_frontend_latest_issue: _sensor_state
    home_assistant_operating_system_latest_issue: _sensor_state
    home_assistant_supervisor_latest_issue: _sensor_state
    internetarchive_openlibrary_client_latest_issue: _sensor_state
    khoih_prog_wifinina_generic_latest_issue: _sensor_state
    marc_romu_home_assistant_blueprints_latest_issue: _sensor_state
    nabucasa_hass_nabucasa_latest_issue: _sensor_state
    rdavydov_twitch_channel_points_miner_v2_latest_issue: _sensor_state
    shaked6540_youtubeplaylistdownloader_latest_issue: _sensor_state
    sherlock_project_sherlock_latest_issue: _sensor_state
    thomasnordquist_mqtt_explorer_latest_issue: _sensor_state
    travisghansen_hass_opnsense_latest_issue: _sensor_state
    vova_sh_termux_api_latest_issue: _sensor_state
    esphome_esphome_latest_pull_request: _sensor_state
    home_assistant_core_latest_pull_request: _sensor_state
    home_assistant_frontend_latest_pull_request: _sensor_state
    home_assistant_operating_system_latest_pull_request: _sensor_state
    home_assistant_supervisor_latest_pull_request: _sensor_state
    internetarchive_openlibrary_client_latest_pull_request: _sensor_state
    khoih_prog_wifinina_generic_latest_pull_request: _sensor_state
    marc_romu_home_assistant_blueprints_latest_pull_request: _sensor_state
    nabucasa_hass_nabucasa_latest_pull_request: _sensor_state
    rdavydov_twitch_channel_points_miner_v2_latest_pull_request: _sensor_state
    shaked6540_youtubeplaylistdownloader_latest_pull_request: _sensor_state
    sherlock_project_sherlock_latest_pull_request: _sensor_state
    thomasnordquist_mqtt_explorer_latest_pull_request: _sensor_state
    travisghansen_hass_opnsense_latest_pull_request: _sensor_state
    vova_sh_termux_api_latest_pull_request: _sensor_state
    esphome_esphome_latest_tag: _sensor_state
    home_assistant_core_latest_tag: _sensor_state
    home_assistant_frontend_latest_tag: _sensor_state
    home_assistant_operating_system_latest_tag: _sensor_state
    home_assistant_supervisor_latest_tag: _sensor_state
    internetarchive_openlibrary_client_latest_tag: _sensor_state
    khoih_prog_wifinina_generic_latest_tag: _sensor_state
    marc_romu_home_assistant_blueprints_latest_tag: _sensor_state
    nabucasa_hass_nabucasa_latest_tag: _sensor_state
    rdavydov_twitch_channel_points_miner_v2_latest_tag: _sensor_state
    shaked6540_youtubeplaylistdownloader_latest_tag: _sensor_state
    sherlock_project_sherlock_latest_tag: _sensor_state
    thomasnordquist_mqtt_explorer_latest_tag: _sensor_state
    travisghansen_hass_opnsense_latest_tag: _sensor_state
    vova_sh_termux_api_latest_tag: _sensor_state
    ashtonparrott_gmail_com_vacation_end_date: _sensor_state
    megaprojects_latest_upload: _sensor_state
    megaprojects_subscribers: _sensor_state
    erra_latest_upload: _sensor_state
    erra_subscribers: _sensor_state
    today_i_found_out_latest_upload: _sensor_state
    today_i_found_out_subscribers: _sensor_state
    the_casual_criminalist_latest_upload: _sensor_state
    the_casual_criminalist_subscribers: _sensor_state
    mightyteapot_latest_upload: _sensor_state
    mightyteapot_subscribers: _sensor_state
    techquickie_latest_upload: _sensor_state
    techquickie_subscribers: _sensor_state
    ayinmaiden_latest_upload: _sensor_state
    ayinmaiden_subscribers: _sensor_state
    techlinked_latest_upload: _sensor_state
    techlinked_subscribers: _sensor_state
    home_assistant_latest_upload: _sensor_state
    home_assistant_subscribers: _sensor_state
    gamelinked_latest_upload: _sensor_state
    gamelinked_subscribers: _sensor_state
    pbs_space_time_latest_upload: _sensor_state
    pbs_space_time_subscribers: _sensor_state
    everything_smart_home_latest_upload: _sensor_state
    everything_smart_home_subscribers: _sensor_state
    pirate_software_latest_upload: _sensor_state
    pirate_software_subscribers: _sensor_state
    biographics_latest_upload: _sensor_state
    biographics_subscribers: _sensor_state
    shortcircuit_latest_upload: _sensor_state
    shortcircuit_subscribers: _sensor_state
    brew_latest_upload: _sensor_state
    brew_subscribers: _sensor_state
    pbs_eons_latest_upload: _sensor_state
    pbs_eons_subscribers: _sensor_state
    tek_syndicate_latest_upload: _sensor_state
    tek_syndicate_subscribers: _sensor_state
    scishow_latest_upload: _sensor_state
    scishow_subscribers: _sensor_state
    scishow_psych_latest_upload: _sensor_state
    scishow_psych_subscribers: _sensor_state
    valve_latest_upload: _sensor_state
    valve_subscribers: _sensor_state
    familyjules_latest_upload: _sensor_state
    familyjules_subscribers: _sensor_state
    level1techs_latest_upload: _sensor_state
    level1techs_subscribers: _sensor_state
    low_level_learning_latest_upload: _sensor_state
    low_level_learning_subscribers: _sensor_state
    linus_tech_tips_latest_upload: _sensor_state
    linus_tech_tips_subscribers: _sensor_state
    paul_s_hardware_latest_upload: _sensor_state
    paul_s_hardware_subscribers: _sensor_state
    fall_of_civilizations_latest_upload: _sensor_state
    fall_of_civilizations_subscribers: _sensor_state
    jeff_geerling_latest_upload: _sensor_state
    jeff_geerling_subscribers: _sensor_state
    the_histocrat_latest_upload: _sensor_state
    the_histocrat_subscribers: _sensor_state
    national_geographic_latest_upload: _sensor_state
    national_geographic_subscribers: _sensor_state
    adam_savages_tested_latest_upload: _sensor_state
    adam_savages_tested_subscribers: _sensor_state
    novelists_latest_upload: _sensor_state
    novelists_subscribers: _sensor_state
    openweathermap_weather: _sensor_state
    openweathermap_dew_point: _sensor_state
    openweathermap_temperature: _sensor_state
    openweathermap_feels_like_temperature: _sensor_state
    openweathermap_wind_speed: _sensor_state
    openweathermap_wind_bearing: _sensor_state
    openweathermap_humidity: _sensor_state
    openweathermap_pressure: _sensor_state
    openweathermap_cloud_coverage: _sensor_state
    openweathermap_rain: _sensor_state
    openweathermap_snow: _sensor_state
    openweathermap_precipitation_kind: _sensor_state
    openweathermap_uv_index: _sensor_state
    openweathermap_visibility: _sensor_state
    openweathermap_condition: _sensor_state
    openweathermap_weather_code: _sensor_state
    debian_hp_expires: _sensor_state
    debian_hp_ip_address: _sensor_state
    debian_hp_last_seen: _sensor_state
    debian_r_expires: _sensor_state
    debian_r_ip_address: _sensor_state
    debian_r_last_seen: _sensor_state
    desk_j_expires: _sensor_state
    desk_j_ip_address: _sensor_state
    desk_j_last_seen: _sensor_state
    desktop_3tursll_expires: _sensor_state
    desktop_3tursll_ip_address: _sensor_state
    desktop_3tursll_last_seen: _sensor_state
    desktop_bcdiv5f_expires: _sensor_state
    desktop_bcdiv5f_ip_address: _sensor_state
    desktop_bcdiv5f_last_seen: _sensor_state
    google_chromecast_1_expires: _sensor_state
    google_chromecast_1_ip_address: _sensor_state
    google_chromecast_1_last_seen: _sensor_state
    homeassistant_j_1_expires: _sensor_state
    homeassistant_j_1_ip_address: _sensor_state
    homeassistant_j_1_last_seen: _sensor_state
    homeassistant_t_1_expires: _sensor_state
    homeassistant_t_1_ip_address: _sensor_state
    homeassistant_t_1_last_seen: _sensor_state
    ipad_gen_6_expires: _sensor_state
    ipad_gen_6_ip_address: _sensor_state
    ipad_gen_6_last_seen: _sensor_state
    iphone_11_pro_max_expires: _sensor_state
    iphone_11_pro_max_ip_address: _sensor_state
    iphone_11_pro_max_last_seen: _sensor_state
    laptop_expires: _sensor_state
    laptop_ip_address: _sensor_state
    laptop_last_seen: _sensor_state
    opnsense_1_expires: _sensor_state
    opnsense_1_ip_address: _sensor_state
    opnsense_1_last_seen: _sensor_state
    raspberrypi_expires: _sensor_state
    raspberrypi_ip_address: _sensor_state
    raspberrypi_last_seen: _sensor_state
    samsung_sm_a136w_1_expires: _sensor_state
    samsung_sm_a136w_1_ip_address: _sensor_state
    samsung_sm_a136w_1_last_seen: _sensor_state
    samsung_sm_a136w_expires: _sensor_state
    samsung_sm_a136w_ip_address: _sensor_state
    samsung_sm_a136w_last_seen: _sensor_state
    samsung_sm_g960w_expires: _sensor_state
    samsung_sm_g960w_ip_address: _sensor_state
    samsung_sm_g960w_last_seen: _sensor_state
    current_version: _sensor_state
    home_assistant_versions: _sensor_state
    home_assistant_website: _sensor_state
    docker_hub: _sensor_state
    python_package_index_pypi: _sensor_state
    steam_76561198025675241: _sensor_state
    erra_views: _sensor_state
    fall_of_civilizations_views: _sensor_state
    ayinmaiden_views: _sensor_state
    jeff_geerling_views: _sensor_state
    today_i_found_out_views: _sensor_state
    home_assistant_views: _sensor_state
    pbs_eons_views: _sensor_state
    paul_s_hardware_views: _sensor_state
    gamelinked_views: _sensor_state
    linus_tech_tips_views: _sensor_state
    pbs_space_time_views: _sensor_state
    megaprojects_views: _sensor_state
    techquickie_views: _sensor_state
    the_histocrat_views: _sensor_state
    shortcircuit_views: _sensor_state
    adam_savages_tested_views: _sensor_state
    tek_syndicate_views: _sensor_state
    level1techs_views: _sensor_state
    scishow_views: _sensor_state
    everything_smart_home_views: _sensor_state
    biographics_views: _sensor_state
    pirate_software_views: _sensor_state
    novelists_views: _sensor_state
    techlinked_views: _sensor_state
    national_geographic_views: _sensor_state
    familyjules_views: _sensor_state
    brew_views: _sensor_state
    scishow_psych_views: _sensor_state
    the_casual_criminalist_views: _sensor_state
    mightyteapot_views: _sensor_state
    low_level_views: _sensor_state
    valve_views: _sensor_state
    next_payment_date: _sensor_state
    second_payment_date: _sensor_state
    third_payment_date: _sensor_state
    fourth_payment_date: _sensor_state
    fifth_payment_date: _sensor_state
    sixth_payment_date: _sensor_state
    seventh_payment_date: _sensor_state
    eighth_payment_date: _sensor_state
    nineth_payment_date: _sensor_state
    tenth_payment_date: _sensor_state
    eleventh_payment_date: _sensor_state
    appium_appium_inspector_discussions: _sensor_state
    archomeda_gw2sharp_discussions: _sensor_state
    collin80_due_can_discussions: _sensor_state
    drant_gw2navi_discussions: _sensor_state
    esphome_esphome_docs_discussions: _sensor_state
    home_assistant_developers_home_assistant_discussions: _sensor_state
    krtirtho_spotube_discussions: _sensor_state
    locaal_ai_obs_backgroundremoval_discussions: _sensor_state
    pascalluginbuehl_home_assistant_tray_menu_discussions: _sensor_state
    puppeteer_puppeteer_discussions: _sensor_state
    rscustom_rocksmith_custom_song_toolkit_discussions: _sensor_state
    valpackett_node_red_contrib_nut_ups_discussions: _sensor_state
    ventoy_ventoy_discussions: _sensor_state
    appium_appium_inspector_stars: _sensor_state
    archomeda_gw2sharp_stars: _sensor_state
    collin80_due_can_stars: _sensor_state
    drant_gw2navi_stars: _sensor_state
    esphome_esphome_docs_stars: _sensor_state
    home_assistant_developers_home_assistant_stars: _sensor_state
    krtirtho_spotube_stars: _sensor_state
    locaal_ai_obs_backgroundremoval_stars: _sensor_state
    pascalluginbuehl_home_assistant_tray_menu_stars: _sensor_state
    puppeteer_puppeteer_stars: _sensor_state
    rscustom_rocksmith_custom_song_toolkit_stars: _sensor_state
    valpackett_node_red_contrib_nut_ups_stars: _sensor_state
    ventoy_ventoy_stars: _sensor_state
    appium_appium_inspector_watchers: _sensor_state
    archomeda_gw2sharp_watchers: _sensor_state
    collin80_due_can_watchers: _sensor_state
    drant_gw2navi_watchers: _sensor_state
    esphome_esphome_docs_watchers: _sensor_state
    home_assistant_developers_home_assistant_watchers: _sensor_state
    krtirtho_spotube_watchers: _sensor_state
    locaal_ai_obs_backgroundremoval_watchers: _sensor_state
    pascalluginbuehl_home_assistant_tray_menu_watchers: _sensor_state
    puppeteer_puppeteer_watchers: _sensor_state
    rscustom_rocksmith_custom_song_toolkit_watchers: _sensor_state
    valpackett_node_red_contrib_nut_ups_watchers: _sensor_state
    ventoy_ventoy_watchers: _sensor_state
    appium_appium_inspector_forks: _sensor_state
    archomeda_gw2sharp_forks: _sensor_state
    collin80_due_can_forks: _sensor_state
    drant_gw2navi_forks: _sensor_state
    esphome_esphome_docs_forks: _sensor_state
    home_assistant_developers_home_assistant_forks: _sensor_state
    krtirtho_spotube_forks: _sensor_state
    locaal_ai_obs_backgroundremoval_forks: _sensor_state
    pascalluginbuehl_home_assistant_tray_menu_forks: _sensor_state
    puppeteer_puppeteer_forks: _sensor_state
    rscustom_rocksmith_custom_song_toolkit_forks: _sensor_state
    valpackett_node_red_contrib_nut_ups_forks: _sensor_state
    ventoy_ventoy_forks: _sensor_state
    appium_appium_inspector_issues: _sensor_state
    archomeda_gw2sharp_issues: _sensor_state
    collin80_due_can_issues: _sensor_state
    drant_gw2navi_issues: _sensor_state
    esphome_esphome_docs_issues: _sensor_state
    home_assistant_developers_home_assistant_issues: _sensor_state
    krtirtho_spotube_issues: _sensor_state
    locaal_ai_obs_backgroundremoval_issues: _sensor_state
    pascalluginbuehl_home_assistant_tray_menu_issues: _sensor_state
    puppeteer_puppeteer_issues: _sensor_state
    rscustom_rocksmith_custom_song_toolkit_issues: _sensor_state
    valpackett_node_red_contrib_nut_ups_issues: _sensor_state
    ventoy_ventoy_issues: _sensor_state
    appium_appium_inspector_pull_requests: _sensor_state
    archomeda_gw2sharp_pull_requests: _sensor_state
    collin80_due_can_pull_requests: _sensor_state
    drant_gw2navi_pull_requests: _sensor_state
    esphome_esphome_docs_pull_requests: _sensor_state
    home_assistant_developers_home_assistant_pull_requests: _sensor_state
    krtirtho_spotube_pull_requests: _sensor_state
    locaal_ai_obs_backgroundremoval_pull_requests: _sensor_state
    pascalluginbuehl_home_assistant_tray_menu_pull_requests: _sensor_state
    puppeteer_puppeteer_pull_requests: _sensor_state
    rscustom_rocksmith_custom_song_toolkit_pull_requests: _sensor_state
    valpackett_node_red_contrib_nut_ups_pull_requests: _sensor_state
    ventoy_ventoy_pull_requests: _sensor_state
    appium_appium_inspector_latest_commit: _sensor_state
    archomeda_gw2sharp_latest_commit: _sensor_state
    collin80_due_can_latest_commit: _sensor_state
    drant_gw2navi_latest_commit: _sensor_state
    esphome_esphome_docs_latest_commit: _sensor_state
    home_assistant_developers_home_assistant_latest_commit: _sensor_state
    krtirtho_spotube_latest_commit: _sensor_state
    locaal_ai_obs_backgroundremoval_latest_commit: _sensor_state
    pascalluginbuehl_home_assistant_tray_menu_latest_commit: _sensor_state
    puppeteer_puppeteer_latest_commit: _sensor_state
    rscustom_rocksmith_custom_song_toolkit_latest_commit: _sensor_state
    valpackett_node_red_contrib_nut_ups_latest_commit: _sensor_state
    ventoy_ventoy_latest_commit: _sensor_state
    appium_appium_inspector_latest_discussion: _sensor_state
    archomeda_gw2sharp_latest_discussion: _sensor_state
    collin80_due_can_latest_discussion: _sensor_state
    drant_gw2navi_latest_discussion: _sensor_state
    esphome_esphome_docs_latest_discussion: _sensor_state
    home_assistant_developers_home_assistant_latest_discussion: _sensor_state
    krtirtho_spotube_latest_discussion: _sensor_state
    locaal_ai_obs_backgroundremoval_latest_discussion: _sensor_state
    pascalluginbuehl_home_assistant_tray_menu_latest_discussion: _sensor_state
    puppeteer_puppeteer_latest_discussion: _sensor_state
    rscustom_rocksmith_custom_song_toolkit_latest_discussion: _sensor_state
    valpackett_node_red_contrib_nut_ups_latest_discussion: _sensor_state
    ventoy_ventoy_latest_discussion: _sensor_state
    appium_appium_inspector_latest_release: _sensor_state
    archomeda_gw2sharp_latest_release: _sensor_state
    collin80_due_can_latest_release: _sensor_state
    drant_gw2navi_latest_release: _sensor_state
    esphome_esphome_docs_latest_release: _sensor_state
    home_assistant_developers_home_assistant_latest_release: _sensor_state
    krtirtho_spotube_latest_release: _sensor_state
    locaal_ai_obs_backgroundremoval_latest_release: _sensor_state
    pascalluginbuehl_home_assistant_tray_menu_latest_release: _sensor_state
    puppeteer_puppeteer_latest_release: _sensor_state
    rscustom_rocksmith_custom_song_toolkit_latest_release: _sensor_state
    valpackett_node_red_contrib_nut_ups_latest_release: _sensor_state
    ventoy_ventoy_latest_release: _sensor_state
    appium_appium_inspector_latest_issue: _sensor_state
    archomeda_gw2sharp_latest_issue: _sensor_state
    collin80_due_can_latest_issue: _sensor_state
    drant_gw2navi_latest_issue: _sensor_state
    esphome_esphome_docs_latest_issue: _sensor_state
    home_assistant_developers_home_assistant_latest_issue: _sensor_state
    krtirtho_spotube_latest_issue: _sensor_state
    locaal_ai_obs_backgroundremoval_latest_issue: _sensor_state
    pascalluginbuehl_home_assistant_tray_menu_latest_issue: _sensor_state
    puppeteer_puppeteer_latest_issue: _sensor_state
    rscustom_rocksmith_custom_song_toolkit_latest_issue: _sensor_state
    valpackett_node_red_contrib_nut_ups_latest_issue: _sensor_state
    ventoy_ventoy_latest_issue: _sensor_state
    appium_appium_inspector_latest_pull_request: _sensor_state
    archomeda_gw2sharp_latest_pull_request: _sensor_state
    collin80_due_can_latest_pull_request: _sensor_state
    drant_gw2navi_latest_pull_request: _sensor_state
    esphome_esphome_docs_latest_pull_request: _sensor_state
    home_assistant_developers_home_assistant_latest_pull_request: _sensor_state
    krtirtho_spotube_latest_pull_request: _sensor_state
    locaal_ai_obs_backgroundremoval_latest_pull_request: _sensor_state
    pascalluginbuehl_home_assistant_tray_menu_latest_pull_request: _sensor_state
    puppeteer_puppeteer_latest_pull_request: _sensor_state
    rscustom_rocksmith_custom_song_toolkit_latest_pull_request: _sensor_state
    valpackett_node_red_contrib_nut_ups_latest_pull_request: _sensor_state
    ventoy_ventoy_latest_pull_request: _sensor_state
    appium_appium_inspector_latest_tag: _sensor_state
    archomeda_gw2sharp_latest_tag: _sensor_state
    collin80_due_can_latest_tag: _sensor_state
    drant_gw2navi_latest_tag: _sensor_state
    esphome_esphome_docs_latest_tag: _sensor_state
    home_assistant_developers_home_assistant_latest_tag: _sensor_state
    krtirtho_spotube_latest_tag: _sensor_state
    locaal_ai_obs_backgroundremoval_latest_tag: _sensor_state
    pascalluginbuehl_home_assistant_tray_menu_latest_tag: _sensor_state
    puppeteer_puppeteer_latest_tag: _sensor_state
    rscustom_rocksmith_custom_song_toolkit_latest_tag: _sensor_state
    valpackett_node_red_contrib_nut_ups_latest_tag: _sensor_state
    ventoy_ventoy_latest_tag: _sensor_state
    steam_76561198114428871: _sensor_state
    steam_76561199028137767: _sensor_state
    steam_76561198110821511: _sensor_state
    steam_76561198065326149: _sensor_state
    steam_76561198090583332: _sensor_state
    steam_76561198124525034: _sensor_state
    steam_76561198147768538: _sensor_state
    flightradar24_current_in_area: _sensor_state
    flightradar24_entered_area: _sensor_state
    flightradar24_exited_area: _sensor_state
    flightradar24_additional_tracked: _sensor_state
    flightradar24_most_tracked: _sensor_state
    fast_gas_regular_gas: _sensor_state
    fast_gas_midgrade_gas: _sensor_state
    fast_gas_premium_gas: _sensor_state
    fast_gas_diesel: _sensor_state
    air_quality: _sensor_state
    alarm_control_panels: _sensor_state
    areas: _sensor_state
    automations: _sensor_state
    binary_sensors: _sensor_state
    buttons: _sensor_state
    calendars: _sensor_state
    cameras: _sensor_state
    climate: _sensor_state
    covers: _sensor_state
    dates: _sensor_state
    datetimes: _sensor_state
    devices: _sensor_state
    device_trackers: _sensor_state
    entities: _sensor_state
    fans: _sensor_state
    humidifiers: _sensor_state
    integrations: _sensor_state
    custom_integrations: _sensor_state
    input_booleans: _sensor_state
    input_buttons: _sensor_state
    input_datetimes: _sensor_state
    input_numbers: _sensor_state
    input_selects: _sensor_state
    input_texts: _sensor_state
    images: _sensor_state
    lights: _sensor_state
    locks: _sensor_state
    media_players: _sensor_state
    numbers: _sensor_state
    persistent_notifications: _sensor_state
    persons: _sensor_state
    remotes: _sensor_state
    scenes: _sensor_state
    scripts: _sensor_state
    selects: _sensor_state
    sensors: _sensor_state
    sirens: _sensor_state
    suns: _sensor_state
    stt: _sensor_state
    switches: _sensor_state
    texts: _sensor_state
    times: _sensor_state
    tts: _sensor_state
    vacuums: _sensor_state
    update: _sensor_state
    water_heaters: _sensor_state
    weather: _sensor_state
    zones: _sensor_state
    issues: _sensor_state
    active_issues: _sensor_state
    ignored_issues: _sensor_state
    lethbridge_moon_age: _sensor_state
    lethbridge_moon_distance: _sensor_state
    lethbridge_moon_illumination_fraction: _sensor_state
    lethbridge_next_full_moon: _sensor_state
    lethbridge_next_new_moon: _sensor_state
    lethbridge_next_third_quarter: _sensor_state
    lethbridge_next_first_quarter: _sensor_state
    lethbridge_moon_rise: _sensor_state
    lethbridge_moon_set: _sensor_state
    lethbridge_moon_high: _sensor_state
    lethbridge_moon_altitude: _sensor_state
    lethbridge_moon_azimuth: _sensor_state
    lethbridge_moon_parallactic_angle: _sensor_state
    lethbridge_next_moon_phase: _sensor_state
    lethbridge_moon_phase: _sensor_state
    lethbridge_alberta_canada_air_quality_index: _sensor_state
    lethbridge_alberta_canada_humidity: _sensor_state
    lethbridge_alberta_canada_pressure: _sensor_state
    lethbridge_alberta_canada_temperature: _sensor_state
    lethbridge_alberta_canada_carbon_monoxide: _sensor_state
    lethbridge_alberta_canada_nitrogen_dioxide: _sensor_state
    lethbridge_alberta_canada_ozone: _sensor_state
    lethbridge_alberta_canada_sulphur_dioxide: _sensor_state
    lethbridge_alberta_canada_pm2_5: _sensor_state
    lethbridge_alberta_canada_dominant_pollutant: _sensor_state
    icloud3_event_log: _sensor_state
    icloud3_wazehist_track: _sensor_state
    steam_76561198822460645: _sensor_state
    channel_super_fun_latest_upload: _sensor_state
    channel_super_fun_subscribers: _sensor_state
    channel_super_fun_views: _sensor_state
    thedooo_latest_upload: _sensor_state
    thedooo_subscribers: _sensor_state
    thedooo_views: _sensor_state
    strange_parts_latest_upload: _sensor_state
    strange_parts_subscribers: _sensor_state
    strange_parts_views: _sensor_state
    hankschannel_latest_upload: _sensor_state
    hankschannel_subscribers: _sensor_state
    hankschannel_views: _sensor_state
    bizarre_beasts_latest_upload: _sensor_state
    bizarre_beasts_subscribers: _sensor_state
    bizarre_beasts_views: _sensor_state
    history_time_latest_upload: _sensor_state
    history_time_subscribers: _sensor_state
    history_time_views: _sensor_state
    guild_wars_2_latest_upload: _sensor_state
    guild_wars_2_subscribers: _sensor_state
    guild_wars_2_views: _sensor_state
    spotify_ashton_parrott_song_danceability: _sensor_state
    spotify_ashton_parrott_song_energy: _sensor_state
    spotify_ashton_parrott_song_mode: _sensor_state
    spotify_ashton_parrott_song_speechiness: _sensor_state
    spotify_ashton_parrott_song_acousticness: _sensor_state
    spotify_ashton_parrott_song_instrumentalness: _sensor_state
    spotify_ashton_parrott_song_liveness: _sensor_state
    spotify_ashton_parrott_song_valence: _sensor_state
    spotify_ashton_parrott_song_time_signature: _sensor_state
    spotify_ashton_parrott_song_key: _sensor_state
    spotify_jusparr_song_tempo: _sensor_state
    spotify_jusparr_song_danceability: _sensor_state
    spotify_jusparr_song_energy: _sensor_state
    spotify_jusparr_song_mode: _sensor_state
    spotify_jusparr_song_speechiness: _sensor_state
    spotify_jusparr_song_acousticness: _sensor_state
    spotify_jusparr_song_instrumentalness: _sensor_state
    spotify_jusparr_song_liveness: _sensor_state
    spotify_jusparr_song_valence: _sensor_state
    spotify_jusparr_song_time_signature: _sensor_state
    spotify_jusparr_song_key: _sensor_state
    temp_outside: _sensor_state
    humidity_outside: _sensor_state
    temp_indoor: _sensor_state
    humidity_indoor: _sensor_state
    temp_soil: _sensor_state
    wmr968_extra_temp: _sensor_state
    temp_extra_sensor_1: _sensor_state
    temp_extra_sensor_2: _sensor_state
    temp_extra_sensor_3: _sensor_state
    temp_extra_sensor_4: _sensor_state
    temp_day_maximum: _sensor_state
    temp_day_minimum: _sensor_state
    temp_hour_01: _sensor_state
    temp_hour_02: _sensor_state
    temp_hour_03: _sensor_state
    temp_hour_04: _sensor_state
    temp_hour_05: _sensor_state
    temp_hour_06: _sensor_state
    temp_hour_07: _sensor_state
    temp_hour_08: _sensor_state
    temp_hour_09: _sensor_state
    temp_hour_10: _sensor_state
    temp_indoor_maximum: _sensor_state
    temp_indoor_minimum: _sensor_state
    apparent_temp: _sensor_state
    apparent_temp_maximum: _sensor_state
    apparent_temp_minimum: _sensor_state
    temp_trend: _sensor_state
    humidity_trend: _sensor_state
    temp_wet_bulb: _sensor_state
    humidity_high_day: _sensor_state
    humidity_low_day: _sensor_state
    temp_maximum_day_time: _sensor_state
    temp_minimum_day_time: _sensor_state
    temp_hour_4: _sensor_state
    temp_hour_5: _sensor_state
    temp_hour_6: _sensor_state
    temp_hour_7: _sensor_state
    temp_hour_8: _sensor_state
    temp_hour_9: _sensor_state
    temp_hour_10_2: _sensor_state
    temp_hour_11: _sensor_state
    temp_hour_12: _sensor_state
    temp_hour_13: _sensor_state
    temp_hour_14: _sensor_state
    temp_hour_15: _sensor_state
    temp_hour_16: _sensor_state
    temp_hour_17: _sensor_state
    temp_hour_18: _sensor_state
    temp_hour_19: _sensor_state
    temp_hour_20: _sensor_state
    temp_high_month_record: _sensor_state
    temp_high_month_record_hour: _sensor_state
    temp_high_month_record_minimum: _sensor_state
    temp_high_month_record_day: _sensor_state
    temp_high_month_record_month: _sensor_state
    temp_high_month_record_year: _sensor_state
    temp_low_month_record: _sensor_state
    temp_low_month_record_hour: _sensor_state
    temp_low_month_record_minimum: _sensor_state
    temp_low_month_record_day: _sensor_state
    temp_low_month_record_month: _sensor_state
    temp_low_month_record_year: _sensor_state
    temp_high_year_to_date_record: _sensor_state
    temp_high_year_to_date_record_hour: _sensor_state
    temp_high_year_to_date_record_minimum: _sensor_state
    temp_high_year_to_date_record_day: _sensor_state
    temp_high_year_to_date_record_month: _sensor_state
    temp_high_year_to_date_record_year: _sensor_state
    temp_low_year_to_date_record: _sensor_state
    temp_low_year_to_date_record_hour: _sensor_state
    temp_low_year_to_date_record_minimum: _sensor_state
    temp_low_year_to_date_record_day: _sensor_state
    temp_low_year_to_date_record_month: _sensor_state
    temp_low_year_to_date_record_year: _sensor_state
    temp_high_all_time_record: _sensor_state
    temp_high_all_time_record_hour: _sensor_state
    temp_high_all_time_record_minimum: _sensor_state
    temp_high_all_time_record_day: _sensor_state
    temp_high_all_time_record_month: _sensor_state
    temp_high_all_time_record_year: _sensor_state
    temp_low_all_time_record: _sensor_state
    temp_low_all_time_record_hour: _sensor_state
    temp_low_all_time_record_minimum: _sensor_state
    temp_low_all_time_record_day: _sensor_state
    temp_low_all_time_record_month: _sensor_state
    temp_low_all_time_record_year: _sensor_state
    temp_hour_21: _sensor_state
    temp_hour_22: _sensor_state
    temp_hour_23: _sensor_state
    temp_hour_24: _sensor_state
    temp_extra_sensor_high_1: _sensor_state
    temp_extra_sensor_low_1: _sensor_state
    temp_extra_sensor_high_2: _sensor_state
    temp_extra_sensor_low_2: _sensor_state
    temp_extra_sensor_high_3: _sensor_state
    temp_extra_sensor_low_3: _sensor_state
    temp_extra_sensor_high_4: _sensor_state
    temp_extra_sensor_low_4: _sensor_state
    temp_extra_sensor_high_5: _sensor_state
    temp_extra_sensor_low_5: _sensor_state
    temp_extra_sensor_high_6: _sensor_state
    temp_extra_sensor_low_6: _sensor_state
    temp_extra_sensor_high_7: _sensor_state
    temp_extra_sensor_low_7: _sensor_state
    temp_extra_sensor_high_8: _sensor_state
    temp_extra_sensor_low_8: _sensor_state
    humidity_hour_1: _sensor_state
    humidity_hour_2: _sensor_state
    humidity_hour_3: _sensor_state
    humidity_hour_4: _sensor_state
    humidity_hour_5: _sensor_state
    humidity_hour_6: _sensor_state
    humidity_hour_7: _sensor_state
    humidity_hour_8: _sensor_state
    humidity_hour_9: _sensor_state
    humidity_hour_10: _sensor_state
    humidity_hour_11: _sensor_state
    humidity_hour_12: _sensor_state
    humidity_hour_13: _sensor_state
    humidity_hour_14: _sensor_state
    humidity_hour_15: _sensor_state
    humidity_hour_16: _sensor_state
    humidity_hour_17: _sensor_state
    humidity_hour_18: _sensor_state
    humidity_hour_19: _sensor_state
    humidity_hour_20: _sensor_state
    humidity_hour_21: _sensor_state
    humidity_hour_22: _sensor_state
    humidity_hour_23: _sensor_state
    humidity_hour_24: _sensor_state
    temperature_indoor_hour_1: _sensor_state
    temperature_indoor_hour_2: _sensor_state
    temperature_indoor_hour_3: _sensor_state
    temperature_indoor_hour_4: _sensor_state
    temperature_indoor_hour_5: _sensor_state
    temperature_indoor_hour_6: _sensor_state
    temperature_indoor_hour_7: _sensor_state
    temperature_indoor_hour_8: _sensor_state
    temperature_indoor_hour_9: _sensor_state
    temperature_indoor_hour_10: _sensor_state
    temperature_indoor_hour_11: _sensor_state
    temperature_indoor_hour_12: _sensor_state
    temperature_indoor_hour_13: _sensor_state
    temperature_indoor_hour_14: _sensor_state
    temperature_indoor_hour_15: _sensor_state
    temperature_indoor_hour_16: _sensor_state
    temperature_indoor_hour_17: _sensor_state
    temperature_indoor_hour_18: _sensor_state
    temperature_indoor_hour_19: _sensor_state
    temperature_indoor_hour_20: _sensor_state
    temperature_indoor_hour_21: _sensor_state
    temperature_indoor_hour_22: _sensor_state
    temperature_indoor_hour_23: _sensor_state
    temperature_indoor_hour_24: _sensor_state
    temp_soil_flag: _sensor_state
    temperature_maximum_yesterday: _sensor_state
    temperature_minimum_yesterday: _sensor_state
    temperature_maximum_yesterday_time: _sensor_state
    temperature_minimum_yesterday_time: _sensor_state
    humidity_maximum_yesterday: _sensor_state
    humidity_minimum_yesterday: _sensor_state
    humidity_maximum_yesterday_time: _sensor_state
    humidity_minimum_yesterday_time: _sensor_state
    temperature_maximum_today: _sensor_state
    temperature_minimum_today: _sensor_state
    temperature_maximum_today_time: _sensor_state
    temperature_minimum_today_time: _sensor_state
    humidity_maximum_today: _sensor_state
    humidity_minimum_today: _sensor_state
    humidity_maximum_today_time: _sensor_state
    humidity_minimum_today_time: _sensor_state
    temp_high_month_1: _sensor_state
    temp_high_month_2: _sensor_state
    temp_high_month_3: _sensor_state
    temp_high_month_6: _sensor_state
    temp_high_month_7: _sensor_state
    temp_high_month_8: _sensor_state
    temp_high_month_9: _sensor_state
    temp_high_month_10: _sensor_state
    temp_high_month_11: _sensor_state
    temp_high_month_15: _sensor_state
    temp_high_month_17: _sensor_state
    temp_high_month_18: _sensor_state
    temp_high_month_19: _sensor_state
    temp_low_month_10: _sensor_state
    temp_low_month_11: _sensor_state
    temp_low_month_12: _sensor_state
    temp_low_month_13: _sensor_state
    temp_low_month_14: _sensor_state
    temp_low_month_17: _sensor_state
    temp_low_month_18: _sensor_state
    temp_low_month_19: _sensor_state
    temp_low_month_20: _sensor_state
    temp_low_month_21: _sensor_state
    temp_low_month_22: _sensor_state
    temp_low_month_23: _sensor_state
    temp_low_month_24: _sensor_state
    temp_low_month_25: _sensor_state
    temp_low_month_26: _sensor_state
    temp_low_month_27: _sensor_state
    temp_low_month_28: _sensor_state
    temp_low_month_29: _sensor_state
    humidity_month_1: _sensor_state
    humidity_month_2: _sensor_state
    humidity_month_3: _sensor_state
    humidity_month_4: _sensor_state
    humidity_month_5: _sensor_state
    humidity_month_6: _sensor_state
    humidity_month_7: _sensor_state
    humidity_month_8: _sensor_state
    humidity_month_9: _sensor_state
    humidity_month_10: _sensor_state
    humidity_month_11: _sensor_state
    humidity_month_12: _sensor_state
    humidity_month_13: _sensor_state
    humidity_month_14: _sensor_state
    humidity_month_15: _sensor_state
    humidity_month_16: _sensor_state
    humidity_month_17: _sensor_state
    humidity_month_18: _sensor_state
    humidity_month_19: _sensor_state
    humidity_month_20: _sensor_state
    humidity_month_21: _sensor_state
    humidity_month_22: _sensor_state
    humidity_month_23: _sensor_state
    humidity_month_24: _sensor_state
    humidity_month_25: _sensor_state
    humidity_month_26: _sensor_state
    humidity_month_27: _sensor_state
    humidity_month_28: _sensor_state
    humidity_month_29: _sensor_state
    humidity_month_30: _sensor_state
    humidity_month_31: _sensor_state
    temperature_day_1_1: _sensor_state
    temperature_day_1_2: _sensor_state
    temperature_day_1_3: _sensor_state
    temperature_day_1_4: _sensor_state
    temperature_day_2_1: _sensor_state
    temperature_day_2_2: _sensor_state
    temperature_day_2_3: _sensor_state
    temperature_day_2_4: _sensor_state
    temperature_day_3_1: _sensor_state
    temperature_day_3_2: _sensor_state
    temperature_day_3_3: _sensor_state
    temperature_day_3_4: _sensor_state
    temperature_day_4_1: _sensor_state
    temperature_day_4_2: _sensor_state
    temperature_day_4_3: _sensor_state
    temperature_day_4_4: _sensor_state
    temperature_day_5_1: _sensor_state
    temperature_day_5_2: _sensor_state
    temperature_day_5_3: _sensor_state
    temperature_day_5_4: _sensor_state
    temperature_day_6_1: _sensor_state
    temperature_day_6_2: _sensor_state
    temperature_day_6_3: _sensor_state
    temperature_day_6_4: _sensor_state
    temperature_day_7_1: _sensor_state
    temperature_day_7_2: _sensor_state
    temperature_day_7_3: _sensor_state
    temperature_day_7_4: _sensor_state
    humidity_day_1_1: _sensor_state
    humidity_day_1_2: _sensor_state
    humidity_day_1_3: _sensor_state
    humidity_day_1_4: _sensor_state
    humidity_day_2_1: _sensor_state
    humidity_day_2_2: _sensor_state
    humidity_day_2_3: _sensor_state
    humidity_day_2_4: _sensor_state
    humidity_day_3_1: _sensor_state
    humidity_day_3_2: _sensor_state
    humidity_day_3_3: _sensor_state
    humidity_day_3_4: _sensor_state
    humidity_day_4_1: _sensor_state
    humidity_day_4_2: _sensor_state
    humidity_day_4_3: _sensor_state
    humidity_day_4_4: _sensor_state
    humidity_day_5_1: _sensor_state
    humidity_day_5_2: _sensor_state
    humidity_day_5_3: _sensor_state
    humidity_day_5_4: _sensor_state
    humidity_day_6_1: _sensor_state
    humidity_day_6_2: _sensor_state
    humidity_day_6_3: _sensor_state
    humidity_day_6_4: _sensor_state
    temperature_for_last_60_minutes_to_minute_01: _sensor_state
    temperature_for_last_60_minutes_to_minute_02: _sensor_state
    temperature_for_last_60_minutes_to_minute_03: _sensor_state
    temperature_for_last_60_minutes_to_minute_04: _sensor_state
    temperature_for_last_60_minutes_to_minute_05: _sensor_state
    temperature_for_last_60_minutes_to_minute_06: _sensor_state
    temperature_for_last_60_minutes_to_minute_50: _sensor_state
    temperature_for_last_60_minutes_to_minute_51: _sensor_state
    temperature_for_last_60_minutes_to_minute_52: _sensor_state
    humidity_for_last_60_minutes_to_minute_21: _sensor_state
    humidity_for_last_60_minutes_to_minute_22: _sensor_state
    humidity_for_last_60_minutes_to_minute_23: _sensor_state
    humidity_for_last_60_minutes_to_minute_24: _sensor_state
    humidity_for_last_60_minutes_to_minute_25: _sensor_state
    humidity_for_last_60_minutes_to_minute_26: _sensor_state
    humidity_for_last_60_minutes_to_minute_27: _sensor_state
    humidity_for_last_60_minutes_to_minute_28: _sensor_state
    humidity_for_last_60_minutes_to_minute_29: _sensor_state
    humidity_for_last_60_minutes_to_minute_30: _sensor_state
    humidity_for_last_60_minutes_to_minute_31: _sensor_state
    humidity_for_last_60_minutes_to_minute_32: _sensor_state
    humidity_for_last_60_minutes_to_minute_33: _sensor_state
    humidity_for_last_60_minutes_to_minute_34: _sensor_state
    humidity_for_last_60_minutes_to_minute_35: _sensor_state
    humidity_for_last_60_minutes_to_minute_36: _sensor_state
    humidity_for_last_60_minutes_to_minute_37: _sensor_state
    humidity_for_last_60_minutes_to_minute_38: _sensor_state
    humidity_for_last_60_minutes_to_minute_39: _sensor_state
    humidity_for_last_60_minutes_to_minute_40: _sensor_state
    humidity_for_last_60_minutes_to_minute_41: _sensor_state
    humidity_for_last_60_minutes_to_minute_42: _sensor_state
    humidity_for_last_60_minutes_to_minute_43: _sensor_state
    humidity_for_last_60_minutes_to_minute_44: _sensor_state
    humidity_for_last_60_minutes_to_minute_45: _sensor_state
    humidity_for_last_60_minutes_to_minute_46: _sensor_state
    humidity_for_last_60_minutes_to_minute_47: _sensor_state
    humidity_for_last_60_minutes_to_minute_48: _sensor_state
    syth_iphone_icloud_home_distance: _sensor_state
    syth_iphone_icloud_badge: _sensor_state
    syth_iphone_icloud_dir_of_travel: _sensor_state
    syth_iphone_icloud_zone_name: _sensor_state
    syth_iphone_icloud_name: _sensor_state
    syth_iphone_icloud_zone_distance: _sensor_state
    syth_iphone_icloud_info: _sensor_state
    syth_iphone_icloud_moved_distance: _sensor_state
    syth_iphone_icloud_battery_status: _sensor_state
    syth_iphone_icloud_next_update: _sensor_state
    syth_iphone_icloud_interval: _sensor_state
    syth_iphone_icloud_battery: _sensor_state
    syth_iphone_icloud_last_located: _sensor_state
    syth_iphone_icloud_travel_time_min: _sensor_state
    syth_iphone_icloud_travel_time: _sensor_state
    syth_iphone_icloud_arrival_time: _sensor_state
    syth_iphone_icloud_last_update: _sensor_state
    syth_iphone_icloud_travel_time_min_costco_wholesale: _sensor_state
    syth_iphone_icloud_travel_time_min_superstore: _sensor_state
    syth_iphone_icloud_travel_time_min_the_home_depot_south: _sensor_state
    syth_iphone_icloud_travel_time_min_wallmart_north: _sensor_state
    syth_iphone_icloud_travel_time_min_wallmart_south: _sensor_state
    syth_iphone_icloud_travel_time_min_home: _sensor_state
    syth_iphone_icloud_arrival_time_costco_wholesale: _sensor_state
    syth_iphone_icloud_arrival_time_superstore: _sensor_state
    syth_iphone_icloud_arrival_time_the_home_depot_south: _sensor_state
    syth_iphone_icloud_arrival_time_wallmart_north: _sensor_state
    syth_iphone_icloud_arrival_time_wallmart_south: _sensor_state
    syth_iphone_icloud_arrival_time_home: _sensor_state
    syth_iphone_icloud_travel_time_costco_wholesale: _sensor_state
    syth_iphone_icloud_travel_time_superstore: _sensor_state
    syth_iphone_icloud_travel_time_the_home_depot_south: _sensor_state
    syth_iphone_icloud_travel_time_wallmart_north: _sensor_state
    syth_iphone_icloud_travel_time_wallmart_south: _sensor_state
    syth_iphone_icloud_travel_time_home: _sensor_state
    syth_iphone_icloud_dir_of_travel_costco_wholesale: _sensor_state
    syth_iphone_icloud_dir_of_travel_superstore: _sensor_state
    syth_iphone_icloud_dir_of_travel_the_home_depot_south: _sensor_state
    syth_iphone_icloud_dir_of_travel_wallmart_north: _sensor_state
    syth_iphone_icloud_dir_of_travel_wallmart_south: _sensor_state
    syth_iphone_icloud_dir_of_travel_home: _sensor_state
    syth_iphone_icloud_zone_info_costco_wholesale: _sensor_state
    syth_iphone_icloud_zone_info_superstore: _sensor_state
    syth_iphone_icloud_zone_info_the_home_depot_south: _sensor_state
    syth_iphone_icloud_zone_info_wallmart_north: _sensor_state
    syth_iphone_icloud_zone_info_wallmart_south: _sensor_state
    syth_iphone_icloud_zone_info_home: _sensor_state
    syth_iphone_icloud_zone_distance_costco_wholesale: _sensor_state
    syth_iphone_icloud_zone_distance_superstore: _sensor_state
    syth_iphone_icloud_zone_distance_the_home_depot_south: _sensor_state
    syth_iphone_icloud_zone_distance_wallmart_north: _sensor_state
    syth_iphone_icloud_zone_distance_wallmart_south: _sensor_state
    syth_iphone_icloud_zone_distance_home: _sensor_state
    syth_iphone_icloud_vertical_accuracy: _sensor_state
    syth_iphone_icloud_calc_distance: _sensor_state
    syth_iphone_icloud_travel_time_hhmm: _sensor_state
    syth_iphone_icloud_last_zone_name: _sensor_state
    syth_iphone_icloud_zone: _sensor_state
    syth_iphone_icloud_gps_accuracy: _sensor_state
    syth_iphone_icloud_trigger: _sensor_state
    syth_iphone_icloud_waze_distance: _sensor_state
    syth_iphone_icloud_altitude: _sensor_state
    syth_iphone_icloud_zone_fname: _sensor_state
    syth_iphone_icloud_travel_time_hhmm_costco_wholesale: _sensor_state
    syth_iphone_icloud_travel_time_hhmm_superstore: _sensor_state
    syth_iphone_icloud_travel_time_hhmm_the_home_depot_south: _sensor_state
    syth_iphone_icloud_travel_time_hhmm_wallmart_north: _sensor_state
    syth_iphone_icloud_travel_time_hhmm_wallmart_south: _sensor_state
    syth_iphone_icloud_travel_time_hhmm_home: _sensor_state
    syth_iphone_icloud_last_zone_fname: _sensor_state
    syth_iphone_icloud_last_zone: _sensor_state
    ufd_tech_latest_upload: _sensor_state
    ufd_tech_subscribers: _sensor_state
    ufd_tech_views: _sensor_state
    lindsay_nikole_latest_upload: _sensor_state
    lindsay_nikole_subscribers: _sensor_state
    lindsay_nikole_views: _sensor_state
    steam_76561197986591355: _sensor_state
    tomorrow_io_home_feels_like: _sensor_state
    tomorrow_io_home_dew_point: _sensor_state
    tomorrow_io_home_pressure: _sensor_state
    tomorrow_io_home_irradiance: _sensor_state
    tomorrow_io_home_cloud_base: _sensor_state
    tomorrow_io_home_cloud_ceiling: _sensor_state
    tomorrow_io_home_cloud_cover: _sensor_state
    tomorrow_io_home_wind_gust: _sensor_state
    tomorrow_io_home_precipitation_type: _sensor_state
    tomorrow_io_home_ozone: _sensor_state
    tomorrow_io_home_pm2_5: _sensor_state
    tomorrow_io_home_pm10: _sensor_state
    tomorrow_io_home_nitrogen_dioxide: _sensor_state
    tomorrow_io_home_carbon_monoxide: _sensor_state
    tomorrow_io_home_sulphur_dioxide: _sensor_state
    tomorrow_io_home_us_epa_air_quality_index: _sensor_state
    tomorrow_io_home_us_epa_primary_pollutant: _sensor_state
    tomorrow_io_home_us_epa_health_concern: _sensor_state
    tomorrow_io_home_tree_pollen_index: _sensor_state
    tomorrow_io_home_weed_pollen_index: _sensor_state
    tomorrow_io_home_grass_pollen_index: _sensor_state
    tomorrow_io_home_fire_index: _sensor_state
    tomorrow_io_home_uv_index: _sensor_state
    tomorrow_io_home_uv_radiation_health_concern: _sensor_state
    electricity_maps_co2_intensity: _sensor_state
    electricity_maps_grid_fossil_fuel_percentage: _sensor_state
    esso_180_columbia_blvd_regular_gas: _sensor_state
    esso_180_columbia_blvd_midgrade_gas: _sensor_state
    esso_180_columbia_blvd_premium_gas: _sensor_state
    esso_180_columbia_blvd_diesel: _sensor_state
    costco_regular_gas: _sensor_state
    costco_midgrade_gas: _sensor_state
    costco_premium_gas: _sensor_state
    gas_king_picture_butte_regular_gas: _sensor_state
    gas_king_picture_butte_midgrade_gas: _sensor_state
    gas_king_picture_butte_premium_gas: _sensor_state
    gas_king_picture_butte_diesel: _sensor_state
    safeway_w_regular_gas: _sensor_state
    safeway_w_midgrade_gas: _sensor_state
    safeway_w_premium_gas: _sensor_state
    safeway_w_diesel: _sensor_state
    gas_king_16th_ave_regular_gas: _sensor_state
    gas_king_16th_ave_midgrade_gas: _sensor_state
    gas_king_16th_ave_premium_gas: _sensor_state
    gas_king_16th_ave_diesel: _sensor_state
    shell_scenic_dr_regular_gas: _sensor_state
    shell_scenic_dr_midgrade_gas: _sensor_state
    shell_scenic_dr_premium_gas: _sensor_state
    shell_scenic_dr_diesel: _sensor_state
    gas_king_mm_dr_regular_gas: _sensor_state
    gas_king_mm_dr_midgrade_gas: _sensor_state
    gas_king_mm_dr_premium_gas: _sensor_state
    gas_king_mm_dr_diesel: _sensor_state
    syth_ipad_info: _sensor_state
    syth_ipad_last_located: _sensor_state
    syth_ipad_home_distance: _sensor_state
    syth_ipad_zone_name: _sensor_state
    syth_ipad_last_zone: _sensor_state
    syth_ipad_battery: _sensor_state
    syth_ipad_arrival_time: _sensor_state
    syth_ipad_waze_distance: _sensor_state
    syth_ipad_calc_distance: _sensor_state
    syth_ipad_last_update: _sensor_state
    syth_ipad_interval: _sensor_state
    syth_ipad_next_update: _sensor_state
    syth_ipad_zone_fname: _sensor_state
    syth_ipad_travel_time_hhmm: _sensor_state
    syth_ipad_badge: _sensor_state
    syth_ipad_travel_time: _sensor_state
    syth_ipad_zone: _sensor_state
    syth_ipad_zone_distance: _sensor_state
    syth_ipad_dir_of_travel: _sensor_state
    syth_ipad_travel_time_min: _sensor_state
    syth_ipad_gps_accuracy: _sensor_state
    syth_ipad_last_zone_fname: _sensor_state
    syth_ipad_vertical_accuracy: _sensor_state
    syth_ipad_battery_status: _sensor_state
    syth_ipad_name: _sensor_state
    syth_ipad_moved_distance: _sensor_state
    syth_ipad_trigger: _sensor_state
    syth_ipad_last_zone_name: _sensor_state
    syth_ipad_altitude: _sensor_state
    syth_ipad_travel_time_hhmm_costco_wholesale: _sensor_state
    syth_ipad_travel_time_hhmm_superstore: _sensor_state
    syth_ipad_travel_time_hhmm_the_home_depot_south: _sensor_state
    syth_ipad_travel_time_hhmm_wallmart_north: _sensor_state
    syth_ipad_travel_time_hhmm_wallmart_south: _sensor_state
    syth_ipad_travel_time_hhmm_home: _sensor_state
    syth_ipad_travel_time_costco_wholesale: _sensor_state
    syth_ipad_travel_time_superstore: _sensor_state
    syth_ipad_travel_time_the_home_depot_south: _sensor_state
    syth_ipad_travel_time_wallmart_north: _sensor_state
    syth_ipad_travel_time_wallmart_south: _sensor_state
    syth_ipad_travel_time_home: _sensor_state
    syth_ipad_dir_of_travel_costco_wholesale: _sensor_state
    syth_ipad_dir_of_travel_superstore: _sensor_state
    syth_ipad_dir_of_travel_the_home_depot_south: _sensor_state
    syth_ipad_dir_of_travel_wallmart_north: _sensor_state
    syth_ipad_dir_of_travel_wallmart_south: _sensor_state
    syth_ipad_dir_of_travel_home: _sensor_state
    syth_ipad_zone_distance_costco_wholesale: _sensor_state
    syth_ipad_zone_distance_superstore: _sensor_state
    syth_ipad_zone_distance_the_home_depot_south: _sensor_state
    syth_ipad_zone_distance_wallmart_north: _sensor_state
    syth_ipad_zone_distance_wallmart_south: _sensor_state
    syth_ipad_zone_distance_home: _sensor_state
    syth_ipad_zone_info_costco_wholesale: _sensor_state
    syth_ipad_zone_info_superstore: _sensor_state
    syth_ipad_zone_info_the_home_depot_south: _sensor_state
    syth_ipad_zone_info_wallmart_north: _sensor_state
    syth_ipad_zone_info_wallmart_south: _sensor_state
    syth_ipad_zone_info_home: _sensor_state
    syth_ipad_travel_time_min_costco_wholesale: _sensor_state
    syth_ipad_travel_time_min_superstore: _sensor_state
    syth_ipad_travel_time_min_the_home_depot_south: _sensor_state
    syth_ipad_travel_time_min_wallmart_north: _sensor_state
    syth_ipad_travel_time_min_wallmart_south: _sensor_state
    syth_ipad_travel_time_min_home: _sensor_state
    syth_ipad_arrival_time_costco_wholesale: _sensor_state
    syth_ipad_arrival_time_superstore: _sensor_state
    syth_ipad_arrival_time_the_home_depot_south: _sensor_state
    syth_ipad_arrival_time_wallmart_north: _sensor_state
    syth_ipad_arrival_time_wallmart_south: _sensor_state
    syth_ipad_arrival_time_home: _sensor_state
    syth_floors_descended: _sensor_state
    syth_distance: _sensor_state
    syth_floors_ascended: _sensor_state
    syth_activity: _sensor_state
    syth_battery_level: _sensor_state
    syth_steps: _sensor_state
    syth_battery_state: _sensor_state
    syth_average_active_pace: _sensor_state
    syth_storage: _sensor_state
    syth_ssid: _sensor_state
    syth_bssid: _sensor_state
    syth_connection_type: _sensor_state
    syth_sim_1: _sensor_state
    syth_sim_2: _sensor_state
    syth_geocoded_location: _sensor_state
    syth_last_update_trigger: _sensor_state
    syth_app_version: _sensor_state
    syth_location_permission: _sensor_state
    average_temperature: _sensor_state
    average_humidity: _sensor_state
    average_wind_bearing: _sensor_state
    average_wind_speed: _sensor_state
    average_compass_direction: _sensor_state
    average_pressure: _sensor_state
    average_weather_state: _sensor_state
    syth_audio_output: _sensor_state
    average_feels_like_temperature: _sensor_state
    home_nearest_device: _sensor_state
    home_nearest_distance: _sensor_state
    home_nearest_direction_of_travel: _sensor_state
    home_ashton_distance: _sensor_state
    home_ashton_direction_of_travel: _sensor_state
    home_2_nearest_device: _sensor_state
    home_2_nearest_distance: _sensor_state
    home_2_nearest_direction_of_travel: _sensor_state
    home_2_kit_distance: _sensor_state
    home_2_kit_direction_of_travel: _sensor_state
    system_monitor_disk_free: _sensor_state
    system_monitor_disk_use: _sensor_state
    system_monitor_disk_usage: _sensor_state
    system_monitor_ipv4_address_hassio: _sensor_state
    system_monitor_ipv4_address_docker0: _sensor_state
    system_monitor_ipv4_address_lo: _sensor_state
    system_monitor_ipv6_address_hassio: _sensor_state
    system_monitor_ipv6_address_docker0: _sensor_state
    system_monitor_ipv6_address_lo: _sensor_state
    system_monitor_last_boot: _sensor_state
    system_monitor_load_15m: _sensor_state
    system_monitor_load_1m: _sensor_state
    system_monitor_load_5m: _sensor_state
    system_monitor_memory_free: _sensor_state
    system_monitor_memory_use: _sensor_state
    system_monitor_memory_usage: _sensor_state
    system_monitor_network_in_hassio: _sensor_state
    system_monitor_network_in_docker0: _sensor_state
    system_monitor_network_in_lo: _sensor_state
    system_monitor_network_out_hassio: _sensor_state
    system_monitor_network_out_docker0: _sensor_state
    system_monitor_network_out_lo: _sensor_state
    system_monitor_packets_in_hassio: _sensor_state
    system_monitor_packets_in_docker0: _sensor_state
    system_monitor_packets_in_lo: _sensor_state
    system_monitor_packets_out_hassio: _sensor_state
    system_monitor_packets_out_docker0: _sensor_state
    system_monitor_packets_out_lo: _sensor_state
    system_monitor_network_throughput_in_hassio: _sensor_state
    system_monitor_network_throughput_in_docker0: _sensor_state
    system_monitor_network_throughput_in_lo: _sensor_state
    system_monitor_network_throughput_out_hassio: _sensor_state
    system_monitor_network_throughput_out_docker0: _sensor_state
    system_monitor_network_throughput_out_lo: _sensor_state
    system_monitor_processor_use: _sensor_state
    system_monitor_processor_temperature: _sensor_state
    system_monitor_swap_free: _sensor_state
    system_monitor_swap_use: _sensor_state
    system_monitor_swap_usage: _sensor_state
    uptime: _sensor_state
    safeway_w_last_updated: _sensor_state
    gas_king_picture_butte_last_updated: _sensor_state
    costco_last_updated: _sensor_state
    esso_180_columbia_blvd_last_updated: _sensor_state
    gas_king_16th_ave_last_updated: _sensor_state
    fast_gas_last_updated: _sensor_state
    gas_king_mm_dr_last_updated: _sensor_state
    shell_scenic_dr_last_updated: _sensor_state
    alexandrerohin_home_assistant_flightradar24_discussions: _sensor_state
    baldarn_whatsapper_discussions: _sensor_state
    hass_agent_hass_agent_discussions: _sensor_state
    itzg_docker_minecraft_server_discussions: _sensor_state
    pedroslopez_whatsapp_web_js_discussions: _sensor_state
    rbrito_usbmount_discussions: _sensor_state
    seleniumbase_seleniumbase_discussions: _sensor_state
    sythsaz_core_discussions: _sensor_state
    sythsaz_hass_opnsense_discussions: _sensor_state
    sythsaz_hass_agent_discussions: _sensor_state
    sythsaz_instacart_photo_convert_discussions: _sensor_state
    yt_dlp_yt_dlp_discussions: _sensor_state
    alexandrerohin_home_assistant_flightradar24_stars: _sensor_state
    baldarn_whatsapper_stars: _sensor_state
    hass_agent_hass_agent_stars: _sensor_state
    itzg_docker_minecraft_server_stars: _sensor_state
    pedroslopez_whatsapp_web_js_stars: _sensor_state
    rbrito_usbmount_stars: _sensor_state
    seleniumbase_seleniumbase_stars: _sensor_state
    sythsaz_core_stars: _sensor_state
    sythsaz_hass_opnsense_stars: _sensor_state
    sythsaz_hass_agent_stars: _sensor_state
    sythsaz_instacart_photo_convert_stars: _sensor_state
    yt_dlp_yt_dlp_stars: _sensor_state
    alexandrerohin_home_assistant_flightradar24_watchers: _sensor_state
    baldarn_whatsapper_watchers: _sensor_state
    hass_agent_hass_agent_watchers: _sensor_state
    itzg_docker_minecraft_server_watchers: _sensor_state
    pedroslopez_whatsapp_web_js_watchers: _sensor_state
    rbrito_usbmount_watchers: _sensor_state
    seleniumbase_seleniumbase_watchers: _sensor_state
    sythsaz_core_watchers: _sensor_state
    sythsaz_hass_opnsense_watchers: _sensor_state
    sythsaz_hass_agent_watchers: _sensor_state
    sythsaz_instacart_photo_convert_watchers: _sensor_state
    yt_dlp_yt_dlp_watchers: _sensor_state
    alexandrerohin_home_assistant_flightradar24_forks: _sensor_state
    baldarn_whatsapper_forks: _sensor_state
    hass_agent_hass_agent_forks: _sensor_state
    itzg_docker_minecraft_server_forks: _sensor_state
    pedroslopez_whatsapp_web_js_forks: _sensor_state
    rbrito_usbmount_forks: _sensor_state
    seleniumbase_seleniumbase_forks: _sensor_state
    sythsaz_core_forks: _sensor_state
    sythsaz_hass_opnsense_forks: _sensor_state
    sythsaz_hass_agent_forks: _sensor_state
    sythsaz_instacart_photo_convert_forks: _sensor_state
    yt_dlp_yt_dlp_forks: _sensor_state
    alexandrerohin_home_assistant_flightradar24_issues: _sensor_state
    baldarn_whatsapper_issues: _sensor_state
    hass_agent_hass_agent_issues: _sensor_state
    itzg_docker_minecraft_server_issues: _sensor_state
    pedroslopez_whatsapp_web_js_issues: _sensor_state
    rbrito_usbmount_issues: _sensor_state
    seleniumbase_seleniumbase_issues: _sensor_state
    sythsaz_core_issues: _sensor_state
    sythsaz_hass_opnsense_issues: _sensor_state
    sythsaz_hass_agent_issues: _sensor_state
    sythsaz_instacart_photo_convert_issues: _sensor_state
    yt_dlp_yt_dlp_issues: _sensor_state
    alexandrerohin_home_assistant_flightradar24_pull_requests: _sensor_state
    baldarn_whatsapper_pull_requests: _sensor_state
    hass_agent_hass_agent_pull_requests: _sensor_state
    itzg_docker_minecraft_server_pull_requests: _sensor_state
    pedroslopez_whatsapp_web_js_pull_requests: _sensor_state
    rbrito_usbmount_pull_requests: _sensor_state
    seleniumbase_seleniumbase_pull_requests: _sensor_state
    sythsaz_core_pull_requests: _sensor_state
    sythsaz_hass_opnsense_pull_requests: _sensor_state
    sythsaz_hass_agent_pull_requests: _sensor_state
    sythsaz_instacart_photo_convert_pull_requests: _sensor_state
    yt_dlp_yt_dlp_pull_requests: _sensor_state
    alexandrerohin_home_assistant_flightradar24_latest_commit: _sensor_state
    baldarn_whatsapper_latest_commit: _sensor_state
    hass_agent_hass_agent_latest_commit: _sensor_state
    itzg_docker_minecraft_server_latest_commit: _sensor_state
    pedroslopez_whatsapp_web_js_latest_commit: _sensor_state
    rbrito_usbmount_latest_commit: _sensor_state
    seleniumbase_seleniumbase_latest_commit: _sensor_state
    sythsaz_core_latest_commit: _sensor_state
    sythsaz_hass_opnsense_latest_commit: _sensor_state
    sythsaz_hass_agent_latest_commit: _sensor_state
    sythsaz_instacart_photo_convert_latest_commit: _sensor_state
    yt_dlp_yt_dlp_latest_commit: _sensor_state
    alexandrerohin_home_assistant_flightradar24_latest_discussion: _sensor_state
    baldarn_whatsapper_latest_discussion: _sensor_state
    hass_agent_hass_agent_latest_discussion: _sensor_state
    itzg_docker_minecraft_server_latest_discussion: _sensor_state
    pedroslopez_whatsapp_web_js_latest_discussion: _sensor_state
    rbrito_usbmount_latest_discussion: _sensor_state
    seleniumbase_seleniumbase_latest_discussion: _sensor_state
    sythsaz_core_latest_discussion: _sensor_state
    sythsaz_hass_opnsense_latest_discussion: _sensor_state
    sythsaz_hass_agent_latest_discussion: _sensor_state
    sythsaz_instacart_photo_convert_latest_discussion: _sensor_state
    yt_dlp_yt_dlp_latest_discussion: _sensor_state
    alexandrerohin_home_assistant_flightradar24_latest_release: _sensor_state
    baldarn_whatsapper_latest_release: _sensor_state
    hass_agent_hass_agent_latest_release: _sensor_state
    itzg_docker_minecraft_server_latest_release: _sensor_state
    pedroslopez_whatsapp_web_js_latest_release: _sensor_state
    rbrito_usbmount_latest_release: _sensor_state
    seleniumbase_seleniumbase_latest_release: _sensor_state
    sythsaz_core_latest_release: _sensor_state
    sythsaz_hass_opnsense_latest_release: _sensor_state
    sythsaz_hass_agent_latest_release: _sensor_state
    sythsaz_instacart_photo_convert_latest_release: _sensor_state
    yt_dlp_yt_dlp_latest_release: _sensor_state
    alexandrerohin_home_assistant_flightradar24_latest_issue: _sensor_state
    baldarn_whatsapper_latest_issue: _sensor_state
    hass_agent_hass_agent_latest_issue: _sensor_state
    itzg_docker_minecraft_server_latest_issue: _sensor_state
    pedroslopez_whatsapp_web_js_latest_issue: _sensor_state
    rbrito_usbmount_latest_issue: _sensor_state
    seleniumbase_seleniumbase_latest_issue: _sensor_state
    sythsaz_core_latest_issue: _sensor_state
    sythsaz_hass_opnsense_latest_issue: _sensor_state
    sythsaz_hass_agent_latest_issue: _sensor_state
    sythsaz_instacart_photo_convert_latest_issue: _sensor_state
    yt_dlp_yt_dlp_latest_issue: _sensor_state
    alexandrerohin_home_assistant_flightradar24_latest_pull_request: _sensor_state
    baldarn_whatsapper_latest_pull_request: _sensor_state
    hass_agent_hass_agent_latest_pull_request: _sensor_state
    itzg_docker_minecraft_server_latest_pull_request: _sensor_state
    pedroslopez_whatsapp_web_js_latest_pull_request: _sensor_state
    rbrito_usbmount_latest_pull_request: _sensor_state
    seleniumbase_seleniumbase_latest_pull_request: _sensor_state
    sythsaz_core_latest_pull_request: _sensor_state
    sythsaz_hass_opnsense_latest_pull_request: _sensor_state
    sythsaz_hass_agent_latest_pull_request: _sensor_state
    sythsaz_instacart_photo_convert_latest_pull_request: _sensor_state
    yt_dlp_yt_dlp_latest_pull_request: _sensor_state
    alexandrerohin_home_assistant_flightradar24_latest_tag: _sensor_state
    baldarn_whatsapper_latest_tag: _sensor_state
    hass_agent_hass_agent_latest_tag: _sensor_state
    itzg_docker_minecraft_server_latest_tag: _sensor_state
    pedroslopez_whatsapp_web_js_latest_tag: _sensor_state
    rbrito_usbmount_latest_tag: _sensor_state
    seleniumbase_seleniumbase_latest_tag: _sensor_state
    sythsaz_core_latest_tag: _sensor_state
    sythsaz_hass_opnsense_latest_tag: _sensor_state
    sythsaz_hass_agent_latest_tag: _sensor_state
    sythsaz_instacart_photo_convert_latest_tag: _sensor_state
    yt_dlp_yt_dlp_latest_tag: _sensor_state
    opnsense_expires: _sensor_state
    opnsense_ip_address: _sensor_state
    opnsense_last_seen: _sensor_state
    reservoir_data: _sensor_state
    oldman_reservoir_storage: _sensor_state
    st_mary_s_current_storage: _sensor_state
    reservoir_data_part_2: _sensor_state
    waterton_current_storage: _sensor_state
    bowhanon: _sensor_state
    bluesage8: _sensor_state
    purplegranny: _sensor_state
    raava: _sensor_state
    guildwars2: _sensor_state
    artyotv: _sensor_state
    emeraldjpg: _sensor_state
    hagridtx: _sensor_state
    tofa_sedai: _sensor_state
    projektdyad: _sensor_state
    linustech: _sensor_state
    lavaslug: _sensor_state
    perfectdee: _sensor_state
    master_liu: _sensor_state
    kunaives: _sensor_state
    taja: _sensor_state
    paleontologizing: _sensor_state
    chipichipicchapachapa: _sensor_state
    shazilee: _sensor_state
    scubasheeves: _sensor_state
    emidotexe: _sensor_state
    vampyreneko93: _sensor_state
    connorconcarne: _sensor_state
    shadowy_figure: _sensor_state
    elajjaz: _sensor_state
    itskiyoshi: _sensor_state
    hellmasker: _sensor_state
    vallun: _sensor_state
    laranity: _sensor_state
    apejunk: _sensor_state
    elr3n1a: _sensor_state
    exosgoddess: _sensor_state
    cellofrag: _sensor_state
    desktop_u5e7nrv_expires: _sensor_state
    desktop_u5e7nrv_ip_address: _sensor_state
    desktop_u5e7nrv_last_seen: _sensor_state
    darenswiths: _sensor_state
    irbaw: _sensor_state
    tramadex: _sensor_state
    sir_lsd: _sensor_state
    exitim: _sensor_state
    awesumness: _sensor_state
    simplytwo: _sensor_state
    idominatedu: _sensor_state
    connorcarbonara: _sensor_state
    axylcross: _sensor_state
    fireballannie: _sensor_state
    tiffymisswiffy: _sensor_state
    grimjacke: _sensor_state
    sythsaz: _sensor_state
    streamelements: _sensor_state
    sangka: _sensor_state
    acrazy86: _sensor_state
    ragnarokevent: _sensor_state
    wombatwaazy: _sensor_state
    samaelletzin: _sensor_state
    rachroyaleforgot: _sensor_state
    foxbelle: _sensor_state
    system_monitor_ipv4_address_enp0s25: _sensor_state
    system_monitor_ipv6_address_enp0s25: _sensor_state
    system_monitor_network_in_enp0s25: _sensor_state
    system_monitor_network_out_enp0s25: _sensor_state
    system_monitor_packets_in_enp0s25: _sensor_state
    system_monitor_packets_out_enp0s25: _sensor_state
    system_monitor_network_throughput_in_enp0s25: _sensor_state
    system_monitor_network_throughput_out_enp0s25: _sensor_state
    backup_backup_manager_state: _sensor_state
    backup_next_scheduled_automatic_backup: _sensor_state
    backup_last_successful_automatic_backup: _sensor_state
    average_precipitation_amount: _sensor_state
    open_weather_map_precipitation_kind_string: _sensor_state
    average_precipitation_kind: _sensor_state
    stovetop_signal_strength: _sensor_state
    furnace_room_1_signal_strength: _sensor_state
    understairs_closet_signal_strength: _sensor_state
    furnace_room_2_signal_strength: _sensor_state
    bedside_lamp_signal_strength: _sensor_state
    bedroom_closet_signal_strength: _sensor_state
    outside_signal_strength: _sensor_state
    aurora_visibility: _sensor_state
    debian_dell_expires: _sensor_state
    debian_dell_ip_address: _sensor_state
    debian_dell_last_seen: _sensor_state
    system_monitor_ipv4_address_tailscale0: _sensor_state
    system_monitor_ipv6_address_tailscale0: _sensor_state
    system_monitor_network_in_tailscale0: _sensor_state
    system_monitor_network_out_tailscale0: _sensor_state
    system_monitor_packets_in_tailscale0: _sensor_state
    system_monitor_packets_out_tailscale0: _sensor_state
    system_monitor_network_throughput_in_tailscale0: _sensor_state
    system_monitor_network_throughput_out_tailscale0: _sensor_state
    backup_last_attempted_automatic_backup: _sensor_state
    opnsense_pf_state_table_used: _sensor_state
    opnsense_pf_state_table_total: _sensor_state
    opnsense_pf_state_table_used_percentage: _sensor_state
    opnsense_memory_buffers_used: _sensor_state
    opnsense_memory_buffers_total: _sensor_state
    opnsense_memory_buffers_used_percentage: _sensor_state
    opnsense_memory_swap_reserved: _sensor_state
    opnsense_memory_physmem: _sensor_state
    opnsense_memory_used: _sensor_state
    opnsense_memory_swap_total: _sensor_state
    opnsense_memory_swap_used_percentage: _sensor_state
    opnsense_memory_used_percentage: _sensor_state
    opnsense_cpu_count: _sensor_state
    opnsense_cpu_usage: _sensor_state
    opnsense_system_load_average_one_minute: _sensor_state
    opnsense_system_load_average_five_minute: _sensor_state
    opnsense_system_load_average_fifteen_minute: _sensor_state
    opnsense_system_boottime: _sensor_state
    opnsense_certificates: _sensor_state
    opnsense_gateway_wan_dhcp6_status: _sensor_state
    opnsense_gateway_wan_dhcp6_delay: _sensor_state
    opnsense_gateway_wan_dhcp6_stddev: _sensor_state
    opnsense_gateway_wan_dhcp6_loss: _sensor_state
    opnsense_gateway_wan_dhcp_status: _sensor_state
    opnsense_gateway_wan_dhcp_delay: _sensor_state
    opnsense_gateway_wan_dhcp_stddev: _sensor_state
    opnsense_gateway_wan_dhcp_loss: _sensor_state
    opnsense_gateway_nordvpn_vpnv6_status: _sensor_state
    opnsense_gateway_nordvpn_vpnv6_delay: _sensor_state
    opnsense_gateway_nordvpn_vpnv6_stddev: _sensor_state
    opnsense_gateway_nordvpn_vpnv6_loss: _sensor_state
    opnsense_gateway_nordvpn_vpnv4_status: _sensor_state
    opnsense_gateway_nordvpn_vpnv4_delay: _sensor_state
    opnsense_gateway_nordvpn_vpnv4_stddev: _sensor_state
    opnsense_gateway_nordvpn_vpnv4_loss: _sensor_state
    opnsense_gateway_wan_gw_status: _sensor_state
    opnsense_gateway_wan_gw_delay: _sensor_state
    opnsense_gateway_wan_gw_stddev: _sensor_state
    opnsense_gateway_wan_gw_loss: _sensor_state
    opnsense_interface_lan_status: _sensor_state
    opnsense_interface_lan_inerrs: _sensor_state
    opnsense_interface_lan_outerrs: _sensor_state
    opnsense_interface_lan_collisions: _sensor_state
    opnsense_interface_lan_inbytes: _sensor_state
    opnsense_interface_lan_inbytes_kilobytes_per_second: _sensor_state
    opnsense_interface_lan_outbytes: _sensor_state
    opnsense_interface_lan_outbytes_kilobytes_per_second: _sensor_state
    opnsense_interface_lan_inpkts: _sensor_state
    opnsense_interface_lan_inpkts_packets_per_second: _sensor_state
    opnsense_interface_lan_outpkts: _sensor_state
    opnsense_interface_lan_outpkts_packets_per_second: _sensor_state
    opnsense_interface_wan_status: _sensor_state
    opnsense_interface_wan_inerrs: _sensor_state
    opnsense_interface_wan_outerrs: _sensor_state
    opnsense_interface_wan_collisions: _sensor_state
    opnsense_interface_wan_inbytes: _sensor_state
    opnsense_interface_wan_inbytes_kilobytes_per_second: _sensor_state
    opnsense_interface_wan_outbytes: _sensor_state
    opnsense_interface_wan_outbytes_kilobytes_per_second: _sensor_state
    opnsense_interface_wan_inpkts: _sensor_state
    opnsense_interface_wan_inpkts_packets_per_second: _sensor_state
    opnsense_interface_wan_outpkts: _sensor_state
    opnsense_interface_wan_outpkts_packets_per_second: _sensor_state
    opnsense_interface_loopback_status: _sensor_state
    opnsense_interface_loopback_inerrs: _sensor_state
    opnsense_interface_loopback_outerrs: _sensor_state
    opnsense_interface_loopback_collisions: _sensor_state
    opnsense_interface_loopback_inbytes: _sensor_state
    opnsense_interface_loopback_inbytes_kilobytes_per_second: _sensor_state
    opnsense_interface_loopback_outbytes: _sensor_state
    opnsense_interface_loopback_outbytes_kilobytes_per_second: _sensor_state
    opnsense_interface_loopback_inpkts: _sensor_state
    opnsense_interface_loopback_inpkts_packets_per_second: _sensor_state
    opnsense_interface_loopback_outpkts: _sensor_state
    opnsense_interface_loopback_outpkts_packets_per_second: _sensor_state
    opnsense_interface_nordvpn_status: _sensor_state
    opnsense_interface_nordvpn_inerrs: _sensor_state
    opnsense_interface_nordvpn_outerrs: _sensor_state
    opnsense_interface_nordvpn_collisions: _sensor_state
    opnsense_interface_nordvpn_inbytes: _sensor_state
    opnsense_interface_nordvpn_inbytes_kilobytes_per_second: _sensor_state
    opnsense_interface_nordvpn_outbytes: _sensor_state
    opnsense_interface_nordvpn_outbytes_kilobytes_per_second: _sensor_state
    opnsense_interface_nordvpn_inpkts: _sensor_state
    opnsense_interface_nordvpn_inpkts_packets_per_second: _sensor_state
    opnsense_interface_nordvpn_outpkts: _sensor_state
    opnsense_interface_nordvpn_outpkts_packets_per_second: _sensor_state
    opnsense_interface_opt1_status: _sensor_state
    opnsense_interface_opt1_inerrs: _sensor_state
    opnsense_interface_opt1_outerrs: _sensor_state
    opnsense_interface_opt1_collisions: _sensor_state
    opnsense_interface_opt1_inbytes: _sensor_state
    opnsense_interface_opt1_inbytes_kilobytes_per_second: _sensor_state
    opnsense_interface_opt1_outbytes: _sensor_state
    opnsense_interface_opt1_outbytes_kilobytes_per_second: _sensor_state
    opnsense_interface_opt1_inpkts: _sensor_state
    opnsense_interface_opt1_inpkts_packets_per_second: _sensor_state
    opnsense_interface_opt1_outpkts: _sensor_state
    opnsense_interface_opt1_outpkts_packets_per_second: _sensor_state
    opnsense_filesystem_used_percentage_root: _sensor_state
    opnsense_filesystem_used_percentage_boot_efi: _sensor_state
    opnsense_temp_cpu_0: _sensor_state
    opnsense_temp_cpu_1: _sensor_state
    opnsense_temp_cpu_2: _sensor_state
    opnsense_temp_cpu_3: _sensor_state
    opnsense_dhcp_leases_lan: _sensor_state
    opnsense_dhcp_leases_all: _sensor_state
    imap_ashtonparrott_gmail_com_messages: _sensor_state
    mastodon_sythsaz_mastodon_social_followers: _sensor_state
    mastodon_sythsaz_mastodon_social_following: _sensor_state
    mastodon_sythsaz_mastodon_social_posts: _sensor_state
    imap_kitara_omand_gmail_com_messages: _sensor_state
    opnsense_wan_out_errors_statistics: _sensor_state
    opnsense_wan_collisions_statistics: _sensor_state
    opnsense_nord_vpn_in_errors_statistics: _sensor_state
    opnsense_nord_vpn_out_errors_statistics: _sensor_state
    opnsense_nord_vpn_collisions_statistics: _sensor_state
    opnsense_lan_in_errors_statistics: _sensor_state
    opnsense_lan_out_errors_statistics: _sensor_state
    opnsense_wan_in_errors_statistics: _sensor_state
    opnsense_lan_collisions_statistics: _sensor_state
    london_england: _sensor_state
    hongkong_china: _sensor_state
    japan: _sensor_state
    ythsaz_trophy_level: _sensor_state
    ythsaz_next_level: _sensor_state
    ythsaz_platinum_trophies: _sensor_state
    ythsaz_gold_trophies: _sensor_state
    ythsaz_silver_trophies: _sensor_state
    ythsaz_bronze_trophies: _sensor_state
    ythsaz_online_id: _sensor_state
    guild_wars_2_server_time: _sensor_state
    gw2_reset_monday: _sensor_state
    monday_reset_list_1: _sensor_state
    monday_reset_list_0: _sensor_state
    monday_reset_list_2: _sensor_state
    monday_reset_list_3: _sensor_state
    monday_reset_list_4: _sensor_state
    monday_reset_list_5: _sensor_state
    monday_reset_list_6: _sensor_state
    monday_reset_list_7: _sensor_state
    monday_reset_list_8: _sensor_state
    monday_reset_list_9: _sensor_state
    monday_reset_list_10: _sensor_state
    monday_reset_list_11: _sensor_state
    monday_reset_list_12: _sensor_state
    monday_reset_list_13: _sensor_state
    monday_reset_list_14: _sensor_state
    monday_reset_list_15: _sensor_state
    thursday_reset: _sensor_state
    thursday_reset_text: _sensor_state
    wvw_eu_reset: _sensor_state
    wvw_eu_reset_text: _sensor_state
    wvw_reset_na: _sensor_state
    wvw_na_reset_text: _sensor_state
    achievements_0: _sensor_state
    achievements_1: _sensor_state
    achievements_2: _sensor_state
    achievements_3: _sensor_state
    achievements_4: _sensor_state
    achievements_5: _sensor_state
    achievements_6: _sensor_state
    achievements_7: _sensor_state
    achievements_8: _sensor_state
    achievements_9: _sensor_state
    achievements_10: _sensor_state
    achievements_11: _sensor_state
    achievements_reset: _sensor_state
    special_events_reset: _sensor_state
    special_events_0: _sensor_state
    special_events_1: _sensor_state
    special_events_2: _sensor_state
    special_events_3: _sensor_state
    special_events_4: _sensor_state
    special_events_5: _sensor_state
    special_events_6: _sensor_state
    notes_0: _sensor_state
    notes_1: _sensor_state
    notes_2: _sensor_state
    sun_next_dawn: _sensor_state
    sun_next_dusk: _sensor_state
    sun_next_midnight: _sensor_state
    sun_next_noon: _sensor_state
    sun_next_rising: _sensor_state
    sun_next_setting: _sensor_state
    sun_solar_elevation: _sensor_state
    sun_solar_azimuth: _sensor_state
    next_waste_collection: _sensor_state
    upcoming_waste_collection_justice: _sensor_state
    icloud3_alerts: _sensor_state
    kierea_sparks: _sensor_state
    date_time_iso: _sensor_state
    date_time_utc: _sensor_state
    date_time: _sensor_state
    ashton_osm: _sensor_state
    steam_wishlist_76561198025675241: _sensor_state
    gas_plus_last_updated: _sensor_state
    gas_plus_regular_gas: _sensor_state
    gas_plus_midgrade_gas: _sensor_state
    gas_plus_premium_gas: _sensor_state
    living_room_device: _sensor_state
    living_room_alarms: _sensor_state
    living_room_timers: _sensor_state
    livingroom_tv_device: _sensor_state
    bathroom_device: _sensor_state
    bathroom_alarms: _sensor_state
    bathroom_timers: _sensor_state
    bedroom_speaker_device: _sensor_state
    bedroom_speaker_alarms: _sensor_state
    bedroom_speaker_timers: _sensor_state
    pirateweather_summary: _sensor_state
    pirateweather_precip: _sensor_state
    pirateweather_precip_intensity: _sensor_state
    pirateweather_precip_probability: _sensor_state
    pirateweather_temperature: _sensor_state
    pirateweather_apparent_temperature: _sensor_state
    pirateweather_dew_point: _sensor_state
    pirateweather_humidity: _sensor_state
    pirateweather_wind_speed: _sensor_state
    pirateweather_wind_gust: _sensor_state
    pirateweather_wind_bearing: _sensor_state
    pirateweather_cloud_coverage: _sensor_state
    pirateweather_pressure: _sensor_state
    pirateweather_visibility: _sensor_state
    pirateweather_ozone: _sensor_state
    pirateweather_minutely_summary: _sensor_state
    pirateweather_hourly_summary: _sensor_state
    pirateweather_daily_summary: _sensor_state
    pirateweather_uv_index: _sensor_state
    pirateweather_nearest_storm_distance: _sensor_state
    pirateweather_alerts: _sensor_state
    pirateweather_nearest_storm_bearing: _sensor_state
    pirateweather_time: _sensor_state
    pirateweather_fire_index: _sensor_state
    pirateweather_fire_risk_level: _sensor_state
    pirateweather_smoke: _sensor_state
    pirateweather_hrrr_subhourly_update_time: _sensor_state
    pirateweather_hrrr_0_18_update_time: _sensor_state
    pirateweather_nbm_update_time: _sensor_state
    pirateweather_nbm_fire_update_time: _sensor_state
    pirateweather_hrrr_18_48_update_time: _sensor_state
    pirateweather_gfs_update_time: _sensor_state
    pirateweather_gefs_update_time: _sensor_state
    pirateweather_current_day_liquid_accumulation: _sensor_state
    pirateweather_current_day_snow_accumulation: _sensor_state
    pirateweather_current_day_ice_accumulation: _sensor_state
    pirateweather_summary_0d: _sensor_state
    pirateweather_summary_1d: _sensor_state
    pirateweather_summary_2d: _sensor_state
    pirateweather_summary_3d: _sensor_state
    pirateweather_summary_4d: _sensor_state
    pirateweather_summary_5d: _sensor_state
    pirateweather_summary_6d: _sensor_state
    pirateweather_summary_0h: _sensor_state
    pirateweather_summary_1h: _sensor_state
    pirateweather_summary_2h: _sensor_state
    pirateweather_summary_3h: _sensor_state
    pirateweather_summary_4h: _sensor_state
    pirateweather_summary_5h: _sensor_state
    pirateweather_summary_6h: _sensor_state
    pirateweather_summary_7h: _sensor_state
    pirateweather_summary_8h: _sensor_state
    pirateweather_summary_9h: _sensor_state
    pirateweather_summary_11h: _sensor_state
    pirateweather_summary_12h: _sensor_state
    pirateweather_precip_0d: _sensor_state
    pirateweather_precip_1d: _sensor_state
    pirateweather_precip_2d: _sensor_state
    pirateweather_precip_3d: _sensor_state
    pirateweather_precip_4d: _sensor_state
    pirateweather_precip_5d: _sensor_state
    pirateweather_precip_6d: _sensor_state
    pirateweather_precip_0h: _sensor_state
    pirateweather_precip_1h: _sensor_state
    pirateweather_precip_2h: _sensor_state
    pirateweather_precip_3h: _sensor_state
    pirateweather_precip_4h: _sensor_state
    pirateweather_precip_5h: _sensor_state
    pirateweather_precip_6h: _sensor_state
    pirateweather_precip_7h: _sensor_state
    pirateweather_precip_8h: _sensor_state
    pirateweather_precip_9h: _sensor_state
    pirateweather_precip_11h: _sensor_state
    pirateweather_precip_12h: _sensor_state
    pirateweather_precip_intensity_0d: _sensor_state
    pirateweather_precip_intensity_1d: _sensor_state
    pirateweather_precip_intensity_2d: _sensor_state
    pirateweather_precip_intensity_3d: _sensor_state
    pirateweather_precip_intensity_4d: _sensor_state
    pirateweather_precip_intensity_5d: _sensor_state
    pirateweather_precip_intensity_6d: _sensor_state
    pirateweather_precip_intensity_0h: _sensor_state
    pirateweather_precip_intensity_1h: _sensor_state
    pirateweather_precip_intensity_2h: _sensor_state
    pirateweather_precip_intensity_3h: _sensor_state
    pirateweather_precip_intensity_4h: _sensor_state
    pirateweather_precip_intensity_5h: _sensor_state
    pirateweather_precip_intensity_6h: _sensor_state
    pirateweather_precip_intensity_7h: _sensor_state
    pirateweather_precip_intensity_8h: _sensor_state
    pirateweather_precip_intensity_9h: _sensor_state
    pirateweather_precip_intensity_11h: _sensor_state
    pirateweather_precip_intensity_12h: _sensor_state
    pirateweather_precip_probability_0d: _sensor_state
    pirateweather_precip_probability_1d: _sensor_state
    pirateweather_precip_probability_2d: _sensor_state
    pirateweather_precip_probability_3d: _sensor_state
    pirateweather_precip_probability_4d: _sensor_state
    pirateweather_precip_probability_5d: _sensor_state
    pirateweather_precip_probability_6d: _sensor_state
    pirateweather_precip_probability_0h: _sensor_state
    pirateweather_precip_probability_1h: _sensor_state
    pirateweather_precip_probability_2h: _sensor_state
    pirateweather_precip_probability_3h: _sensor_state
    pirateweather_precip_probability_4h: _sensor_state
    pirateweather_precip_probability_5h: _sensor_state
    pirateweather_precip_probability_6h: _sensor_state
    pirateweather_precip_probability_7h: _sensor_state
    pirateweather_precip_probability_8h: _sensor_state
    pirateweather_precip_probability_9h: _sensor_state
    pirateweather_precip_probability_11h: _sensor_state
    pirateweather_precip_probability_12h: _sensor_state
    pirateweather_precip_accumulation_0d: _sensor_state
    pirateweather_precip_accumulation_1d: _sensor_state
    pirateweather_precip_accumulation_2d: _sensor_state
    pirateweather_precip_accumulation_3d: _sensor_state
    pirateweather_precip_accumulation_4d: _sensor_state
    pirateweather_precip_accumulation_5d: _sensor_state
    pirateweather_precip_accumulation_6d: _sensor_state
    pirateweather_precip_accumulation_0h: _sensor_state
    pirateweather_precip_accumulation_1h: _sensor_state
    pirateweather_precip_accumulation_2h: _sensor_state
    pirateweather_precip_accumulation_3h: _sensor_state
    pirateweather_precip_accumulation_4h: _sensor_state
    pirateweather_precip_accumulation_5h: _sensor_state
    pirateweather_precip_accumulation_6h: _sensor_state
    pirateweather_precip_accumulation_7h: _sensor_state
    pirateweather_precip_accumulation_8h: _sensor_state
    pirateweather_precip_accumulation_9h: _sensor_state
    pirateweather_precip_accumulation_11h: _sensor_state
    pirateweather_precip_accumulation_12h: _sensor_state
    pirateweather_temperature_0h: _sensor_state
    pirateweather_temperature_1h: _sensor_state
    pirateweather_temperature_2h: _sensor_state
    pirateweather_temperature_3h: _sensor_state
    pirateweather_temperature_4h: _sensor_state
    pirateweather_temperature_5h: _sensor_state
    pirateweather_temperature_6h: _sensor_state
    pirateweather_temperature_7h: _sensor_state
    pirateweather_temperature_8h: _sensor_state
    pirateweather_temperature_9h: _sensor_state
    pirateweather_temperature_11h: _sensor_state
    pirateweather_temperature_12h: _sensor_state
    pirateweather_apparent_temperature_0h: _sensor_state
    pirateweather_apparent_temperature_1h: _sensor_state
    pirateweather_apparent_temperature_2h: _sensor_state
    pirateweather_apparent_temperature_3h: _sensor_state
    pirateweather_apparent_temperature_4h: _sensor_state
    pirateweather_apparent_temperature_5h: _sensor_state
    pirateweather_apparent_temperature_6h: _sensor_state
    pirateweather_apparent_temperature_7h: _sensor_state
    pirateweather_apparent_temperature_8h: _sensor_state
    pirateweather_apparent_temperature_9h: _sensor_state
    pirateweather_apparent_temperature_11h: _sensor_state
    pirateweather_apparent_temperature_12h: _sensor_state
    pirateweather_dew_point_0d: _sensor_state
    pirateweather_dew_point_1d: _sensor_state
    pirateweather_dew_point_2d: _sensor_state
    pirateweather_dew_point_3d: _sensor_state
    pirateweather_dew_point_4d: _sensor_state
    pirateweather_dew_point_5d: _sensor_state
    pirateweather_dew_point_6d: _sensor_state
    pirateweather_dew_point_0h: _sensor_state
    pirateweather_dew_point_1h: _sensor_state
    pirateweather_dew_point_2h: _sensor_state
    pirateweather_dew_point_3h: _sensor_state
    pirateweather_dew_point_4h: _sensor_state
    pirateweather_dew_point_5h: _sensor_state
    pirateweather_dew_point_6h: _sensor_state
    pirateweather_dew_point_7h: _sensor_state
    pirateweather_dew_point_8h: _sensor_state
    pirateweather_dew_point_9h: _sensor_state
    pirateweather_dew_point_11h: _sensor_state
    pirateweather_dew_point_12h: _sensor_state
    pirateweather_humidity_0d: _sensor_state
    pirateweather_humidity_1d: _sensor_state
    pirateweather_humidity_2d: _sensor_state
    pirateweather_humidity_3d: _sensor_state
    pirateweather_humidity_4d: _sensor_state
    pirateweather_humidity_5d: _sensor_state
    pirateweather_humidity_6d: _sensor_state
    pirateweather_humidity_0h: _sensor_state
    pirateweather_humidity_1h: _sensor_state
    pirateweather_humidity_2h: _sensor_state
    pirateweather_humidity_3h: _sensor_state
    pirateweather_humidity_4h: _sensor_state
    pirateweather_humidity_5h: _sensor_state
    pirateweather_humidity_6h: _sensor_state
    pirateweather_humidity_7h: _sensor_state
    pirateweather_humidity_8h: _sensor_state
    pirateweather_humidity_9h: _sensor_state
    pirateweather_humidity_11h: _sensor_state
    pirateweather_humidity_12h: _sensor_state
    pirateweather_wind_speed_0d: _sensor_state
    pirateweather_wind_speed_1d: _sensor_state
    pirateweather_wind_speed_2d: _sensor_state
    pirateweather_wind_speed_3d: _sensor_state
    pirateweather_wind_speed_4d: _sensor_state
    pirateweather_wind_speed_5d: _sensor_state
    pirateweather_wind_speed_6d: _sensor_state
    pirateweather_wind_speed_0h: _sensor_state
    pirateweather_wind_speed_1h: _sensor_state
    pirateweather_wind_speed_2h: _sensor_state
    pirateweather_wind_speed_3h: _sensor_state
    pirateweather_wind_speed_4h: _sensor_state
    pirateweather_wind_speed_5h: _sensor_state
    pirateweather_wind_speed_6h: _sensor_state
    pirateweather_wind_speed_7h: _sensor_state
    pirateweather_wind_speed_8h: _sensor_state
    pirateweather_wind_speed_9h: _sensor_state
    pirateweather_wind_speed_11h: _sensor_state
    pirateweather_wind_speed_12h: _sensor_state
    pirateweather_wind_gust_0d: _sensor_state
    pirateweather_wind_gust_1d: _sensor_state
    pirateweather_wind_gust_2d: _sensor_state
    pirateweather_wind_gust_3d: _sensor_state
    pirateweather_wind_gust_4d: _sensor_state
    pirateweather_wind_gust_5d: _sensor_state
    pirateweather_wind_gust_6d: _sensor_state
    pirateweather_wind_gust_0h: _sensor_state
    pirateweather_wind_gust_1h: _sensor_state
    pirateweather_wind_gust_2h: _sensor_state
    pirateweather_wind_gust_3h: _sensor_state
    pirateweather_wind_gust_4h: _sensor_state
    pirateweather_wind_gust_5h: _sensor_state
    pirateweather_wind_gust_6h: _sensor_state
    pirateweather_wind_gust_7h: _sensor_state
    pirateweather_wind_gust_8h: _sensor_state
    pirateweather_wind_gust_9h: _sensor_state
    pirateweather_wind_gust_11h: _sensor_state
    pirateweather_wind_gust_12h: _sensor_state
    pirateweather_wind_bearing_0d: _sensor_state
    pirateweather_wind_bearing_1d: _sensor_state
    pirateweather_wind_bearing_2d: _sensor_state
    pirateweather_wind_bearing_3d: _sensor_state
    pirateweather_wind_bearing_4d: _sensor_state
    pirateweather_wind_bearing_5d: _sensor_state
    pirateweather_wind_bearing_6d: _sensor_state
    pirateweather_wind_bearing_0h: _sensor_state
    pirateweather_wind_bearing_1h: _sensor_state
    pirateweather_wind_bearing_2h: _sensor_state
    pirateweather_wind_bearing_3h: _sensor_state
    pirateweather_wind_bearing_4h: _sensor_state
    pirateweather_wind_bearing_5h: _sensor_state
    pirateweather_wind_bearing_6h: _sensor_state
    pirateweather_wind_bearing_7h: _sensor_state
    pirateweather_wind_bearing_8h: _sensor_state
    pirateweather_wind_bearing_9h: _sensor_state
    pirateweather_wind_bearing_11h: _sensor_state
    pirateweather_wind_bearing_12h: _sensor_state
    pirateweather_cloud_coverage_0d: _sensor_state
    pirateweather_cloud_coverage_1d: _sensor_state
    pirateweather_cloud_coverage_2d: _sensor_state
    pirateweather_cloud_coverage_3d: _sensor_state
    pirateweather_cloud_coverage_4d: _sensor_state
    pirateweather_cloud_coverage_5d: _sensor_state
    pirateweather_cloud_coverage_6d: _sensor_state
    pirateweather_cloud_coverage_0h: _sensor_state
    pirateweather_cloud_coverage_1h: _sensor_state
    pirateweather_cloud_coverage_2h: _sensor_state
    pirateweather_cloud_coverage_3h: _sensor_state
    pirateweather_cloud_coverage_4h: _sensor_state
    pirateweather_cloud_coverage_5h: _sensor_state
    pirateweather_cloud_coverage_6h: _sensor_state
    pirateweather_cloud_coverage_7h: _sensor_state
    pirateweather_cloud_coverage_8h: _sensor_state
    pirateweather_cloud_coverage_9h: _sensor_state
    pirateweather_cloud_coverage_11h: _sensor_state
    pirateweather_cloud_coverage_12h: _sensor_state
    pirateweather_pressure_0d: _sensor_state
    pirateweather_pressure_1d: _sensor_state
    pirateweather_pressure_2d: _sensor_state
    pirateweather_pressure_3d: _sensor_state
    pirateweather_pressure_4d: _sensor_state
    pirateweather_pressure_5d: _sensor_state
    pirateweather_pressure_6d: _sensor_state
    pirateweather_pressure_0h: _sensor_state
    pirateweather_pressure_1h: _sensor_state
    pirateweather_pressure_2h: _sensor_state
    pirateweather_pressure_3h: _sensor_state
    pirateweather_pressure_4h: _sensor_state
    pirateweather_pressure_5h: _sensor_state
    pirateweather_pressure_6h: _sensor_state
    pirateweather_pressure_7h: _sensor_state
    pirateweather_pressure_8h: _sensor_state
    pirateweather_pressure_9h: _sensor_state
    pirateweather_pressure_11h: _sensor_state
    pirateweather_pressure_12h: _sensor_state
    pirateweather_visibility_0d: _sensor_state
    pirateweather_visibility_1d: _sensor_state
    pirateweather_visibility_2d: _sensor_state
    pirateweather_visibility_3d: _sensor_state
    pirateweather_visibility_4d: _sensor_state
    pirateweather_visibility_5d: _sensor_state
    pirateweather_visibility_6d: _sensor_state
    pirateweather_visibility_0h: _sensor_state
    pirateweather_visibility_1h: _sensor_state
    pirateweather_visibility_2h: _sensor_state
    pirateweather_visibility_3h: _sensor_state
    pirateweather_visibility_4h: _sensor_state
    pirateweather_visibility_5h: _sensor_state
    pirateweather_visibility_6h: _sensor_state
    pirateweather_visibility_7h: _sensor_state
    pirateweather_visibility_8h: _sensor_state
    pirateweather_visibility_9h: _sensor_state
    pirateweather_visibility_11h: _sensor_state
    pirateweather_visibility_12h: _sensor_state
    pirateweather_ozone_0d: _sensor_state
    pirateweather_ozone_1d: _sensor_state
    pirateweather_ozone_2d: _sensor_state
    pirateweather_ozone_3d: _sensor_state
    pirateweather_ozone_4d: _sensor_state
    pirateweather_ozone_5d: _sensor_state
    pirateweather_ozone_6d: _sensor_state
    pirateweather_ozone_0h: _sensor_state
    pirateweather_ozone_1h: _sensor_state
    pirateweather_ozone_2h: _sensor_state
    pirateweather_ozone_3h: _sensor_state
    pirateweather_ozone_4h: _sensor_state
    pirateweather_ozone_5h: _sensor_state
    pirateweather_ozone_6h: _sensor_state
    pirateweather_ozone_7h: _sensor_state
    pirateweather_ozone_8h: _sensor_state
    pirateweather_ozone_9h: _sensor_state
    pirateweather_ozone_11h: _sensor_state
    pirateweather_ozone_12h: _sensor_state
    pirateweather_daytime_high_temperature_0d: _sensor_state
    pirateweather_daytime_high_temperature_1d: _sensor_state
    pirateweather_daytime_high_temperature_2d: _sensor_state
    pirateweather_daytime_high_temperature_3d: _sensor_state
    pirateweather_daytime_high_temperature_4d: _sensor_state
    pirateweather_daytime_high_temperature_5d: _sensor_state
    pirateweather_daytime_high_temperature_6d: _sensor_state
    pirateweather_overnight_low_temperature_0d: _sensor_state
    pirateweather_overnight_low_temperature_1d: _sensor_state
    pirateweather_overnight_low_temperature_2d: _sensor_state
    pirateweather_overnight_low_temperature_3d: _sensor_state
    pirateweather_overnight_low_temperature_4d: _sensor_state
    pirateweather_overnight_low_temperature_5d: _sensor_state
    pirateweather_overnight_low_temperature_6d: _sensor_state
    pirateweather_daytime_high_apparent_temperature_0d: _sensor_state
    pirateweather_daytime_high_apparent_temperature_1d: _sensor_state
    pirateweather_daytime_high_apparent_temperature_2d: _sensor_state
    pirateweather_daytime_high_apparent_temperature_3d: _sensor_state
    pirateweather_daytime_high_apparent_temperature_4d: _sensor_state
    pirateweather_daytime_high_apparent_temperature_5d: _sensor_state
    pirateweather_daytime_high_apparent_temperature_6d: _sensor_state
    pirateweather_overnight_low_apparent_temperature_0d: _sensor_state
    pirateweather_overnight_low_apparent_temperature_1d: _sensor_state
    pirateweather_overnight_low_apparent_temperature_2d: _sensor_state
    pirateweather_overnight_low_apparent_temperature_3d: _sensor_state
    pirateweather_overnight_low_apparent_temperature_4d: _sensor_state
    pirateweather_overnight_low_apparent_temperature_5d: _sensor_state
    pirateweather_overnight_low_apparent_temperature_6d: _sensor_state
    pirateweather_daily_max_precip_intensity_0d: _sensor_state
    pirateweather_daily_max_precip_intensity_1d: _sensor_state
    pirateweather_daily_max_precip_intensity_2d: _sensor_state
    pirateweather_daily_max_precip_intensity_3d: _sensor_state
    pirateweather_daily_max_precip_intensity_4d: _sensor_state
    pirateweather_daily_max_precip_intensity_5d: _sensor_state
    pirateweather_daily_max_precip_intensity_6d: _sensor_state
    pirateweather_uv_index_0d: _sensor_state
    pirateweather_uv_index_1d: _sensor_state
    pirateweather_uv_index_2d: _sensor_state
    pirateweather_uv_index_3d: _sensor_state
    pirateweather_uv_index_4d: _sensor_state
    pirateweather_uv_index_5d: _sensor_state
    pirateweather_uv_index_6d: _sensor_state
    pirateweather_uv_index_0h: _sensor_state
    pirateweather_uv_index_1h: _sensor_state
    pirateweather_uv_index_2h: _sensor_state
    pirateweather_uv_index_3h: _sensor_state
    pirateweather_uv_index_4h: _sensor_state
    pirateweather_uv_index_5h: _sensor_state
    pirateweather_uv_index_6h: _sensor_state
    pirateweather_uv_index_7h: _sensor_state
    pirateweather_uv_index_8h: _sensor_state
    pirateweather_uv_index_9h: _sensor_state
    pirateweather_uv_index_11h: _sensor_state
    pirateweather_uv_index_12h: _sensor_state
    pirateweather_moon_phase_0d: _sensor_state
    pirateweather_moon_phase_1d: _sensor_state
    pirateweather_moon_phase_2d: _sensor_state
    pirateweather_moon_phase_3d: _sensor_state
    pirateweather_moon_phase_4d: _sensor_state
    pirateweather_moon_phase_5d: _sensor_state
    pirateweather_moon_phase_6d: _sensor_state
    pirateweather_sunrise_0d: _sensor_state
    pirateweather_sunrise_1d: _sensor_state
    pirateweather_sunrise_2d: _sensor_state
    pirateweather_sunrise_3d: _sensor_state
    pirateweather_sunrise_4d: _sensor_state
    pirateweather_sunrise_5d: _sensor_state
    pirateweather_sunrise_6d: _sensor_state
    pirateweather_sunset_0d: _sensor_state
    pirateweather_sunset_1d: _sensor_state
    pirateweather_sunset_2d: _sensor_state
    pirateweather_sunset_3d: _sensor_state
    pirateweather_sunset_4d: _sensor_state
    pirateweather_sunset_5d: _sensor_state
    pirateweather_sunset_6d: _sensor_state
    pirateweather_time_0d: _sensor_state
    pirateweather_time_1d: _sensor_state
    pirateweather_time_2d: _sensor_state
    pirateweather_time_3d: _sensor_state
    pirateweather_time_4d: _sensor_state
    pirateweather_time_5d: _sensor_state
    pirateweather_time_6d: _sensor_state
    pirateweather_time_0h: _sensor_state
    pirateweather_time_1h: _sensor_state
    pirateweather_time_2h: _sensor_state
    pirateweather_time_3h: _sensor_state
    pirateweather_time_4h: _sensor_state
    pirateweather_time_5h: _sensor_state
    pirateweather_time_6h: _sensor_state
    pirateweather_time_7h: _sensor_state
    pirateweather_time_8h: _sensor_state
    pirateweather_time_9h: _sensor_state
    pirateweather_time_11h: _sensor_state
    pirateweather_time_12h: _sensor_state
    pirateweather_fire_index_0h: _sensor_state
    pirateweather_fire_index_1h: _sensor_state
    pirateweather_fire_index_2h: _sensor_state
    pirateweather_fire_index_3h: _sensor_state
    pirateweather_fire_index_4h: _sensor_state
    pirateweather_fire_index_5h: _sensor_state
    pirateweather_fire_index_6h: _sensor_state
    pirateweather_fire_index_7h: _sensor_state
    pirateweather_fire_index_8h: _sensor_state
    pirateweather_fire_index_9h: _sensor_state
    pirateweather_fire_index_11h: _sensor_state
    pirateweather_fire_index_12h: _sensor_state
    pirateweather_fire_index_max_0d: _sensor_state
    pirateweather_fire_index_max_1d: _sensor_state
    pirateweather_fire_index_max_2d: _sensor_state
    pirateweather_fire_index_max_3d: _sensor_state
    pirateweather_fire_index_max_4d: _sensor_state
    pirateweather_fire_index_max_5d: _sensor_state
    pirateweather_fire_index_max_6d: _sensor_state
    pirateweather_fire_risk_level_0d: _sensor_state
    pirateweather_fire_risk_level_1d: _sensor_state
    pirateweather_fire_risk_level_2d: _sensor_state
    pirateweather_fire_risk_level_3d: _sensor_state
    pirateweather_fire_risk_level_4d: _sensor_state
    pirateweather_fire_risk_level_5d: _sensor_state
    pirateweather_fire_risk_level_6d: _sensor_state
    pirateweather_fire_risk_level_0h: _sensor_state
    pirateweather_fire_risk_level_1h: _sensor_state
    pirateweather_fire_risk_level_2h: _sensor_state
    pirateweather_fire_risk_level_3h: _sensor_state
    pirateweather_fire_risk_level_4h: _sensor_state
    pirateweather_fire_risk_level_5h: _sensor_state
    pirateweather_fire_risk_level_6h: _sensor_state
    pirateweather_fire_risk_level_7h: _sensor_state
    pirateweather_fire_risk_level_8h: _sensor_state
    pirateweather_fire_risk_level_9h: _sensor_state
    pirateweather_fire_risk_level_11h: _sensor_state
    pirateweather_fire_risk_level_12h: _sensor_state
    pirateweather_smoke_0h: _sensor_state
    pirateweather_smoke_1h: _sensor_state
    pirateweather_smoke_2h: _sensor_state
    pirateweather_smoke_3h: _sensor_state
    pirateweather_smoke_4h: _sensor_state
    pirateweather_smoke_5h: _sensor_state
    pirateweather_smoke_6h: _sensor_state
    pirateweather_smoke_7h: _sensor_state
    pirateweather_smoke_8h: _sensor_state
    pirateweather_smoke_9h: _sensor_state
    pirateweather_smoke_11h: _sensor_state
    pirateweather_smoke_12h: _sensor_state
    pirateweather_smoke_max_0d: _sensor_state
    pirateweather_smoke_max_1d: _sensor_state
    pirateweather_smoke_max_2d: _sensor_state
    pirateweather_smoke_max_3d: _sensor_state
    pirateweather_smoke_max_4d: _sensor_state
    pirateweather_smoke_max_5d: _sensor_state
    pirateweather_smoke_max_6d: _sensor_state
    pirateweather_liquid_accumulation_0d: _sensor_state
    pirateweather_liquid_accumulation_1d: _sensor_state
    pirateweather_liquid_accumulation_2d: _sensor_state
    pirateweather_liquid_accumulation_3d: _sensor_state
    pirateweather_liquid_accumulation_4d: _sensor_state
    pirateweather_liquid_accumulation_5d: _sensor_state
    pirateweather_liquid_accumulation_6d: _sensor_state
    pirateweather_liquid_accumulation_0h: _sensor_state
    pirateweather_liquid_accumulation_1h: _sensor_state
    pirateweather_liquid_accumulation_2h: _sensor_state
    pirateweather_liquid_accumulation_3h: _sensor_state
    pirateweather_liquid_accumulation_4h: _sensor_state
    pirateweather_liquid_accumulation_5h: _sensor_state
    pirateweather_liquid_accumulation_6h: _sensor_state
    pirateweather_liquid_accumulation_7h: _sensor_state
    pirateweather_liquid_accumulation_8h: _sensor_state
    pirateweather_liquid_accumulation_9h: _sensor_state
    pirateweather_liquid_accumulation_11h: _sensor_state
    pirateweather_liquid_accumulation_12h: _sensor_state
    pirateweather_snow_accumulation_0d: _sensor_state
    pirateweather_snow_accumulation_1d: _sensor_state
    pirateweather_snow_accumulation_2d: _sensor_state
    pirateweather_snow_accumulation_3d: _sensor_state
    pirateweather_snow_accumulation_4d: _sensor_state
    pirateweather_snow_accumulation_5d: _sensor_state
    pirateweather_snow_accumulation_6d: _sensor_state
    pirateweather_snow_accumulation_0h: _sensor_state
    pirateweather_snow_accumulation_1h: _sensor_state
    pirateweather_snow_accumulation_2h: _sensor_state
    pirateweather_snow_accumulation_3h: _sensor_state
    pirateweather_snow_accumulation_4h: _sensor_state
    pirateweather_snow_accumulation_5h: _sensor_state
    pirateweather_snow_accumulation_6h: _sensor_state
    pirateweather_snow_accumulation_7h: _sensor_state
    pirateweather_snow_accumulation_8h: _sensor_state
    pirateweather_snow_accumulation_9h: _sensor_state
    pirateweather_snow_accumulation_11h: _sensor_state
    pirateweather_snow_accumulation_12h: _sensor_state
    pirateweather_ice_accumulation_0d: _sensor_state
    pirateweather_ice_accumulation_1d: _sensor_state
    pirateweather_ice_accumulation_2d: _sensor_state
    pirateweather_ice_accumulation_3d: _sensor_state
    pirateweather_ice_accumulation_4d: _sensor_state
    pirateweather_ice_accumulation_5d: _sensor_state
    pirateweather_ice_accumulation_6d: _sensor_state
    pirateweather_ice_accumulation_0h: _sensor_state
    pirateweather_ice_accumulation_1h: _sensor_state
    pirateweather_ice_accumulation_2h: _sensor_state
    pirateweather_ice_accumulation_3h: _sensor_state
    pirateweather_ice_accumulation_4h: _sensor_state
    pirateweather_ice_accumulation_5h: _sensor_state
    pirateweather_ice_accumulation_6h: _sensor_state
    pirateweather_ice_accumulation_7h: _sensor_state
    pirateweather_ice_accumulation_8h: _sensor_state
    pirateweather_ice_accumulation_9h: _sensor_state
    pirateweather_ice_accumulation_11h: _sensor_state
    pirateweather_ice_accumulation_12h: _sensor_state
    pirateweather_daytime_high_apparent_temperature_time_0d: _sensor_state
    pirateweather_daytime_high_apparent_temperature_time_1d: _sensor_state
    pirateweather_daytime_high_apparent_temperature_time_2d: _sensor_state
    pirateweather_daytime_high_apparent_temperature_time_3d: _sensor_state
    pirateweather_daytime_high_apparent_temperature_time_4d: _sensor_state
    pirateweather_daytime_high_apparent_temperature_time_5d: _sensor_state
    pirateweather_daytime_high_apparent_temperature_time_6d: _sensor_state
    pirateweather_overnight_low_apparent_temperature_time_0d: _sensor_state
    pirateweather_overnight_low_apparent_temperature_time_1d: _sensor_state
    pirateweather_overnight_low_apparent_temperature_time_2d: _sensor_state
    pirateweather_overnight_low_apparent_temperature_time_3d: _sensor_state
    pirateweather_overnight_low_apparent_temperature_time_4d: _sensor_state
    pirateweather_overnight_low_apparent_temperature_time_5d: _sensor_state
    pirateweather_overnight_low_apparent_temperature_time_6d: _sensor_state
    pirateweather_daytime_high_temperature_time_0d: _sensor_state
    pirateweather_daytime_high_temperature_time_1d: _sensor_state
    pirateweather_daytime_high_temperature_time_2d: _sensor_state
    pirateweather_daytime_high_temperature_time_3d: _sensor_state
    pirateweather_daytime_high_temperature_time_4d: _sensor_state
    pirateweather_daytime_high_temperature_time_5d: _sensor_state
    pirateweather_daytime_high_temperature_time_6d: _sensor_state
    pirateweather_daily_low_temperature_time_0d: _sensor_state
    pirateweather_daily_low_temperature_time_1d: _sensor_state
    pirateweather_daily_low_temperature_time_2d: _sensor_state
    pirateweather_daily_low_temperature_time_3d: _sensor_state
    pirateweather_daily_low_temperature_time_4d: _sensor_state
    pirateweather_daily_low_temperature_time_5d: _sensor_state
    pirateweather_daily_low_temperature_time_6d: _sensor_state
    ythsaz_last_online: _sensor_state
    ythsaz_online_status: _sensor_state
    ythsaz_now_playing: _sensor_state
    cron_jobs: _sensor_state
    zodiac: _sensor_state
    syth_local_browser_path: _sensor_state
    syth_local_browser_visibility: _sensor_state
    syth_local_browser_useragent: _sensor_state
    syth_local_browser_user: _sensor_state
    syth_local_browser_width: _sensor_state
    syth_local_browser_height: _sensor_state
    desktop_browser_path: _sensor_state
    desktop_browser_visibility: _sensor_state
    desktop_browser_useragent: _sensor_state
    desktop_browser_user: _sensor_state
    desktop_browser_width: _sensor_state
    desktop_browser_height: _sensor_state
    syth_local_panel: _sensor_state
    laptop_browser_path: _sensor_state
    laptop_browser_visibility: _sensor_state
    laptop_browser_useragent: _sensor_state
    laptop_browser_user: _sensor_state
    laptop_browser_width: _sensor_state
    laptop_browser_height: _sensor_state
    laptop_panel: _sensor_state
    breaker_box_bluetooth_proxy_connections_limit: _sensor_state
    breaker_box_wifi_signal_db: _sensor_state
    breaker_box_wifi_signal_percent: _sensor_state
    breaker_box_uptime_sensor: _sensor_state
    breaker_box_breaker_box_mic: _sensor_state
    desktop_panel: _sensor_state
    breaker_box_mean: _sensor_state
    breaker_box_linear_average: _sensor_state
    openweathermap_wind_gust: _sensor_state
    russell117045_online_id: _sensor_state
    russell117045_last_online: _sensor_state
    russell117045_online_status: _sensor_state
    russell117045_now_playing: _sensor_state
    howler4522_online_id: _sensor_state
    howler4522_last_online: _sensor_state
    howler4522_online_status: _sensor_state
    howler4522_now_playing: _sensor_state
    toxiccrumble_online_id: _sensor_state
    toxiccrumble_last_online: _sensor_state
    toxiccrumble_online_status: _sensor_state
    toxiccrumble_now_playing: _sensor_state
    jusparr_online_id: _sensor_state
    jusparr_last_online: _sensor_state
    jusparr_online_status: _sensor_state
    jusparr_now_playing: _sensor_state
    syth_tailscale_browser_path: _sensor_state
    syth_tailscale_browser_visibility: _sensor_state
    syth_tailscale_browser_useragent: _sensor_state
    syth_tailscale_browser_user: _sensor_state
    syth_tailscale_browser_width: _sensor_state
    syth_tailscale_browser_height: _sensor_state
    syth_tailscale_panel: _sensor_state
    time_until_dusk: _sensor_state
    wan_download_mbps: _sensor_state
    wan_upload_mbps: _sensor_state
    wan_download_of_plan: _sensor_state
    wan_upload_of_plan: _sensor_state
    lan_in: _sensor_state
    lan_out: _sensor_state
    lan_in_of_plan: _sensor_state
    lan_out_of_plan: _sensor_state
    debian_dell: _sensor_state
    debian_dell_library_movies: _sensor_state
    debian_dell_library_anime: _sensor_state
    debian_dell_library_tv_shows: _sensor_state
    debian_dell_library_music: _sensor_state
    backyard_camera_hq_camera_fps: _sensor_state
    backyard_camera_hq_process_fps: _sensor_state
    backyard_camera_hq_skipped_fps: _sensor_state
    backyard_camera_hq_detection_fps: _sensor_state
    backyard_camera_hq_sound_level: _sensor_state
    frigate_cpu_inference_speed: _sensor_state
    frigate_detection_fps: _sensor_state
    frigate_intel_vaapi_gpu_load: _sensor_state
    backyard_camera_hq_capture_cpu_usage: _sensor_state
    backyard_camera_hq_detect_cpu_usage: _sensor_state
    backyard_camera_hq_ffmpeg_cpu_usage: _sensor_state
    back_alley_all_count: _sensor_state
    backyard_all_count: _sensor_state
    backyard_fence_person_count: _sensor_state
    alley_speed_person_count: _sensor_state
    parking_pad_person_count: _sensor_state
    backyard_camera_hq_person_count: _sensor_state
    back_alley_person_count: _sensor_state
    backyard_person_count: _sensor_state
    backyard_fence_all_count: _sensor_state
    parking_pad_all_count: _sensor_state
    alley_speed_all_count: _sensor_state
    backyard_camera_hq_all_count: _sensor_state
    back_alley_all_active_count: _sensor_state
    backyard_all_active_count: _sensor_state
    backyard_fence_person_active_count: _sensor_state
    alley_speed_person_active_count: _sensor_state
    parking_pad_person_active_count: _sensor_state
    backyard_camera_hq_person_active_count: _sensor_state
    back_alley_person_active_count: _sensor_state
    backyard_person_active_count: _sensor_state
    backyard_fence_all_active_count: _sensor_state
    parking_pad_all_active_count: _sensor_state
    alley_speed_all_active_count: _sensor_state
    backyard_camera_hq_all_active_count: _sensor_state
    frigate_status: _sensor_state
    frigate_uptime: _sensor_state
    backyard_camera_hq_last_recognized_face: _sensor_state
    dining_room_wifi_connection_type: _sensor_state
    dining_room_wifi_cpu_used: _sensor_state
    dining_room_wifi_memory_used: _sensor_state
    dining_room_wifi_total_clients: _sensor_state
    dining_room_wifi_total_guest_wifi_clients: _sensor_state
    dining_room_wifi_total_iot_clients: _sensor_state
    dining_room_wifi_total_main_wifi_clients: _sensor_state
    dining_room_wifi_total_wired_clients: _sensor_state
    lining_room_wifi_connection_type: _sensor_state
    lining_room_wifi_cpu_used: _sensor_state
    lining_room_wifi_memory_used: _sensor_state
    lining_room_wifi_total_clients: _sensor_state
    lining_room_wifi_total_guest_wifi_clients: _sensor_state
    lining_room_wifi_total_iot_clients: _sensor_state
    lining_room_wifi_total_main_wifi_clients: _sensor_state
    lining_room_wifi_total_wired_clients: _sensor_state
    frigate_onnx_0_inference_speed: _sensor_state
    frigate_error_gpu_gpu_load: _sensor_state
    frigate_ov_inference_speed: _sensor_state
    backyard_camera_hq_last_recognized_plate: _sensor_state
    astroweather_backyard_forecast_length: _sensor_state
    astroweather_backyard_location_name: _sensor_state
    astroweather_backyard_latitude: _sensor_state
    astroweather_backyard_longitude: _sensor_state
    astroweather_backyard_elevation: _sensor_state
    astroweather_backyard_time_shift: _sensor_state
    astroweather_backyard_timestamp: _sensor_state
    astroweather_backyard_cloud_cover: _sensor_state
    astroweather_backyard_cloudless: _sensor_state
    astroweather_backyard_clouds_area: _sensor_state
    astroweather_backyard_clouds_area_high: _sensor_state
    astroweather_backyard_clouds_area_medium: _sensor_state
    astroweather_backyard_clouds_area_low: _sensor_state
    astroweather_backyard_fog_area: _sensor_state
    astroweather_backyard_fog_2m_area: _sensor_state
    astroweather_backyard_seeing_percentage: _sensor_state
    astroweather_backyard_seeing: _sensor_state
    astroweather_backyard_transparency: _sensor_state
    astroweather_backyard_transparency_plain: _sensor_state
    astroweather_backyard_lifted_index: _sensor_state
    astroweather_backyard_lifted_index_plain: _sensor_state
    astroweather_backyard_2m_relative_humidity: _sensor_state
    astroweather_backyard_calm_percentage: _sensor_state
    astroweather_backyard_10m_wind_direction: _sensor_state
    astroweather_backyard_10m_wind_speed: _sensor_state
    astroweather_backyard_2m_temperature: _sensor_state
    astroweather_backyard_2m_dewpoint: _sensor_state
    astroweather_backyard_precipitation_amount: _sensor_state
    astroweather_backyard_condition: _sensor_state
    astroweather_backyard_sun_altitude: _sensor_state
    astroweather_backyard_sun_azimuth: _sensor_state
    astroweather_backyard_sun_next_setting: _sensor_state
    astroweather_backyard_sun_next_setting_nautical: _sensor_state
    astroweather_backyard_sun_next_setting_astronomical: _sensor_state
    astroweather_backyard_sun_next_rising: _sensor_state
    astroweather_backyard_sun_next_rising_nautical: _sensor_state
    astroweather_backyard_sun_next_rising_astronomical: _sensor_state
    astroweather_backyard_sun_constellation: _sensor_state
    astroweather_backyard_moon_next_rising: _sensor_state
    astroweather_backyard_moon_next_setting: _sensor_state
    astroweather_backyard_moon_phase: _sensor_state
    astroweather_backyard_moon_icon: _sensor_state
    astroweather_backyard_moon_next_new_moon: _sensor_state
    astroweather_backyard_moon_next_full_moon: _sensor_state
    astroweather_backyard_moon_altitude: _sensor_state
    astroweather_backyard_moon_azimuth: _sensor_state
    astroweather_backyard_moon_distance: _sensor_state
    astroweather_backyard_moon_relative_distance: _sensor_state
    astroweather_backyard_moon_angular_size: _sensor_state
    astroweather_backyard_moon_relative_size: _sensor_state
    astroweather_backyard_moon_constellation: _sensor_state
    astroweather_backyard_moon_next_dark_night: _sensor_state
    astroweather_backyard_astronomical_night_duration: _sensor_state
    astroweather_backyard_deep_sky_darkness: _sensor_state
    astroweather_backyard_deepsky_forecast_today: _sensor_state
    astroweather_backyard_deepsky_forecast_today_plain: _sensor_state
    astroweather_backyard_deepsky_forecast_today_description: _sensor_state
    astroweather_backyard_deepsky_forecast_tomorrow: _sensor_state
    astroweather_backyard_deepsky_forecast_tomorrow_plain: _sensor_state
    astroweather_backyard_deepsky_forecast_tomorrow_description: _sensor_state
    astroweather_backyard_uptonight: _sensor_state
    discord_user_1236136606126309509: _sensor_state
    discord_user_402643064532893707: _sensor_state
    discord_user_388477010000871425: _sensor_state
    discord_user_287746189263110145: _sensor_state
    discord_user_224478797825703936: _sensor_state
    discord_user_1236136606126309509_user_name: _sensor_state
    discord_user_1236136606126309509_display_name: _sensor_state
    discord_user_1236136606126309509_roles: _sensor_state
    discord_user_1236136606126309509_game: _sensor_state
    discord_user_1236136606126309509_game_state: _sensor_state
    discord_user_1236136606126309509_game_details: _sensor_state
    discord_user_1236136606126309509_game_image_small: _sensor_state
    discord_user_1236136606126309509_game_image_large: _sensor_state
    discord_user_1236136606126309509_game_image_small_text: _sensor_state
    discord_user_1236136606126309509_game_image_large_text: _sensor_state
    discord_user_1236136606126309509_game_image_capsule_231x87: _sensor_state
    discord_user_1236136606126309509_game_image_capsule_467x181: _sensor_state
    discord_user_1236136606126309509_game_image_capsule_616x353: _sensor_state
    discord_user_1236136606126309509_game_image_header: _sensor_state
    discord_user_1236136606126309509_game_image_hero_capsule: _sensor_state
    discord_user_1236136606126309509_game_image_library_600x900: _sensor_state
    discord_user_1236136606126309509_game_image_library_hero: _sensor_state
    discord_user_1236136606126309509_game_image_logo: _sensor_state
    discord_user_1236136606126309509_game_image_page_bg_raw: _sensor_state
    discord_user_1236136606126309509_streaming: _sensor_state
    discord_user_1236136606126309509_streaming_url: _sensor_state
    discord_user_1236136606126309509_streaming_details: _sensor_state
    discord_user_1236136606126309509_listening: _sensor_state
    discord_user_1236136606126309509_listening_url: _sensor_state
    discord_user_1236136606126309509_listening_details: _sensor_state
    discord_user_1236136606126309509_spotify_artists: _sensor_state
    discord_user_1236136606126309509_spotify_title: _sensor_state
    discord_user_1236136606126309509_spotify_album: _sensor_state
    discord_user_1236136606126309509_spotify_album_cover_url: _sensor_state
    discord_user_1236136606126309509_spotify_track_id: _sensor_state
    discord_user_1236136606126309509_spotify_duration: _sensor_state
    discord_user_1236136606126309509_spotify_start: _sensor_state
    discord_user_1236136606126309509_spotify_end: _sensor_state
    discord_user_1236136606126309509_watching: _sensor_state
    discord_user_1236136606126309509_watching_url: _sensor_state
    discord_user_1236136606126309509_watching_details: _sensor_state
    discord_user_1236136606126309509_avatar_url: _sensor_state
    discord_user_1236136606126309509_custom_status: _sensor_state
    discord_user_1236136606126309509_custom_emoji: _sensor_state
    discord_user_1236136606126309509_voice_channel: _sensor_state
    discord_user_1236136606126309509_voice_deaf: _sensor_state
    discord_user_1236136606126309509_voice_mute: _sensor_state
    discord_user_1236136606126309509_voice_self_deaf: _sensor_state
    discord_user_1236136606126309509_voice_self_mute: _sensor_state
    discord_user_1236136606126309509_voice_self_stream: _sensor_state
    discord_user_1236136606126309509_voice_self_video: _sensor_state
    discord_user_1236136606126309509_voice_afk: _sensor_state
    discord_user_402643064532893707_user_name: _sensor_state
    discord_user_402643064532893707_display_name: _sensor_state
    discord_user_402643064532893707_roles: _sensor_state
    discord_user_402643064532893707_game: _sensor_state
    discord_user_402643064532893707_game_state: _sensor_state
    discord_user_402643064532893707_game_details: _sensor_state
    discord_user_402643064532893707_game_image_small: _sensor_state
    discord_user_402643064532893707_game_image_large: _sensor_state
    discord_user_402643064532893707_game_image_small_text: _sensor_state
    discord_user_402643064532893707_game_image_large_text: _sensor_state
    discord_user_402643064532893707_game_image_capsule_231x87: _sensor_state
    discord_user_402643064532893707_game_image_capsule_467x181: _sensor_state
    discord_user_402643064532893707_game_image_capsule_616x353: _sensor_state
    discord_user_402643064532893707_game_image_header: _sensor_state
    discord_user_402643064532893707_game_image_hero_capsule: _sensor_state
    discord_user_402643064532893707_game_image_library_600x900: _sensor_state
    discord_user_402643064532893707_game_image_library_hero: _sensor_state
    discord_user_402643064532893707_game_image_logo: _sensor_state
    discord_user_402643064532893707_game_image_page_bg_raw: _sensor_state
    discord_user_402643064532893707_streaming: _sensor_state
    discord_user_402643064532893707_streaming_url: _sensor_state
    discord_user_402643064532893707_streaming_details: _sensor_state
    discord_user_402643064532893707_listening: _sensor_state
    discord_user_402643064532893707_listening_url: _sensor_state
    discord_user_402643064532893707_listening_details: _sensor_state
    discord_user_402643064532893707_spotify_artists: _sensor_state
    discord_user_402643064532893707_spotify_title: _sensor_state
    discord_user_402643064532893707_spotify_album: _sensor_state
    discord_user_402643064532893707_spotify_album_cover_url: _sensor_state
    discord_user_402643064532893707_spotify_track_id: _sensor_state
    discord_user_402643064532893707_spotify_duration: _sensor_state
    discord_user_402643064532893707_spotify_start: _sensor_state
    discord_user_402643064532893707_spotify_end: _sensor_state
    discord_user_402643064532893707_watching: _sensor_state
    discord_user_402643064532893707_watching_url: _sensor_state
    discord_user_402643064532893707_watching_details: _sensor_state
    discord_user_402643064532893707_avatar_url: _sensor_state
    discord_user_402643064532893707_custom_status: _sensor_state
    discord_user_402643064532893707_custom_emoji: _sensor_state
    discord_user_402643064532893707_voice_channel: _sensor_state
    discord_user_402643064532893707_voice_deaf: _sensor_state
    discord_user_402643064532893707_voice_mute: _sensor_state
    discord_user_402643064532893707_voice_self_deaf: _sensor_state
    discord_user_402643064532893707_voice_self_mute: _sensor_state
    discord_user_402643064532893707_voice_self_stream: _sensor_state
    discord_user_402643064532893707_voice_self_video: _sensor_state
    discord_user_402643064532893707_voice_afk: _sensor_state
    discord_user_388477010000871425_user_name: _sensor_state
    discord_user_388477010000871425_display_name: _sensor_state
    discord_user_388477010000871425_roles: _sensor_state
    discord_user_388477010000871425_game: _sensor_state
    discord_user_388477010000871425_game_state: _sensor_state
    discord_user_388477010000871425_game_details: _sensor_state
    discord_user_388477010000871425_game_image_small: _sensor_state
    discord_user_388477010000871425_game_image_large: _sensor_state
    discord_user_388477010000871425_game_image_small_text: _sensor_state
    discord_user_388477010000871425_game_image_large_text: _sensor_state
    discord_user_388477010000871425_game_image_capsule_231x87: _sensor_state
    discord_user_388477010000871425_game_image_capsule_467x181: _sensor_state
    discord_user_388477010000871425_game_image_capsule_616x353: _sensor_state
    discord_user_388477010000871425_game_image_header: _sensor_state
    discord_user_388477010000871425_game_image_hero_capsule: _sensor_state
    discord_user_388477010000871425_game_image_library_600x900: _sensor_state
    discord_user_388477010000871425_game_image_library_hero: _sensor_state
    discord_user_388477010000871425_game_image_logo: _sensor_state
    discord_user_388477010000871425_game_image_page_bg_raw: _sensor_state
    discord_user_388477010000871425_streaming: _sensor_state
    discord_user_388477010000871425_streaming_url: _sensor_state
    discord_user_388477010000871425_streaming_details: _sensor_state
    discord_user_388477010000871425_listening: _sensor_state
    discord_user_388477010000871425_listening_url: _sensor_state
    discord_user_388477010000871425_listening_details: _sensor_state
    discord_user_388477010000871425_spotify_artists: _sensor_state
    discord_user_388477010000871425_spotify_title: _sensor_state
    discord_user_388477010000871425_spotify_album: _sensor_state
    discord_user_388477010000871425_spotify_album_cover_url: _sensor_state
    discord_user_388477010000871425_spotify_track_id: _sensor_state
    discord_user_388477010000871425_spotify_duration: _sensor_state
    discord_user_388477010000871425_spotify_start: _sensor_state
    discord_user_388477010000871425_spotify_end: _sensor_state
    discord_user_388477010000871425_watching: _sensor_state
    discord_user_388477010000871425_watching_url: _sensor_state
    discord_user_388477010000871425_watching_details: _sensor_state
    discord_user_388477010000871425_avatar_url: _sensor_state
    discord_user_388477010000871425_custom_status: _sensor_state
    discord_user_388477010000871425_custom_emoji: _sensor_state
    discord_user_388477010000871425_voice_channel: _sensor_state
    discord_user_388477010000871425_voice_deaf: _sensor_state
    discord_user_388477010000871425_voice_mute: _sensor_state
    discord_user_388477010000871425_voice_self_deaf: _sensor_state
    discord_user_388477010000871425_voice_self_mute: _sensor_state
    discord_user_388477010000871425_voice_self_stream: _sensor_state
    discord_user_388477010000871425_voice_self_video: _sensor_state
    discord_user_388477010000871425_voice_afk: _sensor_state
    discord_user_287746189263110145_user_name: _sensor_state
    discord_user_287746189263110145_display_name: _sensor_state
    discord_user_287746189263110145_roles: _sensor_state
    discord_user_287746189263110145_game: _sensor_state
    discord_user_287746189263110145_game_state: _sensor_state
    discord_user_287746189263110145_game_details: _sensor_state
    discord_user_287746189263110145_game_image_small: _sensor_state
    discord_user_287746189263110145_game_image_large: _sensor_state
    discord_user_287746189263110145_game_image_small_text: _sensor_state
    discord_user_287746189263110145_game_image_large_text: _sensor_state
    discord_user_287746189263110145_game_image_capsule_231x87: _sensor_state
    discord_user_287746189263110145_game_image_capsule_467x181: _sensor_state
    discord_user_287746189263110145_game_image_capsule_616x353: _sensor_state
    discord_user_287746189263110145_game_image_header: _sensor_state
    discord_user_287746189263110145_game_image_hero_capsule: _sensor_state
    discord_user_287746189263110145_game_image_library_600x900: _sensor_state
    discord_user_287746189263110145_game_image_library_hero: _sensor_state
    discord_user_287746189263110145_game_image_logo: _sensor_state
    discord_user_287746189263110145_game_image_page_bg_raw: _sensor_state
    discord_user_287746189263110145_streaming: _sensor_state
    discord_user_287746189263110145_streaming_url: _sensor_state
    discord_user_287746189263110145_streaming_details: _sensor_state
    discord_user_287746189263110145_listening: _sensor_state
    discord_user_287746189263110145_listening_url: _sensor_state
    discord_user_287746189263110145_listening_details: _sensor_state
    discord_user_287746189263110145_spotify_artists: _sensor_state
    discord_user_287746189263110145_spotify_title: _sensor_state
    discord_user_287746189263110145_spotify_album: _sensor_state
    discord_user_287746189263110145_spotify_album_cover_url: _sensor_state
    discord_user_287746189263110145_spotify_track_id: _sensor_state
    discord_user_287746189263110145_spotify_duration: _sensor_state
    discord_user_287746189263110145_spotify_start: _sensor_state
    discord_user_287746189263110145_spotify_end: _sensor_state
    discord_user_287746189263110145_watching: _sensor_state
    discord_user_287746189263110145_watching_url: _sensor_state
    discord_user_287746189263110145_watching_details: _sensor_state
    discord_user_287746189263110145_avatar_url: _sensor_state
    discord_user_287746189263110145_custom_status: _sensor_state
    discord_user_287746189263110145_custom_emoji: _sensor_state
    discord_user_287746189263110145_voice_channel: _sensor_state
    discord_user_287746189263110145_voice_deaf: _sensor_state
    discord_user_287746189263110145_voice_mute: _sensor_state
    discord_user_287746189263110145_voice_self_deaf: _sensor_state
    discord_user_287746189263110145_voice_self_mute: _sensor_state
    discord_user_287746189263110145_voice_self_stream: _sensor_state
    discord_user_287746189263110145_voice_self_video: _sensor_state
    discord_user_287746189263110145_voice_afk: _sensor_state
    discord_user_224478797825703936_user_name: _sensor_state
    discord_user_224478797825703936_display_name: _sensor_state
    discord_user_224478797825703936_roles: _sensor_state
    discord_user_224478797825703936_game: _sensor_state
    discord_user_224478797825703936_game_state: _sensor_state
    discord_user_224478797825703936_game_details: _sensor_state
    discord_user_224478797825703936_game_image_small: _sensor_state
    discord_user_224478797825703936_game_image_large: _sensor_state
    discord_user_224478797825703936_game_image_small_text: _sensor_state
    discord_user_224478797825703936_game_image_large_text: _sensor_state
    discord_user_224478797825703936_game_image_capsule_231x87: _sensor_state
    discord_user_224478797825703936_game_image_capsule_467x181: _sensor_state
    discord_user_224478797825703936_game_image_capsule_616x353: _sensor_state
    discord_user_224478797825703936_game_image_header: _sensor_state
    discord_user_224478797825703936_game_image_hero_capsule: _sensor_state
    discord_user_224478797825703936_game_image_library_600x900: _sensor_state
    discord_user_224478797825703936_game_image_library_hero: _sensor_state
    discord_user_224478797825703936_game_image_logo: _sensor_state
    discord_user_224478797825703936_game_image_page_bg_raw: _sensor_state
    discord_user_224478797825703936_streaming: _sensor_state
    discord_user_224478797825703936_streaming_url: _sensor_state
    discord_user_224478797825703936_streaming_details: _sensor_state
    discord_user_224478797825703936_listening: _sensor_state
    discord_user_224478797825703936_listening_url: _sensor_state
    discord_user_224478797825703936_listening_details: _sensor_state
    discord_user_224478797825703936_spotify_artists: _sensor_state
    discord_user_224478797825703936_spotify_title: _sensor_state
    discord_user_224478797825703936_spotify_album: _sensor_state
    discord_user_224478797825703936_spotify_album_cover_url: _sensor_state
    discord_user_224478797825703936_spotify_track_id: _sensor_state
    discord_user_224478797825703936_spotify_duration: _sensor_state
    discord_user_224478797825703936_spotify_start: _sensor_state
    discord_user_224478797825703936_spotify_end: _sensor_state
    discord_user_224478797825703936_watching: _sensor_state
    discord_user_224478797825703936_watching_url: _sensor_state
    discord_user_224478797825703936_watching_details: _sensor_state
    discord_user_224478797825703936_avatar_url: _sensor_state
    discord_user_224478797825703936_custom_status: _sensor_state
    discord_user_224478797825703936_custom_emoji: _sensor_state
    discord_user_224478797825703936_voice_channel: _sensor_state
    discord_user_224478797825703936_voice_deaf: _sensor_state
    discord_user_224478797825703936_voice_mute: _sensor_state
    discord_user_224478797825703936_voice_self_deaf: _sensor_state
    discord_user_224478797825703936_voice_self_mute: _sensor_state
    discord_user_224478797825703936_voice_self_stream: _sensor_state
    discord_user_224478797825703936_voice_self_video: _sensor_state
    discord_user_224478797825703936_voice_afk: _sensor_state
    discord_channel_1261511369946169395: _sensor_state
    discord_channel_1175163519344328759: _sensor_state
    discord_channel_1175177744615747606: _sensor_state
    discord_channel_1175163519344328761: _sensor_state
    discord_channel_1247182038201667666: _sensor_state
    discord_channel_1247182327684136971: _sensor_state
    discord_channel_1247182694685609984: _sensor_state
    discord_channel_1257047304637120684: _sensor_state
    discord_channel_1257047563752833165: _sensor_state
    discord_channel_1257047629700005998: _sensor_state
    discord_channel_1257047695202320404: _sensor_state
    discord_channel_1390713041187770388: _sensor_state
    discord_channel_1390713114005344436: _sensor_state
    discord_channel_1390713094333792278: _sensor_state
    discord_channel_1397270147919777802: _sensor_state
    genius_lyrics_desktop_lyrics: _sensor_state
    genius_lyrics_living_room_tv_2_lyrics: _sensor_state
    genius_lyrics_bathroom_2_lyrics: _sensor_state
    genius_lyrics_living_room_2_lyrics: _sensor_state
    genius_lyrics_bedroom_speaker_2_lyrics: _sensor_state
    genius_lyrics_bed_and_bath_2_lyrics: _sensor_state
    genius_lyrics_two_normal_2_lyrics: _sensor_state
    genius_lyrics_speakers_2_lyrics: _sensor_state
    genius_lyrics_playstation_4_2_lyrics: _sensor_state
    genius_lyrics_playstation_4_lyrics: _sensor_state
    genius_lyrics_spotify_ashton_parrott_lyrics: _sensor_state
    genius_lyrics_spotify_jusparr_lyrics: _sensor_state
    genius_lyrics_living_room_lyrics: _sensor_state
    genius_lyrics_bedroom_speaker_lyrics: _sensor_state
    genius_lyrics_bed_and_bath_lyrics: _sensor_state
    genius_lyrics_two_normal_lyrics: _sensor_state
    genius_lyrics_speakers_lyrics: _sensor_state
    genius_lyrics_living_room_tv_lyrics: _sensor_state
    genius_lyrics_tv_group_lyrics: _sensor_state
    genius_lyrics_bathroom_lyrics: _sensor_state
    moon_astro_azimuth: _sensor_state
    moon_astro_elevation: _sensor_state
    moon_astro_illumination: _sensor_state
    moon_astro_distance: _sensor_state
    moon_astro_parallax: _sensor_state
    moon_astro_ecliptic_longitude_topocentric: _sensor_state
    moon_astro_ecliptic_latitude_topocentric: _sensor_state
    moon_astro_ecliptic_longitude_geocentric: _sensor_state
    moon_astro_ecliptic_latitude_geocentric: _sensor_state
    moon_astro_next_rise: _sensor_state
    moon_astro_next_set: _sensor_state
    moon_astro_next_apogee: _sensor_state
    moon_astro_next_perigee: _sensor_state
    moon_astro_next_new_moon: _sensor_state
    moon_astro_next_first_quarter: _sensor_state
    moon_astro_next_full_moon: _sensor_state
    moon_astro_next_last_quarter: _sensor_state
    moon_astro_ecliptic_longitude_at_next_full_moon: _sensor_state
    moon_astro_ecliptic_latitude_at_next_full_moon: _sensor_state
    moon_astro_ecliptic_longitude_at_next_new_moon: _sensor_state
    moon_astro_ecliptic_latitude_at_next_new_moon: _sensor_state
    moon_astro_zodiac_sign_at_next_new_moon: _sensor_state
    moon_astro_zodiac_sign_at_next_full_moon: _sensor_state
    moon_astro_zodiac_degree_at_next_new_moon: _sensor_state
    moon_astro_zodiac_degree_at_next_full_moon: _sensor_state
    moon_astro_phase: _sensor_state
    neo_watcher_stats: _sensor_state
    neo_watcher_potentially_hazardous_1st: _sensor_state
    neo_watcher_potentially_hazardous_2nd: _sensor_state
    neo_watcher_potentially_hazardous_3rd: _sensor_state
    neo_watcher_potentially_hazardous_4th: _sensor_state
    neo_watcher_potentially_hazardous_5th: _sensor_state
    neo_watcher_potentially_hazardous_6th: _sensor_state
    neo_watcher_potentially_hazardous_7th: _sensor_state
    neo_watcher_potentially_hazardous_8th: _sensor_state
    neo_watcher_potentially_hazardous_9th: _sensor_state
    neo_watcher_potentially_hazardous_10th: _sensor_state
    neo_watcher_potentially_hazardous_11th: _sensor_state
    neo_watcher_potentially_hazardous_12th: _sensor_state
    neo_watcher_potentially_hazardous_13th: _sensor_state
    neo_watcher_potentially_hazardous_14th: _sensor_state
    neo_watcher_potentially_hazardous_15th: _sensor_state
    neo_watcher_non_hazardous_1st: _sensor_state
    neo_watcher_non_hazardous_2nd: _sensor_state
    neo_watcher_non_hazardous_3rd: _sensor_state
    neo_watcher_non_hazardous_4th: _sensor_state
    neo_watcher_non_hazardous_5th: _sensor_state
    neo_watcher_non_hazardous_6th: _sensor_state
    neo_watcher_non_hazardous_7th: _sensor_state
    neo_watcher_non_hazardous_8th: _sensor_state
    neo_watcher_non_hazardous_9th: _sensor_state
    neo_watcher_non_hazardous_10th: _sensor_state
    neo_watcher_non_hazardous_11th: _sensor_state
    neo_watcher_non_hazardous_12th: _sensor_state
    neo_watcher_non_hazardous_13th: _sensor_state
    neo_watcher_non_hazardous_14th: _sensor_state
    neo_watcher_non_hazardous_15th: _sensor_state
    neo_watcher_non_hazardous_16th: _sensor_state
    neo_watcher_non_hazardous_17th: _sensor_state
    neo_watcher_non_hazardous_18th: _sensor_state
    neo_watcher_non_hazardous_19th: _sensor_state
    neo_watcher_non_hazardous_20th: _sensor_state
    solar_flux_index: _sensor_state
    a_index: _sensor_state
    a_index_2_day: _sensor_state
    a_index_3_day: _sensor_state
    planetary_k_index: _sensor_state
    sunspot_number: _sensor_state
    polar_cap_absorption: _sensor_state
    x_class_1_day_probability: _sensor_state
    m_class_1_day_probability: _sensor_state
    sun_wall_intensity_front: _sensor_state
    sun_wall_intensity_left: _sensor_state
    sun_wall_intensity_back: _sensor_state
    sun_wall_intensity_right: _sensor_state
    sun_azimuth: _sensor_state
    sun_elevation: _sensor_state
    home_local_observation_time: _sensor_state
    home_weather_description: _sensor_state
    home_relative_humidity: _sensor_state
    home_uv_index: _sensor_state
    home_wind_direction_degrees: _sensor_state
    home_wind_direction_cardinal: _sensor_state
    home_dewpoint: _sensor_state
    home_temperature_feels_like: _sensor_state
    home_temperature: _sensor_state
    home_heat_index: _sensor_state
    home_wind_chill: _sensor_state
    home_precipitation_last_hour: _sensor_state
    home_precipitation_last_6_hours: _sensor_state
    home_precipitation_last_24_hours: _sensor_state
    home_pressure: _sensor_state
    home_wind_gust: _sensor_state
    home_wind_speed: _sensor_state
    home_cloud_ceiling: _sensor_state
    home_pressure_tendency_trend: _sensor_state
    home_cloud_cover_phrase: _sensor_state
    home_latitude: _sensor_state
    home_longitude: _sensor_state
    genius_lyrics_laptop_2_lyrics: _sensor_state
    backyard_fence_dog_count: _sensor_state
    alley_speed_dog_count: _sensor_state
    back_alley_cat_count: _sensor_state
    backyard_camera_hq_motorcycle_count: _sensor_state
    backyard_camera_hq_car_count: _sensor_state
    parking_pad_motorcycle_count: _sensor_state
    backyard_cat_count: _sensor_state
    parking_pad_car_count: _sensor_state
    back_alley_motorcycle_count: _sensor_state
    back_alley_car_count: _sensor_state
    backyard_fence_cat_count: _sensor_state
    alley_speed_cat_count: _sensor_state
    backyard_fence_bicycle_count: _sensor_state
    backyard_motorcycle_count: _sensor_state
    backyard_camera_hq_bicycle_count: _sensor_state
    parking_pad_bicycle_count: _sensor_state
    backyard_car_count: _sensor_state
    backyard_camera_hq_dog_count: _sensor_state
    back_alley_bicycle_count: _sensor_state
    parking_pad_dog_count: _sensor_state
    alley_speed_car_count: _sensor_state
    backyard_fence_motorcycle_count: _sensor_state
    alley_speed_motorcycle_count: _sensor_state
    backyard_fence_car_count: _sensor_state
    back_alley_dog_count: _sensor_state
    backyard_bicycle_count: _sensor_state
    backyard_camera_hq_cat_count: _sensor_state
    backyard_dog_count: _sensor_state
    parking_pad_cat_count: _sensor_state
    alley_speed_bicycle_count: _sensor_state
    backyard_fence_dog_active_count: _sensor_state
    alley_speed_dog_active_count: _sensor_state
    back_alley_cat_active_count: _sensor_state
    backyard_camera_hq_motorcycle_active_count: _sensor_state
    backyard_camera_hq_car_active_count: _sensor_state
    parking_pad_motorcycle_active_count: _sensor_state
    backyard_cat_active_count: _sensor_state
    parking_pad_car_active_count: _sensor_state
    back_alley_motorcycle_active_count: _sensor_state
    back_alley_car_active_count: _sensor_state
    backyard_fence_cat_active_count: _sensor_state
    alley_speed_cat_active_count: _sensor_state
    backyard_fence_bicycle_active_count: _sensor_state
    backyard_motorcycle_active_count: _sensor_state
    backyard_camera_hq_bicycle_active_count: _sensor_state
    parking_pad_bicycle_active_count: _sensor_state
    backyard_car_active_count: _sensor_state
    backyard_camera_hq_dog_active_count: _sensor_state
    back_alley_bicycle_active_count: _sensor_state
    parking_pad_dog_active_count: _sensor_state
    alley_speed_car_active_count: _sensor_state
    backyard_fence_motorcycle_active_count: _sensor_state
    alley_speed_motorcycle_active_count: _sensor_state
    backyard_fence_car_active_count: _sensor_state
    back_alley_dog_active_count: _sensor_state
    backyard_bicycle_active_count: _sensor_state
    backyard_camera_hq_cat_active_count: _sensor_state
    backyard_dog_active_count: _sensor_state
    parking_pad_cat_active_count: _sensor_state
    alley_speed_bicycle_active_count: _sensor_state
    server_fan_server_fan_status: _sensor_state
    printer_printer_status: _sensor_state
    genius_lyrics_syth_local_lyrics: _sensor_state
    backyard_occupancy: _sensor_state
    pirate_weather_emoji: _sensor_state
    dashboard_header_status: _sensor_state
    dashboard_greeting: _sensor_state
    active_frontend_user: _sensor_state
    ipad_local_browser_path: _sensor_state
    ipad_local_browser_visibility: _sensor_state
    ipad_local_browser_useragent: _sensor_state
    ipad_local_browser_user: _sensor_state
    ipad_local_browser_width: _sensor_state
    ipad_local_browser_height: _sensor_state
    ipad_local_panel: _sensor_state
    ipad_activity: _sensor_state
    ipad_battery_level: _sensor_state
    ipad_battery_state: _sensor_state
    ipad_storage: _sensor_state
    ipad_ssid: _sensor_state
    ipad_bssid: _sensor_state
    ipad_connection_type: _sensor_state
    ipad_geocoded_location: _sensor_state
    ipad_last_update_trigger: _sensor_state
    ipad_app_version: _sensor_state
    ipad_audio_output: _sensor_state
    ipad_location_permission: _sensor_state
    intel_core_i7_5500u_cpu_core_voltage: _sensor_state
    intel_core_i7_5500u_cpu_core_1_voltage: _sensor_state
    intel_core_i7_5500u_cpu_core_2_voltage: _sensor_state
    intel_core_i7_5500u_cpu_package_power: _sensor_state
    intel_core_i7_5500u_cpu_cores_power: _sensor_state
    intel_core_i7_5500u_cpu_memory_power: _sensor_state
    intel_core_i7_5500u_bus_speed_clock: _sensor_state
    intel_core_i7_5500u_cpu_core_1_clock: _sensor_state
    intel_core_i7_5500u_cpu_core_2_clock: _sensor_state
    intel_core_i7_5500u_core_max_temperature: _sensor_state
    intel_core_i7_5500u_core_average_temperature: _sensor_state
    intel_core_i7_5500u_cpu_core_1_temperature: _sensor_state
    intel_core_i7_5500u_cpu_core_2_temperature: _sensor_state
    intel_core_i7_5500u_cpu_package_temperature: _sensor_state
    intel_core_i7_5500u_cpu_core_1_distance_to_tjmax_temperature: _sensor_state
    intel_core_i7_5500u_cpu_core_2_distance_to_tjmax_temperature: _sensor_state
    intel_core_i7_5500u_cpu_total_load: _sensor_state
    intel_core_i7_5500u_cpu_core_max_load: _sensor_state
    intel_core_i7_5500u_cpu_core_1_thread_1_load: _sensor_state
    intel_core_i7_5500u_cpu_core_1_thread_2_load: _sensor_state
    intel_core_i7_5500u_cpu_core_2_thread_1_load: _sensor_state
    intel_core_i7_5500u_cpu_core_2_thread_2_load: _sensor_state
    laptop_temperature_range: _sensor_state
    bedroom_closet_door_battery: _sensor_state
    bedroom_closet_door_device_temperature: _sensor_state
    lumi_lumi_sensor_magnet_aq2_rssi_2: _sensor_state
    lumi_lumi_sensor_magnet_aq2_lqi_2: _sensor_state
    furnace_room_door_battery: _sensor_state
    furnace_room_door_device_temperature: _sensor_state
    lumi_lumi_sensor_magnet_aq2_rssi: _sensor_state
    lumi_lumi_sensor_magnet_aq2_lqi: _sensor_state
    local_time_with_seconds: _sensor_state
    tab_header_status: _sensor_state
    genius_lyrics_ipad_local_lyrics: _sensor_state
    home_assistant_web_status: _sensor_state
    website: _sensor_state
    developer_docs: _sensor_state
    data_portal: _sensor_state
    netifly: _sensor_state
    forums: _sensor_state
    mailgun: _sensor_state
    aws_ec2: _sensor_state
    remote_ui: _sensor_state
    alexa: _sensor_state
    google_assistant: _sensor_state
    cloud_storage: _sensor_state
    webhooks: _sensor_state
    account_linking: _sensor_state
    account: _sensor_state
    push_notifications: _sensor_state
    updater: _sensor_state
    cloudflair: _sensor_state
    aws_dynamodb_us_west_2: _sensor_state
    aws_lambda_us_west_2: _sensor_state
    aws_sns_us_west_2: _sensor_state
    aws_lambda_us_east_1: _sensor_state
    github_git_operations: _sensor_state
    github_issues_prs_dashboard_projects: _sensor_state
    github_actions: _sensor_state
    npm_inc_package_publishing: _sensor_state
    pypi: _sensor_state
    npm_inc_package_installation: _sensor_state
    past_incidents_reported_today: _sensor_state
    syth_local_browser_id: _sensor_state
    laptop_browser_id: _sensor_state
    desktop_browser_id: _sensor_state
    ipad_local_browser_id: _sensor_state
    basnijholt_adaptive_lighting_discussions: _sensor_state
    boralyl_cookiecutter_homeassistant_component_discussions: _sensor_state
    boralyl_steam_wishlist_discussions: _sensor_state
    bportaluri_wifiesp_discussions: _sensor_state
    build_wars_gw1_database_discussions: _sensor_state
    custom_cards_upcoming_media_card_discussions: _sensor_state
    custom_components_pyscript_discussions: _sensor_state
    custom_components_sensor_plex_recently_added_discussions: _sensor_state
    home_assistant_addons_discussions: _sensor_state
    home_assistant_home_assistant_io_discussions: _sensor_state
    home_assistant_ios_discussions: _sensor_state
    huggingface_transformers_discussions: _sensor_state
    leikoilja_ha_google_home_discussions: _sensor_state
    librehardwaremonitor_librehardwaremonitor_discussions: _sensor_state
    limych_ha_tor_check_discussions: _sensor_state
    ludeeus_integration_blueprint_discussions: _sensor_state
    maselkov_gw2bot_discussions: _sensor_state
    mweinelt_ha_prometheus_sensor_discussions: _sensor_state
    nationalsecurityagency_ghidra_discussions: _sensor_state
    oncleben31_cookiecutter_homeassistant_custom_component_discussions: _sensor_state
    permissionlesstech_bitchat_discussions: _sensor_state
    pirate_weather_pirate_weather_ha_discussions: _sensor_state
    psp_archive_psp_ftpd_discussions: _sensor_state
    public_apis_public_apis_discussions: _sensor_state
    sythsaz_home_assistant_discussions: _sensor_state
    taschenbuch_blishhud_farmingtracker_discussions: _sensor_state
    tiimgreen_github_cheat_sheet_discussions: _sensor_state
    vinta_awesome_python_discussions: _sensor_state
    viatsko_awesome_vscode_discussions: _sensor_state
    wasabeef_awesome_android_ui_discussions: _sensor_state
    waujito_tpllax1500gpl_discussions: _sensor_state
    basnijholt_adaptive_lighting_stars: _sensor_state
    boralyl_cookiecutter_homeassistant_component_stars: _sensor_state
    boralyl_steam_wishlist_stars: _sensor_state
    bportaluri_wifiesp_stars: _sensor_state
    build_wars_gw1_database_stars: _sensor_state
    custom_cards_upcoming_media_card_stars: _sensor_state
    custom_components_pyscript_stars: _sensor_state
    custom_components_sensor_plex_recently_added_stars: _sensor_state
    home_assistant_addons_stars: _sensor_state
    home_assistant_home_assistant_io_stars: _sensor_state
    home_assistant_ios_stars: _sensor_state
    huggingface_transformers_stars: _sensor_state
    leikoilja_ha_google_home_stars: _sensor_state
    librehardwaremonitor_librehardwaremonitor_stars: _sensor_state
    limych_ha_tor_check_stars: _sensor_state
    ludeeus_integration_blueprint_stars: _sensor_state
    maselkov_gw2bot_stars: _sensor_state
    mweinelt_ha_prometheus_sensor_stars: _sensor_state
    nationalsecurityagency_ghidra_stars: _sensor_state
    oncleben31_cookiecutter_homeassistant_custom_component_stars: _sensor_state
    permissionlesstech_bitchat_stars: _sensor_state
    pirate_weather_pirate_weather_ha_stars: _sensor_state
    psp_archive_psp_ftpd_stars: _sensor_state
    public_apis_public_apis_stars: _sensor_state
    sythsaz_home_assistant_stars: _sensor_state
    taschenbuch_blishhud_farmingtracker_stars: _sensor_state
    tiimgreen_github_cheat_sheet_stars: _sensor_state
    vinta_awesome_python_stars: _sensor_state
    viatsko_awesome_vscode_stars: _sensor_state
    wasabeef_awesome_android_ui_stars: _sensor_state
    waujito_tpllax1500gpl_stars: _sensor_state
    basnijholt_adaptive_lighting_watchers: _sensor_state
    boralyl_cookiecutter_homeassistant_component_watchers: _sensor_state
    boralyl_steam_wishlist_watchers: _sensor_state
    bportaluri_wifiesp_watchers: _sensor_state
    build_wars_gw1_database_watchers: _sensor_state
    custom_cards_upcoming_media_card_watchers: _sensor_state
    custom_components_pyscript_watchers: _sensor_state
    custom_components_sensor_plex_recently_added_watchers: _sensor_state
    home_assistant_addons_watchers: _sensor_state
    home_assistant_home_assistant_io_watchers: _sensor_state
    home_assistant_ios_watchers: _sensor_state
    huggingface_transformers_watchers: _sensor_state
    leikoilja_ha_google_home_watchers: _sensor_state
    librehardwaremonitor_librehardwaremonitor_watchers: _sensor_state
    limych_ha_tor_check_watchers: _sensor_state
    ludeeus_integration_blueprint_watchers: _sensor_state
    maselkov_gw2bot_watchers: _sensor_state
    mweinelt_ha_prometheus_sensor_watchers: _sensor_state
    nationalsecurityagency_ghidra_watchers: _sensor_state
    oncleben31_cookiecutter_homeassistant_custom_component_watchers: _sensor_state
    permissionlesstech_bitchat_watchers: _sensor_state
    pirate_weather_pirate_weather_ha_watchers: _sensor_state
    psp_archive_psp_ftpd_watchers: _sensor_state
    public_apis_public_apis_watchers: _sensor_state
    sythsaz_home_assistant_watchers: _sensor_state
    taschenbuch_blishhud_farmingtracker_watchers: _sensor_state
    tiimgreen_github_cheat_sheet_watchers: _sensor_state
    vinta_awesome_python_watchers: _sensor_state
    viatsko_awesome_vscode_watchers: _sensor_state
    wasabeef_awesome_android_ui_watchers: _sensor_state
    waujito_tpllax1500gpl_watchers: _sensor_state
    basnijholt_adaptive_lighting_forks: _sensor_state
    boralyl_cookiecutter_homeassistant_component_forks: _sensor_state
    boralyl_steam_wishlist_forks: _sensor_state
    bportaluri_wifiesp_forks: _sensor_state
    build_wars_gw1_database_forks: _sensor_state
    custom_cards_upcoming_media_card_forks: _sensor_state
    custom_components_pyscript_forks: _sensor_state
    custom_components_sensor_plex_recently_added_forks: _sensor_state
    home_assistant_addons_forks: _sensor_state
    home_assistant_home_assistant_io_forks: _sensor_state
    home_assistant_ios_forks: _sensor_state
    huggingface_transformers_forks: _sensor_state
    leikoilja_ha_google_home_forks: _sensor_state
    librehardwaremonitor_librehardwaremonitor_forks: _sensor_state
    limych_ha_tor_check_forks: _sensor_state
    ludeeus_integration_blueprint_forks: _sensor_state
    maselkov_gw2bot_forks: _sensor_state
    mweinelt_ha_prometheus_sensor_forks: _sensor_state
    nationalsecurityagency_ghidra_forks: _sensor_state
    oncleben31_cookiecutter_homeassistant_custom_component_forks: _sensor_state
    permissionlesstech_bitchat_forks: _sensor_state
    pirate_weather_pirate_weather_ha_forks: _sensor_state
    psp_archive_psp_ftpd_forks: _sensor_state
    public_apis_public_apis_forks: _sensor_state
    sythsaz_home_assistant_forks: _sensor_state
    taschenbuch_blishhud_farmingtracker_forks: _sensor_state
    tiimgreen_github_cheat_sheet_forks: _sensor_state
    vinta_awesome_python_forks: _sensor_state
    viatsko_awesome_vscode_forks: _sensor_state
    wasabeef_awesome_android_ui_forks: _sensor_state
    waujito_tpllax1500gpl_forks: _sensor_state
    basnijholt_adaptive_lighting_issues: _sensor_state
    boralyl_cookiecutter_homeassistant_component_issues: _sensor_state
    boralyl_steam_wishlist_issues: _sensor_state
    bportaluri_wifiesp_issues: _sensor_state
    build_wars_gw1_database_issues: _sensor_state
    custom_cards_upcoming_media_card_issues: _sensor_state
    custom_components_pyscript_issues: _sensor_state
    custom_components_sensor_plex_recently_added_issues: _sensor_state
    home_assistant_addons_issues: _sensor_state
    home_assistant_home_assistant_io_issues: _sensor_state
    home_assistant_ios_issues: _sensor_state
    huggingface_transformers_issues: _sensor_state
    leikoilja_ha_google_home_issues: _sensor_state
    librehardwaremonitor_librehardwaremonitor_issues: _sensor_state
    limych_ha_tor_check_issues: _sensor_state
    ludeeus_integration_blueprint_issues: _sensor_state
    maselkov_gw2bot_issues: _sensor_state
    mweinelt_ha_prometheus_sensor_issues: _sensor_state
    nationalsecurityagency_ghidra_issues: _sensor_state
    oncleben31_cookiecutter_homeassistant_custom_component_issues: _sensor_state
    permissionlesstech_bitchat_issues: _sensor_state
    pirate_weather_pirate_weather_ha_issues: _sensor_state
    psp_archive_psp_ftpd_issues: _sensor_state
    public_apis_public_apis_issues: _sensor_state
    sythsaz_home_assistant_issues: _sensor_state
    taschenbuch_blishhud_farmingtracker_issues: _sensor_state
    tiimgreen_github_cheat_sheet_issues: _sensor_state
    vinta_awesome_python_issues: _sensor_state
    viatsko_awesome_vscode_issues: _sensor_state
    wasabeef_awesome_android_ui_issues: _sensor_state
    waujito_tpllax1500gpl_issues: _sensor_state
    basnijholt_adaptive_lighting_pull_requests: _sensor_state
    boralyl_cookiecutter_homeassistant_component_pull_requests: _sensor_state
    boralyl_steam_wishlist_pull_requests: _sensor_state
    bportaluri_wifiesp_pull_requests: _sensor_state
    build_wars_gw1_database_pull_requests: _sensor_state
    custom_cards_upcoming_media_card_pull_requests: _sensor_state
    custom_components_pyscript_pull_requests: _sensor_state
    custom_components_sensor_plex_recently_added_pull_requests: _sensor_state
    home_assistant_addons_pull_requests: _sensor_state
    home_assistant_home_assistant_io_pull_requests: _sensor_state
    home_assistant_ios_pull_requests: _sensor_state
    huggingface_transformers_pull_requests: _sensor_state
    leikoilja_ha_google_home_pull_requests: _sensor_state
    librehardwaremonitor_librehardwaremonitor_pull_requests: _sensor_state
    limych_ha_tor_check_pull_requests: _sensor_state
    ludeeus_integration_blueprint_pull_requests: _sensor_state
    maselkov_gw2bot_pull_requests: _sensor_state
    mweinelt_ha_prometheus_sensor_pull_requests: _sensor_state
    nationalsecurityagency_ghidra_pull_requests: _sensor_state
    oncleben31_cookiecutter_homeassistant_custom_component_pull_requests: _sensor_state
    permissionlesstech_bitchat_pull_requests: _sensor_state
    pirate_weather_pirate_weather_ha_pull_requests: _sensor_state
    psp_archive_psp_ftpd_pull_requests: _sensor_state
    public_apis_public_apis_pull_requests: _sensor_state
    sythsaz_home_assistant_pull_requests: _sensor_state
    taschenbuch_blishhud_farmingtracker_pull_requests: _sensor_state
    tiimgreen_github_cheat_sheet_pull_requests: _sensor_state
    vinta_awesome_python_pull_requests: _sensor_state
    viatsko_awesome_vscode_pull_requests: _sensor_state
    wasabeef_awesome_android_ui_pull_requests: _sensor_state
    waujito_tpllax1500gpl_pull_requests: _sensor_state
    basnijholt_adaptive_lighting_latest_commit: _sensor_state
    boralyl_cookiecutter_homeassistant_component_latest_commit: _sensor_state
    boralyl_steam_wishlist_latest_commit: _sensor_state
    bportaluri_wifiesp_latest_commit: _sensor_state
    build_wars_gw1_database_latest_commit: _sensor_state
    custom_cards_upcoming_media_card_latest_commit: _sensor_state
    custom_components_pyscript_latest_commit: _sensor_state
    custom_components_sensor_plex_recently_added_latest_commit: _sensor_state
    home_assistant_addons_latest_commit: _sensor_state
    home_assistant_home_assistant_io_latest_commit: _sensor_state
    home_assistant_ios_latest_commit: _sensor_state
    huggingface_transformers_latest_commit: _sensor_state
    leikoilja_ha_google_home_latest_commit: _sensor_state
    librehardwaremonitor_librehardwaremonitor_latest_commit: _sensor_state
    limych_ha_tor_check_latest_commit: _sensor_state
    ludeeus_integration_blueprint_latest_commit: _sensor_state
    maselkov_gw2bot_latest_commit: _sensor_state
    mweinelt_ha_prometheus_sensor_latest_commit: _sensor_state
    nationalsecurityagency_ghidra_latest_commit: _sensor_state
    oncleben31_cookiecutter_homeassistant_custom_component_latest_commit: _sensor_state
    permissionlesstech_bitchat_latest_commit: _sensor_state
    pirate_weather_pirate_weather_ha_latest_commit: _sensor_state
    psp_archive_psp_ftpd_latest_commit: _sensor_state
    public_apis_public_apis_latest_commit: _sensor_state
    sythsaz_home_assistant_latest_commit: _sensor_state
    taschenbuch_blishhud_farmingtracker_latest_commit: _sensor_state
    tiimgreen_github_cheat_sheet_latest_commit: _sensor_state
    vinta_awesome_python_latest_commit: _sensor_state
    viatsko_awesome_vscode_latest_commit: _sensor_state
    wasabeef_awesome_android_ui_latest_commit: _sensor_state
    waujito_tpllax1500gpl_latest_commit: _sensor_state
    basnijholt_adaptive_lighting_latest_discussion: _sensor_state
    boralyl_cookiecutter_homeassistant_component_latest_discussion: _sensor_state
    boralyl_steam_wishlist_latest_discussion: _sensor_state
    bportaluri_wifiesp_latest_discussion: _sensor_state
    build_wars_gw1_database_latest_discussion: _sensor_state
    custom_cards_upcoming_media_card_latest_discussion: _sensor_state
    custom_components_pyscript_latest_discussion: _sensor_state
    custom_components_sensor_plex_recently_added_latest_discussion: _sensor_state
    home_assistant_addons_latest_discussion: _sensor_state
    home_assistant_home_assistant_io_latest_discussion: _sensor_state
    home_assistant_ios_latest_discussion: _sensor_state
    huggingface_transformers_latest_discussion: _sensor_state
    leikoilja_ha_google_home_latest_discussion: _sensor_state
    librehardwaremonitor_librehardwaremonitor_latest_discussion: _sensor_state
    limych_ha_tor_check_latest_discussion: _sensor_state
    ludeeus_integration_blueprint_latest_discussion: _sensor_state
    maselkov_gw2bot_latest_discussion: _sensor_state
    mweinelt_ha_prometheus_sensor_latest_discussion: _sensor_state
    nationalsecurityagency_ghidra_latest_discussion: _sensor_state
    oncleben31_cookiecutter_homeassistant_custom_component_latest_discussion: _sensor_state
    permissionlesstech_bitchat_latest_discussion: _sensor_state
    pirate_weather_pirate_weather_ha_latest_discussion: _sensor_state
    psp_archive_psp_ftpd_latest_discussion: _sensor_state
    public_apis_public_apis_latest_discussion: _sensor_state
    sythsaz_home_assistant_latest_discussion: _sensor_state
    taschenbuch_blishhud_farmingtracker_latest_discussion: _sensor_state
    tiimgreen_github_cheat_sheet_latest_discussion: _sensor_state
    vinta_awesome_python_latest_discussion: _sensor_state
    viatsko_awesome_vscode_latest_discussion: _sensor_state
    wasabeef_awesome_android_ui_latest_discussion: _sensor_state
    waujito_tpllax1500gpl_latest_discussion: _sensor_state
    basnijholt_adaptive_lighting_latest_release: _sensor_state
    boralyl_cookiecutter_homeassistant_component_latest_release: _sensor_state
    boralyl_steam_wishlist_latest_release: _sensor_state
    bportaluri_wifiesp_latest_release: _sensor_state
    build_wars_gw1_database_latest_release: _sensor_state
    custom_cards_upcoming_media_card_latest_release: _sensor_state
    custom_components_pyscript_latest_release: _sensor_state
    custom_components_sensor_plex_recently_added_latest_release: _sensor_state
    home_assistant_addons_latest_release: _sensor_state
    home_assistant_home_assistant_io_latest_release: _sensor_state
    home_assistant_ios_latest_release: _sensor_state
    huggingface_transformers_latest_release: _sensor_state
    leikoilja_ha_google_home_latest_release: _sensor_state
    librehardwaremonitor_librehardwaremonitor_latest_release: _sensor_state
    limych_ha_tor_check_latest_release: _sensor_state
    ludeeus_integration_blueprint_latest_release: _sensor_state
    maselkov_gw2bot_latest_release: _sensor_state
    mweinelt_ha_prometheus_sensor_latest_release: _sensor_state
    nationalsecurityagency_ghidra_latest_release: _sensor_state
    oncleben31_cookiecutter_homeassistant_custom_component_latest_release: _sensor_state
    permissionlesstech_bitchat_latest_release: _sensor_state
    pirate_weather_pirate_weather_ha_latest_release: _sensor_state
    psp_archive_psp_ftpd_latest_release: _sensor_state
    public_apis_public_apis_latest_release: _sensor_state
    sythsaz_home_assistant_latest_release: _sensor_state
    taschenbuch_blishhud_farmingtracker_latest_release: _sensor_state
    tiimgreen_github_cheat_sheet_latest_release: _sensor_state
    vinta_awesome_python_latest_release: _sensor_state
    viatsko_awesome_vscode_latest_release: _sensor_state
    wasabeef_awesome_android_ui_latest_release: _sensor_state
    waujito_tpllax1500gpl_latest_release: _sensor_state
    basnijholt_adaptive_lighting_latest_issue: _sensor_state
    boralyl_cookiecutter_homeassistant_component_latest_issue: _sensor_state
    boralyl_steam_wishlist_latest_issue: _sensor_state
    bportaluri_wifiesp_latest_issue: _sensor_state
    build_wars_gw1_database_latest_issue: _sensor_state
    custom_cards_upcoming_media_card_latest_issue: _sensor_state
    custom_components_pyscript_latest_issue: _sensor_state
    custom_components_sensor_plex_recently_added_latest_issue: _sensor_state
    home_assistant_addons_latest_issue: _sensor_state
    home_assistant_home_assistant_io_latest_issue: _sensor_state
    home_assistant_ios_latest_issue: _sensor_state
    huggingface_transformers_latest_issue: _sensor_state
    leikoilja_ha_google_home_latest_issue: _sensor_state
    librehardwaremonitor_librehardwaremonitor_latest_issue: _sensor_state
    limych_ha_tor_check_latest_issue: _sensor_state
    ludeeus_integration_blueprint_latest_issue: _sensor_state
    maselkov_gw2bot_latest_issue: _sensor_state
    mweinelt_ha_prometheus_sensor_latest_issue: _sensor_state
    nationalsecurityagency_ghidra_latest_issue: _sensor_state
    oncleben31_cookiecutter_homeassistant_custom_component_latest_issue: _sensor_state
    permissionlesstech_bitchat_latest_issue: _sensor_state
    pirate_weather_pirate_weather_ha_latest_issue: _sensor_state
    psp_archive_psp_ftpd_latest_issue: _sensor_state
    public_apis_public_apis_latest_issue: _sensor_state
    sythsaz_home_assistant_latest_issue: _sensor_state
    taschenbuch_blishhud_farmingtracker_latest_issue: _sensor_state
    tiimgreen_github_cheat_sheet_latest_issue: _sensor_state
    vinta_awesome_python_latest_issue: _sensor_state
    viatsko_awesome_vscode_latest_issue: _sensor_state
    wasabeef_awesome_android_ui_latest_issue: _sensor_state
    waujito_tpllax1500gpl_latest_issue: _sensor_state
    basnijholt_adaptive_lighting_latest_pull_request: _sensor_state
    boralyl_cookiecutter_homeassistant_component_latest_pull_request: _sensor_state
    boralyl_steam_wishlist_latest_pull_request: _sensor_state
    bportaluri_wifiesp_latest_pull_request: _sensor_state
    build_wars_gw1_database_latest_pull_request: _sensor_state
    custom_cards_upcoming_media_card_latest_pull_request: _sensor_state
    custom_components_pyscript_latest_pull_request: _sensor_state
    custom_components_sensor_plex_recently_added_latest_pull_request: _sensor_state
    home_assistant_addons_latest_pull_request: _sensor_state
    home_assistant_home_assistant_io_latest_pull_request: _sensor_state
    home_assistant_ios_latest_pull_request: _sensor_state
    huggingface_transformers_latest_pull_request: _sensor_state
    leikoilja_ha_google_home_latest_pull_request: _sensor_state
    librehardwaremonitor_librehardwaremonitor_latest_pull_request: _sensor_state
    limych_ha_tor_check_latest_pull_request: _sensor_state
    ludeeus_integration_blueprint_latest_pull_request: _sensor_state
    maselkov_gw2bot_latest_pull_request: _sensor_state
    mweinelt_ha_prometheus_sensor_latest_pull_request: _sensor_state
    nationalsecurityagency_ghidra_latest_pull_request: _sensor_state
    oncleben31_cookiecutter_homeassistant_custom_component_latest_pull_request: _sensor_state
    permissionlesstech_bitchat_latest_pull_request: _sensor_state
    pirate_weather_pirate_weather_ha_latest_pull_request: _sensor_state
    psp_archive_psp_ftpd_latest_pull_request: _sensor_state
    public_apis_public_apis_latest_pull_request: _sensor_state
    sythsaz_home_assistant_latest_pull_request: _sensor_state
    taschenbuch_blishhud_farmingtracker_latest_pull_request: _sensor_state
    tiimgreen_github_cheat_sheet_latest_pull_request: _sensor_state
    vinta_awesome_python_latest_pull_request: _sensor_state
    viatsko_awesome_vscode_latest_pull_request: _sensor_state
    wasabeef_awesome_android_ui_latest_pull_request: _sensor_state
    waujito_tpllax1500gpl_latest_pull_request: _sensor_state
    basnijholt_adaptive_lighting_latest_tag: _sensor_state
    boralyl_cookiecutter_homeassistant_component_latest_tag: _sensor_state
    boralyl_steam_wishlist_latest_tag: _sensor_state
    bportaluri_wifiesp_latest_tag: _sensor_state
    build_wars_gw1_database_latest_tag: _sensor_state
    custom_cards_upcoming_media_card_latest_tag: _sensor_state
    custom_components_pyscript_latest_tag: _sensor_state
    custom_components_sensor_plex_recently_added_latest_tag: _sensor_state
    home_assistant_addons_latest_tag: _sensor_state
    home_assistant_home_assistant_io_latest_tag: _sensor_state
    home_assistant_ios_latest_tag: _sensor_state
    huggingface_transformers_latest_tag: _sensor_state
    leikoilja_ha_google_home_latest_tag: _sensor_state
    librehardwaremonitor_librehardwaremonitor_latest_tag: _sensor_state
    limych_ha_tor_check_latest_tag: _sensor_state
    ludeeus_integration_blueprint_latest_tag: _sensor_state
    maselkov_gw2bot_latest_tag: _sensor_state
    mweinelt_ha_prometheus_sensor_latest_tag: _sensor_state
    nationalsecurityagency_ghidra_latest_tag: _sensor_state
    oncleben31_cookiecutter_homeassistant_custom_component_latest_tag: _sensor_state
    permissionlesstech_bitchat_latest_tag: _sensor_state
    pirate_weather_pirate_weather_ha_latest_tag: _sensor_state
    psp_archive_psp_ftpd_latest_tag: _sensor_state
    public_apis_public_apis_latest_tag: _sensor_state
    sythsaz_home_assistant_latest_tag: _sensor_state
    taschenbuch_blishhud_farmingtracker_latest_tag: _sensor_state
    tiimgreen_github_cheat_sheet_latest_tag: _sensor_state
    vinta_awesome_python_latest_tag: _sensor_state
    viatsko_awesome_vscode_latest_tag: _sensor_state
    wasabeef_awesome_android_ui_latest_tag: _sensor_state
    waujito_tpllax1500gpl_latest_tag: _sensor_state
    bedroom_closet_door_battery_type: _sensor_state
    bedroom_closet_door_battery_last_replaced: _sensor_state
    bedroom_closet_door_battery_plus: _sensor_state
    furnace_room_door_battery_type: _sensor_state
    furnace_room_door_battery_last_replaced: _sensor_state
    furnace_room_door_battery_plus: _sensor_state
    ipad_battery_type: _sensor_state
    ipad_battery_last_replaced: _sensor_state
    ipad_battery_plus: _sensor_state
    s9_battery_type: _sensor_state
    s9_battery_last_replaced: _sensor_state
    s9_battery_plus: _sensor_state
    syth_battery_type: _sensor_state
    syth_battery_last_replaced: _sensor_state
    syth_battery_plus: _sensor_state
    local_ip: _sensor_state
    neo_watcher_potentially_hazardous_16th: _sensor_state
    neo_watcher_potentially_hazardous_17th: _sensor_state
    env_can_advisory_titles: _sensor_state
    env_can_warning_titles: _sensor_state
    env_can_watches_titles: _sensor_state
    syth_tailscale_browser_id: _sensor_state
    telegram_client_zashtys_id: _sensor_state
    telegram_client_zashtys_username: _sensor_state
    telegram_client_zashtys_last_name: _sensor_state
    telegram_client_zashtys_first_name: _sensor_state
    telegram_client_zashtys_phone: _sensor_state
    telegram_client_zashtys_last_sent_message_id: _sensor_state
    telegram_client_zashtys_last_edited_message_id: _sensor_state
    telegram_client_zashtys_last_deleted_message_id: _sensor_state
    opnsense_dhcp_leases_lan_2: _sensor_state
    opnsense_sythsaz_dpdns_org: _sensor_state
    opnsense_sythsaz_dpdns_org_ipv6: _sensor_state
    neo_watcher_potentially_hazardous_18th: _sensor_state
    genius_lyrics_plex_plex_for_android_tv_chromecast_google_tv_lyrics: _sensor_state
    imap_sythsaz_gmail_com_messages: _sensor_state
    neo_watcher_potentially_hazardous_19th: _sensor_state
    hwmon_temperatures_dell_smm_cpu: _sensor_state
    hwmon_temperatures_dell_smm_ambient: _sensor_state
    hwmon_temperatures_radeon: _sensor_state
    hwmon_temperatures_package_id_0: _sensor_state
    hwmon_temperatures_core_0: _sensor_state
    hwmon_temperatures_core_1: _sensor_state
    hwmon_temperatures_core_2: _sensor_state
    hwmon_temperatures_core_3: _sensor_state
    genius_lyrics_magic_areas_media_player_groups_bedroom_media_player_group_lyrics: _sensor_state
    sythsaz_dpdns_org_admin: _sensor_state
    sythsaz_dpdns_org_created: _sensor_state
    sythsaz_dpdns_org_days_until_expiration: _sensor_state
    sythsaz_dpdns_org_expires: _sensor_state
    sythsaz_dpdns_org_last_updated: _sensor_state
    sythsaz_dpdns_org_owner: _sensor_state
    sythsaz_dpdns_org_registrant: _sensor_state
    sythsaz_dpdns_org_registrar: _sensor_state
    sythsaz_dpdns_org_reseller: _sensor_state
    sythsaz_dpdns_org_status: _sensor_state
    local_api_version: _sensor_state
    local_kernel_version: _sensor_state
    local_operating_system: _sensor_state
    local_operating_system_version: _sensor_state
    local_docker_version: _sensor_state
    local_architecture: _sensor_state
    local_container_count: _sensor_state
    local_containers_running: _sensor_state
    local_containers_stopped: _sensor_state
    local_image_count: _sensor_state
    local_total_memory: _sensor_state
    local_total_cpu: _sensor_state
    homeassistant_image: _sensor_state
    piper_image: _sensor_state
    whisper_image: _sensor_state
    wordpress_wordpress_1_image: _sensor_state
    esphome_image: _sensor_state
    portainer_image: _sensor_state
    music_assistant_image: _sensor_state
    prometheus_image: _sensor_state
    mailcowdockerized_watchdog_mailcow_1_image: _sensor_state
    mailcowdockerized_acme_mailcow_1_image: _sensor_state
    mailcowdockerized_nginx_mailcow_1_image: _sensor_state
    mailcowdockerized_ofelia_mailcow_1_image: _sensor_state
    mailcowdockerized_rspamd_mailcow_1_image: _sensor_state
    mailcowdockerized_postfix_mailcow_1_image: _sensor_state
    mailcowdockerized_dovecot_mailcow_1_image: _sensor_state
    mailcowdockerized_php_fpm_mailcow_1_image: _sensor_state
    mailcowdockerized_mysql_mailcow_1_image: _sensor_state
    mailcowdockerized_clamd_mailcow_1_image: _sensor_state
    mailcowdockerized_postfix_tlspol_mailcow_1_image: _sensor_state
    mailcowdockerized_redis_mailcow_1_image: _sensor_state
    mailcowdockerized_sogo_mailcow_1_image: _sensor_state
    mailcowdockerized_dockerapi_mailcow_1_image: _sensor_state
    mailcowdockerized_olefy_mailcow_1_image: _sensor_state
    mailcowdockerized_memcached_mailcow_1_image: _sensor_state
    mailcowdockerized_unbound_mailcow_1_image: _sensor_state
    mailcowdockerized_netfilter_mailcow_1_image: _sensor_state
    plex_image: _sensor_state
    frigate_image: _sensor_state
    wordpress_db_1_image: _sensor_state
    watchtower_image: _sensor_state
    tasmoadmin_image: _sensor_state
    scrutiny_image: _sensor_state
    opnsense_exporter_image: _sensor_state
    nodered_image: _sensor_state
    grafana_image: _sensor_state
    timescaledb_poc_image: _sensor_state
    postgres_exporter_image: _sensor_state
    zashtys_status: _sensor_state
    zashtys_gamer_score: _sensor_state
    zashtys_last_online: _sensor_state
    zashtys_following: _sensor_state
    zashtys_follower: _sensor_state
    zashtys_now_playing: _sensor_state
    ziji: _sensor_state
    lilyvelour: _sensor_state
    skyhook: _sensor_state
    redspecter23: _sensor_state
    tiptoethetank: _sensor_state
    justjakenlina: _sensor_state
    bombasticsly: _sensor_state
    obkatiekat: _sensor_state
    sirantakouhi: _sensor_state
    brokendejavu: _sensor_state
    ayinmaiden: _sensor_state
    wendilunar: _sensor_state
    ultrareviewshow: _sensor_state
    heroinedark7734: _sensor_state
    mightyteapot: _sensor_state
    admiralbahroo: _sensor_state
    viking_carebear: _sensor_state
    timelyfoxstudios: _sensor_state
    enyokitty: _sensor_state
    itmejp: _sensor_state
    shroud: _sensor_state
    addyvillimey: _sensor_state
    kewnedragon: _sensor_state
    zentreya: _sensor_state
    ironmouse: _sensor_state
    gcxevent: _sensor_state
    onesassycat: _sensor_state
    studytme: _sensor_state
    minikomew: _sensor_state
    sequisha: _sensor_state
    kiwelyndiopside: _sensor_state
    floraleibloodwood: _sensor_state
    aegyaegy: _sensor_state
    lowleveltv: _sensor_state
    mela: _sensor_state
    mrsdyad: _sensor_state
    berylbones: _sensor_state
    tatsuya_inc: _sensor_state
    jannidegen: _sensor_state
    malchemisttv: _sensor_state
    ordsighelm: _sensor_state
    meatbeastt: _sensor_state
    reggielc: _sensor_state
    booberry_mischief: _sensor_state
    engelburtmeow: _sensor_state
    filian: _sensor_state
    theprimeagen: _sensor_state
    justsaydizz: _sensor_state
    cynder8342: _sensor_state
    iseemangos: _sensor_state
    stankrat: _sensor_state
    vedal987: _sensor_state
    leomonaz: _sensor_state
    torovi03: _sensor_state
    arilozen: _sensor_state
    aurorapeachy: _sensor_state
    jjiinxymayalyneah: _sensor_state
    bashbunni: _sensor_state
    taylien: _sensor_state
    azureavocado: _sensor_state
    angelwriter428: _sensor_state
    zeplahq: _sensor_state
    premiertwo: _sensor_state
    puinacuppa: _sensor_state
    bluespecter23: _sensor_state
    bazza: _sensor_state
    acottonsockk: _sensor_state
    shxtou: _sensor_state
    simpleflips: _sensor_state
    juspar: _sensor_state
    cdawgva: _sensor_state
    dooper: _sensor_state
    ferretsoftware: _sensor_state
    squchan: _sensor_state
    solartoker: _sensor_state
    zeusxperience: _sensor_state
    doigswift: _sensor_state
    aicandii: _sensor_state
    limealicious: _sensor_state
    springsims: _sensor_state
    kitboga: _sensor_state
    jusparr: _sensor_state
    zefrine: _sensor_state
    dabswithnate: _sensor_state
    thespudhunter: _sensor_state
    arva: _sensor_state
    godotengine_official: _sensor_state
    alveussanctuary: _sensor_state
    mukluk: _sensor_state
    justfaelia: _sensor_state
    barnacules: _sensor_state
    whitevault: _sensor_state
    piratesoftware: _sensor_state
    excessiveprofanity: _sensor_state
    neo_watcher_potentially_hazardous_20th: _sensor_state
    intel_xeon_e3_1246_v3_cpu_core_voltage: _sensor_state
    intel_xeon_e3_1246_v3_cpu_core_1_voltage: _sensor_state
    intel_xeon_e3_1246_v3_cpu_core_2_voltage: _sensor_state
    intel_xeon_e3_1246_v3_cpu_core_3_voltage: _sensor_state
    intel_xeon_e3_1246_v3_cpu_core_4_voltage: _sensor_state
    intel_xeon_e3_1246_v3_cpu_package_power: _sensor_state
    intel_xeon_e3_1246_v3_cpu_cores_power: _sensor_state
    intel_xeon_e3_1246_v3_cpu_memory_power: _sensor_state
    intel_xeon_e3_1246_v3_bus_speed_clock: _sensor_state
    intel_xeon_e3_1246_v3_cpu_core_1_clock: _sensor_state
    intel_xeon_e3_1246_v3_cpu_core_2_clock: _sensor_state
    intel_xeon_e3_1246_v3_cpu_core_3_clock: _sensor_state
    intel_xeon_e3_1246_v3_cpu_core_4_clock: _sensor_state
    intel_xeon_e3_1246_v3_core_max_temperature: _sensor_state
    intel_xeon_e3_1246_v3_core_average_temperature: _sensor_state
    intel_xeon_e3_1246_v3_cpu_core_1_temperature: _sensor_state
    intel_xeon_e3_1246_v3_cpu_core_2_temperature: _sensor_state
    intel_xeon_e3_1246_v3_cpu_core_3_temperature: _sensor_state
    intel_xeon_e3_1246_v3_cpu_core_4_temperature: _sensor_state
    intel_xeon_e3_1246_v3_cpu_package_temperature: _sensor_state
    intel_xeon_e3_1246_v3_cpu_core_1_distance_to_tjmax_temperature: _sensor_state
    intel_xeon_e3_1246_v3_cpu_core_2_distance_to_tjmax_temperature: _sensor_state
    intel_xeon_e3_1246_v3_cpu_core_3_distance_to_tjmax_temperature: _sensor_state
    intel_xeon_e3_1246_v3_cpu_core_4_distance_to_tjmax_temperature: _sensor_state
    intel_xeon_e3_1246_v3_cpu_total_load: _sensor_state
    intel_xeon_e3_1246_v3_cpu_core_max_load: _sensor_state
    intel_xeon_e3_1246_v3_cpu_core_1_thread_1_load: _sensor_state
    intel_xeon_e3_1246_v3_cpu_core_1_thread_2_load: _sensor_state
    intel_xeon_e3_1246_v3_cpu_core_2_thread_1_load: _sensor_state
    intel_xeon_e3_1246_v3_cpu_core_2_thread_2_load: _sensor_state
    intel_xeon_e3_1246_v3_cpu_core_3_thread_1_load: _sensor_state
    intel_xeon_e3_1246_v3_cpu_core_3_thread_2_load: _sensor_state
    intel_xeon_e3_1246_v3_cpu_core_4_thread_1_load: _sensor_state
    intel_xeon_e3_1246_v3_cpu_core_4_thread_2_load: _sensor_state
    generic_memory_memory_load: _sensor_state
    generic_memory_virtual_memory_load: _sensor_state
    generic_memory_memory_used_data: _sensor_state
    generic_memory_memory_available_data: _sensor_state
    generic_memory_virtual_memory_used_data: _sensor_state
    generic_memory_virtual_memory_available_data: _sensor_state
    homeassistant_memory_limit: _sensor_state
    homeassistant_memory_usage: _sensor_state
    homeassistant_memory_usage_percentage: _sensor_state
    homeassistant_cpu_usage_total: _sensor_state
    nodered_memory_limit: _sensor_state
    nodered_memory_usage: _sensor_state
    nodered_memory_usage_percentage: _sensor_state
    nodered_cpu_usage_total: _sensor_state
    esphome_memory_limit: _sensor_state
    esphome_memory_usage: _sensor_state
    esphome_memory_usage_percentage: _sensor_state
    esphome_cpu_usage_total: _sensor_state
    wordpress_db_1_memory_limit: _sensor_state
    wordpress_db_1_memory_usage: _sensor_state
    wordpress_db_1_memory_usage_percentage: _sensor_state
    wordpress_db_1_cpu_usage_total: _sensor_state
    wordpress_wordpress_1_memory_limit: _sensor_state
    wordpress_wordpress_1_memory_usage: _sensor_state
    wordpress_wordpress_1_memory_usage_percentage: _sensor_state
    wordpress_wordpress_1_cpu_usage_total: _sensor_state
    portainer_memory_limit: _sensor_state
    portainer_memory_usage: _sensor_state
    portainer_memory_usage_percentage: _sensor_state
    portainer_cpu_usage_total: _sensor_state
    plex_memory_limit: _sensor_state
    plex_memory_usage: _sensor_state
    plex_memory_usage_percentage: _sensor_state
    plex_cpu_usage_total: _sensor_state
    prometheus_memory_limit: _sensor_state
    prometheus_memory_usage: _sensor_state
    prometheus_memory_usage_percentage: _sensor_state
    prometheus_cpu_usage_total: _sensor_state
    mailcowdockerized_mysql_mailcow_1_memory_limit: _sensor_state
    mailcowdockerized_mysql_mailcow_1_memory_usage: _sensor_state
    mailcowdockerized_mysql_mailcow_1_memory_usage_percentage: _sensor_state
    mailcowdockerized_mysql_mailcow_1_cpu_usage_total: _sensor_state
    music_assistant_memory_limit: _sensor_state
    music_assistant_memory_usage: _sensor_state
    music_assistant_memory_usage_percentage: _sensor_state
    music_assistant_cpu_usage_total: _sensor_state
    piper_memory_limit: _sensor_state
    piper_memory_usage: _sensor_state
    piper_memory_usage_percentage: _sensor_state
    piper_cpu_usage_total: _sensor_state
    whisper_memory_limit: _sensor_state
    whisper_memory_usage: _sensor_state
    whisper_memory_usage_percentage: _sensor_state
    whisper_cpu_usage_total: _sensor_state
    mailcowdockerized_watchdog_mailcow_1_memory_limit: _sensor_state
    mailcowdockerized_watchdog_mailcow_1_memory_usage: _sensor_state
    mailcowdockerized_watchdog_mailcow_1_memory_usage_percentage: _sensor_state
    mailcowdockerized_watchdog_mailcow_1_cpu_usage_total: _sensor_state
    mailcowdockerized_acme_mailcow_1_memory_limit: _sensor_state
    mailcowdockerized_acme_mailcow_1_memory_usage: _sensor_state
    mailcowdockerized_acme_mailcow_1_memory_usage_percentage: _sensor_state
    mailcowdockerized_acme_mailcow_1_cpu_usage_total: _sensor_state
    mailcowdockerized_nginx_mailcow_1_memory_limit: _sensor_state
    mailcowdockerized_nginx_mailcow_1_memory_usage: _sensor_state
    mailcowdockerized_nginx_mailcow_1_memory_usage_percentage: _sensor_state
    mailcowdockerized_nginx_mailcow_1_cpu_usage_total: _sensor_state
    mailcowdockerized_ofelia_mailcow_1_memory_limit: _sensor_state
    mailcowdockerized_ofelia_mailcow_1_memory_usage: _sensor_state
    mailcowdockerized_ofelia_mailcow_1_memory_usage_percentage: _sensor_state
    mailcowdockerized_ofelia_mailcow_1_cpu_usage_total: _sensor_state
    mailcowdockerized_rspamd_mailcow_1_memory_limit: _sensor_state
    mailcowdockerized_rspamd_mailcow_1_memory_usage: _sensor_state
    mailcowdockerized_rspamd_mailcow_1_memory_usage_percentage: _sensor_state
    mailcowdockerized_rspamd_mailcow_1_cpu_usage_total: _sensor_state
    mailcowdockerized_postfix_mailcow_1_memory_limit: _sensor_state
    mailcowdockerized_postfix_mailcow_1_memory_usage: _sensor_state
    mailcowdockerized_postfix_mailcow_1_memory_usage_percentage: _sensor_state
    mailcowdockerized_postfix_mailcow_1_cpu_usage_total: _sensor_state
    mailcowdockerized_dovecot_mailcow_1_memory_limit: _sensor_state
    mailcowdockerized_dovecot_mailcow_1_memory_usage: _sensor_state
    mailcowdockerized_dovecot_mailcow_1_memory_usage_percentage: _sensor_state
    mailcowdockerized_dovecot_mailcow_1_cpu_usage_total: _sensor_state
    mailcowdockerized_php_fpm_mailcow_1_memory_limit: _sensor_state
    mailcowdockerized_php_fpm_mailcow_1_memory_usage: _sensor_state
    mailcowdockerized_php_fpm_mailcow_1_memory_usage_percentage: _sensor_state
    mailcowdockerized_php_fpm_mailcow_1_cpu_usage_total: _sensor_state
    mailcowdockerized_clamd_mailcow_1_memory_limit: _sensor_state
    mailcowdockerized_clamd_mailcow_1_memory_usage: _sensor_state
    mailcowdockerized_clamd_mailcow_1_memory_usage_percentage: _sensor_state
    mailcowdockerized_clamd_mailcow_1_cpu_usage_total: _sensor_state
    mailcowdockerized_postfix_tlspol_mailcow_1_memory_limit: _sensor_state
    mailcowdockerized_postfix_tlspol_mailcow_1_memory_usage: _sensor_state
    mailcowdockerized_postfix_tlspol_mailcow_1_memory_usage_percentage: _sensor_state
    mailcowdockerized_postfix_tlspol_mailcow_1_cpu_usage_total: _sensor_state
    mailcowdockerized_redis_mailcow_1_memory_limit: _sensor_state
    mailcowdockerized_redis_mailcow_1_memory_usage: _sensor_state
    mailcowdockerized_redis_mailcow_1_memory_usage_percentage: _sensor_state
    mailcowdockerized_redis_mailcow_1_cpu_usage_total: _sensor_state
    mailcowdockerized_sogo_mailcow_1_memory_limit: _sensor_state
    mailcowdockerized_sogo_mailcow_1_memory_usage: _sensor_state
    mailcowdockerized_sogo_mailcow_1_memory_usage_percentage: _sensor_state
    mailcowdockerized_sogo_mailcow_1_cpu_usage_total: _sensor_state
    mailcowdockerized_dockerapi_mailcow_1_memory_limit: _sensor_state
    mailcowdockerized_dockerapi_mailcow_1_memory_usage: _sensor_state
    mailcowdockerized_dockerapi_mailcow_1_memory_usage_percentage: _sensor_state
    mailcowdockerized_dockerapi_mailcow_1_cpu_usage_total: _sensor_state
    mailcowdockerized_olefy_mailcow_1_memory_limit: _sensor_state
    mailcowdockerized_olefy_mailcow_1_memory_usage: _sensor_state
    mailcowdockerized_olefy_mailcow_1_memory_usage_percentage: _sensor_state
    mailcowdockerized_olefy_mailcow_1_cpu_usage_total: _sensor_state
    mailcowdockerized_memcached_mailcow_1_memory_limit: _sensor_state
    mailcowdockerized_memcached_mailcow_1_memory_usage: _sensor_state
    mailcowdockerized_memcached_mailcow_1_memory_usage_percentage: _sensor_state
    mailcowdockerized_memcached_mailcow_1_cpu_usage_total: _sensor_state
    mailcowdockerized_unbound_mailcow_1_memory_limit: _sensor_state
    mailcowdockerized_unbound_mailcow_1_memory_usage: _sensor_state
    mailcowdockerized_unbound_mailcow_1_memory_usage_percentage: _sensor_state
    mailcowdockerized_unbound_mailcow_1_cpu_usage_total: _sensor_state
    mailcowdockerized_netfilter_mailcow_1_memory_limit: _sensor_state
    mailcowdockerized_netfilter_mailcow_1_memory_usage: _sensor_state
    mailcowdockerized_netfilter_mailcow_1_memory_usage_percentage: _sensor_state
    mailcowdockerized_netfilter_mailcow_1_cpu_usage_total: _sensor_state
    frigate_memory_limit: _sensor_state
    frigate_memory_usage: _sensor_state
    frigate_memory_usage_percentage: _sensor_state
    frigate_cpu_usage_total: _sensor_state
    watchtower_memory_limit: _sensor_state
    watchtower_memory_usage: _sensor_state
    watchtower_memory_usage_percentage: _sensor_state
    watchtower_cpu_usage_total: _sensor_state
    tasmoadmin_memory_limit: _sensor_state
    tasmoadmin_memory_usage: _sensor_state
    tasmoadmin_memory_usage_percentage: _sensor_state
    tasmoadmin_cpu_usage_total: _sensor_state
    scrutiny_memory_limit: _sensor_state
    scrutiny_memory_usage: _sensor_state
    scrutiny_memory_usage_percentage: _sensor_state
    scrutiny_cpu_usage_total: _sensor_state
    opnsense_exporter_memory_limit: _sensor_state
    opnsense_exporter_memory_usage: _sensor_state
    opnsense_exporter_memory_usage_percentage: _sensor_state
    opnsense_exporter_cpu_usage_total: _sensor_state
    grafana_memory_limit: _sensor_state
    grafana_memory_usage: _sensor_state
    grafana_memory_usage_percentage: _sensor_state
    grafana_cpu_usage_total: _sensor_state
    timescaledb_poc_memory_limit: _sensor_state
    timescaledb_poc_memory_usage: _sensor_state
    timescaledb_poc_memory_usage_percentage: _sensor_state
    timescaledb_poc_cpu_usage_total: _sensor_state
    postgres_exporter_memory_limit: _sensor_state
    postgres_exporter_memory_usage: _sensor_state
    postgres_exporter_memory_usage_percentage: _sensor_state
    postgres_exporter_cpu_usage_total: _sensor_state
    russell117045_trophy_level: _sensor_state
    russell117045_next_level: _sensor_state
    russell117045_platinum_trophies: _sensor_state
    russell117045_gold_trophies: _sensor_state
    russell117045_silver_trophies: _sensor_state
    russell117045_bronze_trophies: _sensor_state
    howler4522_trophy_level: _sensor_state
    howler4522_next_level: _sensor_state
    howler4522_platinum_trophies: _sensor_state
    howler4522_gold_trophies: _sensor_state
    howler4522_silver_trophies: _sensor_state
    howler4522_bronze_trophies: _sensor_state
    toxiccrumble_trophy_level: _sensor_state
    toxiccrumble_next_level: _sensor_state
    toxiccrumble_platinum_trophies: _sensor_state
    toxiccrumble_gold_trophies: _sensor_state
    toxiccrumble_silver_trophies: _sensor_state
    toxiccrumble_bronze_trophies: _sensor_state
    jusparr_trophy_level: _sensor_state
    jusparr_next_level: _sensor_state
    jusparr_platinum_trophies: _sensor_state
    jusparr_gold_trophies: _sensor_state
    jusparr_silver_trophies: _sensor_state
    jusparr_bronze_trophies: _sensor_state
    zashtys_friends: _sensor_state
    zashtys_in_party: _sensor_state
    zashtys_party_join_restrictions: _sensor_state
    backyard_camera_hq_review_status: _sensor_state
    moon_astro_next_full_moon_name: _sensor_state
    moon_astro_next_full_moon_alternative_names: _sensor_state
    moon_astro_zodiac_sign_current: _sensor_state
    moon_astro_none: _sensor_state
    moon_astro_previous_rise: _sensor_state
    moon_astro_previous_set: _sensor_state
    moon_astro_previous_apogee: _sensor_state
    moon_astro_previous_perigee: _sensor_state
    moon_astro_previous_first_quarter: _sensor_state
    moon_astro_previous_full_moon: _sensor_state
    moon_astro_previous_last_quarter: _sensor_state
    moon_astro_previous_new_moon: _sensor_state
    moon_astro_previous_full_moon_name: _sensor_state
    moon_astro_previous_full_moon_alternative_names: _sensor_state
    moon_astro_ecliptic_longitude_at_previous_full_moon: _sensor_state
    moon_astro_ecliptic_latitude_at_previous_full_moon: _sensor_state
    moon_astro_ecliptic_longitude_at_previous_new_moon: _sensor_state
    moon_astro_ecliptic_latitude_at_previous_new_moon: _sensor_state
    moon_astro_zodiac_sign_at_previous_full_moon: _sensor_state
    moon_astro_zodiac_sign_at_previous_new_moon: _sensor_state
    moon_astro_zodiac_degree_at_previous_new_moon: _sensor_state
    moon_astro_zodiac_degree_at_previous_full_moon: _sensor_state
    ashtonparrott_gmail_com_total_available_storage: _sensor_state
    ashtonparrott_gmail_com_used_storage: _sensor_state
    jusparr_status: _sensor_state
    jusparr_gamer_score: _sensor_state
    jusparr_last_online_2: _sensor_state
    jusparr_following: _sensor_state
    jusparr_follower: _sensor_state
    jusparr_now_playing_2: _sensor_state
    jusparr_friends: _sensor_state
    jusparr_in_party: _sensor_state
    jusparr_party_join_restrictions: _sensor_state
    sig1325_status: _sensor_state
    sig1325_last_online: _sensor_state
    sig1325_following: _sensor_state
    sig1325_follower: _sensor_state
    sig1325_now_playing: _sensor_state
    sig1325_friends: _sensor_state
    sig1325_in_party: _sensor_state
    sig1325_party_join_restrictions: _sensor_state
    mrcolvan1_status: _sensor_state
    mrcolvan1_gamer_score: _sensor_state
    mrcolvan1_last_online: _sensor_state
    mrcolvan1_following: _sensor_state
    mrcolvan1_follower: _sensor_state
    mrcolvan1_now_playing: _sensor_state
    mrcolvan1_friends: _sensor_state
    mrcolvan1_in_party: _sensor_state
    mrcolvan1_party_join_restrictions: _sensor_state
    maxdeath397_status: _sensor_state
    maxdeath397_gamer_score: _sensor_state
    maxdeath397_last_online: _sensor_state
    maxdeath397_following: _sensor_state
    maxdeath397_follower: _sensor_state
    maxdeath397_now_playing: _sensor_state
    maxdeath397_friends: _sensor_state
    maxdeath397_in_party: _sensor_state
    maxdeath397_party_join_restrictions: _sensor_state
    lining_room_wifi_wan_ipv4_address: _sensor_state
    lining_room_wifi_lan_ipv4_address: _sensor_state
    dining_room_wifi_wan_ipv4_address: _sensor_state
    dining_room_wifi_lan_ipv4_address: _sensor_state
    nvidia_geforce_840m_gpu_core_clock: _sensor_state
    nvidia_geforce_840m_gpu_memory_clock: _sensor_state
    nvidia_geforce_840m_gpu_core_temperature: _sensor_state
    nvidia_geforce_840m_gpu_core_load: _sensor_state
    nvidia_geforce_840m_gpu_memory_controller_load: _sensor_state
    nvidia_geforce_840m_gpu_video_engine_load: _sensor_state
    nvidia_geforce_840m_gpu_bus_load: _sensor_state
    nvidia_geforce_840m_gpu_memory_free_smalldata: _sensor_state
    nvidia_geforce_840m_gpu_memory_used_smalldata: _sensor_state
    nvidia_geforce_840m_gpu_memory_total_smalldata: _sensor_state
    nvidia_geforce_840m_gpu_pcie_rx_throughput: _sensor_state
    nvidia_geforce_840m_gpu_pcie_tx_throughput: _sensor_state
    intel_r_hd_graphics_5500_gpu_power_power: _sensor_state
    intel_r_hd_graphics_5500_d3d_3d_load: _sensor_state
    intel_r_hd_graphics_5500_d3d_copy_load: _sensor_state
    intel_r_hd_graphics_5500_d3d_gdi_render_load: _sensor_state
    intel_r_hd_graphics_5500_d3d_other_load: _sensor_state
    intel_r_hd_graphics_5500_d3d_overlay_load: _sensor_state
    intel_r_hd_graphics_5500_d3d_video_decode_load: _sensor_state
    intel_r_hd_graphics_5500_d3d_video_decode_load_2: _sensor_state
    intel_r_hd_graphics_5500_d3d_video_processing_load: _sensor_state
    intel_r_hd_graphics_5500_d3d_video_processing_load_2: _sensor_state
    intel_r_hd_graphics_5500_d3d_shared_memory_used_smalldata: _sensor_state
    intel_r_hd_graphics_5500_d3d_shared_memory_free_smalldata: _sensor_state
    intel_r_hd_graphics_5500_d3d_shared_memory_total_smalldata: _sensor_state
    sythsaz_giveaway_bot_discussions: _sensor_state
    sythsaz_giveaway_bot_stars: _sensor_state
    sythsaz_giveaway_bot_watchers: _sensor_state
    sythsaz_giveaway_bot_forks: _sensor_state
    sythsaz_giveaway_bot_issues: _sensor_state
    sythsaz_giveaway_bot_pull_requests: _sensor_state
    sythsaz_giveaway_bot_latest_commit: _sensor_state
    sythsaz_giveaway_bot_latest_discussion: _sensor_state
    sythsaz_giveaway_bot_latest_release: _sensor_state
    sythsaz_giveaway_bot_latest_issue: _sensor_state
    sythsaz_giveaway_bot_latest_pull_request: _sensor_state
    sythsaz_giveaway_bot_latest_tag: _sensor_state
    flightradar24_airport_arrivals_on_time: _sensor_state
    flightradar24_airport_arrivals_delayed: _sensor_state
    flightradar24_airport_arrivals_canceled: _sensor_state
    flightradar24_airport_arrivals: _sensor_state
    flightradar24_airport_departures_on_time: _sensor_state
    flightradar24_airport_departures_delayed: _sensor_state
    flightradar24_airport_departures_canceled: _sensor_state
    flightradar24_airport_departures: _sensor_state
    mastodon_sythsaz_mastodon_social_last_post: _sensor_state
    mastodon_sythsaz_mastodon_social_username: _sensor_state
    homeassistant_state: _sensor_state
    esphome_state: _sensor_state
    wordpress_wordpress_1_state: _sensor_state
    scrutiny_state: _sensor_state
    wordpress_db_1_state: _sensor_state
    whisper_state: _sensor_state
    piper_state: _sensor_state
    music_assistant_state: _sensor_state
    frigate_state: _sensor_state
    plex_state: _sensor_state
    nodered_state: _sensor_state
    tasmoadmin_state: _sensor_state
    prometheus_state: _sensor_state
    portainer_state: _sensor_state
    watchtower_state: _sensor_state
    opnsense_exporter_state: _sensor_state
    grafana_state: _sensor_state
    timescaledb_poc_state: _sensor_state
    postgres_exporter_state: _sensor_state
    genius_lyrics_plex_plex_for_playstation_4_ps4_200_lyrics: _sensor_state
    jusparr_docker_api_version: _sensor_state
    jusparr_docker_kernel_version: _sensor_state
    jusparr_docker_operating_system: _sensor_state
    jusparr_docker_operating_system_version: _sensor_state
    jusparr_docker_docker_version: _sensor_state
    jusparr_docker_architecture: _sensor_state
    jusparr_docker_container_count: _sensor_state
    jusparr_docker_containers_running: _sensor_state
    jusparr_docker_containers_stopped: _sensor_state
    jusparr_docker_image_count: _sensor_state
    jusparr_docker_total_memory: _sensor_state
    jusparr_docker_total_cpu: _sensor_state
    portainer_agent_image: _sensor_state
    portainer_agent_state: _sensor_state
    portainer_agent_memory_limit: _sensor_state
    portainer_agent_memory_usage: _sensor_state
    portainer_agent_memory_usage_percentage: _sensor_state
    portainer_agent_cpu_usage_total: _sensor_state
    ha_esphome_1_image: _sensor_state
    ha_esphome_1_state: _sensor_state
    ha_esphome_1_memory_limit: _sensor_state
    ha_esphome_1_memory_usage: _sensor_state
    ha_esphome_1_memory_usage_percentage: _sensor_state
    ha_esphome_1_cpu_usage_total: _sensor_state
    ha_nodered_1_image: _sensor_state
    ha_nodered_1_state: _sensor_state
    ha_nodered_1_memory_limit: _sensor_state
    ha_nodered_1_memory_usage: _sensor_state
    ha_nodered_1_memory_usage_percentage: _sensor_state
    ha_nodered_1_cpu_usage_total: _sensor_state
    ha_watchtower_1_image: _sensor_state
    ha_watchtower_1_state: _sensor_state
    ha_watchtower_1_memory_limit: _sensor_state
    ha_watchtower_1_memory_usage: _sensor_state
    ha_watchtower_1_memory_usage_percentage: _sensor_state
    ha_watchtower_1_cpu_usage_total: _sensor_state
    ha_whisper_1_image: _sensor_state
    ha_whisper_1_state: _sensor_state
    ha_whisper_1_memory_limit: _sensor_state
    ha_whisper_1_memory_usage: _sensor_state
    ha_whisper_1_memory_usage_percentage: _sensor_state
    ha_whisper_1_cpu_usage_total: _sensor_state
    ha_piper_1_image: _sensor_state
    ha_piper_1_state: _sensor_state
    ha_piper_1_memory_limit: _sensor_state
    ha_piper_1_memory_usage: _sensor_state
    ha_piper_1_memory_usage_percentage: _sensor_state
    ha_piper_1_cpu_usage_total: _sensor_state
    ha_aircast_1_image: _sensor_state
    ha_aircast_1_state: _sensor_state
    ha_aircast_1_memory_limit: _sensor_state
    ha_aircast_1_memory_usage: _sensor_state
    ha_aircast_1_memory_usage_percentage: _sensor_state
    ha_aircast_1_cpu_usage_total: _sensor_state
    ha_scrutiny_1_image: _sensor_state
    ha_scrutiny_1_state: _sensor_state
    ha_scrutiny_1_memory_limit: _sensor_state
    ha_scrutiny_1_memory_usage: _sensor_state
    ha_scrutiny_1_memory_usage_percentage: _sensor_state
    ha_scrutiny_1_cpu_usage_total: _sensor_state
    mediamtx_image: _sensor_state
    mediamtx_state: _sensor_state
    mediamtx_memory_limit: _sensor_state
    mediamtx_memory_usage: _sensor_state
    mediamtx_memory_usage_percentage: _sensor_state
    mediamtx_cpu_usage_total: _sensor_state
    opnsense_data_received: _sensor_state
    opnsense_data_sent: _sensor_state
    opnsense_external_ip: _sensor_state
    opnsense_uptime: _sensor_state
    opnsense_wan_status: _sensor_state
    opnsense_number_of_port_mapping_entries_ipv4: _sensor_state
    opnsense_download_speed: _sensor_state
    opnsense_upload_speed: _sensor_state
    laptop_intel_core_i7_5500u_cpu_platform_power: _sensor_state
    laptop_virtual_memory_memory_load: _sensor_state
    laptop_virtual_memory_memory_used_data: _sensor_state
    laptop_virtual_memory_memory_available_data: _sensor_state
    laptop_nvidia_geforce_840m_d3d_3d_load: _sensor_state
    laptop_nvidia_geforce_840m_d3d_compute_0_load: _sensor_state
    laptop_nvidia_geforce_840m_d3d_compute_1_load: _sensor_state
    laptop_nvidia_geforce_840m_d3d_copy_load: _sensor_state
    laptop_nvidia_geforce_840m_d3d_copy_load_2: _sensor_state
    laptop_nvidia_geforce_840m_d3d_copy_load_3: _sensor_state
    laptop_nvidia_geforce_840m_d3d_copy_load_4: _sensor_state
    laptop_nvidia_geforce_840m_d3d_dedicated_memory_used_data: _sensor_state
    laptop_nvidia_geforce_840m_d3d_shared_memory_used_data: _sensor_state
    asus_sabertooth_z77_vcore_voltage: _sensor_state
    asus_sabertooth_z77_voltage_2_voltage: _sensor_state
    asus_sabertooth_z77_avcc_voltage: _sensor_state
    asus_sabertooth_z77_3_3v_voltage: _sensor_state
    asus_sabertooth_z77_voltage_5_voltage: _sensor_state
    asus_sabertooth_z77_voltage_6_voltage: _sensor_state
    asus_sabertooth_z77_voltage_7_voltage: _sensor_state
    asus_sabertooth_z77_3v_standby_voltage: _sensor_state
    asus_sabertooth_z77_cmos_battery_voltage: _sensor_state
    asus_sabertooth_z77_cpu_termination_voltage: _sensor_state
    asus_sabertooth_z77_voltage_11_voltage: _sensor_state
    asus_sabertooth_z77_voltage_12_voltage: _sensor_state
    asus_sabertooth_z77_voltage_13_voltage: _sensor_state
    asus_sabertooth_z77_voltage_14_voltage: _sensor_state
    asus_sabertooth_z77_voltage_15_voltage: _sensor_state
    asus_sabertooth_z77_cpu_core_temperature: _sensor_state
    asus_sabertooth_z77_temperature_1_temperature: _sensor_state
    asus_sabertooth_z77_temperature_2_temperature: _sensor_state
    asus_sabertooth_z77_temperature_5_temperature: _sensor_state
    asus_sabertooth_z77_fan_1_fan: _sensor_state
    asus_sabertooth_z77_fan_2_fan: _sensor_state
    asus_sabertooth_z77_fan_3_fan: _sensor_state
    asus_sabertooth_z77_fan_4_fan: _sensor_state
    asus_sabertooth_z77_fan_5_fan: _sensor_state
    asus_sabertooth_z77_fan_1_control: _sensor_state
    asus_sabertooth_z77_fan_2_control: _sensor_state
    asus_sabertooth_z77_fan_3_control: _sensor_state
    asus_sabertooth_z77_fan_4_control: _sensor_state
    asus_sabertooth_z77_fan_5_control: _sensor_state
    s9_plus_detected_activity: _sensor_state
    s9_plus_sleep_confidence: _sensor_state
    s9_plus_sleep_segment: _sensor_state
    s9_plus_os_version: _sensor_state
    s9_plus_security_patch: _sensor_state
    s9_plus_current_version: _sensor_state
    s9_plus_app_rx_gb: _sensor_state
    s9_plus_app_tx_gb: _sensor_state
    s9_plus_app_memory: _sensor_state
    s9_plus_app_standby_bucket: _sensor_state
    s9_plus_app_importance: _sensor_state
    s9_plus_ringer_mode: _sensor_state
    s9_plus_audio_mode: _sensor_state
    s9_plus_volume_level_alarm: _sensor_state
    s9_plus_volume_level_call: _sensor_state
    s9_plus_volume_level_music: _sensor_state
    s9_plus_volume_level_ringer: _sensor_state
    s9_plus_volume_level_notification: _sensor_state
    s9_plus_volume_level_system: _sensor_state
    s9_plus_volume_level_dtmf: _sensor_state
    s9_plus_volume_level_accessibility: _sensor_state
    s9_plus_battery_level: _sensor_state
    s9_plus_battery_state: _sensor_state
    s9_plus_charger_type: _sensor_state
    s9_plus_battery_health: _sensor_state
    s9_plus_battery_temperature: _sensor_state
    s9_plus_battery_power: _sensor_state
    s9_plus_remaining_charge_time: _sensor_state
    s9_plus_bluetooth_connection: _sensor_state
    s9_plus_ble_transmitter: _sensor_state
    s9_plus_beacon_monitor: _sensor_state
    s9_plus_car_battery: _sensor_state
    s9_plus_car_name: _sensor_state
    s9_plus_car_charging_status: _sensor_state
    s9_plus_car_ev_connector_type: _sensor_state
    s9_plus_car_fuel: _sensor_state
    s9_plus_car_fuel_type: _sensor_state
    s9_plus_car_odometer: _sensor_state
    s9_plus_car_speed: _sensor_state
    s9_plus_car_range_remaining: _sensor_state
    s9_plus_screen_brightness: _sensor_state
    s9_plus_screen_off_timeout: _sensor_state
    s9_plus_screen_orientation: _sensor_state
    s9_plus_screen_rotation: _sensor_state
    s9_plus_do_not_disturb_sensor: _sensor_state
    s9_plus_geocoded_location: _sensor_state
    s9_plus_last_used_app: _sensor_state
    s9_plus_last_reboot: _sensor_state
    s9_plus_last_update_trigger: _sensor_state
    s9_plus_light_sensor: _sensor_state
    s9_plus_high_accuracy_update_interval: _sensor_state
    s9_plus_wi_fi_connection: _sensor_state
    s9_plus_wi_fi_bssid: _sensor_state
    s9_plus_wi_fi_ip_address: _sensor_state
    s9_plus_wi_fi_link_speed: _sensor_state
    s9_plus_wi_fi_frequency: _sensor_state
    s9_plus_wi_fi_signal_strength: _sensor_state
    s9_plus_public_ip_address: _sensor_state
    s9_plus_network_type: _sensor_state
    s9_plus_ipv6_addresses: _sensor_state
    s9_plus_next_alarm: _sensor_state
    s9_plus_last_notification: _sensor_state
    s9_plus_last_removed_notification: _sensor_state
    s9_plus_active_notification_count: _sensor_state
    s9_plus_media_session: _sensor_state
    s9_plus_phone_state: _sensor_state
    s9_plus_sim_1: _sensor_state
    s9_plus_sim_2: _sensor_state
    s9_plus_pressure_sensor: _sensor_state
    s9_plus_proximity_sensor: _sensor_state
    s9_plus_steps_sensor: _sensor_state
    s9_plus_internal_storage: _sensor_state
    s9_plus_external_storage: _sensor_state
    s9_plus_current_time_zone: _sensor_state
    s9_plus_total_rx_gb: _sensor_state
    s9_plus_total_tx_gb: _sensor_state
    samsung_sm_g991w_expires: _sensor_state
    samsung_sm_g991w_ip_address: _sensor_state
    samsung_sm_g991w_last_seen: _sensor_state
    zashtys_satellite_cpu_load: _sensor_state
    zashtys_satellite_cpu_temperature: _sensor_state
    zashtys_satellite_disk_usage: _sensor_state
    zashtys_satellite_memory_usage: _sensor_state
    zashtys_satellite_uptime: _sensor_state
    zashtys_satellite_status: _sensor_state
    zashtys_satellite_data_sent: _sensor_state
    zashtys_satellite_data_received: _sensor_state
    zashtys_satellite_cpu_voltage: _sensor_state
    zashtys_satellite_cpu_clock_speed: _sensor_state
    zashtys_satellite_disk_swap: _sensor_state
    zashtys_satellite_uptime_2: _sensor_state
    zashtys_satellite_wifi_signal: _sensor_state
    zashtys_satellite_wifi_signal_strength: _sensor_state
    zashtys_satellite_fan_speed: _sensor_state
    frigate_upstairs_guy_last_camera: _sensor_state
    frigate_upstairs_lady_last_camera: _sensor_state
    frigate_murphy_last_camera: _sensor_state
    frigate_tristian_last_camera: _sensor_state
    frigate_jeff_last_camera: _sensor_state
    frigate_ashton_last_camera: _sensor_state
    frigate_kit_last_camera: _sensor_state
    browser_mod_c9a5c39b_a64fa6bd_browser_id: _sensor_state
    browser_mod_c9a5c39b_a64fa6bd_browser_path: _sensor_state
    browser_mod_c9a5c39b_a64fa6bd_browser_visibility: _sensor_state
    browser_mod_c9a5c39b_a64fa6bd_browser_useragent: _sensor_state
    browser_mod_c9a5c39b_a64fa6bd_browser_user: _sensor_state
    browser_mod_c9a5c39b_a64fa6bd_browser_width: _sensor_state
    browser_mod_c9a5c39b_a64fa6bd_browser_height: _sensor_state
    browser_mod_c9a5c39b_a64fa6bd_panel: _sensor_state
    zashtys_satellite_apt_updates: _sensor_state
    laptop_wdc_wdbk3u5000anc_temperature: _sensor_state
    laptop_wdc_wdbk3u5000anc_used_space_load: _sensor_state
    laptop_wdc_wdbk3u5000anc_read_activity_load: _sensor_state
    laptop_wdc_wdbk3u5000anc_write_activity_load: _sensor_state
    laptop_wdc_wdbk3u5000anc_total_activity_load: _sensor_state
    laptop_wdc_wdbk3u5000anc_life_level: _sensor_state
    laptop_wdc_wdbk3u5000anc_power_on_count_factor: _sensor_state
    laptop_wdc_wdbk3u5000anc_power_on_hours_factor: _sensor_state
    laptop_wdc_wdbk3u5000anc_data_read: _sensor_state
    laptop_wdc_wdbk3u5000anc_data_written: _sensor_state
    laptop_wdc_wdbk3u5000anc_free_space_data: _sensor_state
    laptop_wdc_wdbk3u5000anc_total_space_data: _sensor_state
    laptop_wdc_wdbk3u5000anc_read_rate_throughput: _sensor_state
    laptop_wdc_wdbk3u5000anc_write_rate_throughput: _sensor_state
    st1000lm048_2e7172_temperature_temperature: _sensor_state
    laptop_st1000lm048_2e7172_used_space_load: _sensor_state
    laptop_st1000lm048_2e7172_read_activity_load: _sensor_state
    laptop_st1000lm048_2e7172_write_activity_load: _sensor_state
    laptop_st1000lm048_2e7172_total_activity_load: _sensor_state
    laptop_st1000lm048_2e7172_power_on_count_factor: _sensor_state
    laptop_st1000lm048_2e7172_power_on_hours_factor: _sensor_state
    laptop_st1000lm048_2e7172_free_space_data: _sensor_state
    laptop_st1000lm048_2e7172_total_space_data: _sensor_state
    laptop_st1000lm048_2e7172_read_rate_throughput: _sensor_state
    laptop_st1000lm048_2e7172_write_rate_throughput: _sensor_state
    bluetooth_network_connection_network_utilization_load: _sensor_state
    bluetooth_network_connection_data_uploaded_data: _sensor_state
    bluetooth_network_connection_data_downloaded_data: _sensor_state
    bluetooth_network_connection_upload_speed_throughput: _sensor_state
    bluetooth_network_connection_download_speed_throughput: _sensor_state
    ethernet_network_utilization_load: _sensor_state
    ethernet_data_uploaded_data: _sensor_state
    ethernet_data_downloaded_data: _sensor_state
    ethernet_upload_speed_throughput: _sensor_state
    ethernet_download_speed_throughput: _sensor_state
    local_area_connection_2_network_utilization_load: _sensor_state
    local_area_connection_2_data_uploaded_data: _sensor_state
    local_area_connection_2_data_downloaded_data: _sensor_state
    local_area_connection_2_upload_speed_throughput: _sensor_state
    local_area_connection_2_download_speed_throughput: _sensor_state
    local_area_connection_9_network_utilization_load: _sensor_state
    local_area_connection_9_data_uploaded_data: _sensor_state
    local_area_connection_9_data_downloaded_data: _sensor_state
    local_area_connection_9_upload_speed_throughput: _sensor_state
    local_area_connection_9_download_speed_throughput: _sensor_state
    openvpn_data_channel_offload_for_nordvpn_network_utilization_load: _sensor_state
    openvpn_data_channel_offload_for_nordvpn_data_uploaded_data: _sensor_state
    openvpn_data_channel_offload_for_nordvpn_data_downloaded_data: _sensor_state
    openvpn_data_channel_offload_for_nordvpn_upload_speed_throughput: _sensor_state
    openvpn_data_channel_offload_for_nordvpn_download_speed_throughput: _sensor_state
    tailscale_network_utilization_load: _sensor_state
    tailscale_data_uploaded_data: _sensor_state
    tailscale_data_downloaded_data: _sensor_state
    tailscale_upload_speed_throughput: _sensor_state
    tailscale_download_speed_throughput: _sensor_state
    wi_fi_network_utilization_load: _sensor_state
    wi_fi_data_uploaded_data: _sensor_state
    wi_fi_data_downloaded_data: _sensor_state
    wi_fi_upload_speed_throughput: _sensor_state
    wi_fi_download_speed_throughput: _sensor_state
    desktop_3pnv5bo_intel_xeon_e3_1246_v3_cpu_platform_power: _sensor_state
    desktop_3pnv5bo_virtual_memory_memory_load: _sensor_state
    desktop_3pnv5bo_virtual_memory_memory_used_data: _sensor_state
    desktop_3pnv5bo_virtual_memory_memory_available_data: _sensor_state
    generic_memory_memory_load_3: _sensor_state
    generic_memory_memory_used_data_3: _sensor_state
    generic_memory_memory_available_data_3: _sensor_state
    genius_lyrics_browser_mod_c9a5c39b_a64fa6bd_lyrics: _sensor_state
    jusparr_docker_container_disk_usage_total_size: _sensor_state
    jusparr_docker_image_disk_usage_reclaimable: _sensor_state
    jusparr_docker_image_disk_usage_total_size: _sensor_state
    jusparr_docker_volume_disk_usage_total_size: _sensor_state
    mediamtx_image_2: _sensor_state
    mediamtx_state_2: _sensor_state
    mediamtx_memory_limit_2: _sensor_state
    mediamtx_memory_usage_2: _sensor_state
    mediamtx_memory_usage_percentage_2: _sensor_state
    mediamtx_cpu_usage_total_2: _sensor_state
    wordpress_wordpress_1_image_2: _sensor_state
    wordpress_wordpress_1_state_2: _sensor_state
    wordpress_wordpress_1_memory_limit_2: _sensor_state
    wordpress_wordpress_1_memory_usage_2: _sensor_state
    wordpress_wordpress_1_memory_usage_percentage_2: _sensor_state
    wordpress_wordpress_1_cpu_usage_total_2: _sensor_state
    homeassistant_image_2: _sensor_state
    homeassistant_state_2: _sensor_state
    homeassistant_memory_limit_2: _sensor_state
    homeassistant_memory_usage_2: _sensor_state
    homeassistant_memory_usage_percentage_2: _sensor_state
    homeassistant_cpu_usage_total_2: _sensor_state
    plex_image_2: _sensor_state
    plex_state_2: _sensor_state
    plex_memory_limit_2: _sensor_state
    plex_memory_usage_2: _sensor_state
    plex_memory_usage_percentage_2: _sensor_state
    plex_cpu_usage_total_2: _sensor_state
    aircast_image_2: _sensor_state
    aircast_state_2: _sensor_state
    aircast_memory_limit_2: _sensor_state
    aircast_memory_usage_2: _sensor_state
    aircast_memory_usage_percentage_2: _sensor_state
    aircast_cpu_usage_total_2: _sensor_state
    wordpress_db_1_image_2: _sensor_state
    wordpress_db_1_state_2: _sensor_state
    wordpress_db_1_memory_limit_2: _sensor_state
    wordpress_db_1_memory_usage_2: _sensor_state
    wordpress_db_1_memory_usage_percentage_2: _sensor_state
    wordpress_db_1_cpu_usage_total_2: _sensor_state
    music_assistant_image_2: _sensor_state
    music_assistant_state_2: _sensor_state
    music_assistant_memory_limit_2: _sensor_state
    music_assistant_memory_usage_2: _sensor_state
    music_assistant_memory_usage_percentage_2: _sensor_state
    music_assistant_cpu_usage_total_2: _sensor_state
    tasmoadmin_image_2: _sensor_state
    tasmoadmin_state_2: _sensor_state
    tasmoadmin_memory_limit_2: _sensor_state
    tasmoadmin_memory_usage_2: _sensor_state
    tasmoadmin_memory_usage_percentage_2: _sensor_state
    tasmoadmin_cpu_usage_total_2: _sensor_state
    nodered_image_2: _sensor_state
    nodered_state_2: _sensor_state
    nodered_memory_limit_2: _sensor_state
    nodered_memory_usage_2: _sensor_state
    nodered_memory_usage_percentage_2: _sensor_state
    nodered_cpu_usage_total_2: _sensor_state
    esphome_image_2: _sensor_state
    esphome_state_2: _sensor_state
    esphome_memory_limit_2: _sensor_state
    esphome_memory_usage_2: _sensor_state
    esphome_memory_usage_percentage_2: _sensor_state
    esphome_cpu_usage_total_2: _sensor_state
    frigate_image_2: _sensor_state
    frigate_state_2: _sensor_state
    frigate_memory_limit_2: _sensor_state
    frigate_memory_usage_2: _sensor_state
    frigate_memory_usage_percentage_2: _sensor_state
    frigate_cpu_usage_total_2: _sensor_state
    portainer_image_2: _sensor_state
    portainer_state_2: _sensor_state
    portainer_memory_limit_2: _sensor_state
    portainer_memory_usage_2: _sensor_state
    portainer_memory_usage_percentage_2: _sensor_state
    portainer_cpu_usage_total_2: _sensor_state
    watchtower_image_2: _sensor_state
    watchtower_state_2: _sensor_state
    watchtower_memory_limit_2: _sensor_state
    watchtower_memory_usage_2: _sensor_state
    watchtower_memory_usage_percentage_2: _sensor_state
    watchtower_cpu_usage_total_2: _sensor_state
    scrutiny_image_2: _sensor_state
    scrutiny_state_2: _sensor_state
    scrutiny_memory_limit_2: _sensor_state
    scrutiny_memory_usage_2: _sensor_state
    scrutiny_memory_usage_percentage_2: _sensor_state
    scrutiny_cpu_usage_total_2: _sensor_state
    piper_image_2: _sensor_state
    piper_state_2: _sensor_state
    piper_memory_limit_2: _sensor_state
    piper_memory_usage_2: _sensor_state
    piper_memory_usage_percentage_2: _sensor_state
    piper_cpu_usage_total_2: _sensor_state
    whisper_image_2: _sensor_state
    whisper_state_2: _sensor_state
    whisper_memory_limit_2: _sensor_state
    whisper_memory_usage_2: _sensor_state
    whisper_memory_usage_percentage_2: _sensor_state
    whisper_cpu_usage_total_2: _sensor_state
    prometheus_image_2: _sensor_state
    prometheus_state_2: _sensor_state
    prometheus_memory_limit_2: _sensor_state
    prometheus_memory_usage_2: _sensor_state
    prometheus_memory_usage_percentage_2: _sensor_state
    prometheus_cpu_usage_total_2: _sensor_state
    opnsense_exporter_image_2: _sensor_state
    opnsense_exporter_state_2: _sensor_state
    opnsense_exporter_memory_limit_2: _sensor_state
    opnsense_exporter_memory_usage_2: _sensor_state
    opnsense_exporter_memory_usage_percentage_2: _sensor_state
    opnsense_exporter_cpu_usage_total_2: _sensor_state
    grafana_image_2: _sensor_state
    grafana_state_2: _sensor_state
    grafana_memory_limit_2: _sensor_state
    grafana_memory_usage_2: _sensor_state
    grafana_memory_usage_percentage_2: _sensor_state
    grafana_cpu_usage_total_2: _sensor_state
    timescaledb_poc_image_2: _sensor_state
    timescaledb_poc_state_2: _sensor_state
    timescaledb_poc_memory_limit_2: _sensor_state
    timescaledb_poc_memory_usage_2: _sensor_state
    timescaledb_poc_memory_usage_percentage_2: _sensor_state
    timescaledb_poc_cpu_usage_total_2: _sensor_state
    postgres_exporter_image_2: _sensor_state
    postgres_exporter_state_2: _sensor_state
    postgres_exporter_memory_limit_2: _sensor_state
    postgres_exporter_memory_usage_2: _sensor_state
    postgres_exporter_memory_usage_percentage_2: _sensor_state
    postgres_exporter_cpu_usage_total_2: _sensor_state
    ha_aircast_1_image_2: _sensor_state
    ha_aircast_1_state_2: _sensor_state
    ha_aircast_1_memory_limit_2: _sensor_state
    ha_aircast_1_memory_usage_2: _sensor_state
    ha_aircast_1_memory_usage_percentage_2: _sensor_state
    ha_aircast_1_cpu_usage_total_2: _sensor_state
    ha_nodered_1_image_2: _sensor_state
    ha_nodered_1_state_2: _sensor_state
    ha_nodered_1_memory_limit_2: _sensor_state
    ha_nodered_1_memory_usage_2: _sensor_state
    ha_nodered_1_memory_usage_percentage_2: _sensor_state
    ha_nodered_1_cpu_usage_total_2: _sensor_state
    ha_esphome_1_image_2: _sensor_state
    ha_esphome_1_state_2: _sensor_state
    ha_esphome_1_memory_limit_2: _sensor_state
    ha_esphome_1_memory_usage_2: _sensor_state
    ha_esphome_1_memory_usage_percentage_2: _sensor_state
    ha_esphome_1_cpu_usage_total_2: _sensor_state
    portainer_agent_image_2: _sensor_state
    portainer_agent_state_2: _sensor_state
    portainer_agent_memory_limit_2: _sensor_state
    portainer_agent_memory_usage_2: _sensor_state
    portainer_agent_memory_usage_percentage_2: _sensor_state
    portainer_agent_cpu_usage_total_2: _sensor_state
    ha_watchtower_1_image_2: _sensor_state
    ha_watchtower_1_state_2: _sensor_state
    ha_watchtower_1_memory_limit_2: _sensor_state
    ha_watchtower_1_memory_usage_2: _sensor_state
    ha_watchtower_1_memory_usage_percentage_2: _sensor_state
    ha_watchtower_1_cpu_usage_total_2: _sensor_state
    ha_whisper_1_image_2: _sensor_state
    ha_whisper_1_state_2: _sensor_state
    ha_whisper_1_memory_limit_2: _sensor_state
    ha_whisper_1_memory_usage_2: _sensor_state
    ha_whisper_1_memory_usage_percentage_2: _sensor_state
    ha_whisper_1_cpu_usage_total_2: _sensor_state
    ha_piper_1_image_2: _sensor_state
    ha_piper_1_state_2: _sensor_state
    ha_piper_1_memory_limit_2: _sensor_state
    ha_piper_1_memory_usage_2: _sensor_state
    ha_piper_1_memory_usage_percentage_2: _sensor_state
    ha_piper_1_cpu_usage_total_2: _sensor_state
    ha_scrutiny_1_image_2: _sensor_state
    ha_scrutiny_1_state_2: _sensor_state
    ha_scrutiny_1_memory_limit_2: _sensor_state
    ha_scrutiny_1_memory_usage_2: _sensor_state
    ha_scrutiny_1_memory_usage_percentage_2: _sensor_state
    ha_scrutiny_1_cpu_usage_total_2: _sensor_state
    home_assistant_main_type: _sensor_state
    home_assistant_main_containers: _sensor_state
    timescale_db_type: _sensor_state
    timescale_db_containers: _sensor_state
    wordpress_type: _sensor_state
    wordpress_containers: _sensor_state
    rtmp_relay_type: _sensor_state
    rtmp_relay_containers: _sensor_state
    rtmp_relay_type_2: _sensor_state
    rtmp_relay_containers_2: _sensor_state
    intel_core_i5_3570k_cpu_core_voltage: _sensor_state
    intel_core_i5_3570k_cpu_core_1_voltage: _sensor_state
    intel_core_i5_3570k_cpu_core_2_voltage: _sensor_state
    intel_core_i5_3570k_cpu_core_3_voltage: _sensor_state
    intel_core_i5_3570k_cpu_core_4_voltage: _sensor_state
    intel_core_i5_3570k_cpu_package_power: _sensor_state
    intel_core_i5_3570k_cpu_cores_power: _sensor_state
    desktop_u5e7nrv_intel_core_i5_3570k_cpu_memory_power: _sensor_state
    desktop_u5e7nrv_intel_core_i5_3570k_cpu_platform_power: _sensor_state
    intel_core_i5_3570k_bus_speed_clock: _sensor_state
    intel_core_i5_3570k_cpu_core_1_clock: _sensor_state
    intel_core_i5_3570k_cpu_core_2_clock: _sensor_state
    intel_core_i5_3570k_cpu_core_3_clock: _sensor_state
    intel_core_i5_3570k_cpu_core_4_clock: _sensor_state
    intel_core_i5_3570k_core_max_temperature: _sensor_state
    intel_core_i5_3570k_core_average_temperature: _sensor_state
    intel_core_i5_3570k_cpu_core_1_temperature: _sensor_state
    intel_core_i5_3570k_cpu_core_2_temperature: _sensor_state
    intel_core_i5_3570k_cpu_core_3_temperature: _sensor_state
    intel_core_i5_3570k_cpu_core_4_temperature: _sensor_state
    intel_core_i5_3570k_cpu_package_temperature: _sensor_state
    intel_core_i5_3570k_cpu_core_1_distance_to_tjmax_temperature: _sensor_state
    intel_core_i5_3570k_cpu_core_2_distance_to_tjmax_temperature: _sensor_state
    intel_core_i5_3570k_cpu_core_3_distance_to_tjmax_temperature: _sensor_state
    intel_core_i5_3570k_cpu_core_4_distance_to_tjmax_temperature: _sensor_state
    intel_core_i5_3570k_cpu_total_load: _sensor_state
    intel_core_i5_3570k_cpu_core_max_load: _sensor_state
    intel_core_i5_3570k_cpu_core_1_load: _sensor_state
    intel_core_i5_3570k_cpu_core_2_load: _sensor_state
    intel_core_i5_3570k_cpu_core_3_load: _sensor_state
    intel_core_i5_3570k_cpu_core_4_load: _sensor_state
    desktop_u5e7nrv_virtual_memory_memory_load: _sensor_state
    desktop_u5e7nrv_virtual_memory_memory_used_data: _sensor_state
    desktop_u5e7nrv_virtual_memory_memory_available_data: _sensor_state
    generic_memory_memory_load_2: _sensor_state
    generic_memory_memory_used_data_2: _sensor_state
    generic_memory_memory_available_data_2: _sensor_state
    amd_radeon_hd_7900_series_gpu_core_voltage: _sensor_state
    amd_radeon_hd_7900_series_gpu_core_clock: _sensor_state
    amd_radeon_hd_7900_series_gpu_memory_clock: _sensor_state
    amd_radeon_hd_7900_series_gpu_core_temperature: _sensor_state
    amd_radeon_hd_7900_series_gpu_core_load: _sensor_state
    amd_radeon_hd_7900_series_d3d_3d_load: _sensor_state
    amd_radeon_hd_7900_series_d3d_compute_0_load: _sensor_state
    amd_radeon_hd_7900_series_d3d_compute_1_load: _sensor_state
    amd_radeon_hd_7900_series_d3d_copy_load: _sensor_state
    amd_radeon_hd_7900_series_d3d_copy_load_2: _sensor_state
    amd_radeon_hd_7900_series_d3d_security_0_load: _sensor_state
    amd_radeon_hd_7900_series_d3d_timer_0_load: _sensor_state
    amd_radeon_hd_7900_series_d3d_video_decode_load: _sensor_state
    amd_radeon_hd_7900_series_d3d_video_encode_load: _sensor_state
    amd_radeon_hd_7900_series_d3d_video_encode_load_2: _sensor_state
    amd_radeon_hd_7900_series_gpu_fan_fan: _sensor_state
    amd_radeon_hd_7900_series_gpu_fan_control: _sensor_state
    amd_radeon_hd_7900_series_fullscreen_fps_factor: _sensor_state
    amd_radeon_hd_7900_series_d3d_dedicated_memory_used_smalldata: _sensor_state
    amd_radeon_hd_7900_series_d3d_dedicated_memory_free_smalldata: _sensor_state
    amd_radeon_hd_7900_series_d3d_dedicated_memory_total_smalldata: _sensor_state
    amd_radeon_hd_7900_series_d3d_shared_memory_used_smalldata: _sensor_state
    amd_radeon_hd_7900_series_d3d_shared_memory_free_smalldata: _sensor_state
    amd_radeon_hd_7900_series_d3d_shared_memory_total_smalldata: _sensor_state
    radeon_rx_570_series_gpu_core_voltage: _sensor_state
    radeon_rx_570_series_gpu_package_power: _sensor_state
    radeon_rx_570_series_gpu_core_clock: _sensor_state
    radeon_rx_570_series_gpu_memory_clock: _sensor_state
    radeon_rx_570_series_gpu_core_temperature: _sensor_state
    radeon_rx_570_series_gpu_core_load: _sensor_state
    radeon_rx_570_series_d3d_3d_load: _sensor_state
    radeon_rx_570_series_d3d_compute_0_load: _sensor_state
    radeon_rx_570_series_d3d_compute_1_load: _sensor_state
    radeon_rx_570_series_d3d_compute_3_load: _sensor_state
    radeon_rx_570_series_d3d_copy_load: _sensor_state
    radeon_rx_570_series_d3d_copy_load_2: _sensor_state
    radeon_rx_570_series_d3d_high_priority_3d_load: _sensor_state
    radeon_rx_570_series_d3d_high_priority_compute_load: _sensor_state
    radeon_rx_570_series_d3d_security_0_load: _sensor_state
    radeon_rx_570_series_d3d_timer_0_load: _sensor_state
    radeon_rx_570_series_d3d_true_audio_0_load: _sensor_state
    radeon_rx_570_series_d3d_true_audio_1_load: _sensor_state
    radeon_rx_570_series_d3d_video_decode_load: _sensor_state
    radeon_rx_570_series_d3d_video_encode_load: _sensor_state
    radeon_rx_570_series_d3d_video_encode_load_2: _sensor_state
    radeon_rx_570_series_d3d_video_encode_load_3: _sensor_state
    radeon_rx_570_series_d3d_video_encode_load_4: _sensor_state
    radeon_rx_570_series_d3d_video_encode_load_5: _sensor_state
    radeon_rx_570_series_gpu_fan_fan: _sensor_state
    radeon_rx_570_series_gpu_fan_control: _sensor_state
    radeon_rx_570_series_fullscreen_fps_factor: _sensor_state
    radeon_rx_570_series_gpu_memory_used_smalldata: _sensor_state
    radeon_rx_570_series_gpu_memory_free_smalldata: _sensor_state
    radeon_rx_570_series_gpu_memory_total_smalldata: _sensor_state
    radeon_rx_570_series_d3d_dedicated_memory_used_smalldata: _sensor_state
    radeon_rx_570_series_d3d_dedicated_memory_free_smalldata: _sensor_state
    radeon_rx_570_series_d3d_dedicated_memory_total_smalldata: _sensor_state
    radeon_rx_570_series_d3d_shared_memory_used_smalldata: _sensor_state
    radeon_rx_570_series_d3d_shared_memory_free_smalldata: _sensor_state
    radeon_rx_570_series_d3d_shared_memory_total_smalldata: _sensor_state
    wdc_wd10ezex_00kuwa0_temperature_temperature: _sensor_state
    desktop_u5e7nrv_wdc_wd10ezex_00kuwa0_used_space_load: _sensor_state
    desktop_u5e7nrv_wdc_wd10ezex_00kuwa0_read_activity_load: _sensor_state
    desktop_u5e7nrv_wdc_wd10ezex_00kuwa0_write_activity_load: _sensor_state
    desktop_u5e7nrv_wdc_wd10ezex_00kuwa0_total_activity_load: _sensor_state
    desktop_u5e7nrv_wdc_wd10ezex_00kuwa0_power_on_count_factor: _sensor_state
    desktop_u5e7nrv_wdc_wd10ezex_00kuwa0_power_on_hours_factor: _sensor_state
    desktop_u5e7nrv_wdc_wd10ezex_00kuwa0_free_space_data: _sensor_state
    desktop_u5e7nrv_wdc_wd10ezex_00kuwa0_total_space_data: _sensor_state
    desktop_u5e7nrv_wdc_wd10ezex_00kuwa0_read_rate_throughput: _sensor_state
    desktop_u5e7nrv_wdc_wd10ezex_00kuwa0_write_rate_throughput: _sensor_state
    st500dm002_1bd142_temperature_temperature: _sensor_state
    desktop_u5e7nrv_st500dm002_1bd142_used_space_load: _sensor_state
    desktop_u5e7nrv_st500dm002_1bd142_read_activity_load: _sensor_state
    desktop_u5e7nrv_st500dm002_1bd142_write_activity_load: _sensor_state
    desktop_u5e7nrv_st500dm002_1bd142_total_activity_load: _sensor_state
    desktop_u5e7nrv_st500dm002_1bd142_power_on_count_factor: _sensor_state
    desktop_u5e7nrv_st500dm002_1bd142_power_on_hours_factor: _sensor_state
    desktop_u5e7nrv_st500dm002_1bd142_free_space_data: _sensor_state
    desktop_u5e7nrv_st500dm002_1bd142_total_space_data: _sensor_state
    desktop_u5e7nrv_st500dm002_1bd142_read_rate_throughput: _sensor_state
    desktop_u5e7nrv_st500dm002_1bd142_write_rate_throughput: _sensor_state
    st8000vn004_2m2101_temperature_temperature: _sensor_state
    desktop_u5e7nrv_st8000vn004_2m2101_used_space_load: _sensor_state
    desktop_u5e7nrv_st8000vn004_2m2101_read_activity_load: _sensor_state
    desktop_u5e7nrv_st8000vn004_2m2101_write_activity_load: _sensor_state
    desktop_u5e7nrv_st8000vn004_2m2101_total_activity_load: _sensor_state
    desktop_u5e7nrv_st8000vn004_2m2101_power_on_count_factor: _sensor_state
    desktop_u5e7nrv_st8000vn004_2m2101_power_on_hours_factor: _sensor_state
    desktop_u5e7nrv_st8000vn004_2m2101_free_space_data: _sensor_state
    desktop_u5e7nrv_st8000vn004_2m2101_total_space_data: _sensor_state
    desktop_u5e7nrv_st8000vn004_2m2101_read_rate_throughput: _sensor_state
    desktop_u5e7nrv_st8000vn004_2m2101_write_rate_throughput: _sensor_state
    samsung_ssd_860_evo_1tb_temperature_temperature: _sensor_state
    desktop_u5e7nrv_samsung_ssd_860_evo_1tb_used_space_load: _sensor_state
    desktop_u5e7nrv_samsung_ssd_860_evo_1tb_read_activity_load: _sensor_state
    desktop_u5e7nrv_samsung_ssd_860_evo_1tb_write_activity_load: _sensor_state
    desktop_u5e7nrv_samsung_ssd_860_evo_1tb_total_activity_load: _sensor_state
    desktop_u5e7nrv_samsung_ssd_860_evo_1tb_life_level: _sensor_state
    desktop_u5e7nrv_samsung_ssd_860_evo_1tb_power_on_count_factor: _sensor_state
    desktop_u5e7nrv_samsung_ssd_860_evo_1tb_power_on_hours_factor: _sensor_state
    desktop_u5e7nrv_samsung_ssd_860_evo_1tb_data_written: _sensor_state
    desktop_u5e7nrv_samsung_ssd_860_evo_1tb_free_space_data: _sensor_state
    desktop_u5e7nrv_samsung_ssd_860_evo_1tb_total_space_data: _sensor_state
    desktop_u5e7nrv_samsung_ssd_860_evo_1tb_read_rate_throughput: _sensor_state
    desktop_u5e7nrv_samsung_ssd_860_evo_1tb_write_rate_throughput: _sensor_state
    bluetooth_network_connection_network_utilization_load_2: _sensor_state
    bluetooth_network_connection_data_uploaded_data_2: _sensor_state
    bluetooth_network_connection_data_downloaded_data_2: _sensor_state
    bluetooth_network_connection_upload_speed_throughput_2: _sensor_state
    bluetooth_network_connection_download_speed_throughput_2: _sensor_state
    ethernet_network_utilization_load_2: _sensor_state
    ethernet_data_uploaded_data_2: _sensor_state
    ethernet_data_downloaded_data_2: _sensor_state
    ethernet_upload_speed_throughput_2: _sensor_state
    ethernet_download_speed_throughput_2: _sensor_state
    tailscale_network_utilization_load_2: _sensor_state
    tailscale_data_uploaded_data_2: _sensor_state
    tailscale_data_downloaded_data_2: _sensor_state
    tailscale_upload_speed_throughput_2: _sensor_state
    tailscale_download_speed_throughput_2: _sensor_state
    genius_lyrics_livingroom_tv_lyrics: _sensor_state
    genius_lyrics_tv_group_2_lyrics: _sensor_state
    genius_lyrics_tv_group_3_lyrics: _sensor_state
    genius_lyrics_speakers_3_lyrics: _sensor_state
    genius_lyrics_livingroom_tv_2_lyrics: _sensor_state
    genius_lyrics_living_room_3_lyrics: _sensor_state
    genius_lyrics_bedroom_speaker_3_lyrics: _sensor_state
    genius_lyrics_two_normal_3_lyrics: _sensor_state
    genius_lyrics_bed_and_bath_3_lyrics: _sensor_state
    genius_lyrics_bathroom_3_lyrics: _sensor_state
    genius_lyrics_bathroom_airplay_lyrics: _sensor_state
    genius_lyrics_bedroom_speaker_4_lyrics: _sensor_state
    genius_lyrics_bedroom_speaker_airplay_lyrics: _sensor_state
    genius_lyrics_livingroom_tv_airplay_lyrics: _sensor_state
    genius_lyrics_living_room_4_lyrics: _sensor_state
    genius_lyrics_tv_group_airplay_lyrics: _sensor_state
    genius_lyrics_livingroom_tv_3_lyrics: _sensor_state
    genius_lyrics_bed_and_bath_4_lyrics: _sensor_state
    genius_lyrics_speakers_airplay_lyrics: _sensor_state
    desktop_u5e7nrv_vethernet_ethernet_network_utilization_load: _sensor_state
    desktop_u5e7nrv_vethernet_ethernet_data_uploaded: _sensor_state
    desktop_u5e7nrv_vethernet_ethernet_data_downloaded: _sensor_state
    desktop_u5e7nrv_vethernet_ethernet_upload_speed_throughput: _sensor_state
    desktop_u5e7nrv_vethernet_ethernet_download_speed_throughput: _sensor_state
    desktop_u5e7nrv_vethernet_wsl_network_utilization_load: _sensor_state
    desktop_u5e7nrv_vethernet_wsl_data_uploaded: _sensor_state
    desktop_u5e7nrv_vethernet_wsl_data_downloaded: _sensor_state
    desktop_u5e7nrv_vethernet_wsl_upload_speed_throughput: _sensor_state
    desktop_u5e7nrv_vethernet_wsl_download_speed_throughput: _sensor_state
    genius_lyrics_two_normal_airplay_lyrics: _sensor_state
    wdc_wd7502aaex_00y9a0_temperature_temperature: _sensor_state
    desktop_3pnv5bo_st33000651as_used_space_load: _sensor_state
    desktop_3pnv5bo_st33000651as_read_activity_load: _sensor_state
    desktop_3pnv5bo_st33000651as_write_activity_load: _sensor_state
    desktop_3pnv5bo_st33000651as_total_activity_load: _sensor_state
    desktop_3pnv5bo_st33000651as_power_on_count_factor: _sensor_state
    desktop_3pnv5bo_st33000651as_power_on_hours_factor: _sensor_state
    desktop_3pnv5bo_st33000651as_free_space_data: _sensor_state
    desktop_3pnv5bo_st33000651as_total_space_data: _sensor_state
    desktop_3pnv5bo_st33000651as_read_rate_throughput: _sensor_state
    desktop_3pnv5bo_st33000651as_write_rate_throughput: _sensor_state
    st33000651as_temperature_temperature: _sensor_state
    desktop_3pnv5bo_wdc_wd7502aaex_00y9a0_used_space_load: _sensor_state
    desktop_3pnv5bo_wdc_wd7502aaex_00y9a0_read_activity_load: _sensor_state
    desktop_3pnv5bo_wdc_wd7502aaex_00y9a0_write_activity_load: _sensor_state
    desktop_3pnv5bo_wdc_wd7502aaex_00y9a0_total_activity_load: _sensor_state
    desktop_3pnv5bo_wdc_wd7502aaex_00y9a0_power_on_count_factor: _sensor_state
    desktop_3pnv5bo_wdc_wd7502aaex_00y9a0_power_on_hours_factor: _sensor_state
    desktop_3pnv5bo_wdc_wd7502aaex_00y9a0_free_space_data: _sensor_state
    desktop_3pnv5bo_wdc_wd7502aaex_00y9a0_total_space_data: _sensor_state
    desktop_3pnv5bo_wdc_wd7502aaex_00y9a0_read_rate_throughput: _sensor_state
    desktop_3pnv5bo_wdc_wd7502aaex_00y9a0_write_rate_throughput: _sensor_state
    ethernet_network_utilization_load_3: _sensor_state
    ethernet_data_uploaded_data_3: _sensor_state
    ethernet_data_downloaded_data_3: _sensor_state
    ethernet_upload_speed_throughput_3: _sensor_state
    ethernet_download_speed_throughput_3: _sensor_state
    genius_lyrics_bed_and_bath_airplay_lyrics: _sensor_state
    zashtys_duolingo_user: _sensor_state
    zashtys_duolingo_gems: _sensor_state
    zashtys_duolingo_leaderboard: _sensor_state
    zashtys_duolingo_leaderboard_tier: _sensor_state
    zashtys_duolingo_friends: _sensor_state
    zashtys_duolingo_streak: _sensor_state
    zashtys_duolingo_longest_streak: _sensor_state
    zashtys_duolingo_previous_streak: _sensor_state
    zashtys_duolingo_today_xp: _sensor_state
    zashtys_duolingo_friend_quest: _sensor_state
    zashtys_duolingo_monthly_challenge: _sensor_state
    zashtys_duolingo_language_french_en: _sensor_state
    zashtys_duolingo_language_spanish_en: _sensor_state
    zashtys_duolingo_language_dutch_en: _sensor_state
    leaderboard_duolingo_today: _sensor_state
    leaderboard_duolingo_week: _sensor_state
    esphome_esphome_merged_pull_requests: _sensor_state
    home_assistant_core_merged_pull_requests: _sensor_state
    home_assistant_frontend_merged_pull_requests: _sensor_state
    home_assistant_operating_system_merged_pull_requests: _sensor_state
    home_assistant_supervisor_merged_pull_requests: _sensor_state
    internetarchive_openlibrary_client_merged_pull_requests: _sensor_state
    khoih_prog_wifinina_generic_merged_pull_requests: _sensor_state
    marc_romu_home_assistant_blueprints_merged_pull_requests: _sensor_state
    nabucasa_hass_nabucasa_merged_pull_requests: _sensor_state
    rdavydov_twitch_channel_points_miner_v2_merged_pull_requests: _sensor_state
    shaked6540_youtubeplaylistdownloader_merged_pull_requests: _sensor_state
    sherlock_project_sherlock_merged_pull_requests: _sensor_state
    thomasnordquist_mqtt_explorer_merged_pull_requests: _sensor_state
    travisghansen_hass_opnsense_merged_pull_requests: _sensor_state
    vova_sh_termux_api_merged_pull_requests: _sensor_state
    appium_appium_inspector_merged_pull_requests: _sensor_state
    archomeda_gw2sharp_merged_pull_requests: _sensor_state
    collin80_due_can_merged_pull_requests: _sensor_state
    drant_gw2navi_merged_pull_requests: _sensor_state
    esphome_esphome_docs_merged_pull_requests: _sensor_state
    home_assistant_developers_home_assistant_merged_pull_requests: _sensor_state
    krtirtho_spotube_merged_pull_requests: _sensor_state
    royshil_obs_backgroundremoval_merged_pull_requests: _sensor_state
    pascalluginbuehl_home_assistant_tray_menu_merged_pull_requests: _sensor_state
    puppeteer_puppeteer_merged_pull_requests: _sensor_state
    rscustom_rocksmith_custom_song_toolkit_merged_pull_requests: _sensor_state
    valpackett_node_red_contrib_nut_ups_merged_pull_requests: _sensor_state
    ventoy_ventoy_merged_pull_requests: _sensor_state
    alexandrerohin_home_assistant_flightradar24_merged_pull_requests: _sensor_state
    baldarn_whatsapper_merged_pull_requests: _sensor_state
    hass_agent_hass_agent_merged_pull_requests: _sensor_state
    itzg_docker_minecraft_server_merged_pull_requests: _sensor_state
    wwebjs_whatsapp_web_js_merged_pull_requests: _sensor_state
    rbrito_usbmount_merged_pull_requests: _sensor_state
    seleniumbase_seleniumbase_merged_pull_requests: _sensor_state
    sythsaz_core_merged_pull_requests: _sensor_state
    sythsaz_hass_opnsense_merged_pull_requests: _sensor_state
    sythsaz_hass_agent_merged_pull_requests: _sensor_state
    yt_dlp_yt_dlp_merged_pull_requests: _sensor_state
    basnijholt_adaptive_lighting_merged_pull_requests: _sensor_state
    boralyl_cookiecutter_homeassistant_component_merged_pull_requests: _sensor_state
    boralyl_steam_wishlist_merged_pull_requests: _sensor_state
    bportaluri_wifiesp_merged_pull_requests: _sensor_state
    build_wars_gw1_database_merged_pull_requests: _sensor_state
    custom_cards_upcoming_media_card_merged_pull_requests: _sensor_state
    custom_components_pyscript_merged_pull_requests: _sensor_state
    custom_components_sensor_plex_recently_added_merged_pull_requests: _sensor_state
    home_assistant_addons_merged_pull_requests: _sensor_state
    home_assistant_home_assistant_io_merged_pull_requests: _sensor_state
    home_assistant_ios_merged_pull_requests: _sensor_state
    huggingface_transformers_merged_pull_requests: _sensor_state
    leikoilja_ha_google_home_merged_pull_requests: _sensor_state
    librehardwaremonitor_librehardwaremonitor_merged_pull_requests: _sensor_state
    limych_ha_tor_check_merged_pull_requests: _sensor_state
    ludeeus_integration_blueprint_merged_pull_requests: _sensor_state
    maselkov_gw2bot_merged_pull_requests: _sensor_state
    mweinelt_ha_prometheus_sensor_merged_pull_requests: _sensor_state
    nationalsecurityagency_ghidra_merged_pull_requests: _sensor_state
    oncleben31_cookiecutter_homeassistant_custom_component_merged_pull_requests: _sensor_state
    permissionlesstech_bitchat_merged_pull_requests: _sensor_state
    pirate_weather_pirate_weather_ha_merged_pull_requests: _sensor_state
    psp_archive_psp_ftpd_merged_pull_requests: _sensor_state
    public_apis_public_apis_merged_pull_requests: _sensor_state
    sythsaz_home_assistant_merged_pull_requests: _sensor_state
    sythsaz_instacart_photo_convert_merged_pull_requests: _sensor_state
    taschenbuch_blishhud_farmingtracker_merged_pull_requests: _sensor_state
    tiimgreen_github_cheat_sheet_merged_pull_requests: _sensor_state
    vinta_awesome_python_merged_pull_requests: _sensor_state
    viatsko_awesome_vscode_merged_pull_requests: _sensor_state
    wasabeef_awesome_android_ui_merged_pull_requests: _sensor_state
    waujito_tpllax1500gpl_merged_pull_requests: _sensor_state
    sythsaz_giveaway_bot_merged_pull_requests: _sensor_state

class shell_command:

    @staticmethod
    def create_gif_hwy3() -> dict[str, Any]:
        ...

    @staticmethod
    def create_gif_wude() -> dict[str, Any]:
        ...

    @staticmethod
    def create_gif_wudw() -> dict[str, Any]:
        ...

    @staticmethod
    def create_gif_wude4() -> dict[str, Any]:
        ...

    @staticmethod
    def create_gif_wudw2() -> dict[str, Any]:
        ...

    @staticmethod
    def apt_update_check() -> dict[str, Any]:
        ...

    @staticmethod
    def apt_perform_upgrade() -> dict[str, Any]:
        ...

    @staticmethod
    def ha_send_sensor() -> dict[str, Any]:
        ...

    @staticmethod
    def ha_send_radar() -> dict[str, Any]:
        ...

class shopping_list:

    @staticmethod
    def add_item(*, name: str):
        """

        Args:
            name:  Example: Beer"""
        ...

    @staticmethod
    def remove_item(*, name: str):
        """

        Args:
            name:  Example: Beer"""
        ...

    @staticmethod
    def complete_item(*, name: str):
        """

        Args:
            name:  Example: Beer"""
        ...

    @staticmethod
    def incomplete_item(*, name: str):
        """

        Args:
            name:  Example: Beer"""
        ...

    @staticmethod
    def complete_all():
        ...

    @staticmethod
    def incomplete_all():
        ...

    @staticmethod
    def clear_completed_items():
        ...

    @staticmethod
    def sort(*, reverse: bool=False):
        ...

class siren:

    @staticmethod
    def turn_on(*, entity_id: str, tone: str | None=None, volume_level: int | None=None, duration: str | None=None):
        """

        Args:
            entity_id: Entity ID
            tone:  Example: fire
            volume_level:  Example: 0.5
            duration:  Example: 15"""
        ...

    @staticmethod
    def turn_off(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

class spook:

    @staticmethod
    def boo():
        """Calling this action spooks Home Assistant. Performing this action will always fail."""
        ...

    @staticmethod
    def random_fail():
        """Performing this action will randomly fail."""
        ...

class _stt_state(StateVal):
    ...

class stt:
    google_ai_stt: _stt_state
    faster_whisper: _stt_state

class sun2:

    @staticmethod
    def reload():
        ...

    @staticmethod
    def get_location(*, location: str='Home') -> dict[str, Any]:
        """

        Args:
            location:  Example: Home"""
        ...

    @staticmethod
    def update_location(*, location: str='Home', latitude: float | None=None, longitude: float | None=None, time_zone: str | None=None, observer_elevation: Any | None=None):
        """

        Args:
            location:  Example: Home
            latitude:  Example: 51.51
            longitude:  Example: -0.13
            time_zone:  Example: Europe/London"""
        ...

class _switch_state(StateVal):
    Name: str
    autoreset_time_remaining: dict
    brightness_pct: int | float
    color_temp_kelvin: int
    color_temp_mired: int
    configuration: dict
    force_rgb_color: bool
    hs_color: tuple
    manual_control: list
    name: str
    restored: bool
    rgb_color: tuple
    service_id: str
    service_name: str
    sun_position: float
    supported_features: int
    uuid: str
    xy_color: tuple

    def turn_off(self):
        ...

    def turn_on(self):
        ...

    def toggle(self):
        ...

class switch:
    adaptive_lighting_sleep_mode_bedroom_kit: _switch_state
    adaptive_lighting_adapt_color_bedroom_kit: _switch_state
    adaptive_lighting_adapt_brightness_bedroom_kit: _switch_state
    adaptive_lighting_bedroom_kit: _switch_state
    adaptive_lighting_sleep_mode_bedroom_ashton: _switch_state
    adaptive_lighting_adapt_color_bedroom_ashton: _switch_state
    adaptive_lighting_adapt_brightness_bedroom_ashton: _switch_state
    adaptive_lighting_bedroom_ashton: _switch_state
    adaptive_lighting_sleep_mode_bedroom_closet: _switch_state
    adaptive_lighting_adapt_color_bedroom_closet: _switch_state
    adaptive_lighting_adapt_brightness_bedroom_closet: _switch_state
    adaptive_lighting_bedroom_closet: _switch_state
    adaptive_lighting_sleep_mode_furnace_room: _switch_state
    adaptive_lighting_adapt_color_furnace_room: _switch_state
    adaptive_lighting_adapt_brightness_furnace_room: _switch_state
    adaptive_lighting_furnace_room: _switch_state
    adaptive_lighting_sleep_mode_outside: _switch_state
    adaptive_lighting_adapt_color_outside: _switch_state
    adaptive_lighting_adapt_brightness_outside: _switch_state
    adaptive_lighting_outside: _switch_state
    adaptive_lighting_sleep_mode_stovetop: _switch_state
    adaptive_lighting_adapt_color_stovetop: _switch_state
    adaptive_lighting_adapt_brightness_stovetop: _switch_state
    adaptive_lighting_stovetop: _switch_state
    hacs_pre_release: _switch_state
    cloud_alexa: _switch_state
    cloud_alexa_report_state: _switch_state
    cloud_google: _switch_state
    cloud_google_report_state: _switch_state
    cloud_remote: _switch_state
    api_data_fetching: _switch_state
    opnsense_service_cron_status: _switch_state
    opnsense_service_gateway_monitor_wan_dhcp6_status: _switch_state
    opnsense_service_gateway_monitor_wan_dhcp_status: _switch_state
    opnsense_service_gateway_monitor_nordvpn_vpnv6_status: _switch_state
    opnsense_service_gateway_monitor_nordvpn_vpnv4_status: _switch_state
    opnsense_service_haproxy_load_balancer_status: _switch_state
    opnsense_service_iperf_performance_test_status: _switch_state
    opnsense_service_kea_dhcpv4_server_status: _switch_state
    opnsense_service_universal_plug_and_play_status: _switch_state
    opnsense_service_network_time_daemon_status: _switch_state
    opnsense_service_secure_shell_daemon_status: _switch_state
    opnsense_service_opnarp_daemon_status: _switch_state
    opnsense_service_router_advertisement_daemon_status: _switch_state
    opnsense_service_netflow_distributor_status: _switch_state
    opnsense_service_net_snmp_daemon_status: _switch_state
    opnsense_service_syslog_ng_daemon_status: _switch_state
    opnsense_service_tailscale_status: _switch_state
    opnsense_service_unbound_dns_status: _switch_state
    opnsense_openvpn_client_nord_vpn: _switch_state
    guest_wifi_2_4g: _switch_state
    guest_wifi_5g: _switch_state
    guest_wifi_6g: _switch_state
    wifi_2_4g: _switch_state
    wifi_5g: _switch_state
    wifi_6g: _switch_state
    iot_wifi_2_4g: _switch_state
    iot_wifi_5g: _switch_state
    iot_wifi_6g: _switch_state
    router_data_fetching: _switch_state
    guest_wifi_2_4g_2: _switch_state
    guest_wifi_5g_2: _switch_state
    guest_wifi_6g_2: _switch_state
    wifi_2_4g_2: _switch_state
    wifi_5g_2: _switch_state
    wifi_6g_2: _switch_state
    iot_wifi_2_4g_2: _switch_state
    iot_wifi_5g_2: _switch_state
    iot_wifi_6g_2: _switch_state
    router_data_fetching_2: _switch_state
    living_room_do_not_disturb: _switch_state
    bathroom_do_not_disturb: _switch_state
    bedroom_speaker_do_not_disturb: _switch_state
    backyard_camera_hq_detect: _switch_state
    backyard_camera_hq_motion: _switch_state
    backyard_camera_hq_recordings: _switch_state
    backyard_camera_hq_snapshots: _switch_state
    backyard_camera_hq_improve_contrast: _switch_state
    backyard_camera_hq_audio_detection: _switch_state
    none_server_fan_server_fan: _switch_state
    none_printer_printer: _switch_state
    adaptive_lighting_sleep_mode_understairs_light: _switch_state
    adaptive_lighting_adapt_color_understairs_light: _switch_state
    adaptive_lighting_adapt_brightness_understairs_light: _switch_state
    adaptive_lighting_understairs_light: _switch_state
    opnsense_service_acme_client_status: _switch_state
    opnsense_service_ddclient_status: _switch_state
    piper_container: _switch_state
    homeassistant_container: _switch_state
    whisper_container: _switch_state
    wordpress_wordpress_1_container: _switch_state
    esphome_container: _switch_state
    portainer_container: _switch_state
    music_assistant_container: _switch_state
    prometheus_container: _switch_state
    mailcowdockerized_watchdog_mailcow_1_container: _switch_state
    mailcowdockerized_acme_mailcow_1_container: _switch_state
    mailcowdockerized_nginx_mailcow_1_container: _switch_state
    mailcowdockerized_ofelia_mailcow_1_container: _switch_state
    mailcowdockerized_rspamd_mailcow_1_container: _switch_state
    mailcowdockerized_postfix_mailcow_1_container: _switch_state
    mailcowdockerized_dovecot_mailcow_1_container: _switch_state
    mailcowdockerized_php_fpm_mailcow_1_container: _switch_state
    mailcowdockerized_mysql_mailcow_1_container: _switch_state
    mailcowdockerized_clamd_mailcow_1_container: _switch_state
    mailcowdockerized_postfix_tlspol_mailcow_1_container: _switch_state
    mailcowdockerized_redis_mailcow_1_container: _switch_state
    mailcowdockerized_sogo_mailcow_1_container: _switch_state
    mailcowdockerized_dockerapi_mailcow_1_container: _switch_state
    mailcowdockerized_olefy_mailcow_1_container: _switch_state
    mailcowdockerized_memcached_mailcow_1_container: _switch_state
    mailcowdockerized_unbound_mailcow_1_container: _switch_state
    mailcowdockerized_netfilter_mailcow_1_container: _switch_state
    plex_container: _switch_state
    frigate_container: _switch_state
    wordpress_db_1_container: _switch_state
    watchtower_container: _switch_state
    tasmoadmin_container: _switch_state
    scrutiny_container: _switch_state
    opnsense_exporter_container: _switch_state
    nodered_container: _switch_state
    grafana_container: _switch_state
    timescaledb_poc_container: _switch_state
    postgres_exporter_container: _switch_state
    opnsense_unbound_blocklist_default: _switch_state
    backyard_camera_hq_review_alerts: _switch_state
    backyard_camera_hq_review_detections: _switch_state
    opnsense_service_host_discovery_service_status: _switch_state
    portainer_agent_container: _switch_state
    ha_esphome_1_container: _switch_state
    ha_nodered_1_container: _switch_state
    ha_watchtower_1_container: _switch_state
    ha_whisper_1_container: _switch_state
    ha_piper_1_container: _switch_state
    ha_aircast_1_container: _switch_state
    ha_scrutiny_1_container: _switch_state
    mediamtx_container: _switch_state
    mediamtx_container_2: _switch_state
    wordpress_wordpress_1_container_2: _switch_state
    homeassistant_container_2: _switch_state
    plex_container_2: _switch_state
    aircast_container_2: _switch_state
    wordpress_db_1_container_2: _switch_state
    music_assistant_container_2: _switch_state
    tasmoadmin_container_2: _switch_state
    nodered_container_2: _switch_state
    esphome_container_2: _switch_state
    frigate_container_2: _switch_state
    portainer_container_2: _switch_state
    watchtower_container_2: _switch_state
    scrutiny_container_2: _switch_state
    piper_container_2: _switch_state
    whisper_container_2: _switch_state
    prometheus_container_2: _switch_state
    opnsense_exporter_container_2: _switch_state
    grafana_container_2: _switch_state
    timescaledb_poc_container_2: _switch_state
    postgres_exporter_container_2: _switch_state
    ha_aircast_1_container_2: _switch_state
    ha_nodered_1_container_2: _switch_state
    ha_esphome_1_container_2: _switch_state
    portainer_agent_container_2: _switch_state
    ha_watchtower_1_container_2: _switch_state
    ha_whisper_1_container_2: _switch_state
    ha_piper_1_container_2: _switch_state
    ha_scrutiny_1_container_2: _switch_state
    home_assistant_main_stack: _switch_state
    timescale_db_stack: _switch_state
    wordpress_stack: _switch_state
    rtmp_relay_stack: _switch_state
    rtmp_relay_stack_2: _switch_state

    @staticmethod
    def turn_off(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_on(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

class system_log:

    @staticmethod
    def clear():
        ...

    @staticmethod
    def write(*, message: str, level: Literal['', 'debug', 'info', 'warning', 'error', 'critical']='error', logger: str | None=None):
        """

        Args:
            message:  Example: Something went wrong
            logger:  Example: mycomponent.myplatform"""
        ...

class telegram_bot:

    @staticmethod
    def send_message(*, message: str, entity_id: str | None=None, title: str | None=None, parse_mode: Literal['', 'html', 'markdown', 'markdownv2', 'plain_text'] | None=None, disable_notification: bool | None=None, disable_web_page_preview: bool | None=None, keyboard: str | None=None, inline_keyboard: Any | None=None, message_tag: str | None=None, reply_to_message_id: float | None=None, message_thread_id: float | None=None, advanced=None) -> dict[str, Any]:
        """

        Args:
            message:  Example: The garage door has been open for 10 minutes.
            title:  Example: Your Garage Door Friend
            keyboard:  Example: ["/command1, /command2", "/command3"]
            inline_keyboard:  Example: ["/button1, /button2", "/button3"] or ["Text button1:/button1, Text button2:/button2", "Text button3:/button3"] or [[["Text button1", "/button1"], ["Text button2", "/button2"]], [["Text button3", "/button3"]]]
            message_tag:  Example: msg_to_edit"""
        ...

    @staticmethod
    def send_chat_action(*, entity_id: str | None=None, chat_action: Literal['', 'typing', 'upload_photo', 'record_video', 'upload_video', 'record_voice', 'upload_voice', 'upload_document', 'choose_sticker', 'find_location', 'record_video_note', 'upload_video_note'] | None=None, message_thread_id: float | None=None, advanced=None) -> dict[str, Any]:
        ...

    @staticmethod
    def send_photo(*, entity_id: str | None=None, url: str | None=None, url_options=None, file: str | None=None, caption: str | None=None, parse_mode: Literal['', 'html', 'markdown', 'markdownv2', 'plain_text'] | None=None, disable_notification: bool | None=None, keyboard: str | None=None, inline_keyboard: Any | None=None, message_tag: str | None=None, reply_to_message_id: float | None=None, message_thread_id: float | None=None, advanced=None) -> dict[str, Any]:
        """

        Args:
            url:  Example: http://example.org/path/to/the/image.png
            file:  Example: /path/to/the/image.png
            caption:  Example: My image
            keyboard:  Example: ["/command1, /command2", "/command3"]
            inline_keyboard:  Example: ["/button1, /button2", "/button3"] or [[["Text button1", "/button1"], ["Text button2", "/button2"]], [["Text button3", "/button3"]]]
            message_tag:  Example: msg_to_edit"""
        ...

    @staticmethod
    def send_media_group(*, media: Any, entity_id: str | None=None, parse_mode: Literal['', 'html', 'markdown', 'markdownv2', 'plain_text'] | None=None, disable_notification: bool | None=None, protect_content: bool | None=None, reply_to_message_id: float | None=None, message_thread_id: float | None=None, advanced=None) -> dict[str, Any]:
        ...

    @staticmethod
    def send_sticker(*, entity_id: str | None=None, url: str | None=None, url_options=None, file: str | None=None, sticker_id: str | None=None, disable_notification: bool | None=None, keyboard: str | None=None, inline_keyboard: Any | None=None, message_tag: str | None=None, reply_to_message_id: float | None=None, message_thread_id: float | None=None, advanced=None) -> dict[str, Any]:
        """

        Args:
            url:  Example: http://example.org/path/to/the/sticker.webp
            file:  Example: /path/to/the/sticker.webp
            sticker_id:  Example: CAACAgIAAxkBAAEDDldhZD-hqWclr6krLq-FWSfCrGNmOQAC9gAD9HsZAAFeYY-ltPYnrCEE
            keyboard:  Example: ["/command1, /command2", "/command3"]
            inline_keyboard:  Example: ["/button1, /button2", "/button3"] or [[["Text button1", "/button1"], ["Text button2", "/button2"]], [["Text button3", "/button3"]]]
            message_tag:  Example: msg_to_edit"""
        ...

    @staticmethod
    def send_animation(*, entity_id: str | None=None, url: str | None=None, url_options=None, file: str | None=None, caption: str | None=None, parse_mode: Literal['', 'html', 'markdown', 'markdownv2', 'plain_text'] | None=None, disable_notification: bool | None=None, keyboard: str | None=None, inline_keyboard: Any | None=None, message_tag: str | None=None, reply_to_message_id: float | None=None, message_thread_id: float | None=None, advanced=None) -> dict[str, Any]:
        """

        Args:
            url:  Example: http://example.org/path/to/the/animation.gif
            file:  Example: /path/to/the/animation.gif
            caption:  Example: My animation
            keyboard:  Example: ["/command1, /command2", "/command3"]
            inline_keyboard:  Example: ["/button1, /button2", "/button3"] or [[["Text button1", "/button1"], ["Text button2", "/button2"]], [["Text button3", "/button3"]]]
            message_tag:  Example: msg_to_edit"""
        ...

    @staticmethod
    def send_video(*, entity_id: str | None=None, url: str | None=None, url_options=None, file: str | None=None, caption: str | None=None, parse_mode: Literal['', 'html', 'markdown', 'markdownv2', 'plain_text'] | None=None, disable_notification: bool | None=None, keyboard: str | None=None, inline_keyboard: Any | None=None, message_tag: str | None=None, reply_to_message_id: float | None=None, message_thread_id: float | None=None, advanced=None) -> dict[str, Any]:
        """

        Args:
            url:  Example: http://example.org/path/to/the/video.mp4
            file:  Example: /path/to/the/video.mp4
            caption:  Example: My video
            keyboard:  Example: ["/command1, /command2", "/command3"]
            inline_keyboard:  Example: ["/button1, /button2", "/button3"] or [[["Text button1", "/button1"], ["Text button2", "/button2"]], [["Text button3", "/button3"]]]
            message_tag:  Example: msg_to_edit"""
        ...

    @staticmethod
    def send_voice(*, entity_id: str | None=None, url: str | None=None, url_options=None, file: str | None=None, caption: str | None=None, disable_notification: bool | None=None, keyboard: str | None=None, inline_keyboard: Any | None=None, message_tag: str | None=None, reply_to_message_id: float | None=None, message_thread_id: float | None=None, advanced=None) -> dict[str, Any]:
        """

        Args:
            url:  Example: http://example.org/path/to/the/voice.opus
            file:  Example: /path/to/the/voice.opus
            caption:  Example: My microphone recording
            keyboard:  Example: ["/command1, /command2", "/command3"]
            inline_keyboard:  Example: ["/button1, /button2", "/button3"] or [[["Text button1", "/button1"], ["Text button2", "/button2"]], [["Text button3", "/button3"]]]
            message_tag:  Example: msg_to_edit"""
        ...

    @staticmethod
    def send_document(*, entity_id: str | None=None, url: str | None=None, url_options=None, file: str | None=None, caption: str | None=None, parse_mode: Literal['', 'html', 'markdown', 'markdownv2', 'plain_text'] | None=None, disable_notification: bool | None=None, keyboard: str | None=None, inline_keyboard: Any | None=None, message_tag: str | None=None, reply_to_message_id: float | None=None, message_thread_id: float | None=None, advanced=None) -> dict[str, Any]:
        """

        Args:
            url:  Example: http://example.org/path/to/the/document.odf
            file:  Example: /tmp/whatever.odf
            caption:  Example: Document Title xy
            keyboard:  Example: ["/command1, /command2", "/command3"]
            inline_keyboard:  Example: ["/button1, /button2", "/button3"] or [[["Text button1", "/button1"], ["Text button2", "/button2"]], [["Text button3", "/button3"]]]
            message_tag:  Example: msg_to_edit"""
        ...

    @staticmethod
    def send_location(*, latitude: int, longitude: int, entity_id: str | None=None, disable_notification: bool | None=None, keyboard: str | None=None, inline_keyboard: Any | None=None, message_tag: str | None=None, reply_to_message_id: float | None=None, message_thread_id: float | None=None, advanced=None) -> dict[str, Any]:
        """

        Args:
            keyboard:  Example: ["/command1, /command2", "/command3"]
            inline_keyboard:  Example: ["/button1, /button2", "/button3"] or [[["Text button1", "/button1"], ["Text button2", "/button2"]], [["Text button3", "/button3"]]]
            message_tag:  Example: msg_to_edit"""
        ...

    @staticmethod
    def send_poll(*, question: str, options: str, entity_id: str | None=None, is_anonymous: bool=True, allows_multiple_answers: bool | None=None, open_period: int | None=None, disable_notification: bool | None=None, reply_to_message_id: float | None=None, message_thread_id: float | None=None, advanced=None) -> dict[str, Any]:
        """

        Args:
            options:  Example: ["Option 1", "Option 2", "Option 3"]"""
        ...

    @staticmethod
    def edit_message(*, message_id: str, entity_id: str | None=None, message: str | None=None, title: str | None=None, parse_mode: Literal['', 'html', 'markdown', 'markdownv2', 'plain_text'] | None=None, disable_web_page_preview: bool | None=None, inline_keyboard: Any | None=None, advanced=None):
        """

        Args:
            message_id:  Example: {{ trigger.event.data.message.message_id }}
            message:  Example: The garage door has been open for 10 minutes.
            title:  Example: Your Garage Door Friend
            inline_keyboard:  Example: ["/button1, /button2", "/button3"] or [[["Text button1", "/button1"], ["Text button2", "/button2"]], [["Text button3", "/button3"]]]"""
        ...

    @staticmethod
    def edit_message_media(*, message_id: str, entity_id: str | None=None, media_type: Literal['', 'animation', 'audio', 'document', 'photo', 'video'] | None=None, url: str | None=None, url_options=None, file: str | None=None, caption: str | None=None, inline_keyboard: Any | None=None, advanced=None):
        """

        Args:
            message_id:  Example: {{ trigger.event.data.message.message_id }}
            url:  Example: http://example.org/path/to/the/image.png
            file:  Example: /path/to/the/image.png
            caption:  Example: Document Title xy
            inline_keyboard:  Example: ["/button1, /button2", "/button3"] or [[["Text button1", "/button1"], ["Text button2", "/button2"]], [["Text button3", "/button3"]]]"""
        ...

    @staticmethod
    def edit_caption(*, message_id: str, caption: str, entity_id: str | None=None, inline_keyboard: Any | None=None, advanced=None):
        """

        Args:
            message_id:  Example: {{ trigger.event.data.message.message_id }}
            caption:  Example: The garage door has been open for 10 minutes.
            inline_keyboard:  Example: ["/button1, /button2", "/button3"] or [[["Text button1", "/button1"], ["Text button2", "/button2"]], [["Text button3", "/button3"]]]"""
        ...

    @staticmethod
    def edit_replymarkup(*, message_id: str, inline_keyboard: Any, entity_id: str | None=None, advanced=None):
        """

        Args:
            message_id:  Example: {{ trigger.event.data.message.message_id }}
            inline_keyboard:  Example: ["/button1, /button2", "/button3"] or [[["Text button1", "/button1"], ["Text button2", "/button2"]], [["Text button3", "/button3"]]]"""
        ...

    @staticmethod
    def answer_callback_query(*, message: str, callback_query_id: str, show_alert: bool, config_entry_id: str | None=None):
        """

        Args:
            message:  Example: OK, I'm listening
            callback_query_id:  Example: {{ trigger.event.data.id }}"""
        ...

    @staticmethod
    def delete_message(*, message_id: str, entity_id: str | None=None, advanced=None):
        """

        Args:
            message_id:  Example: {{ trigger.event.data.message.message_id }}"""
        ...

    @staticmethod
    def leave_chat(*, entity_id: str | None=None, advanced=None):
        ...

    @staticmethod
    def set_message_reaction(*, message_id: str, reaction: str, entity_id: str | None=None, is_big: bool | None=None, advanced=None):
        """

        Args:
            message_id:  Example: 54321
            reaction:  Example: 👍"""
        ...

    @staticmethod
    def download_file(*, file_id: str, config_entry_id: str | None=None, directory_path: str='/config/telegram_bot', file_name: str | None=None) -> dict[str, Any]:
        """

        Args:
            file_id:  Example: ABCD1234Efgh5678Ijkl90mnopQRStuvwx
            file_name:  Example: my_downloaded_file"""
        ...

class telegram_client:

    @staticmethod
    def send_messages(*, config_entry_id: str | None=None, target_username: str | None=None, target_id: str | None=None, message: str | None=None, reply_to: float | None=None, parse_mode: Literal['', 'html', 'markdown'] | None=None, link_preview: bool | None=None, file: str | None=None, force_document: bool | None=None, clear_draft: bool | None=None, keyboard: Any | None=None, inline_keyboard: Any | None=None, keyboard_resize: bool | None=None, keyboard_single_use: bool | None=None, silent: bool | None=None, supports_streaming: bool | None=None, schedule: datetime | None=None, comment_to: float | None=None, nosound_video: bool | None=None):
        """

        Args:
            target_username:  Example: me
            message:  Example: This is the test message, sent from **Telegram client** for Home Assistant.
            parse_mode:  Example: markdown
            file:  Example: configuration.yaml
            inline_keyboard:  Example: [[{'text': '😂', 'data': 'joy'}, {'text': '🤣', 'data': 'rofl'}, {'text': '😅', 'data': 'sweat'}], [{'text': '😀', 'data': 'grinning'}, {'text': '😃', 'data': 'smiley'}, {'text': '😄', 'data': 'smile'}]]"""
        ...

    @staticmethod
    def edit_message(*, config_entry_id: str, message: float, text: str, target_username: str | None=None, target_id: float | None=None, parse_mode: Literal['', 'html', 'markdown'] | None=None, link_preview: bool | None=None, file: str | None=None, force_document: bool | None=None, keyboard: Any | None=None, inline_keyboard: Any | None=None, keyboard_resize: bool | None=None, keyboard_single_use: bool | None=None, supports_streaming: bool | None=None, schedule: datetime | None=None):
        """

        Args:
            message:  Example: 100
            text:  Example: **New** message text.
            target_username:  Example: me
            parse_mode:  Example: markdown
            file:  Example: configuration.yaml
            inline_keyboard:  Example: [[{'text': '😂', 'data': 'joy'}, {'text': '🤣', 'data': 'rofl'}, {'text': '😅', 'data': 'sweat'}], [{'text': '😀', 'data': 'grinning'}, {'text': '😃', 'data': 'smiley'}, {'text': 'smile', 'data': '😄'}]]"""
        ...

    @staticmethod
    def delete_messages(*, config_entry_id: str, message_ids: str, target_username: str | None=None, target_id: str | None=None, revoke: bool | None=None):
        """

        Args:
            message_ids:  Example: 2
            target_username:  Example: me"""
        ...

class template:

    @staticmethod
    def reload():
        ...

class _text_state(StateVal):
    max: int
    min: int
    mode: str
    pattern: Any

    def set_value(self, value: str):
        """

        Args:
            value:  Example: Hello world!"""
        ...

class text:
    flightradar24_add_to_track: _text_state
    flightradar24_remove_from_track: _text_state
    sir_flop_s_puzzle_helper: _text_state
    bing_wallpaper_description_bing_wallpaper: _text_state
    flightradar24_airport_track: _text_state

    @staticmethod
    def set_value(*, entity_id: str, value: str):
        """

        Args:
            entity_id: Entity ID
            value:  Example: Hello world!"""
        ...

class time:

    @staticmethod
    def set_value(*, entity_id: str, time: str):
        """

        Args:
            entity_id: Entity ID
            time:  Example: 22:15"""
        ...

class _timer_state(StateVal):
    duration: str
    editable: bool
    restore: bool

    def start(self, duration):
        """

        Args:
            duration:  Example: 00:01:00 or 60"""
        ...

    def pause(self):
        ...

    def cancel(self):
        ...

    def finish(self):
        ...

    def change(self, duration):
        """

        Args:
            duration:  Example: 00:01:00, 60 or -60"""
        ...

    def set_duration(self, duration: str):
        """Set duration for an existing timer.

        Args:
            duration: New duration for the timer, as a timedelta string. Example: 00:01:00, 60"""
        ...

class timer:
    outside_light_timer: _timer_state
    fan_timer: _timer_state
    under_stairs_closet_light: _timer_state
    night_outside_light: _timer_state
    piper_speak: _timer_state
    bread_timer: _timer_state
    adjustable_timer: _timer_state
    bread_warming_timer: _timer_state

    @staticmethod
    def reload():
        ...

    @staticmethod
    def start(*, entity_id: str, duration=None):
        """

        Args:
            entity_id: Entity ID
            duration:  Example: 00:01:00 or 60"""
        ...

    @staticmethod
    def pause(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def cancel(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def finish(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def change(*, entity_id: str, duration=0):
        """

        Args:
            entity_id: Entity ID
            duration:  Example: 00:01:00, 60 or -60"""
        ...

    @staticmethod
    def set_duration(*, entity_id: str, duration: str):
        """Set duration for an existing timer.

        Args:
            entity_id: Entity ID
            duration: New duration for the timer, as a timedelta string. Example: 00:01:00, 60"""
        ...

class _todo_state(StateVal):
    restored: bool
    supported_features: int

    def add_item(self, *, item: str, due_date: datetime | None=None, due_datetime: datetime | None=None, description: str | None=None):
        """

        Args:
            item:  Example: Submit income tax return
            due_date:  Example: 2023-11-17
            due_datetime:  Example: 2023-11-17 13:30:00
            description:  Example: A more complete description of the to-do item than that provided by the summary."""
        ...

    def update_item(self, *, item: str, rename: str | None=None, status: Literal['', 'needs_action', 'completed'] | None=None, due_date: datetime | None=None, due_datetime: datetime | None=None, description: str | None=None):
        """

        Args:
            item:  Example: Submit income tax return
            rename:  Example: Something else
            status:  Example: needs_action
            due_date:  Example: 2023-11-17
            due_datetime:  Example: 2023-11-17 13:30:00
            description:  Example: A more complete description of the to-do item than that provided by the summary."""
        ...

    def remove_item(self, item: str):
        """

        Args:
            item:  Example: Submit income tax return"""
        ...

    def get_items(self, status: Literal['', 'needs_action', 'completed']) -> dict[str, Any]:
        """

        Args:
            status:  Example: needs_action"""
        ...

    def remove_completed_items(self):
        ...

class todo:
    shopping_list: _todo_state
    home_assistant_setup: _todo_state
    personal: _todo_state
    clean_up: _todo_state
    house: _todo_state
    justice: _todo_state
    telus_website_support: _todo_state
    laptop: _todo_state
    reminders: _todo_state
    sir_flop_s_puzzles: _todo_state
    inbox: _todo_state
    home: _todo_state
    my_work: _todo_state
    inbox_2: _todo_state
    home_2: _todo_state
    my_work_2: _todo_state

    @staticmethod
    def add_item(*, entity_id: str, item: str, due_date: datetime | None=None, due_datetime: datetime | None=None, description: str | None=None):
        """

        Args:
            entity_id: Entity ID
            item:  Example: Submit income tax return
            due_date:  Example: 2023-11-17
            due_datetime:  Example: 2023-11-17 13:30:00
            description:  Example: A more complete description of the to-do item than that provided by the summary."""
        ...

    @staticmethod
    def update_item(*, entity_id: str, item: str, rename: str | None=None, status: Literal['', 'needs_action', 'completed'] | None=None, due_date: datetime | None=None, due_datetime: datetime | None=None, description: str | None=None):
        """

        Args:
            entity_id: Entity ID
            item:  Example: Submit income tax return
            rename:  Example: Something else
            status:  Example: needs_action
            due_date:  Example: 2023-11-17
            due_datetime:  Example: 2023-11-17 13:30:00
            description:  Example: A more complete description of the to-do item than that provided by the summary."""
        ...

    @staticmethod
    def remove_item(*, entity_id: str, item: str):
        """

        Args:
            entity_id: Entity ID
            item:  Example: Submit income tax return"""
        ...

    @staticmethod
    def get_items(*, entity_id: str, status: Literal['', 'needs_action', 'completed']='needs_action') -> dict[str, Any]:
        """

        Args:
            entity_id: Entity ID
            status:  Example: needs_action"""
        ...

    @staticmethod
    def remove_completed_items(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

class todoist:

    @staticmethod
    def new_task(*, content: str, description: str | None=None, project: str='Inbox', section: str | None=None, labels: str | None=None, assignee: str | None=None, priority: int | None=None, due_date_string: str | None=None, due_date_lang: Literal['', 'da', 'de', 'en', 'es', 'fr', 'it', 'ja', 'ko', 'nl', 'pl', 'pt', 'ru', 'sv', 'zh'] | None=None, due_date: str | None=None, reminder_date_string: str | None=None, reminder_date_lang: Literal['', 'da', 'de', 'en', 'es', 'fr', 'it', 'ja', 'ko', 'nl', 'pl', 'pt', 'ru', 'sv', 'zh'] | None=None, reminder_date: str | None=None):
        """

        Args:
            content:  Example: Pick up the mail.
            project:  Example: Errands
            section:  Example: Deliveries
            labels:  Example: Chores,Delivieries
            assignee:  Example: username
            due_date_string:  Example: Tomorrow
            due_date:  Example: 2019-10-22
            reminder_date_string:  Example: Tomorrow
            reminder_date:  Example: 2019-10-22T10:30:00"""
        ...

class _tts_state(StateVal):

    def speak(self, *, media_player_entity_id: str, message: str, cache: bool=True, language: str | None=None, options: Any | None=None):
        """

        Args:
            message:  Example: My name is hanna
            language:  Example: ru
            options:  Example: platform specific"""
        ...

class tts:
    google_en_com: _tts_state
    google_translate_en_ca: _tts_state
    google_ai_tts: _tts_state
    piper: _tts_state

    @staticmethod
    def speak(*, entity_id: str, media_player_entity_id: str, message: str, cache: bool=True, language: str | None=None, options: Any | None=None):
        """

        Args:
            entity_id: Entity ID
            message:  Example: My name is hanna
            language:  Example: ru
            options:  Example: platform specific"""
        ...

    @staticmethod
    def clear_cache():
        ...

    @staticmethod
    def cloud_say(*, entity_id: str, message: str, cache: bool=False, language: str | None=None, options: Any | None=None):
        """Say something using text-to-speech on a media player with cloud.

        Args:
            message:  Example: My name is hanna
            language:  Example: ru
            options:  Example: platform specific"""
        ...

class _update_state(StateVal):
    auto_update: bool
    display_precision: int
    entity_picture: str
    in_progress: bool
    installed_version: str
    latest_version: str
    opnsense_download_size: str
    opnsense_last_check: str
    opnsense_needs_reboot: str
    opnsense_os_version: str
    opnsense_product_id: str
    opnsense_product_target: str
    opnsense_product_version: str
    opnsense_status: str
    opnsense_status_msg: str
    opnsense_upgrade_needs_reboot: str
    release_summary: str
    release_url: str
    restored: bool
    skipped_version: Any
    supported_features: int
    title: str
    update_percentage: Any

    def install(self, *, version: str | None=None, backup: bool | None=None):
        """

        Args:
            version:  Example: 1.0.0"""
        ...

    def skip(self):
        ...

    def clear_skipped(self):
        ...

class update:
    hacs_update: _update_state
    adaptive_lighting_update: _update_state
    iphone_device_tracker_update: _update_state
    horizon_card_update: _update_state
    browser_mod_update: _update_state
    node_red_companion_update: _update_state
    opnsense_integration_for_home_assistant_update: _update_state
    sun2_update: _update_state
    pyscript_update: _update_state
    flightradar24_update: _update_state
    openweathermaphistory_update: _update_state
    met_no_next_6_hours_forecast_update: _update_state
    gasbuddy_update: _update_state
    spook_your_homie_update: _update_state
    lunar_phase_update: _update_state
    icloud3_v3_idevice_tracker_update: _update_state
    universal_remote_card_update: _update_state
    wapi_custom_whatsapp_notifications_update: _update_state
    timer_bar_card_update: _update_state
    hass_agent_2_integration_media_player_notifications_update: _update_state
    simpleicons_update: _update_state
    google_home_update: _update_state
    weather_com_update: _update_state
    compass_card_update: _update_state
    zha_toolkit_service_for_advanced_zigbee_usage_update: _update_state
    hp_printers_integration_update: _update_state
    upnp_availability_update: _update_state
    steam_wishlist_update: _update_state
    places_update: _update_state
    battery_notes_update: _update_state
    waste_collection_schedule_update: _update_state
    qbittorrent_mkii_update: _update_state
    opnsense_firmware_updates_available: _update_state
    event_sensor_update: _update_state
    bluesky_post_integration_update: _update_state
    pirate_weather_update: _update_state
    yahoo_finance_update: _update_state
    tp_link_router_update: _update_state
    ha_floorplan_your_imagination_almost_defines_the_limits_update: _update_state
    met_no_nowcast_update: _update_state
    ai_automation_suggester_update: _update_state
    status_card_update: _update_state
    custom_icons_update: _update_state
    debian_dell_update: _update_state
    frigate_update: _update_state
    advanced_camera_card_update: _update_state
    frigate_server: _update_state
    astroweather_update: _update_state
    discord_game_update: _update_state
    genius_lyrics_update: _update_state
    lovelace_google_keep_card_update: _update_state
    qr_code_generator_update: _update_state
    noaa_space_weather_update: _update_state
    playstation_r_3_update: _update_state
    folding_homecontrol_update: _update_state
    sunlight_intensity_update: _update_state
    virtual_keys_update: _update_state
    music_assistant_queue_actions_update: _update_state
    weatherapi_update: _update_state
    gpio_integration_update: _update_state
    telegram_client_update: _update_state
    file_update: _update_state
    moon_astro_update: _update_state
    pypi_updates_update: _update_state
    neo_watcher_update: _update_state
    duolingo_update: _update_state
    tor_check_update: _update_state
    astroweather_card_update: _update_state
    custom_features_for_home_assistant_cards_update: _update_state
    generate_readme_update: _update_state
    simple_plant_update: _update_state
    z_wave_card_set_update: _update_state
    atomic_calendar_revive_update: _update_state
    home_maintenance_update: _update_state
    gauge_card_pro_update: _update_state
    rss_accordion_update: _update_state
    feedparser_update: _update_state
    optimistic_feedback_update: _update_state
    expander_card_update: _update_state
    navbar_card_update: _update_state
    prometheus_sensor_update: _update_state
    music_assistant_player_card_update: _update_state
    canary_update: _update_state
    wall_clock_card_update: _update_state
    mushroom_dashboard_strategy_update: _update_state
    hwmon_temperatures_update: _update_state
    nhl_api_update: _update_state
    paper_buttons_row_update: _update_state
    background_graph_entities_update: _update_state
    google_assistant_sdk_custom_update: _update_state
    bing_wallpaper_update: _update_state
    gif_update: _update_state
    psychrometric_chart_update: _update_state
    magic_areas_update: _update_state
    microsoft_365_mail_update: _update_state
    clash_royale_update: _update_state
    shopping_list_with_grocy_update: _update_state
    material_home_component_update: _update_state
    card_mod_update: _update_state
    mail_and_packages_update: _update_state
    zashtys_satellite_rpi_mqtt_monitor: _update_state
    llm_vision_update: _update_state

    @staticmethod
    def install(*, entity_id: str, version: str | None=None, backup: bool | None=None):
        """

        Args:
            entity_id: Entity ID
            version:  Example: 1.0.0"""
        ...

    @staticmethod
    def skip(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def clear_skipped(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

class vacuum:

    @staticmethod
    def start(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def pause(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def return_to_base(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def clean_spot(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def clean_area(*, entity_id: str, cleaning_area_id):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def locate(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def stop(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_fan_speed(*, entity_id: str, fan_speed: str):
        """

        Args:
            entity_id: Entity ID
            fan_speed:  Example: low"""
        ...

    @staticmethod
    def send_command(*, entity_id: str, command: str, params: Any | None=None):
        """

        Args:
            entity_id: Entity ID
            command:  Example: set_dnd_timer
            params:  Example: { "key": "value" }"""
        ...

class valve:

    @staticmethod
    def open_valve(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def close_valve(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_valve_position(*, entity_id: str, position: int):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def stop_valve(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

class wake_on_lan:

    @staticmethod
    def send_magic_packet(*, mac: str, broadcast_address: str | None=None, broadcast_port: float=9):
        """

        Args:
            mac:  Example: aa:bb:cc:dd:ee:ff
            broadcast_address:  Example: 192.168.255.255"""
        ...

class waste_collection_schedule:

    @staticmethod
    def fetch_data():
        """Fetch data from all sources."""
        ...

class water_heater:

    @staticmethod
    def turn_on(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_off(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_away_mode(*, entity_id: str, away_mode: bool):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_temperature(*, entity_id: str, temperature: float, operation_mode: str | None=None):
        """

        Args:
            entity_id: Entity ID
            operation_mode:  Example: eco"""
        ...

    @staticmethod
    def set_operation_mode(*, entity_id: str, operation_mode: str):
        """

        Args:
            entity_id: Entity ID
            operation_mode:  Example: eco"""
        ...

class _weather_state(StateVal):
    apparent_temperature: float
    attribution: str
    calm_percentage: int
    cloud_area_fraction: int
    cloud_area_fraction_high: int
    cloud_area_fraction_low: int
    cloud_area_fraction_medium: int
    cloud_coverage: int | float
    cloudcover_percentage: int
    cloudless_percentage: int
    condition_percentage: int
    condition_plain: str
    datetime: datetime
    deep_sky_darkness: float
    deepsky_forecast_today_dayname: str
    deepsky_forecast_today_desc: str
    deepsky_forecast_today_plain: str
    deepsky_forecast_today_precipitation_amount6: float
    deepsky_forecast_tomorrow_dayname: str
    deepsky_forecast_tomorrow_desc: str
    deepsky_forecast_tomorrow_plain: str
    deepsky_forecast_tomorrow_precipitation_amount6: float
    dew_point: float
    dewpoint: float
    fog2m_area_fraction: int
    fog_area_fraction: int
    humidity: int | float
    lifted_index: float
    location_name: str
    moon_icon: str
    moon_next_dark_night: datetime
    moon_next_full_moon: datetime
    moon_next_new_moon: datetime
    moon_next_rising: datetime
    moon_next_setting: datetime
    moon_phase: float
    night_duration_astronomical: float
    ozone: float
    precipitation_amount: float
    precipitation_unit: str
    pressure: float
    pressure_unit: str
    seeing: float
    seeing_percentage: int
    sun_next_rising: datetime
    sun_next_rising_astro: datetime
    sun_next_rising_nautical: datetime
    sun_next_setting: datetime
    sun_next_setting_astro: datetime
    sun_next_setting_nautical: datetime
    supported_features: int
    temperature: float
    temperature_unit: str
    time_shift: int
    transparency: float
    transparency_percentage: int
    uv_index: int | float
    visibility: float
    visibility_unit: str
    wind_bearing: int | str | float
    wind_gust_speed: float
    wind_speed: float
    wind_speed_unit: str

    def get_forecasts(self, type: Literal['', 'daily', 'hourly', 'twice_daily']) -> dict[str, Any]:
        ...

class weather:
    met_io_forcast_home: _weather_state
    env_can_forecast: _weather_state
    openweathermap: _weather_state
    tomorrow_io_home_daily: _weather_state
    pirateweather: _weather_state
    astroweather_backyard: _weather_state
    home: _weather_state

    @staticmethod
    def get_forecasts(*, entity_id: str, type: Literal['', 'daily', 'hourly', 'twice_daily']) -> dict[str, Any]:
        """

        Args:
            entity_id: Entity ID"""
        ...

class workday:

    @staticmethod
    def check_date(*, entity_id: str, check_date: datetime | None=None) -> dict[str, Any]:
        """

        Args:
            entity_id: Entity ID
            check_date:  Example: 2022-12-25"""
        ...

class zha_toolkit:

    @staticmethod
    def execute(*, command: Literal['', 'add_group', 'add_to_group', 'all_routes_and_neighbours', 'attr_read', 'attr_write', 'backup', 'bind_group', 'bind_ieee', 'binds_get', 'binds_remove_all', 'conf_report', 'conf_report_read', 'ezsp_add_key', 'ezsp_backup', 'ezsp_clear_keys', 'ezsp_get_config_value', 'ezsp_get_ieee_by_nwk', 'ezsp_get_keys', 'ezsp_get_policy', 'ezsp_get_token', 'ezsp_get_value', 'ezsp_set_channel', 'ezsp_start_mfg', 'get_groups', 'get_routes_and_neighbours', 'get_zll_groups', 'handle_join', 'ieee_ping', 'leave', 'misc_reinitialize', 'misc_settime', 'ota_notify', 'rejoin', 'remove_all_groups', 'remove_from_group', 'remove_group', 'scan_device', 'tuya_magic', 'unbind_coordinator', 'unbind_group', 'zcl_cmd', 'zdo_flood_parent_annce', 'zdo_join_with_code', 'zdo_scan_now', 'zdo_update_nwk_id', 'znp_backup', 'znp_nvram_backup', 'znp_nvram_reset', 'znp_nvram_restore', 'znp_restore'], ieee: str | None=None, command_data: str | None=None, manf: float | None=None, cmd: float | None=None, endpoint: float | None=None, dst_endpoint: float | None=None, cluster: float | None=None, attribute: float | None=None, attr_type: float | None=None, attr_val: str | None=None, min_interval: float | None=None, max_interval: float | None=None, reportable_change: float | None=None, dir: float | None=None, tries: float | None=None, state_id: str | None=None, state_attr: str | None=None, state_value_template: str | None=None, force_update: bool | None=None, use_cache: bool | None=None, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None, allow_create: bool | None=None, read_before_write: bool | None=None, read_after_write: bool | None=None, write_if_equal: bool | None=None, expect_reply: bool | None=None, csvout: str | None=None, csvlabel: str | None=None) -> dict[str, Any]:
        """Execute ZHA Toolkit service (Examine the documentation or code to know which parameters are needed)

        Args:
            command: Command name Example: scan_device
            ieee: Entity name, device name, or IEEE address of the node to execute command Example: 00:0d:6f:00:05:7d:2d:34
            command_data: data for the command (specific command. Example, second IEEE address for binding) Example: 00:0d:6f:00:05:7d:2d:34
            manf: Manufacturer id (0 = No manufacturer id, empty=possibly automatic)
            cmd: Command Id (zcl_cmd)
            endpoint: target endpoint
            dst_endpoint: destination endpoint
            cluster: target cluster
            attribute: target attribute id (or name, accepted in most cases)
            attr_type: Attribute type (to write, ...)
            attr_val: Attribute value to write
            min_interval: Minimum report interval (seconds)
            max_interval: Maximum report interval (seconds)
            reportable_change: Minimum change before reporting
            dir: Direction indicator, according to command
            tries: Number of times the zigbee packet should be attempted
            state_id: When defined, name of state to write the read attribute value to Example: sensor.example
            state_attr: When defined, attribute in state_id to write the read attribute value to.  Write to state value when missing (and state_id is defined) Example: other_attr
            state_value_template: When defined, the read attribute is converted using this template before writing it to the state. Example: value / 100
            force_update: Force an update event when the state is written When not set or false, if the state value is unchanged, the update may not trigger an automation.
                 Example: True
            use_cache: Use zigpy attribute cache to get the value of an attribute. (Does not send a zigbee packet to read the attribute). Can also be 0, 1 or 2, where 2 has a special meaning with attr_write where it falls back to an actual read when the value is not in cache.
                 Example: True
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations
            allow_create: Allow state creation (given by state_id) if it does not exist
            read_before_write: Read attribute before writing it (used with attr_write).  When the read value matches the value to write, no write is done. Defaults to True.
            read_after_write: Read attribute after writing.  Can be used to ensure the values match.  Defaults to True
            write_if_equal: Force writing the attribute even if the read attribute already matches.  Defaults to False
            expect_reply: Wait for/expect a reply (not used yet)
            csvout: Filename of CSV to write read data to.  Written to 'csv' directory Example: ../web/mycsv.csv
            csvlabel: Label to use for read value (in CSV file) Example: SecretAttributeName"""
        ...

    @staticmethod
    def add_group(*, ieee: str, command_data: float, endpoint: float | None=None, tries: float | None=None, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None) -> dict[str, Any]:
        """Add group to endpoint groups list of device.  May be equivalent to `add_to_group`

        Args:
            ieee: Entity name, device name, or IEEE address of the node Example: 00:0d:6f:00:05:7d:2d:34
            command_data: Group id to add Example: 2
            endpoint: endpoint to get information for (all endpoints when not set)
            tries: Number of times the zigbee packet should be attempted
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations"""
        ...

    @staticmethod
    def add_to_group(*, ieee: str, command_data: float, endpoint: float | None=None, tries: float | None=None, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None) -> dict[str, Any]:
        """Add device to group

        Args:
            ieee: Entity name, device name, or IEEE address of the node Example: 00:0d:6f:00:05:7d:2d:34
            command_data: Group id to remove Example: 2
            endpoint: endpoint to remove group from (or all EP if not set)
            tries: Number of times the zigbee packet should be attempted
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations"""
        ...

    @staticmethod
    def all_routes_and_neighbours(*, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None, expect_reply: bool | None=None) -> dict[str, Any]:
        """Scan for all routes and neighbours, results saved to config/scans/...

        Args:
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations
            expect_reply: Wait for/expect a reply (not used yet)"""
        ...

    @staticmethod
    def attr_read(*, ieee: str, cluster: float, attribute: float, manf: float | None=None, endpoint: float | None=None, tries: float | None=None, state_id: str | None=None, state_attr: str | None=None, state_value_template: str | None=None, force_update: bool | None=None, use_cache: bool | None=None, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None, allow_create: bool | None=None, expect_reply: bool | None=None, csvout: str | None=None, csvlabel: str | None=None) -> dict[str, Any]:
        """Read Attribute

        Args:
            ieee: Entity name, device name, or IEEE address of the node to execute command Example: 00:0d:6f:00:05:7d:2d:34
            cluster: target cluster
            attribute: target attribute id (or name, accepted in most cases)
            manf: Manufacturer id (0 = No manufacturer id, empty=possibly automatic)
            endpoint: target endpoint
            tries: Number of times the zigbee packet should be attempted
            state_id: When defined, name of state to write the read attribute value to Example: sensor.example
            state_attr: When defined, attribute in state_id to write the read attribute value to.  Write to state value when missing (and state_id is defined) Example: other_attr
            state_value_template: When defined, the read attribute is converted using this template before writing it to the state. Example: value / 100
            force_update: Force an update event when the state is written When not set or false, if the state value is unchanged, the update may not trigger an automation.
                 Example: True
            use_cache: Use zigpy attribute cache to get the value of an attribute. (Does not send a zigbee packet to read the attribute). Can also be 0, 1 or 2, where 2 has a special meaning where it falls back to an actual read when the value is not in cache.
                 Example: True
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations
            allow_create: Allow state creation (given by state_id) if it does not exist
            expect_reply: Wait for/expect a reply (not used yet)
            csvout: Filename of CSV to write read data to.  Written to 'csv' directory Example: ../web/mycsv.csv
            csvlabel: Label to use for read value (in CSV file) Example: SecretAttributeName"""
        ...

    @staticmethod
    def attr_write(*, ieee: str, cluster: float, attribute: float, attr_val: str, manf: float | None=None, endpoint: float | None=None, attr_type: float | None=None, use_cache: bool | None=None, tries: float | None=None, state_id: str | None=None, state_attr: str | None=None, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None, allow_create: bool | None=None, read_before_write: bool | None=None, read_after_write: bool | None=None, write_if_equal: bool | None=None, expect_reply: bool | None=None, csvout: str | None=None, csvlabel: str | None=None) -> dict[str, Any]:
        """Write Attribute

        Args:
            ieee: Entity name, device name, or IEEE address of the node to execute command Example: 00:0d:6f:00:05:7d:2d:34
            cluster: target cluster
            attribute: target attribute id (or name, accepted in most cases)
            attr_val: Attribute value to write
            manf: Manufacturer id (0 = No manufacturer id, empty=possibly automatic)
            endpoint: target endpoint
            attr_type: Attribute type (to write, ...)
            use_cache: Use zigpy attribute cache to get the value of an attribute. (Does not send a zigbee packet to read the attribute). Can also be 0, 1 or 2, where 2 has a special meaning where it falls back to an actual read (when reading before a write) when the value is not in cache.
                 Example: True
            tries: Number of times the zigbee packet should be attempted
            state_id: When defined, name of state to write the read attribute value to Example: sensor.example
            state_attr: When defined, attribute in state_id to write the read attribute value to.  Write to state value when missing (and state_id is defined) Example: other_attr
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations
            allow_create: Allow state creation (given by state_id) if it does not exist
            read_before_write: Read attribute before writing it (used with attr_write).  When the read value matches the value to write, no write is done. Defaults to True.
            read_after_write: Read attribute after writing.  Can be used to ensure the values match.  Defaults to True
            write_if_equal: Force writing the attribute even if the read attribute already matches.  Defaults to False
            expect_reply: Wait for/expect a reply (not used yet)
            csvout: Filename of CSV to write read data to.  Written to 'csv' directory Example: ../web/mycsv.csv
            csvlabel: Label to use for read value (in CSV file) Example: SecretAttributeName"""
        ...

    @staticmethod
    def backup(*, command_data: str | None=None, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None, expect_reply: bool | None=None) -> dict[str, Any]:
        """Backup coordinator data (znp, bellows/ezsp)

        Args:
            command_data: Suffix for backup file Example: _bathroom_added
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations
            expect_reply: Wait for/expect a reply (not used yet)"""
        ...

    @staticmethod
    def bind_group(*, ieee: str, command_data: float, endpoint: float | None=None, cluster: float | None=None, tries: float | None=None, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None, expect_reply: bool | None=None) -> dict[str, Any]:
        """Bind clusters from ieee device to command_data device

        Args:
            ieee: Entity name, device name, or IEEE address of the node to execute command Example: 00:0d:6f:00:05:7d:2d:34
            command_data: Target group for binding Example: 00:0d:6f:00:05:7d:2d:34
            endpoint: Target endpoint (when missing: all endpoints)
            cluster: Target cluster (when missing: all internally defined cluster)
            tries: Number of times the zigbee packet should be attempted
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations
            expect_reply: Wait for/expect a reply (not used yet)"""
        ...

    @staticmethod
    def bind_ieee(*, ieee: str, command_data: str | None=None, endpoint: float | None=None, dst_endpoint: float | None=None, cluster: float | None=None, tries: float | None=None, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None, expect_reply: bool | None=None) -> dict[str, Any]:
        """Bind clusters from ieee device to command_data device

        Args:
            ieee: Entity name, device name, or IEEE address of the node to execute command Example: 00:0d:6f:00:05:7d:2d:34
            command_data: Binding target (Entity name, device name, or IEEE address of the node to execute command).  By default: coordinator Example: 00:0d:6f:00:05:7d:2d:34
            endpoint: Target endpoint (when missing: all endpoints)
            dst_endpoint: Destination endpoint (when missing: first EP with matching cluster)
            cluster: Target cluster (or all internally defined ones)
            tries: Number of times the zigbee packet should be attempted
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations
            expect_reply: Wait for/expect a reply (not used yet)"""
        ...

    @staticmethod
    def binds_get(*, ieee: str, tries: float | None=None, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None, expect_reply: bool | None=None) -> dict[str, Any]:
        """Get binding table from device.

        Args:
            ieee: Entity name, device name, or IEEE address of the node to execute command Example: 00:0d:6f:00:05:7d:2d:34
            tries: Number of times the zigbee packet should be attempted
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations
            expect_reply: Wait for/expect a reply (not used yet)"""
        ...

    @staticmethod
    def binds_remove_all(*, ieee: str, command_data: str | None=None, endpoint: float | None=None, cluster: float | None=None, tries: float | None=None, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None, expect_reply: bool | None=None) -> dict[str, Any]:
        """Remove (Unbind) all bindings from device

        Args:
            ieee: Entity name, device name, or IEEE address of the node to execute command Example: 00:0d:6f:00:05:7d:2d:34
            command_data: When provided, remove only bindings towards this device (Entity name, device name, or IEEE address of the binding destination) Example: 00:0d:6f:00:05:7d:2d:34
            endpoint: When provided, remove only bindings for this endpoint or list of endpoints (single value or list. Example: 20 or [20, 30]) Otherwise: removes bindings for all endpoints
            cluster: When provided, remove only bindings for this cluster or list of clusters (single value or list. Example: 0x0200 or [0x200, 0x300]) Otherwise: removes bindings for all clusters
            tries: Number of times the zigbee packet should be attempted
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations
            expect_reply: Wait for/expect a reply (not used yet)"""
        ...

    @staticmethod
    def conf_report(*, ieee: str, cluster: float, attribute: float, min_interval: float, max_interval: float, reportable_change: float, endpoint: float | None=None, manf: float | None=None, tries: float | None=None, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None, expect_reply: bool | None=None) -> dict[str, Any]:
        """Configure attribute reporting. You can set a high value for tries (100 or more) for sleepy devices."

        Args:
            ieee: Entity name, device name, or IEEE address of the node to execute command" Example: 00:0d:6f:00:05:7d:2d:34
            cluster: target cluster
            attribute: target attribute id (or name, accepted in most cases)
            min_interval: Minimum report interval (seconds)
            max_interval: Maximum report interval (seconds)
            reportable_change: Minimum change before reporting
            endpoint: target endpoint
            manf: Manufacturer id (0 = No manufacturer id, empty=possibly automatic)
            tries: Number of times the zigbee packet should be attempted
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations
            expect_reply: Wait for/expect a reply (not used yet)"""
        ...

    @staticmethod
    def conf_report_read(*, ieee: str, cluster: float, attribute: float, endpoint: float | None=None, manf: float | None=None, tries: float | None=None, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None, expect_reply: bool | None=None) -> dict[str, Any]:
        """Read attribute report configuration You can set a high value for tries (100 or more) for sleepy devices."

        Args:
            ieee: Entity name, device name, or IEEE address of the node to execute command" Example: 00:0d:6f:00:05:7d:2d:34
            cluster: target cluster
            attribute: target attribute id (or name, accepted in most cases), can be a list
            endpoint: target endpoint
            manf: Manufacturer id (0 = No manufacturer id, empty=possibly automatic)
            tries: Number of times the zigbee packet should be attempted
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations
            expect_reply: Wait for/expect a reply (not used yet)"""
        ...

    @staticmethod
    def ezsp_add_key() -> dict[str, Any]:
        ...

    @staticmethod
    def ezsp_backup(*, command_data: str | None=None, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None, expect_reply: bool | None=None) -> dict[str, Any]:
        """Backup coordinator data (bellows/ezsp)

        Args:
            command_data: Suffix for backup file Example: _bathroom_added
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations
            expect_reply: Wait for/expect a reply (not used yet)"""
        ...

    @staticmethod
    def ezsp_clear_keys() -> dict[str, Any]:
        ...

    @staticmethod
    def ezsp_get_config_value() -> dict[str, Any]:
        ...

    @staticmethod
    def ezsp_get_ieee_by_nwk() -> dict[str, Any]:
        ...

    @staticmethod
    def ezsp_get_keys() -> dict[str, Any]:
        ...

    @staticmethod
    def ezsp_get_policy() -> dict[str, Any]:
        ...

    @staticmethod
    def ezsp_get_token() -> dict[str, Any]:
        ...

    @staticmethod
    def ezsp_get_value() -> dict[str, Any]:
        ...

    @staticmethod
    def ezsp_set_channel() -> dict[str, Any]:
        ...

    @staticmethod
    def ezsp_start_mfg() -> dict[str, Any]:
        ...

    @staticmethod
    def get_groups(*, ieee: str, endpoint: float | None=None, tries: float | None=None, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None) -> dict[str, Any]:
        """Get groups set on the endpoints of the device

        Args:
            ieee: Entity name, device name, or IEEE address of the node Example: 00:0d:6f:00:05:7d:2d:34
            endpoint: endpoint to get information for (all endpoints when not set)
            tries: Number of times the zigbee packet should be attempted
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations"""
        ...

    @staticmethod
    def get_routes_and_neighbours(*, ieee: str, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None, expect_reply: bool | None=None) -> dict[str, Any]:
        """Scan for all routes and neighbours, results saved to config/scans/...

        Args:
            ieee: Entity name, device name, or IEEE address of the node Example: 00:0d:6f:00:05:7d:2d:34
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations
            expect_reply: Wait for/expect a reply (not used yet)"""
        ...

    @staticmethod
    def get_zll_groups(*, ieee: str, tries: float | None=None, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None) -> dict[str, Any]:
        """Get groups for zll_cluster (if present)

        Args:
            ieee: Entity name, device name, or IEEE address of the node Example: 00:0d:6f:00:05:7d:2d:34
            tries: Number of times the zigbee packet should be attempted
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations"""
        ...

    @staticmethod
    def ha_set_state(*, attr_val: str, state_id: str, tries: float | None=None, state_attr: str | None=None, state_value_template: str | None=None, allow_create: bool | None=None, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None, csvout: str | None=None, csvlabel: str | None=None) -> dict[str, Any]:
        """Set/update a Home Assistant state

        Args:
            attr_val: value to write to the state (or use in the template)
            state_id: Name of state to write the read attribute value to Example: sensor.example
            tries: Number of times the zigbee packet should be attempted
            state_attr: When defined, attribute in state_id to write the read attribute value to.  Write to state value when missing (and state_id is defined) Example: other_attr
            state_value_template: When defined, used as a template expression. For example "value + 10" will be internally interpreted as "{{ value + 10 }}" where 'value' is substituted with the value for 'attr_val' Example: value + 10
            allow_create: Allow state creation (given by state_id) if it does not exist
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations
            csvout: Filename of CSV to write the update state information to.  Written to 'csv' directory. Example: ../web/mystatecsv.csv
            csvlabel: Label to designate value written (in CSV file) Example: Updated from zha_toolkit.ha_set_state"""
        ...

    @staticmethod
    def zha_devices(*, ieee: str | None=None, command_data: str | None=None, csvout: str | None=None, csvlabel: Literal['', 'ieee', 'nwk', 'manufacturer', 'model', 'name', 'quirk_applied', 'quirk_class', 'manufacturer_code', 'power_source', 'lqi', 'rssi', 'last_seen', 'available', 'device_type', 'user_given_name', 'device_reg_id', 'area_id'] | None=None, json_out: str | None=None, json_timestamp: bool | None=None, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None) -> dict[str, Any]:
        """Export device information (Response, CSV File, JSON File, Event)

        Args:
            ieee: Optional Entity name, device name, or IEEE address of the device to provide details for.  Defaults to all devices Example: 00:0d:6f:00:05:7d:2d:34
            command_data: Selected Fields Example: ['ieee', 'lqi', 'name']
            csvout: Filename of CSV to write read data to.  Written to 'csv' directory (can be relative as in example). Example: ../web/mycsv.csv
            csvlabel: Column to sort table by Example: lqi
            json_out: Filename of JSON to write read data to.  Written to '/config/json' directory Example: zha_devices.json
            json_timestamp: Add timestamp to Filename of JSON file. Defaults to False. Example: True
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations"""
        ...

    @staticmethod
    def handle_join(*, ieee: str, command_data: float | None=None) -> dict[str, Any]:
        """Handle join (ZHA should re-interrogate the device as on new join)

        Args:
            ieee: Entity name, device name, or IEEE address of the node to execute command Example: 00:0d:6f:00:05:7d:2d:34
            command_data: Short network address of the device (optional, if known in ZHA)"""
        ...

    @staticmethod
    def ieee_ping(*, ieee: str, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None, expect_reply: bool | None=None) -> dict[str, Any]:
        """Ping device

        Args:
            ieee: Ping: Requests IEEE address (using the known NWK Address) Example: 00:0d:6f:00:05:7d:2d:34
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations
            expect_reply: Wait for/expect a reply (not used yet)"""
        ...

    @staticmethod
    def leave(*, ieee: str, tries: float | None=None, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None, expect_reply: bool | None=None) -> dict[str, Any]:
        """Send a Leave request to the device

        Args:
            ieee: Entity name, device name, or IEEE address of the node to leave the network Example: 00:0d:6f:00:05:7d:2d:34
            tries: Number of times the zigbee packet should be attempted
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations
            expect_reply: Wait for/expect a reply (not used yet)"""
        ...

    @staticmethod
    def misc_reinitialize(*, ieee: str) -> dict[str, Any]:
        """Reinitialize device

        Args:
            ieee: Entity name, device name, or IEEE address of the node to execute command" Example: 00:0d:6f:00:05:7d:2d:34"""
        ...

    @staticmethod
    def misc_settime(*, ieee: str, endpoint: float | None=None, tries: float | None=None, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None, read_before_write: bool | None=None, read_after_write: bool | None=None, csvout: str | None=None) -> dict[str, Any]:
        """Set Time Cluster attributes (Time, DST - except TimeStatus)

        Args:
            ieee: Entity name, device name, or IEEE address Example: 00:0d:6f:00:05:7d:2d:34
            endpoint: target endpoint
            tries: Number of times the zigbee packet should be attempted
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations
            read_before_write: Read attributes before writing them
            read_after_write: Read attribute after writing.  Can be used to ensure the values match.  Defaults to True
            csvout: Filename of CSV to write read data to.  Written to 'csv' directory Example: ../web/mycsv.csv"""
        ...

    @staticmethod
    def ota_notify(*, ieee: str, download: bool | None=None, path: str | None=None, tries: float | None=None, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None, expect_reply: bool | None=None) -> dict[str, Any]:
        """Notify a device that an update is available, after triggering ota image providers to fetch new images.

        Args:
            ieee: Entity name, device name, or IEEE address of the node to execute command Example: entity.name_of_zigbee_device
            download: When True, download FW from KKoenk's list that possibly matches devices.
            path: Path to write ota image(s) to (defaults to zha:zigpy_config:ota:otau_directory value or /config/zigpy_ota)
            tries: Number of times the zigbee packet should be attempted
            event_success: Event name in case of success Example: ota_notify_success
            event_fail: Event name in case of failure Example: ota_notify_fail
            event_done: Event name when the images were updated and the device notified (either success or failure). Example: ota_notify_done
            fail_exception: Throw exception when success==False, useful to stop scripts, automations
            expect_reply: Wait for/expect a reply (not used yet)"""
        ...

    @staticmethod
    def rejoin(*, ieee: str, command_data: str | None=None, tries: float | None=None, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None, expect_reply: bool | None=None) -> dict[str, Any]:
        """Send a rejoin request to the device (=leave with rejoin)

        Args:
            ieee: Entity name, device name, or IEEE address of the node to request rejoin Example: 00:0d:6f:00:05:7d:2d:34
            command_data: Node used to accept the rejoin (Entity name, device name, or IEEE address of the node) Example: 00:0d:6f:00:05:7d:2d:34
            tries: Number of times the zigbee packet should be attempted
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations
            expect_reply: Wait for/expect a reply (not used yet)"""
        ...

    @staticmethod
    def register_services() -> dict[str, Any]:
        """Reregister zha-toolkit services Useful during development when they are updated in __init__.py"""
        ...

    @staticmethod
    def remove_all_groups(*, ieee: str, endpoint: float | None=None, tries: float | None=None, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None) -> dict[str, Any]:
        """Remove all groups from (selected) endpoints on device

        Args:
            ieee: Entity name, device name, or IEEE address of the node Example: 00:0d:6f:00:05:7d:2d:34
            endpoint: endpoint to remove group from (all endpoints when not set)
            tries: Number of times the zigbee packet should be attempted
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations"""
        ...

    @staticmethod
    def remove_from_group(*, ieee: str, command_data: float, endpoint: float | None=None, tries: float | None=None, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None) -> dict[str, Any]:
        """Remove device endpoints from group

        Args:
            ieee: Entity name, device name, or IEEE address of the node Example: 00:0d:6f:00:05:7d:2d:34
            command_data: Group id to remove Example: 2
            endpoint: endpoint to remove group from (or all EP if not set)
            tries: Number of times the zigbee packet should be attempted
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations"""
        ...

    @staticmethod
    def remove_group(*, ieee: str, command_data: float, endpoint: float | None=None, tries: float | None=None, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None) -> dict[str, Any]:
        """Remove group from endpoint groups list of device.  May be equivalent to `remove_from_group`

        Args:
            ieee: Entity name, device name, or IEEE address of the node Example: 00:0d:6f:00:05:7d:2d:34
            command_data: Group id to remove Example: 2
            endpoint: endpoint to remove group from (or all EP if not set)
            tries: Number of times the zigbee packet should be attempted
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations"""
        ...

    @staticmethod
    def scan_device(*, ieee: str, endpoint: float | None=None, tries: float | None=None, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None, expect_reply: bool | None=None) -> dict[str, Any]:
        """Scan device (result written to file in /config/scans)

        Args:
            ieee: Entity name, device name, or IEEE address of the node to execute command Example: 00:0d:6f:00:05:7d:2d:34
            endpoint: Target endpoint, or list of endpoints Example: 1
            tries: Number of times a zigbee packet is repeated when no response
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations
            expect_reply: Wait for/expect a reply (not used yet)"""
        ...

    @staticmethod
    def tuya_magic(*, ieee: str, tries: float | None=None, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None, expect_reply: bool | None=None) -> dict[str, Any]:
        """Do Tuya magic spell (= make most Tuya devices work normally)

        Args:
            ieee: Entity name, device name, or IEEE address of the node to execute command Example: 00:0d:6f:00:05:7d:2d:34
            tries: Number of times the zigbee packet should be attempted
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations
            expect_reply: Wait for/expect a reply (not used yet)"""
        ...

    @staticmethod
    def unbind_coordinator(*, ieee: str, endpoint: float | None=None, cluster: float | None=None, tries: float | None=None, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None, expect_reply: bool | None=None) -> dict[str, Any]:
        """Remove (Unbind) all bindings from device to the coordinator (your HA Instance)

        Args:
            ieee: Entity name, device name, or IEEE address of the node to execute command Example: 00:0d:6f:00:05:7d:2d:34
            endpoint: When provided, remove only bindings for this endpoint or list of endpoints (single value or list. Example: 20 or [20, 30]) Otherwise: removes bindings for all endpoints
            cluster: When provided, remove only bindings for this cluster or list of clusters (single value or list. Example: 0x0200 or [0x200, 0x300]) Otherwise: removes bindings for all clusters
            tries: Number of times the zigbee packet should be attempted
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations
            expect_reply: Wait for/expect a reply (not used yet)"""
        ...

    @staticmethod
    def unbind_group() -> dict[str, Any]:
        ...

    @staticmethod
    def zcl_cmd(*, ieee: str, cluster: float, cmd: float, manf: float | None=None, endpoint: float | None=None, args: str | None=None, kwargs: str | None=None, tries: float | None=None, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None, expect_reply: bool | None=None) -> dict[str, Any]:
        """Send cluster command

        Args:
            ieee: Entity name, device name, or IEEE address of the node to send\\ command to Example: 00:0d:6f:00:05:7d:2d:34
            cluster: target cluster
            cmd: Command Id to execute
            manf: Manufacturer id (0 = No manufacturer id, empty=possibly automatic)
            endpoint: target endpoint
            args: Arguments for command when needed (as per zigpy's definition corresponding to Zigbee Library Cluster (ZCL) specification) Example: [1, 'abcd', 3]
            kwargs: Keyword arguments for command Example: {'code': 'cool_code'}
            tries: Number of times the zigbee packet should be attempted
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations
            expect_reply: Wait for/expect a reply (not used yet)"""
        ...

    @staticmethod
    def zdo_flood_parent_annce() -> dict[str, Any]:
        ...

    @staticmethod
    def zdo_join_with_code(*, ieee: str, code: str, command_data: str | None=None, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None, expect_reply: bool | None=None) -> dict[str, Any]:
        """Allow a device to join with a code (bellows radio type only)

        Args:
            ieee: Entity name, device name, or IEEE address of the node to request rejoin Example: 00:0d:6f:00:05:7d:2d:34
            code: The code the device needs to present Example: 01234567
            command_data: Node used to accept the rejoin (Entity name, device name, or IEEE address of the node) Example: 00:0d:6f:00:05:7d:2d:34
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations
            expect_reply: Wait for/expect a reply (not used yet)"""
        ...

    @staticmethod
    def zdo_scan_now() -> dict[str, Any]:
        ...

    @staticmethod
    def zdo_update_nwk_id() -> dict[str, Any]:
        ...

    @staticmethod
    def znp_backup(*, command_data: str | None=None, event_success: str | None=None, event_fail: str | None=None, event_done: str | None=None, fail_exception: bool | None=None, expect_reply: bool | None=None) -> dict[str, Any]:
        """Backup coordinator data (znp, bellows/ezsp)

        Args:
            command_data: Suffix for backup file Example: _bathroom_added
            event_success: Event name in case of success Example: my_read_success_trigger_event
            event_fail: Event name in case of failure Example: my_read_fail_trigger_event
            event_done: Event name when the service call did all its work (either success or failure).  Has event data with relevant attributes. Example: my_read_done_trigger_event
            fail_exception: Throw exception when success==False, useful to stop scripts, automations
            expect_reply: Wait for/expect a reply (not used yet)"""
        ...

    @staticmethod
    def znp_nvram_backup() -> dict[str, Any]:
        ...

    @staticmethod
    def znp_nvram_reset() -> dict[str, Any]:
        ...

    @staticmethod
    def znp_nvram_restore() -> dict[str, Any]:
        ...

    @staticmethod
    def znp_restore() -> dict[str, Any]:
        ...

class _zone_state(StateVal):
    editable: bool
    latitude: float
    longitude: float
    passive: bool
    persons: list
    radius: float

class zone:
    costco_wholesale: _zone_state
    wallmart_south: _zone_state
    the_home_depot_south: _zone_state
    superstore: _zone_state
    wallmart_north: _zone_state
    dad_s_shop: _zone_state
    mcdonald_s_whoop_up_west: _zone_state
    no_frills_vets: _zone_state
    bryans: _zone_state
    justices_house: _zone_state

    @staticmethod
    def reload():
        ...

    @staticmethod
    def update(*, entity_id: str, name: str | None=None, icon: str | None=None, latitude: float | None=None, longitude: float | None=None, radius: float=100):
        """Update properties of a zone on the fly.

        Args:
            entity_id: The ID of the entity (or entities) to update.
            name: Name of the zone
            icon: Icon to use for the zone
            latitude: Latitude of the zone
            longitude: Longitude of the zone
            radius: Radius of the zone"""
        ...

    @staticmethod
    def delete(*, entity_id: str):
        """Delete a zone. This works only with zones created and managed via the UI. Zones created and managed in YAML cannot be managed by Spook.

        Args:
            entity_id: The ID of the entity (or entities) to remove."""
        ...

    @staticmethod
    def create(*, name: str, latitude: float, longitude: float, icon: str | None=None, radius: float=100):
        """Create a new zone in Home Assistant on the fly.

        Args:
            name: Name of the zone
            latitude: Latitude of the zone
            longitude: Longitude of the zone
            icon: Icon to use for the zone
            radius: Radius of the zone"""
        ...