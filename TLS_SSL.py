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
