import json
import random
from pathlib import Path


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


    scenario = f"""
INCIDENT REPORT
================================


Organisation:
A {industry}


Incident Summary:

The security team detected that {event}.


Investigation Context:

SOC analysts are investigating activity
associated with adversary behaviour mapped
to MITRE ATT&CK.


MITRE ATT&CK MAPPING:

Technique:
{get_attack_id(technique)} - {technique.get("name")}


Tactic:
{tactic.replace("-", " ").title()}


ANALYST OBJECTIVE:

You are the assigned SOC analyst.

Determine which evidence source should
be reviewed first during investigation.


Recommended Evidence Source:

{evidence}
"""


    return scenario



# ==========================================================
# QUIZ GENERATOR
# ==========================================================


def generate_quiz(technique):

    tactic = choose_primary_tactic(
        technique.get("tactics", [])
    )


    evidence_sources = SCENARIO_DATA["evidence_sources"].get(
        tactic,
        SCENARIO_DATA["evidence_sources"]["execution"]
    )


    correct_answer = random.choice(
        evidence_sources
    )


    wrong_answers = [
        "Employee attendance records",
        "Office maintenance reports",
        "Company financial documents"
    ]


    options = [
        correct_answer
    ] + wrong_answers


    random.shuffle(options)


    return {

        "question":
        "Which evidence source should analysts prioritise during investigation?",


        "options":
        options,


        "answer":
        correct_answer

    }