from dependency_engine import eta_variance_days


def calculate_emerging_risk(dep):
    """
    Calculate an explainable emerging-risk score.

    This is a deterministic prediction signal, not a machine-learning model.
    """

    score = 0
    signals = []

    # Current ETA slippage
    variance = eta_variance_days(
        dep["planned_eta"],
        dep["current_eta"]
    )

    if variance >= 3:
        score += 3
        signals.append(f"ETA slipped by {variance} days")
    elif variance > 0:
        score += 1
        signals.append(f"ETA slipped by {variance} day(s)")

    # Critical-path exposure
    if dep.get("critical_path"):
        score += 3
        signals.append("dependency is on the critical path")

    # Downstream impact
    downstream_count = len(
        dep.get("downstream_dependencies", [])
    )

    if downstream_count >= 2:
        score += 2
        signals.append(
            f"{downstream_count} downstream dependencies"
        )
    elif downstream_count == 1:
        score += 1
        signals.append("one downstream dependency")

    # Current status
    if dep["status"].lower() == "at risk":
        score += 2
        signals.append("dependency is currently marked At Risk")

    # Classify emerging risk
    if score >= 6:
        risk = "HIGH"
    elif score >= 3:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return {
        "emerging_risk": risk,
        "score": score,
        "signals": signals
    }
