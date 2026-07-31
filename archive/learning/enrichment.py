from datetime import datetime
import random

THREAT_DB = {
    "1.1.1.1": {
        "risk_score": 5,
        "reputation": "Clean",
        "first_seen": "2024-01-15",
        "last_seen": "2026-07-30",
        "notes": "Public DNS service"
    },
    "google.com": {
        "risk_score": 2,
        "reputation": "Trusted",
        "first_seen": "1997-09-15",
        "last_seen": "2026-07-30",
        "notes": "Major public web service"
    },
    "malicious.com": {
        "risk_score": 90,
        "reputation": "Malicious",
        "first_seen": "2026-07-01",
        "last_seen": "2026-07-29",
        "notes": "Associated with phishing activity"
    }
}

def enrich_ioc(ioc):
    if ioc in THREAT_DB:
        return THREAT_DB[ioc]
    return {
        "risk_score": "Unknown",
        "reputation": "Unknown",
        "first_seen": "Unknown",
        "last_seen": "Unknown",
        "notes": "No intelligence available"
    }
print("\nAOTIS THREAT ENRICHMENT\n")

ioc = input("Enter IOC: ").strip().lower()

result = enrich_ioc(ioc)
print("\n=== ENRICHMENT RESULT ===")
print("IOC:", ioc)
print("Risk Score:", result["risk_score"])
print("Reputation:", result["reputation"])
print("First Seen:", result["first_seen"])
print("Last Seen:", result["last_seen"])
print("Notes:", result["notes"])