from dependency_engine import eta_variance_days

def test_eta_variance():
    assert eta_variance_days("2026-10-10", "2026-10-14") == 4
    assert eta_variance_days("2026-10-10", "2026-10-10") == 0
