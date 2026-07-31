def generate_assessment(ioc, reputation, risk_score):
    if risk_score >= 80:
        severity = "HIGH"
        scenario = (
            "The indicator is likely associated with malicious activity such as "
            "phishing, malware delivery, or command-and-control communication."
        )
        mitre = ["T1566 - Phishing", "T1071 - Application Layer Protocol"]
        actions = [
            "Block the indicator",
            "Search SIEM logs for related activity",
            "Investigate affected endpoints",
        ]

    elif risk_score >= 40:
        severity = "MEDIUM"
        scenario = (
            "The indicator has suspicious characteristics and should be monitored "
            "for additional malicious activity."
        )
        mitre = ["T1583 - Acquire Infrastructure"]
        actions = [
            "Monitor network activity",
            "Review recent connections",
        ]

    else:
        severity = "LOW"
        scenario = (
            "The indicator currently appears low risk based on available intelligence."
        )
        mitre = ["No significant mapping"]
        actions = [
            "No immediate action required",
            "Continue routine monitoring",
        ]

    return {
        "severity": severity,
        "scenario": scenario,
        "mitre": mitre,
        "actions": actions,
    }

print("\nAOTIS AI THREAT ANALYST\n")

ioc = input("Enter IOC: ").strip().lower()
reputation = input("Enter reputation (Trusted/Clean/Unknown/Malicious): ").strip()
risk_score = int(input("Enter risk score (0-100): "))

assessment = generate_assessment(ioc, reputation, risk_score)

print("\n=== AI THREAT ASSESSMENT ===")
print("IOC:", ioc)
print("Reputation:", reputation)
print("Risk Score:", risk_score)
print("Severity:", assessment["severity"])

print("\nScenario:")
print(assessment["scenario"])

print("\nMITRE ATT&CK Mapping:")
for item in assessment["mitre"]:
    print("-", item)

print("\nRecommended Actions:")
for action in assessment["actions"]:
    print("-", action)