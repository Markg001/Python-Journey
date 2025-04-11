import os
import socket
import struct

def send_file(sock: socket.socket, filename):
    filesize = os.path.getsize(filename)
    # Send the filesize as an 8-byte little-endian unsigned long long
    sock.sendall(struct.pack("<Q", filesize))
    
    with open(filename, "rb") as f:
        while (read_bytes := f.read(1024)):
            sock.sendall(read_bytes)

# Connect to the file receiver server
with socket.create_connection(("localhost", 9999)) as connection:
    print("Connecting with the server...")
    print("Sending file...")
    send_file(connection, "send_file.py")
    print("File sent successfully.")
