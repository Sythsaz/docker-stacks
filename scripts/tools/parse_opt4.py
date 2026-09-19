import xml.etree.ElementTree as ET
tree = ET.parse(r'C:\Users\ashto\Docker\opnsense\config-OPNsense.sythsaz.ca-20260912191025.xml')
for rule in tree.getroot().findall('.//Firewall/Filter/rules/rule'):
    interface = rule.find('interface').text or ''
    if interface == 'opt4':
        descr = rule.find('description').text or ''
        dst = rule.find('destination_net').text or ''
        dst_node = rule.find('destination/network')
        if dst_node is not None:
             dst = dst_node.text
        if not dst:
             dst_port = rule.find('destination/port')
             if dst_port is not None:
                 dst += " Port: " + dst_port.text
        
        src = rule.find('source_net').text or ''
        action = rule.find('action').text or ''
        invert = ''
        if rule.find('destination_not') is not None and rule.find('destination_not').text == '1':
            invert = 'NOT '
        print(f"Action: {action} | Desc: {descr} | Src: {src} | Dst: {invert}{dst}")
