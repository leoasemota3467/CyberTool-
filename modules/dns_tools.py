import socket

def dns_lookup(domain):
    domain = domain.strip()
    addresses = sorted({x[4][0] for x in socket.getaddrinfo(domain, None)})
    try:
        reverse = socket.gethostbyaddr(addresses[0])[0] if addresses else None
    except OSError:
        reverse = None
    return {"domain": domain, "addresses": addresses, "reverse_dns": reverse}
