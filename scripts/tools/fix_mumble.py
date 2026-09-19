import yaml

compose_path = r'C:\Users\ashto\Docker\stacks\dell-server\media\compose.yaml'
with open(compose_path, 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

# Fix mumble-server
mumble = data['services']['mumble-server']
# Remove read_only: true just in case
if 'read_only' in mumble:
    del mumble['read_only']

# Change the config mount from :ro to :rw
new_vols = []
for vol in mumble['volumes']:
    if isinstance(vol, dict) and 'source' in vol and 'mumble.ini' in vol['source']:
        vol['read_only'] = False
    elif isinstance(vol, str) and 'mumble.ini' in vol:
        vol = vol.replace(':ro', '')
    new_vols.append(vol)
mumble['volumes'] = new_vols

class MyDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(MyDumper, self).increase_indent(flow, False)

with open(compose_path, 'w', encoding='utf-8') as f:
    yaml.dump(data, f, sort_keys=False, default_flow_style=False, Dumper=MyDumper)
