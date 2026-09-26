import socket
import re

def parse_ports(spec):
    ports = set()
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-", 1)
            a, b = int(a), int(b)
            if a < 1 or b > 65535 or a > b:
                raise ValueError("Invalid port range")
            if b - a > 4096:
                raise ValueError("Maximum range is 4096 ports per scan")
            ports.update(range(a, b + 1))
        else:
            p = int(part)
            if not 1 <= p <= 65535:
                raise ValueError("Port must be 1-65535")
            ports.add(p)
    return sorted(ports)

def scan_ports(host, spec="1-1024", timeout=0.5):
    ports = parse_ports(spec)
    ip = socket.gethostbyname(host)
    open_ports = []
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            if s.connect_ex((ip, port)) == 0:
                try:
                    service = socket.getservbyport(port, "tcp")
                except OSError:
                    service = "unknown"
                open_ports.append({"port": port, "service": service})
    return {"host": host, "ip": ip, "scanned": len(ports), "open": open_ports}
