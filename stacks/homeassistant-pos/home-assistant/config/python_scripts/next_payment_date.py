now = hass.states.get("sensor.date").state  # Assumes you have `sensor.date` in "YYYY-MM-DD" format

payment_sensors = [
    "sensor.eighth_payment_date",
    "sensor.eleventh_payment_date",
    # Add the rest of your sensors here
]

next_payment_sensor = None
next_payment_date = None

for sensor in payment_sensors:
    sensor_state = hass.states.get(sensor)
    if sensor_state and sensor_state.state not in ["unknown", "unavailable"]:
        payment_date = sensor_state.state  # Should be in "YYYY-MM-DD" format

        # Compare dates as strings directly
        if payment_date > now and (next_payment_date is None or payment_date < next_payment_date):
            next_payment_date = payment_date
            next_payment_sensor = sensor

# Create message or set as unknown if no next payment date is found
result_message = (
    f"The next payment date is {next_payment_date}"
    if next_payment_sensor else
    "No upcoming payment date found."
)

# Update input_text with result message
hass.services.call("input_text", "set_value", {
    "entity_id": "input_text.next_payment_message",
    "value": result_message
})
