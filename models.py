from dataclasses import dataclass
from typing import List

@dataclass
class Dependency:
    id: str
    name: str
    owner: str
    status: str
    planned_eta: str
    current_eta: str
    critical_path: bool
    downstream_dependencies: List[str]
    impact: str
