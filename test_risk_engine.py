from risk_engine import assess_dependency

def test_critical_late_is_red():
    dep = {
        "id":"1","name":"Test","owner":"Team","status":"At Risk",
        "planned_eta":"2026-10-10","current_eta":"2026-10-14",
        "critical_path":True,"downstream_dependencies":["2"],"impact":"Blocks testing"
    }
    result = assess_dependency(dep)
    assert result["risk_level"] == "RED"
    assert result["eta_variance_days"] == 4

def test_on_track_is_green():
    dep = {
        "id":"1","name":"Test","owner":"Team","status":"On Track",
        "planned_eta":"2026-10-10","current_eta":"2026-10-10",
        "critical_path":False,"downstream_dependencies":[],"impact":"None"
    }
    assert assess_dependency(dep)["risk_level"] == "GREEN"
