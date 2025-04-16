# This script is a simple port scanner that uses multi-threading
# to scan multiple ports on a given host. It defines two main functions:
# socketScan and portScanning. The socketScan function attempts to establish
# a TCP connection to a specific port on the host and reports whether the port
# is open or closed. The portScanning function resolves the host's IP address,'
# ' optionally retrieves the host's name, and then creates a separate thread for
# each port to perform the scan concurrently. The main function uses the optparse
# module to parse command-line arguments for the host and port(s) to scan. If the user
#  doesn't provide valid inputs, it exits; otherwise, it calls the portScanning function'
# #  to start scanning the provided ports.
import optparse
from socket import *
from threading import *

# Function to scan a single port on a host
def socketScan(host, port):
    try:
        # Create a socket object
        socket_connect = socket(AF_INET, SOCK_STREAM)
        socket_connect.settimeout(5)
        result = socket_connect.connect((host, port))  # Attempt to connect to the port
        print('[+] %d/tcp open' % port)
    except Exception as exception:
        print('[-] %d/tcp closed' % port)
        print('[-] Reason:%s' % str(exception))
    finally:
        socket_connect.close()

# Function to scan multiple ports on a host
def portScanning(host, ports):
    try:
        # Resolve host to IP address
        ip = gethostbyname(host)
    except:
        print("[-] Cannot resolve '%s': Unknown host" % host)
        return
    
    try:
        # Get the host name (optional)
        name = gethostbyaddr(ip)
        print('[+] Scan Results for: ' + ip + " " + name[0])
    except:
        print('[+] Scan Results for: ' + ip)
    
    # Scan each port by creating a new thread
    for port in ports:
        t = Thread(target=socketScan, args=(ip, port))
        t.start()

# Main function to handle user input and initiate port scanning
def main():
    # Setting up command-line argument parsing
    parser = optparse.OptionParser('socket_portScan ' + '-H <Host> -P <Port>')
    parser.add_option('-H', dest='host', type='string', help='specify host')
    parser.add_option('-P', dest='port', type='string', help='specify port[s] separated by comma')
    (options, args) = parser.parse_args()

    # Extract host and ports from the command-line arguments
    host = options.host
    if options.port:
        try:
            ports = [int(port) for port in str(options.port).split(',')]  # Convert string ports to integers
        except ValueError:
            print("[-] Invalid port number. Please enter integer values for ports.")
            exit(0)
    else:
        print("[-] Please specify at least one port.")
        print(parser.usage)
        exit(0)

    # Validate input and call the port scanning function
    if host == None or not ports:
        print(parser.usage)
        exit(0)
    
    portScanning(host, ports)

# Run the main function if this script is executed directly
if __name__ == '__main__':
    main()
