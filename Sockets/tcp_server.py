import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9999

# Create the socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and port
server.bind((SERVER_IP, SERVER_PORT))

# Start listening for incoming connections
server.listen(5)
print("[*] Server Listening on %s:%d" % (SERVER_IP, SERVER_PORT))

# Accept a connection
client, addr = server.accept()
print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))

# Send a welcome message to the client
client.send("I am the server accepting connections on port 999...".encode())

# Handle client requests in a loop
while True:
    request = client.recv(1024).decode()
    print("[*] Received request: %s" % request)
    
    if request != "quit":
        client.send("ACK".encode())
    else:
        break

# Close the client and server sockets
client.close()
server.close()
