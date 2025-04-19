# This chapter introduces the fundamentals of analyzing network traffic in Python using 
# pcapy-ng and scapy—two powerful modules for packet capture and manipulation. 
# These tools are crucial for anyone diving into cybersecurity, ethical hacking, or 
# network diagnostics. pcapy-ng allows low-level packet capturing directly from network 
# interfaces, while scapy offers advanced packet crafting, decoding, and analysis 
# capabilities.

# The chapter covers essential concepts such as capturing and injecting packets using 
# pcapy-ng, using scapy for port scanning and ARP spoofing detection, and reading .pcap 
# files for forensic analysis. With basic networking knowledge and a Python 3.10 environment 
# on Unix-based systems, users can begin creating their own network sniffers and analysis 
# tools.

import pcapy
import datetime

# List all available network interfaces on the machine
interfaces = pcapy.findalldevs()
print("Available interfaces are :")
for interface in interfaces:
    print(interface)

# User selects the interface to sniff
interface = input("Enter interface name to sniff : ")
print("Sniffing interface " + interface)

# Open the selected interface in live capture mode
# Parameters: interface, max bytes per packet, promiscuous mode (1=on), timeout (0=immediate)
cap = pcapy.open_live(interface, 65536 , 1 , 0)

# Infinite loop to capture packets in real time
while True:
    (header, payload) = cap.next()
    print('%s: captured %d bytes' % (datetime.datetime.now(), header.getlen()))
