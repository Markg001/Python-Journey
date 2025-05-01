# # Scapy is a powerful Python-based tool for creating, manipulating, sending, and analyzing 
# network packets across multiple layers of the TCP/IP stack. It allows users to craft 
# custom packets layer-by-layer — from Ethernet and IP to TCP, UDP, or ICMP — enabling 
# asks such as scanning networks, spoofing ARP entries, or building protocol-specific 
# payloads. For example, users can generate an ICMP echo request packet using 
# IP(dst='www.python.org')/ICMP() and view its structure with the .show() or .show2() 
# methods. Scapy offers deep visibility into packets and their fields using functions 
# like ls() and summary() and supports real-time interaction through its interactive 
# shell or Python scripts.

# For sending packets, Scapy provides send() for layer 3 and sendp() for layer 2. 
# These can be used with parameters like loop, inter, or iface to control timing and 
# network interface behavior. For bidirectional communication, Scapy’s sr(), sr1(), srp(), 
# and srp1() functions allow sending and receiving packets, making it ideal for ping sweeps, 
# port scanning, and traffic sniffing tasks. For instance, 
# srp(Ether()/ARP(pdst="192.168.18.0/24")) sends ARP requests across a subnet and captures 
# live responses to identify active devices. Scapy’s versatility and scriptability 
# make it an essential tool for network analysts, penetration testers, and cybersecurity 
# learners.

from scapy.all import *

# 1. Create and display an ICMP echo request packet
icmp_packet = IP(dst="www.python.org") / ICMP()
icmp_packet.show()       # Detailed structure
icmp_packet.summary()    # Brief overview

# 2. Send the packet and receive a response
response = sr1(icmp_packet, timeout=2)
if response:
    response.show()

# 3. ARP ping sweep on a local subnet
arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst="192.168.18.0/24")
answered, unanswered = srp(arp_request, timeout=2, verbose=False)

print("Active hosts:")
for sent, received in answered:
    print(f"{received.psrc} is alive, MAC: {received.hwsrc}")

# 4. Sniff 5 packets on the default interface
packets = sniff(count=5)
print("\nSniffed Packets Summary:")
for pkt in packets:
    print(pkt.summary())
# run as administrator