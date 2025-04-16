# The Main Difference between the TCP and UDP is 
# 1.    UDP does not have control over erros in packets that are sent between the client and server
# 2.    UDP you need to specify SOCK_DGRAM instaed of SOCK_STREAM when creating the socket object

import socket
import sys

# Server configuration
Server_ip = '127.0.0.1'      # Localhost (server only accepts local connections)
server_port = 6789           # Port number to listen on

# Create a UDP socket
socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the IP and port
socket_server.bind((Server_ip, server_port))
print("[*] Server UDP Listening on %s:%d" % (Server_ip, server_port))

try:
    while True:
        # Receive data from client (4096 bytes max)
        data, address = socket_server.recvfrom(4096)

        # Send acknowledgment to the client
        socket_server.sendto("I am the server accepting connections...".encode(), address)

        # Remove whitespace and newlines
        data = data.strip()

        # Print the message and sender info
        print("Message '%s' received from %s" % (data.decode(), address))

        try:
            # Send back the server's platform info
            response = "Hi from %s" % sys.platform
        except Exception:
            # In case of error, send back the error type
            response = str(sys.exc_info()[0])

        print("Response:", response)

        # Send the response to the client
        socket_server.sendto(response.encode('utf8'), address)

        # OPTIONAL: Stop the server if client sends "exit"
        if data.decode().strip().lower() == "exit":
            print("Shutting down server...")
            break

finally:
    # Close the socket properly
    socket_server.close()
    print("Server closed.")
