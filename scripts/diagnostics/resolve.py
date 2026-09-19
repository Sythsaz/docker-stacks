import socket
import urllib.request

try:
    print("sythsaz.dpdns.org resolves to: ", socket.gethostbyname('sythsaz.dpdns.org'))
except Exception as e:
    print("sythsaz.dpdns.org DNS error:", e)

try:
    print("sythsaz.ca resolves to: ", socket.gethostbyname('sythsaz.ca'))
except Exception as e:
    print("sythsaz.ca DNS error:", e)
