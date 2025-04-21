# The code provided demonstrates how to read and analyze packets from a .pcap file using the 
# pcapy library in Python. .pcap (Packet Capture) files store captured network traffic and 
# are commonly used for offline analysis in network security and forensics. With 
# pcapy.open_offline("packets.pcap"), the code opens a previously recorded packet 
# capture file, allowing analysis without needing to actively sniff live traffic. 
# This is especially useful in post-incident analysis or when working with sample 
# traffic in training and research environments.

# In the main loop, the code processes up to 500 packets from the file. Each iteration 
# retrieves a packet using pcap_file.next() and extracts the first 14 bytes (payload[:14]) 
# as the Layer 2 header (Ethernet). Using struct.unpack("!6s6sH", l2hdr), it decodes the 
# Ethernet frame to extract MAC addresses and EtherType. The source and destination MAC 
# addresses are then formatted into the standard hexadecimal representation using string 
# formatting.

# Following this, the IP header is parsed from bytes 14 to 34 of the payload using another 
# unpack() call with the format '!BBHHHBBH4s4s'. From this header, the script extracts the 
# protocol used (e.g., TCP, UDP, ICMP) and the TTL (Time To Live), which is a field used to 
# limit the lifespan of a packet in a network. This simple script provides a practical 
# introduction to offline packet analysis using Python, helping users understand key 
# elements in packet structure and offering a foundation for deeper traffic inspection or 
# automation in network forensics.

import pcapy
from struct import *

# Open the pcap file
pcap_file = pcapy.open_offline("packets.pcap")

# Initialize packet counter
count = 1

# Read up to 500 packets
while count < 500:
    print("Packet #: ", count)

    try:
        # Read next packet (returns header and payload)
        (header, payload) = pcap_file.next()
    except:
        # Stop if there are no more packets
        print("End of file or error reading packet.")
        break

    # Extract Layer 2 (Ethernet) header (first 14 bytes)
    l2hdr = payload[:14]
    l2data = unpack("!6s6sH", l2hdr)

    # Extract MAC addresses
    srcmac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (
        l2hdr[6], l2hdr[7], l2hdr[8], l2hdr[9], l2hdr[10], l2hdr[11])
    dstmac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (
        l2hdr[0], l2hdr[1], l2hdr[2], l2hdr[3], l2hdr[4], l2hdr[5])

    print("Source MAC: ", srcmac, " Destination MAC: ", dstmac)

    # Extract Layer 3 (IP) header (usually follows Ethernet header)
    ip_header = unpack('!BBHHHBBH4s4s', payload[14:34])
    timetolive = ip_header[5]
    protocol = ip_header[6]

    print("Protocol: ", protocol, " Time To Live: ", timetolive)

    # Increment counter
    count += 1
