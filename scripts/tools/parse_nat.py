import xml.etree.ElementTree as ET
tree = ET.parse(r'C:\Users\ashto\Docker\opnsense\config-OPNsense.sythsaz.ca-20260912191025.xml')
for rule in tree.getroot().findall('.//nat/rule'):
    descr_node = rule.find('description')
    descr = descr_node.text if descr_node is not None else ''
    
    target_node = rule.find('target')
    target = target_node.text if target_node is not None else ''
    
    local_port_node = rule.find('local-port')
    local_port = local_port_node.text if local_port_node is not None else ''
    
    if target or local_port or descr:
        print(f"NAT Desc: {descr} | Target: {target} | Local Port: {local_port}")
