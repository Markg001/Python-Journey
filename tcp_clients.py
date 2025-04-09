import socket

host = "127.0.0.1"
port = 9999

try:
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect((host, port))
    print('Connected to host ' + str(host) + ' on port: ' + str(port))

    # Receive the welcome message
    message = mysocket.recv(1024)
    print("Message received from the server:", message.decode())

    # Start communication
    while True:
        message = input("Enter your message > ")
        mysocket.sendall(message.encode('utf-8'))
        
        if message == "quit":
            break

        # Receive acknowledgment from the server
        response = mysocket.recv(1024)
        print("Server says:", response.decode())

except socket.error as error:
    print("Socket error:", error)

finally:
    mysocket.close()
