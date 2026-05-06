# Cybersecurity Risk Assessment Toolkit

A Python and Streamlit-based cybersecurity risk assessment tool that evaluates organisational assets, threats, and vulnerabilities, calculates risk scores, classifies risk levels, and recommends mitigation actions.

## Features

- Upload cybersecurity risk data using CSV
- Calculate risk score using Likelihood x Impact
- Classify risks as Low, Medium, High, or Critical
- Generate mitigation recommendations
- Display summary metrics
- Show risk-level chart
- Download assessed risk report as CSV

## Tech Stack

- Python
- Pandas
- Streamlit

## CSV Format

```csv
asset,threat,vulnerability,likelihood,impact
Customer Database,Phishing Attack,No MFA,High,Critical