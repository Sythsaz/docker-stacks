#!/bin/bash
# Read the password from the injected secrets.yaml file
python3 -c "import yaml; print(yaml.safe_load(open('/config/secrets.yaml'))['hassio_sudo_password'])"
