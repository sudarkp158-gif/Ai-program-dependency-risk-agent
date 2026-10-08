def find_critical_dependencies(dependencies):
    return [d for d in dependencies if d.get("critical_path") is True]
