# risk_engine.py

def calculate_risk_score(likelihood, impact):
    likelihood = int(likelihood)
    impact = int(impact)

    if not 1 <= likelihood <= 5:
        raise ValueError("Likelihood must be between 1 and 5.")

    if not 1 <= impact <= 5:
        raise ValueError("Impact must be between 1 and 5.")

    return likelihood * impact


def classify_risk(score):
    """
    Classifies risk level based on score.
    """

    if score >= 20:
        return "Critical"
    elif score >= 12:
        return "High"
    elif score >= 6:
        return "Medium"
    else:
        return "Low"


def get_recommendation(threat, vulnerability):
    """
    Provides a simple mitigation recommendation based on the threat or vulnerability.
    """

    threat = threat.lower()
    vulnerability = vulnerability.lower()

    if "phishing" in threat or "email" in threat:
        return "Implement security awareness training, email filtering, and multi-factor authentication."

    elif "malware" in threat:
        return "Update antivirus tools, patch systems regularly, and restrict suspicious downloads."

    elif "ddos" in threat:
        return "Use traffic filtering, rate limiting, and DDoS protection services."

    elif "insider" in threat or "privileges" in vulnerability:
        return "Apply least privilege access, monitor user activity, and review permissions regularly."

    elif "data leak" in threat or "misconfigured" in vulnerability:
        return "Review cloud permissions, enable access logging, and apply data loss prevention controls."

    elif "ransomware" in threat:
        return "Maintain offline backups, patch systems, and conduct ransomware response drills."

    elif "credential" in threat or "password" in vulnerability:
        return "Enforce strong password policies, multi-factor authentication, and login monitoring."

    elif "fraud" in threat or "approval" in vulnerability:
        return "Introduce approval workflows, transaction monitoring, and segregation of duties."

    else:
        return "Perform a detailed security review and implement appropriate technical and administrative controls."


def assess_risk(asset, threat, vulnerability, likelihood, impact):
    """
    Creates a full cybersecurity risk assessment.
    """

    score = calculate_risk_score(likelihood, impact)
    risk_level = classify_risk(score)
    recommendation = get_recommendation(threat, vulnerability)

    return {
        "asset": asset,
        "threat": threat,
        "vulnerability": vulnerability,
        "likelihood": likelihood,
        "impact": impact,
        "risk_score": score,
        "risk_level": risk_level,
        "recommendation": recommendation
    }