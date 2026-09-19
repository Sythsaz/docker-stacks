import xml.etree.ElementTree as ET
tree = ET.parse(r'C:\Users\ashto\Docker\opnsense\config-OPNsense.sythsaz.ca-20260912191025.xml')
for rule in tree.getroot().findall('.//Firewall/Filter/rules/rule'):
    interface = rule.find('interface').text or ''
    if interface == 'opt3':
        ET.dump(rule)
        break
