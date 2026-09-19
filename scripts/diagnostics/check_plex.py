import xml.etree.ElementTree as ET
try:
    tree = ET.parse(r'C:\Users\ashto\Docker\opnsense\config-OPNsense.sythsaz.ca-20260912191025.xml')
    for rule in tree.getroot().findall('.//nat/rule'):
        target_node = rule.find('target')
        local_port_node = rule.find('local-port')
        if local_port_node is not None and local_port_node.text == '32400':
             print(f"Plex Target: {target_node.text if target_node is not None else 'None'}")
except Exception as e:
    print(e)
