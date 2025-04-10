# The Main Difference between the TCP and UDP is 
# 1.    UDP does not have control over erros in packets that are sent between the client and server
# 2.    UDP you need to specify SOCK_DGRAM instaed of SOCK_STREAM when creating the socket object

import socket  # ✅ Import socket module

# Server connection details
Server_ip = "127.0.0.1"
Server_port = 6789
address = (Server_ip, Server_port)

# Create UDP socket
socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Enter your message > ")
    
    if message.lower() == "quit":
        break
    
    # Send message to server
    socket_client.sendto(bytes(message, encoding='utf8'), address)
    
    # Receive response from server
    response_server, addr = socket_client.recvfrom(4096)
    print("Response from the server => %s" % response_server.decode())

# Close socket
socket_client.close()
