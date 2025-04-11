print("=============================================================================")
print("==                        Testing the HTTP server                          ==")
print("=============================================================================")

import socket

# Target server details
webhost = "localhost"
webport = 8080

# Inform the user
print("Contacting %s on port %d..." % (webhost, webport))

# Create the socket and connect to the server
webclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
webclient.connect((webhost, webport))

# Send a basic HTTP GET request
http_request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
webclient.send(http_request.encode('utf-8'))

# Receive and print the response
reply = webclient.recv(4096)
print("Response from %s:" % webhost)
print(reply.decode())

# Optional: close the socket
webclient.close()
