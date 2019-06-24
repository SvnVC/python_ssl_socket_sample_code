import ssl
import socket
import time


now = time.time()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('api.binance.com', 443))
s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)


#interesting, the get request has to keep the HTTP, NOT HTTPS! the https is made by the ssl wrapping
s.send("GET /api/v1/time HTTP/1.1\r\nHost: api.binance.com\r\nConnection: close\r\n\r\n")

response = s.recv(4096)
print response
s.close()
print "script took %s seconds "%(time.time() - now)

#get content json from response: https://stackoverflow.com/questions/7337523/how-to-read-json-from-socket-in-python-incremental-parsing-of-json


