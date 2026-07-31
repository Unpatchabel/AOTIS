import json

# ==========================================================
# LOAD ATT&CK DATASET
# ==========================================================

file_path = "data/enterprise-attack.json"

with open(file_path, "r") as f:
    data = json.load(f)

# ==========================================================
# BUILD TECHNIQUE DATABASE
# ==========================================================

techniques = []

for obj in data["objects"]:
    if obj.get("type") == "attack-pattern":
        techniques.append(obj)

# ==========================================================
# SEARCH FUNCTIONS
# ==========================================================

def search_by_id(search_term):
    """Search for one exact ATT&CK Technique ID."""

    results = []

    for tech in techniques:

        attack_id = ""
        refs = tech.get("external_references", [])

        for ref in refs:
            if ref.get("source_name") == "mitre-attack":
                attack_id = ref.get("external_id", "")
                break

        if search_term == attack_id.lower():
            results.append(tech)

    return results


def search_by_keyword(search_term):
    """Search technique names and descriptions."""

    results = []

    for tech in techniques:

        name = tech.get("name", "")
        description = tech.get("description", "")

        if (
            search_term in name.lower()
            or search_term in description.lower()
        ):
            results.append(tech)

    return results

# ==========================================================
# DISPLAY RESULTS
# ==========================================================

def display_results(results):

    if not results:
        print("\nNo ATT&CK techniques found.")
        return

    print(f"\nFound {len(results)} result(s)\n")

    for tech in results[:5]:

        name = tech.get("name", "")
        description = tech.get("description", "")

        attack_id = "Unknown"

        refs = tech.get("external_references", [])

        for ref in refs:
            if ref.get("source_name") == "mitre-attack":
                attack_id = ref.get("external_id", "Unknown")
                break

        print("=" * 60)
        print(f"Technique ID : {attack_id}")
        print(f"Name         : {name}")

        tactics = tech.get("kill_chain_phases", [])

        if tactics:
            tactic_names = [t["phase_name"] for t in tactics]
            print("Tactics      :", ", ".join(tactic_names))
        else:
            print("Tactics      : N/A")

        print("\nDescription:")

        short_desc = description.replace("\n", " ")[:300]

        if len(description) > 300:
            print(short_desc + "...")
        else:
            print(short_desc)

        print("=" * 60)

# ==========================================================
# MAIN PROGRAM
# ==========================================================

print("\n==============================")
print(" AOTIS ATT&CK SEARCH ENGINE")
print("==============================")

print("\nSearch Mode")
print("1. Technique ID")
print("2. Keyword")

mode = input("\nChoose search mode (1 or 2): ").strip()
search = input("Enter search term: ").strip().lower()

if mode == "1":

    results = search_by_id(search)

elif mode == "2":

    results = search_by_keyword(search)

else:

    print("\nInvalid option.")
    exit()

display_results(results)

        