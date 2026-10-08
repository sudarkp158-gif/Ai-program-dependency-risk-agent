"""
AI layer placeholder.

Python calculates objective facts.
An LLM interprets those facts and recommends action.
The TPM validates the output and owns the decision.
"""

def build_ai_input(dep, deterministic_result):
    return {"dependency": dep, "deterministic_signals": deterministic_result}

def analyze_with_ai(dep, deterministic_result):
    raise NotImplementedError("Add an approved LLM provider in this module.")
