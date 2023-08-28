import socket

def scan_ports(target, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) # Adjust the timeout as needed
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

if __name__ == "__main__":
    target_host = "127.0.0.1" # Replace this with the target IP address or domain name
    target_ports = [80, 443, 22, 3389, 8080] # Replace this with a list of ports to scan

    open_ports = scan_ports(target_host, target_ports)

    if open_ports:
        print(f"Open ports on {target_host}: {', '.join(map(str, open_ports))}")
    else:
        print("No open ports found.")

