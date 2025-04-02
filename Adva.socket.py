import socket
import sys
from datetime import datetime
import errno
from urllib.parse import urlparse  # Import to handle URLs

# Ask the user for a remote host (domain or URL)
remoteServer = input("Enter a remote host to scan: ")

# Remove the 'https://' or 'http://' part if present
parsed_url = urlparse(remoteServer)
remoteServer = parsed_url.hostname  # This extracts the domain name

# Resolve the hostname to an IP address
try:
    remoteServerIP = socket.gethostbyname(remoteServer)
    print("Please enter the range of ports you would like to scan on the machine")
    
    # Get start and end ports from the user
    startPort = int(input("Enter start port: "))  # Convert input to integer
    endPort = int(input("Enter end port: "))      # Convert input to integer
    
    print("Please wait, scanning remote host", remoteServerIP)
    
    # Record the start time for the scan
    time_init = datetime.now()
    
except socket.gaierror:
    print(f"Unable to resolve host: {remoteServer}")
    sys.exit()
except ValueError:
    print("Invalid port number. Please enter integer values for ports.")
    sys.exit()

# Scan the ports
open_ports = []  # List to store open ports

for port in range(startPort, endPort + 1):
    try:
        # Create a socket object for TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Set a timeout for 1 second
            result = sock.connect_ex((remoteServerIP, port))  # Try to connect to the server and port
            
            # If result is 0, the port is open
            if result == 0:
                print(f"Port {port} is open.")
                open_ports.append(port)
            else:
                print(f"Port {port} is closed.")
                
    except socket.error as e:
        print(f"Error connecting to port {port}: {e}")

# Calculate and print the duration of the scan
time_end = datetime.now()
scan_duration = time_end - time_init
print(f"Scanning completed in {scan_duration}")

# Summary of open ports
if open_ports:
    print(f"\nOpen ports on {remoteServerIP}: {open_ports}")
else:
    print("No open ports found.")
