import json

# Load ATT&CK dataset
file_path = "data/enterprise-attack.json"

with open(file_path, "r") as f:
    data = json.load(f)

# Build technique list
techniques = []

for obj in data["objects"]:
    if obj.get("type") == "attack-pattern":
        techniques.append(obj)


# ----------------------------------------------------------
# Helpers
# ----------------------------------------------------------

def get_attack_id(tech):
    refs = tech.get("external_references", [])

    for ref in refs:
        if ref.get("source_name") == "mitre-attack":
            return ref.get("external_id", "Unknown")

    return "Unknown"


def get_tactics(tech):
    tactics = tech.get("kill_chain_phases", [])

    if tactics:
        return [t["phase_name"] for t in tactics]

    return []


def get_technique_count():
    return len(techniques)


# ----------------------------------------------------------
# Search functions
# ----------------------------------------------------------

def search_by_id(search_term):
    search_term = search_term.lower()

    results = []

    for tech in techniques:
        attack_id = get_attack_id(tech).lower()

        if attack_id == search_term:
            results.append(tech)

    return results


def search_by_keyword(search_term):
    search_term = search_term.lower()

    results = []

    for tech in techniques:
        name = tech.get("name", "").lower()
        description = tech.get("description", "").lower()

        if search_term in name or search_term in description:
            results.append(tech)

    return results