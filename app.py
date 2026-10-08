from dependency_engine import load_dependencies
from risk_engine import assess_dependency

def main():
    dependencies = load_dependencies("dependencies.json")
    print("\nPROGRAM DEPENDENCY RISK REPORT")
    print("=" * 70)
    for dep in dependencies:
        result = assess_dependency(dep)
        print(f"\n{dep['id']} - {dep['name']}")
        print(f"Owner: {dep['owner']} | Status: {dep['status']}")
        print(f"ETA: {dep['planned_eta']} -> {dep['current_eta']}")
        print(f"Critical Path: {dep['critical_path']}")
        print(f"ETA Variance: {result['eta_variance_days']} day(s)")
        print(f"Downstream Impact: {result['downstream_count']}")
        print(f"Risk: {result['risk_level']}")
        print(f"Reason: {result['reason']}")

if __name__ == "__main__":
    main()
