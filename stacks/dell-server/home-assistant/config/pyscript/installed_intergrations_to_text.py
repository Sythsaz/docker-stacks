# /config/pyscript/installed_intergrations_to_text.py

# Define a native (blocking) helper that runs in a worker thread
@pyscript_executor
def write_file_native(path, data):
    try:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(data)
        return True, None
    except Exception as exc:
        return False, exc

# Main pyscript logic (runs in pyscript sandbox)
entries = hass.config_entries.async_entries()

lines = []
for e in entries:
    title = e.title or e.data.get("name", "—")
    lines.append(f"{e.domain} - {title} ({e.entry_id})")

text = "\n".join(lines)

success, exception = write_file_native("/config/integrations_list_from_pyscript.txt", text)
if exception:
    # re-raise so it shows in the logs, or handle however you prefer
    raise exception