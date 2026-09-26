import json
from datetime import datetime, timezone
from pathlib import Path

def save_report(data, directory="reports"):
    Path(directory).mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    path = Path(directory) / f"report_{stamp}.json"
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    return str(path)
