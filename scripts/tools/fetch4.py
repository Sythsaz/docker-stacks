import urllib.request
class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

opener = urllib.request.build_opener(NoRedirect)
try:
    req = urllib.request.Request('http://sythsaz.dpdns.org', headers={'User-Agent': 'Mozilla/5.0'})
    resp = opener.open(req)
    print("No redirect. Status:", resp.getcode())
except urllib.error.HTTPError as e:
    print("Status:", e.code)
    print("Headers:\n", e.headers)
