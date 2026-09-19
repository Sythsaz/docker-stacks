import xml.etree.ElementTree as ET
try:
    tree = ET.parse(r'C:\Users\ashto\Docker\opnsense\config-OPNsense.sythsaz.ca-20260912191025.xml')
    unbound = tree.getroot().find('.//unbound')
    if unbound is not None:
        custom_opts = unbound.find('custom_options')
        print("Unbound Custom Opts:", custom_opts.text if custom_opts is not None else "None")
        
        forwarding = unbound.find('forwarding')
        print("Unbound Forwarding:", forwarding.text if forwarding is not None else "None")

    dots = tree.getroot().findall('.//OPNsense/unboundplus/dots/dot')
    if dots:
        print("DNS over TLS Upstreams configured:", len(dots))
        for dot in dots:
            print("-", dot.find('server').text)
    else:
        print("No DoT upstream servers configured.")
except Exception as e:
    print(e)
