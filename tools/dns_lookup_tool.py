import socket

def dns_lookup(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"{domain} → {ip}")
    except socket.gaierror:
        print("Could not resolve domain.")

if __name__ == "__main__":
    dom = input("Enter domain: ")
    dns_lookup(dom)
