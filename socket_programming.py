# Summary of Socket Programming in Python
# Introduction to Socket Programming

#     The socket module allows creating TCP and UDP clients and servers for network applications.
#     Sockets enable communication between processes on the same or different machines.
#     A socket address consists of an IP address and a port number.

# Types of Sockets

#     TCP Sockets (socket.SOCK_STREAM): Connection-oriented and reliable.
#     UDP Sockets (socket.SOCK_DGRAM): Connectionless and faster, but less reliable.

# Categoties of Sockets

#     UNIX Sockets (socket.AF_UNIX): Used for local inter-process communication.
#     IPv4 (socket.AF_INET) 
#     IPv6 (socket.AF_INET6): Used for network communication.
#     Raw Sockets: Allow direct access to network and transport layer protocols.

# Key Socket Functions

#     socket.socket(socket_family, socket_type): Creates a socket.
#     socket.bind(address): Binds a socket to an IP and port.
#     socket.listen(count): Listens for incoming connections.
#     socket.accept(): Accepts a client connection.
#     socket.connect(ip_address): Connects a client to a server.
#     socket.send(data): Sends data through the socket.
#     socket.recv(buflen): Receives data from a socket.
#     socket.close(): Closes the socket and releases resources.

# Server and Client Socket Methods
# Server-Side:

#     bind(address): Assigns an address to a socket.
#     listen(count): Starts listening for incoming connections.
#     accept(): Accepts client connections.

# Client-Side:

#     connect(ip_address): Connects to a server.
#     connect_ext(ip_address): Connects with error handling.

# Additional Information

#     Python’s socket module includes built-in methods for IP resolution, hostname retrieval, and network communication.
#     The module comes pre-installed with Python and can be imported using import socket.
#     Network tools like Scapy can manipulate and analyze network packets.
import socket
ip = '10.16.0.51'
portlist = [21,22,23,80]
for port in portlist:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    results= sock.connect_ex((ip,port))
    print(port,':', results)
    sock.close()

# we are making a connection to a web server that listens on port 80 and we
# access a specific route within this server to request a text document. 

import socket
sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('ftp.debian.org', 80))
cmd = 'GET http://ftp.debian.org/debian/README.mirrors.txt HTTP/1.0\r\n\r\n'.encode()
sock.send(cmd)
while True:
    data = sock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end= "")
sock.close()
'/n-------------------------------------------------------------'
import socket

try:
    hostname = socket.gethostname()
    print("gethostname:", hostname)
    
    ip_address = socket.gethostbyname(hostname)
    print("Local IP address:", ip_address)
    
    print("gethostbyname:", socket.gethostbyname('www.python.org'))
    print("gethostbyname_ex:", socket.gethostbyname_ex('www.python.org'))
    print("gethostbyaddr:", socket.gethostbyaddr('8.8.8.8'))
    print("getfqdn:", socket.getfqdn('www.google.com'))
    
    print("getaddrinfo:", socket.getaddrinfo("www.google.com", None, 0, socket.SOCK_STREAM))

except socket.error as error:
    print(str(error))
    print("Connection error")
