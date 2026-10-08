from critical_path import find_critical_dependencies

def test_find_critical_dependencies():
    deps = [{"id":"1","critical_path":True},{"id":"2","critical_path":False}]
    assert [d["id"] for d in find_critical_dependencies(deps)] == ["1"]
