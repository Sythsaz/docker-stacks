import urllib.request
import re
import sys

try:
    url = 'https://docs.opnsense.org/manual/how-tos/multicast-dns.html'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    text = re.sub('<[^<]+>', ' ', html)
    sentences = text.split('.')
    for s in sentences:
        if 'firewall' in s.lower() or 'rule' in s.lower() or 'allow' in s.lower():
            sys.stdout.buffer.write((s.strip().replace('\n', ' ') + '\n').encode('utf-8', 'ignore'))
except Exception as e:
    print(e)
