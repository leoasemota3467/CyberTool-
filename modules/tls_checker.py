import socket
import ssl
from datetime import datetime, timezone

def check_tls(host, port=443):
    context = ssl.create_default_context()
    with socket.create_connection((host, port), timeout=8) as sock:
        with context.wrap_socket(sock, server_hostname=host) as tls:
            cert = tls.getpeercert()
            cipher = tls.cipher()
            return {
                "host": host,
                "port": port,
                "tls_version": tls.version(),
                "cipher": cipher[0] if cipher else None,
                "subject": dict(x[0] for x in cert.get("subject", [])),
                "issuer": dict(x[0] for x in cert.get("issuer", [])),
                "not_before": cert.get("notBefore"),
                "not_after": cert.get("notAfter"),
                "checked_utc": datetime.now(timezone.utc).isoformat(),
            }
