from dependency_engine import dependency_signals

def assess_dependency(dep):
    s = dependency_signals(dep)
    variance = s["eta_variance_days"]
    status = s["status"].lower()

    # Illustrative/configurable rules, not universal business rules.
    if s["critical_path"] and variance > 0:
        level, reason = "RED", "Critical-path dependency is late."
    elif s["critical_path"] and status == "at risk":
        level, reason = "RED", "Critical-path dependency is marked at risk."
    elif variance > 0:
        level, reason = "AMBER", "Dependency ETA has slipped from baseline."
    elif status == "at risk":
        level, reason = "AMBER", "Dependency is explicitly marked at risk."
    else:
        level, reason = "GREEN", "No deterministic high-risk signal detected."

    return {**s, "risk_level": level, "reason": reason}
