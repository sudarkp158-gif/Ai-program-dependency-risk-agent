# AI Program Dependency & Risk Prediction Agent

## Objective
I started building an AI-powered program dependency and risk assessment workflow
because dependency management is one of the highest manual-toil areas for a TPM
managing complex programs. The workflow first calculates objective signals such
as ETA variance, downstream impact and critical-path exposure using deterministic
Python logic. An AI layer then interprets those signals to explain risk,
potential impact and recommended actions. I intentionally separated deterministic
calculations from probabilistic AI so the LLM is not responsible for date
arithmetic or business-rule calculations. The TPM validates the AI output and
owns the decision. The next stage is predictive risk using historical ETA
slippage, dependency age and downstream impact to identify emerging risks.

## Design principle
**AI predicts/explains; deterministic code calculates.**

Python calculates ETA variance, downstream impact and deterministic risk signals.
AI interprets those signals and can generate risk explanations, impact analysis,
recommended actions and escalation recommendations.
The TPM validates the AI output and owns the decision.

## Run
```bash
python app.py
pytest
```

## Architecture

Step 1 - Deterministic risk
Step 2 - Emerging-risk scoring
Step 3 - AI-powered TPM recommendation

Python calculates ETA variance, downstream impact and deterministic risk signals.
AI interprets those signals and can generate risk explanations, impact analysis,
recommended actions and escalation recommendations.
The TPM validates the AI output and owns the decision.

Deterministic facts → AI reasoning → Human decision

```
Dependency Data
      ↓
Deterministic Analysis
      ↓
Current Risk
      ↓
Emerging Risk
      ↓
AI Reasoning
      ↓
TPM Action
Dependency Data
      ↓
Deterministic Analysis
      ↓
Current Risk
      ↓
Emerging Risk
      ↓
AI Reasoning
      ↓
TPM Action
```
