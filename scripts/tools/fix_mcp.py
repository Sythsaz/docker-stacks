import yaml

compose_path = r'C:\Users\ashto\Docker\stacks\dell-server\mcp\compose.yaml'
with open(compose_path, 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

services = data.get('services', {})
if 'ha-mcp' in services:
    services['ha-mcp']['environment']['HOMEASSISTANT_URL'] = "http://10.0.20.23:8123"

class MyDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(MyDumper, self).increase_indent(flow, False)

with open(compose_path, 'w', encoding='utf-8') as f:
    yaml.dump(data, f, sort_keys=False, default_flow_style=False, Dumper=MyDumper)
