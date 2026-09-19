import xml.etree.ElementTree as ET
tree = ET.parse(r'C:\Users\ashto\Docker\opnsense\config-OPNsense.sythsaz.ca-20260912191025.xml')
unbound = tree.getroot().find('.//OPNsense/unboundplus/dnsbl')
if unbound is not None:
    enabled = unbound.find('enabled')
    print("Unbound DNSBL enabled:", enabled.text if enabled is not None else "False")
