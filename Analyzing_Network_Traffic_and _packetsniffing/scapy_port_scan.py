# The provided script is a custom TCP port scanner built using Python and the scapy library, which allows low-level packet crafting and manipulation. The script mimics what tools like nmap do: scanning a range of ports 
# on a target host to determine whether they are open, closed, or filtered. For each port, 
# it sends a TCP SYN packet (flags="S"). If the response has a SYN-ACK flag (flags=18), 
# the port is open. If it receives a RST-ACK (flags=0x14), the port is closed. If an 
# ICMP unreachable error is returned with specific codes, the port is filtered, 
# indicating a firewall or other security measure is blocking access.

# The script also allows setting the verbosity level to control the amount of debug 
# output during scanning. It uses command-line arguments to take in the target IP, 
# port range, and verbosity level. Below is the complete code:

import sys
from scapy.all import *
import logging

# Disable scapy runtime warnings
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

# Analyze the status of a given port
def analyze_port(host, port, verbose_level):
    print("[+] Scanning port %s" % port)
    packet = IP(dst=host)/TCP(dport=port, flags="S")
    response = sr1(packet, timeout=0.5, verbose=verbose_level)

    if response is not None and response.haslayer(TCP):
        # SYN-ACK (open)
        if response[TCP].flags == 18:
            print("Port "+str(port)+" is open!")
            # Send RST to close the connection politely
            sr(IP(dst=host)/TCP(dport=response.sport, flags="R"), timeout=0.5, verbose=0)
        # RST-ACK (closed)
        elif response.getlayer(TCP).flags == 0x14:
            print("Port:"+str(port)+" Closed")
    elif response is not None and response.haslayer(ICMP):
        # ICMP unreachable (filtered)
        if (int(response.getlayer(ICMP).type) == 3 and 
            int(response.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]):
            print("Port:"+str(port)+" Filtered")

# Main driver logic
if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: %s target startport endport verbose_level" % (sys.argv[0]))
        sys.exit(0)

    target = str(sys.argv[1])
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3]) + 1
    verbose_level = int(sys.argv[4])

    print("Scanning "+target+" for open TCP ports\n")
    for port in range(start_port, end_port):
        analyze_port(target, port, verbose_level)
    print("Scan complete!")

# it demonstrates a basic implementation of Traceroute using Scapy by manipulating the 
# TTL (Time-To-Live) value in IP headers and analyzing the responses. However, a few 
# improvements can make the code more readable and functionally safe:

from scapy.all import *

host = "45.33.32.156"

for i in range(1, 20):
    packet = IP(dst=host, ttl=i) / UDP(dport=33434)
    reply = sr1(packet, verbose=0, timeout=1)

    if reply is None:
        print(f"{i} hops away: No reply")
    elif reply.type == 3:
        # Destination reached (Port Unreachable)
        print("Done! Reached destination:", reply.src)
        break
    else:
        # Intermediate hop
        print(f"{i} hops away:", reply.src)
