import urllib.request
try:
    req = urllib.request.Request('http://sythsaz.dpdns.org', headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    print("HTTP Success:", html[:100])
except Exception as e:
    print("HTTP Error:", e)

try:
    import ssl
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request('https://sythsaz.dpdns.org', headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
    print("HTTPS Success:", html[:100])
except Exception as e:
    print("HTTPS Error:", e)
