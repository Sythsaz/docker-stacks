import urllib.request
try:
    req = urllib.request.Request('https://sythsaz.dpdns.org', headers={'User-Agent': 'Mozilla/5.0'})
    resp = urllib.request.urlopen(req)
    print("URL after redirects:", resp.geturl())
    print("Status:", resp.getcode())
except Exception as e:
    print("Error:", e)
