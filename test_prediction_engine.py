from prediction_engine import calculate_emerging_risk


def test_high_emerging_risk():
    dep = {
        "id": "DEP-001",
        "name": "Identity API Integration",
        "owner": "Identity Team",
        "status": "At Risk",
        "planned_eta": "2026-10-10",
        "current_eta": "2026-10-14",
        "critical_path": True,
        "downstream_dependencies": [
            "DEP-004",
            "DEP-006"
        ],
        "impact": "Blocks integration testing"
    }

    result = calculate_emerging_risk(dep)

    assert result["emerging_risk"] == "HIGH"


def test_low_emerging_risk():
    dep = {
        "id": "DEP-002",
        "name": "Data Pipeline",
        "owner": "Data Platform",
        "status": "On Track",
        "planned_eta": "2026-10-15",
        "current_eta": "2026-10-15",
        "critical_path": False,
        "downstream_dependencies": [],
        "impact": "No current launch impact"
    }

    result = calculate_emerging_risk(dep)

    assert result["emerging_risk"] == "LOW"
