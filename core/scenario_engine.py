import json
import random
from pathlib import Path


# ----------------------------------------------------------
# ROLE-BASED DIFFICULTY LEVELS
# ----------------------------------------------------------

ROLE_LEVELS = {
    "Student": "easy",
    "IT Support": "easy",
    "Junior SOC Analyst": "easy_medium",
    "Junior Pentester": "medium",
    "SOC Analyst": "medium",
    "Pentester": "medium_hard",
    "Senior SOC Analyst": "hard",
    "Senior Pentester": "hard",
    "Threat Hunter": "hard",
    "Incident Responder": "hard"
}

# ==========================================================
# LOAD SCENARIO TEMPLATE DATABASE
# ==========================================================


BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATE_FILE = (
    BASE_DIR /
    "data" /
    "scenario_templates.json"
)


with open(TEMPLATE_FILE, "r") as file:
    SCENARIO_DATA = json.load(file)



# ==========================================================
# HELPER FUNCTIONS
# ==========================================================


def choose_primary_tactic(tactics):

    if tactics:
        return tactics[0].lower()

    return "execution"



def get_attack_id(technique):

    return technique.get(
        "id",
        "Unknown"
    )



# ==========================================================
# SCENARIO GENERATOR
# ==========================================================


def generate_scenario(technique):

    tactic = choose_primary_tactic(
        technique.get("tactics", [])
    )

    industry = random.choice(
        SCENARIO_DATA["industries"]
    )

    events = SCENARIO_DATA["events"].get(
        tactic,
        SCENARIO_DATA["events"]["execution"]
    )

    evidence_sources = SCENARIO_DATA["evidence_sources"].get(
        tactic,
        SCENARIO_DATA["evidence_sources"]["execution"]
    )

    event = random.choice(events)

    evidence = random.choice(
        evidence_sources
    )

    scenario = f"""INCIDENT REPORT

Organisation: A {industry}

Incident Summary:
The security team detected that {event}.

Investigation Context:
SOC analysts are investigating activity associated with adversary behaviour mapped to MITRE ATT&CK.

MITRE ATT&CK MAPPING
Technique: {get_attack_id(technique)} - {technique.get("name")}
Tactic: {tactic.replace("-", " ").title()}

ANALYST OBJECTIVE
You are the assigned SOC analyst. Determine which evidence source should be reviewed first during investigation.

Recommended Evidence Source: {evidence}"""

    return scenario
# ==========================================================
# QUIZ GENERATOR
# ==========================================================


def generate_quiz(technique, role="Student"):

    tactic = choose_primary_tactic(
        technique.get("tactics", [])
    )

    level = ROLE_LEVELS.get(role, "easy")

    # ------------------------------------------------------
    # EASY
    # ------------------------------------------------------
    if level == "easy":

        question = "What should be reviewed first?"

        options = [
            "Endpoint antivirus alert",
            "Office attendance records",
            "Building maintenance schedule",
            "Printer supply inventory"
        ]

        answer = "Endpoint antivirus alert"

    # ------------------------------------------------------
    # EASY-MEDIUM
    # ------------------------------------------------------
    elif level == "easy_medium":

        question = "Which evidence source is the best initial investigation step?"

        options = [
            "Process execution logs",
            "Printer activity",
            "Employee parking records",
            "Cafeteria transaction logs"
        ]

        answer = "Process execution logs"

    # ------------------------------------------------------
    # MEDIUM
    # ------------------------------------------------------
    elif level == "medium":

        question = "Which evidence source would provide the strongest initial indicator of adversary execution activity?"

        options = [
            "Process creation and command-line telemetry",
            "Office attendance records",
            "Building access logs",
            "Printer queue history"
        ]

        answer = "Process creation and command-line telemetry"

    # ------------------------------------------------------
    # MEDIUM-HARD
    # ------------------------------------------------------
    elif level == "medium_hard":

        question = "Which evidence source would best support reconstruction of the attacker execution chain and persistence activity?"

        options = [
            "Process creation telemetry correlated with parent-child relationships",
            "Email signature settings",
            "Employee payroll records",
            "Conference room booking logs"
        ]

        answer = "Process creation telemetry correlated with parent-child relationships"

    # ------------------------------------------------------
    # HARD
    # ------------------------------------------------------
    else:

        question = "Which investigation approach would most effectively validate adversary execution, persistence, and lateral movement hypotheses while preserving forensic integrity?"

        options = [
            "Correlate EDR process telemetry, command-line history, authentication events, and network connections within a defined incident timeline",
            "Review employee attendance records",
            "Delete suspicious files immediately",
            "Reboot the workstation before collecting evidence"
        ]

        answer = "Correlate EDR process telemetry, command-line history, authentication events, and network connections within a defined incident timeline"

    random.shuffle(options)

    return {
        "question": question,
        "options": options,
        "answer": answer,
        "role": role,
        "difficulty": level
    }