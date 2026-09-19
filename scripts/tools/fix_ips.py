import yaml

compose_path = r'C:\Users\ashto\Docker\stacks\dell-server\media\compose.yaml'
with open(compose_path, 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

# The new mapping we want:
# plex: 10.0.20.27, mac: 02:42:0a:00:14:1b
# music_assistant: 10.0.20.28, mac: 02:42:0a:00:14:1c
# aircast: 10.0.20.29, mac: 02:42:0a:00:14:1d
# mediamtx: 10.0.20.30, mac: 02:42:0a:00:14:1e
# mumble-server: 10.0.20.31, mac: 02:42:0a:00:14:1f

mapping = {
    'plex': {'ip': '10.0.20.27', 'mac': '02:42:0a:00:14:1b'},
    'music_assistant': {'ip': '10.0.20.28', 'mac': '02:42:0a:00:14:1c'},
    'aircast': {'ip': '10.0.20.29', 'mac': '02:42:0a:00:14:1d'},
    'mediamtx': {'ip': '10.0.20.30', 'mac': '02:42:0a:00:14:1e'},
    'mumble-server': {'ip': '10.0.20.31', 'mac': '02:42:0a:00:14:1f'}
}

services = data.get('services', {})
for svc, m in mapping.items():
    if svc in services:
        services[svc]['mac_address'] = m['mac']
        services[svc]['networks']['vlan20_servers']['ipv4_address'] = m['ip']

class MyDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(MyDumper, self).increase_indent(flow, False)

with open(compose_path, 'w', encoding='utf-8') as f:
    yaml.dump(data, f, sort_keys=False, default_flow_style=False, Dumper=MyDumper)
