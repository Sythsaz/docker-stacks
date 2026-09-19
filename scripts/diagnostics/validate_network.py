import os
import yaml

stacks_dir = r'C:\Users\ashto\Docker\stacks\dell-server'
used_ips = {}
used_macs = {}
errors = False

for stack in os.listdir(stacks_dir):
    compose_path = os.path.join(stacks_dir, stack, 'compose.yaml')
    if os.path.exists(compose_path):
        with open(compose_path, 'r', encoding='utf-8') as f:
            try:
                data = yaml.safe_load(f)
                services = data.get('services', {})
                for svc_name, svc_data in services.items():
                    # Check IPs
                    networks = svc_data.get('networks', {})
                    if isinstance(networks, dict):
                        for net_name, net_data in networks.items():
                            if isinstance(net_data, dict) and 'ipv4_address' in net_data:
                                ip = net_data['ipv4_address']
                                identifier = f"{stack}/{svc_name}"
                                if ip in used_ips:
                                    print(f"COLLISION IP: {ip} used by {used_ips[ip]} AND {identifier}")
                                    errors = True
                                else:
                                    used_ips[ip] = identifier
                    
                    # Check MACs
                    mac = svc_data.get('mac_address')
                    if mac:
                        if mac in used_macs:
                            print(f"COLLISION MAC: {mac} used by {used_macs[mac]} AND {identifier}")
                            errors = True
                        else:
                            used_macs[mac] = identifier
            except Exception as e:
                print(f"Error parsing {compose_path}: {e}")
                errors = True

if not errors:
    print("All IPs and MACs are unique!")
