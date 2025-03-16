import argparse
import socket
import threading

def scan_port(target, port, protocol):
    try:
        if protocol == "tcp":
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[+] TCP Port {port} is open")
            sock.close()
        elif protocol == "udp":
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(1)
            sock.sendto(b"\x00", (target, port))
            try:
                data, _ = sock.recvfrom(1024)
                print(f"[+] UDP Port {port} is open")
            except socket.timeout:
                pass
            sock.close()
    except Exception as e:
        print(f"[-] Error scanning port {port}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Simple Network Port Scanner")
    parser.add_argument("-t", "--target", required=True, help="Target IP address")
    parser.add_argument("-p", "--ports", required=True, help="Port range to scan (e.g., 20-100)")
    parser.add_argument("-m", "--mode", choices=["tcp", "udp"], default="tcp", help="Scan mode: tcp or udp")
    args = parser.parse_args()

    start_port, end_port = map(int, args.ports.split("-"))
    print(f"Scanning {args.target} from port {start_port} to {end_port} using {args.mode.upper()} protocol")

    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(args.target, port, args.mode))
        thread.start()

if __name__ == "__main__":
    main()
