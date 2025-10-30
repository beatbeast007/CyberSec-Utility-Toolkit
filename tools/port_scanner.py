import socket

def scan_ports(target, ports):
    print(f"Scanning {target}...")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
            sock.close()
        except socket.error:
            print("Error connecting to target.")
            break

if __name__ == "__main__":
    host = input("Enter target IP/hostname: ")
    ports_to_scan = range(20, 1025)
    scan_ports(host, ports_to_scan)
