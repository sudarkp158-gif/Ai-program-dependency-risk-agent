import json
from datetime import date

def load_dependencies(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def eta_variance_days(planned_eta, current_eta):
    return (date.fromisoformat(current_eta) - date.fromisoformat(planned_eta)).days

def dependency_signals(dep):
    return {
        "eta_variance_days": eta_variance_days(dep["planned_eta"], dep["current_eta"]),
        "downstream_count": len(dep.get("downstream_dependencies", [])),
        "critical_path": dep["critical_path"],
        "status": dep["status"],
    }
