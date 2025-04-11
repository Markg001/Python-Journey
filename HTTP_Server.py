import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.bind(('localhost', 8080))
mysocket.listen(5)

while True:  # changed `with True:` to `while True:`
    print('Waiting for connections...')
    recvSocket, address = mysocket.accept()
    print(f'Connection from: {address}')
    request = recvSocket.recv(1024).decode()
    print('HTTP request received:')
    print(request)

    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html\r\n\r\n"
        "<html><body><h1>Hello World!</h1></body></html>\r\n"
    )
    recvSocket.send(response.encode('utf-8'))
    recvSocket.close()


print("=============================================================================")
print("==                        Testing the HTTP server                          ==")
print("=============================================================================")
