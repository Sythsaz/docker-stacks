import yaml
import os

compose_path = r'C:\Users\ashto\Docker\stacks\dell-server\mcp\compose.yaml'
if os.path.exists(compose_path):
    with open(compose_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    # Remove emqx-mcp since they use mosquitto on HA
    if 'services' in data and 'emqx-mcp' in data['services']:
        del data['services']['emqx-mcp']
        
    class MyDumper(yaml.Dumper):
        def increase_indent(self, flow=False, indentless=False):
            return super(MyDumper, self).increase_indent(flow, False)

    with open(compose_path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, sort_keys=False, default_flow_style=False, Dumper=MyDumper)
    print("mcp/compose.yaml cleaned up.")
