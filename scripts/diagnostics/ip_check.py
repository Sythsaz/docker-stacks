import os
import yaml

stacks_dir = r'C:\Users\ashto\Docker\stacks\dell-server'
used_ips = {}
for stack in os.listdir(stacks_dir):
    compose_path = os.path.join(stacks_dir, stack, 'compose.yaml')
    if os.path.exists(compose_path):
        with open(compose_path, 'r', encoding='utf-8') as f:
            try:
                data = yaml.safe_load(f)
                services = data.get('services', {})
                for svc_name, svc_data in services.items():
                    networks = svc_data.get('networks', {})
                    if isinstance(networks, dict):
                        for net_name, net_data in networks.items():
                            if isinstance(net_data, dict) and 'ipv4_address' in net_data:
                                ip = net_data['ipv4_address']
                                mac = svc_data.get('mac_address', 'None')
                                used_ips[ip] = f"{stack}/{svc_name} (MAC: {mac})"
            except Exception as e:
                print(f"Error parsing {compose_path}: {e}")

for ip, name in sorted(used_ips.items(), key=lambda x: [int(p) for p in x[0].split('.')]):
    print(f"{ip}: {name}")
