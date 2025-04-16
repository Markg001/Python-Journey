#This code sets up a simple HTTPS server in Python. 
# It uses HTTPServer and BaseHTTPRequestHandler to respond with "Hello, world!" 
# to any GET request. To secure the server with SSL/TLS, it wraps the server's 
# socket using the ssl module, loading a self-signed certificate (cert.pem) and 
# private key (key.pem) generated with OpenSSL. This allows the server to accept 
# HTTPS connections on port 4443. When accessed through a browser or 
# client via https://localhost:4443, it returns the simple response securely.

from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

if __name__ == '__main__':
    server_address = ('localhost', 4443)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

    # Create SSL context and load certificate and private key
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')

    # Wrap the server socket with SSL
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

    print("Serving on https://localhost:4443")
    httpd.serve_forever()


print("=============QUESTIONS==============")

# As we conclude, here is a list of questions for you to test your knowledge regarding this chapter’s
# material. You will find the answers in the Assessments section of the Appendix:
# 1. Which method of the socket module allows a server socket to accept requests from a client
# socket from another host?
# 2. Which methods of the socket module allow you to send and receive data from an IP ad-
# dress?
# 3. Which method of the socket module allows you to implement port scanning with sockets
# and to check the port state?
# 4. What is the difference between the TCP and UDP protocols, and how do you implement
# them in Python with the socket module?
# 5. What is the Python module and the main classes we can use to create an HTTP server?
###########                             ANSWER          ###############
# socket.accept()

# socket.send() , socket.recv() .sendto() , .recvfrom()

# socket.connectex()

#TCP = socket.SOCK_STREAM and it is slow due to security reasons
#UDP = socket.SOCK_DGRAM it is first compared to TCP 
#implementing them on we use socket.socket(socket.AF_INET, for_tcp you use the above for udp we use)

# to create HTTP we use the module The Python module is http.server, and the main classes are HTTPServer 
# for setting up the server and BaseHTTPRequestHandler (or SimpleHTTPRequestHandler) to define how HTTP requests are handled.