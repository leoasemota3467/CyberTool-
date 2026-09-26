import re

def check_password(password):
    score = 0
    reasons = []
    if len(password) >= 12: score += 2
    elif len(password) >= 8: score += 1
    else: reasons.append("Use at least 8 characters; 12+ is preferable.")
    if re.search(r"[a-z]", password): score += 1
    else: reasons.append("Add lowercase letters.")
    if re.search(r"[A-Z]", password): score += 1
    else: reasons.append("Add uppercase letters.")
    if re.search(r"\d", password): score += 1
    else: reasons.append("Add numbers.")
    if re.search(r"[^A-Za-z0-9]", password): score += 1
    else: reasons.append("Add symbols.")
    labels = {0:"very weak",1:"weak",2:"fair",3:"moderate",4:"strong",5:"strong",6:"very strong"}
    return {"score": score, "rating": labels[score], "suggestions": reasons}
