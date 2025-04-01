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

#  Useful methods for gathering more information
# about an IP address or hostname include the following:
# • socket�gethostbyname(hostname): This method returns a string converting a hostname
#       to the IPv4 address format.
#            Socket Programming84
#       This method is equivalent to the nslookup command we can find in some operating sys-
#          tems.
# • socket�gethostbyname_ex(name): This method returns a tuple that contains an IP ad-
#   dress for a specific domain name. If we see more than one IP address, this means one
#    domain runs on multiple IP addresses:
# • socket�getfqdn([domain]): This is used to find the fully qualified name of a domain.
# • socket�gethostbyaddr(ip_address): This method returns a tuple with three values
#   (hostname, name, ip_address_list). hostname represents the host that corresponds to the
#   given IP address, name is a list of names associated with this IP address, and ip_address_
#   list is a list of IP addresses that are available on the same host.
# • socket�getservbyname(servicename[, protocol_name]): This method allows you to ob-
#   tain the port number from the port name.
# • socket�getservbyport(port[, protocol_name]): This method performs the reverse op-
#   eration to the previous one, allowing you to obtain the port name from the port number.

import socket

def find_services_name():
    for port in [21, 22, 23, 25, 80]:
        print("Port: %s => Service Name: %s" % (port, socket.getservbyport(port, 'tcp')))
    
    # Checking service for port 53 with UDP
    print("Port: %s => Service Name: %s" % (53, socket.getservbyport(53, 'udp')))

if __name__ == '__main__':
    find_services_name()

'/n--------------------------------------------------------------------------------------------'
import socket

host = input("Enter host name: ")
port = int(input("Enter port number: "))

try:
    # Create a socket object for TCP (IPv4)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
        socket_tcp.settimeout(10)  # Set a timeout of 10 seconds
        
        # Try to connect to the server and port
        if socket_tcp.connect_ex((host, port)) == 0:
            print("Established connection to the server %s in the port %s" % (host, port))
            
            # Prepare the HTTP request
            request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % host
            socket_tcp.send(request.encode())  # Send the request to the server
            
            # Receive the data from the server
            data = socket_tcp.recv(4096)  # 4096 bytes
            print("Data:", repr(data))
            print("Length of data:", len(data))
        else:
            print(f"Connection failed to {host} on port {port}")

except socket.timeout as error:
    print("Timeout error:", error)

except socket.gaierror as error:
    print("Connection error to the server:", error)

except socket.error as error:
    print("Connection error:", error)

