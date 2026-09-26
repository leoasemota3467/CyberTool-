import urllib.request
import urllib.error

def check_http(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    req = urllib.request.Request(url, method="GET", headers={"User-Agent": "CyberTool/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=8) as r:
            return {
                "url": url,
                "status": r.status,
                "final_url": r.geturl(),
                "server": r.headers.get("Server"),
                "content_type": r.headers.get("Content-Type"),
            }
    except urllib.error.HTTPError as e:
        return {"url": url, "status": e.code, "error": str(e)}
