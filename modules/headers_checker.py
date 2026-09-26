import urllib.request

SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Referrer-Policy",
    "Permissions-Policy",
]

def check_headers(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    req = urllib.request.Request(url, method="HEAD",
                                  headers={"User-Agent": "CyberTool/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=8) as r:
            present = {h: bool(r.headers.get(h)) for h in SECURITY_HEADERS}
            return {"url": url, "status": r.status, "headers": present}
    except Exception:
        # Some servers reject HEAD, so retry with GET.
        req = urllib.request.Request(url, method="GET",
                                      headers={"User-Agent": "CyberTool/1.0"})
        with urllib.request.urlopen(req, timeout=8) as r:
            present = {h: bool(r.headers.get(h)) for h in SECURITY_HEADERS}
            return {"url": url, "status": r.status, "headers": present}
