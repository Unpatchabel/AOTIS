import base64
from pathlib import Path
import random
import streamlit as st

from core.attack_search import (
    search_by_id,
    search_by_keyword,
    get_attack_id,
    get_technique_count,
    get_all_techniques
)

from core.scenario_engine import (
    generate_scenario,
    generate_quiz
)

# ----------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------

st.set_page_config(
    page_title="TALOS",
    page_icon="assets/logo.png",
    layout="wide"
)

# ----------------------------------------------------------
# BACKGROUND IMAGE ONLY
# ----------------------------------------------------------

def set_background(image_path: str):
    image_file = Path(image_path)

    if image_file.exists():
        with open(image_file, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()

        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image:
                    linear-gradient(
                        rgba(0,0,0,0.30),
                        rgba(0,0,0,0.52)
                    ),
                    url("data:image/png;base64,{encoded}");

                background-size: cover;
                background-position: center;
                background-attachment: fixed;
                background-repeat: no-repeat;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

# Apply wallpaper
set_background("assets/banner.png")

# ----------------------------------------------------------
# LOAD EXTERNAL CSS
# ----------------------------------------------------------

css_path = Path("assets/styles.css")

if css_path.exists():
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# ----------------------------------------------------------
# SIDEBAR
# ----------------------------------------------------------


st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Dashboard",
        "ATT&CK Explorer",
        "Tabletop Simulator",
        "Reports"
    ]
)

# ----------------------------------------------------------
# DASHBOARD
# ----------------------------------------------------------

if page == "Dashboard":

    st.markdown(
        """
        <div class="hero-panel">

        <h1>TALOS</h1>

        <p style="font-size:1.1rem;">
        Your Personal Threat Awareness & Training Platform
        </p>

        <hr style="border:0;border-top:1px solid rgba(255,255,255,0.08);margin:18px 0;">

        <h2>Threat Awareness Dashboard</h2>

        <p>
        TALOS is an AI-driven OSINT threat awareness and tabletop exercise platform
        powered by MITRE ATT&CK. It provides interactive analyst training,
        scenario-based exercises, and threat intelligence exploration in a single
        unified environment.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("ATT&CK Techniques", get_technique_count())

    with col2:
        st.metric("Exercises Generated", "0")

    with col3:
        st.metric("Training Score", "0%")

    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

    st.subheader("Current Threat Focus")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(
            """
            <div class="warning-card">
            <b>Phishing & Initial Access</b><br><br>
            T1566 - Phishing
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            """
            <div class="danger-card">
            <b>Data Exfiltration</b><br><br>
            T1567 - Exfiltration Over Web Service
            </div>
            """,
            unsafe_allow_html=True
        )
# ----------------------------------------------------------
# ATT&CK EXPLORER
# ----------------------------------------------------------

elif page == "ATT&CK Explorer":

    st.header("MITRE ATT&CK Explorer")

    mode = st.radio(
        "Search Mode",
        ["Technique ID", "Keyword"]
    )

    query = st.text_input("Enter ATT&CK ID or Keyword")

    if st.button("Search"):

        if mode == "Technique ID":
            results = search_by_id(query)
        else:
            results = search_by_keyword(query)

        if results:

            st.markdown(
                f"""
                <div class="report-box">
                Found {len(results)} result(s)
                </div>
                """,
                unsafe_allow_html=True
            )

            for tech in results[:10]:

                st.subheader(
                    f"{get_attack_id(tech)} - {tech.get('name')}"
                )

                st.write(
                    tech.get("description", "No description")
                )

                st.divider()

        else:
            st.warning("No techniques found.")

# ----------------------------------------------------------
# TABLETOP SIMULATOR
# ----------------------------------------------------------

# ----------------------------------------------------------
# TABLETOP SIMULATOR
# ----------------------------------------------------------

elif page == "Tabletop Simulator":

    st.header("Tabletop Simulator")

    techniques = get_all_techniques()

    role = st.selectbox(
        "Training Role",
        [
            "Student",
            "IT Support",
            "Junior SOC Analyst",
            "Junior Pentester",
            "SOC Analyst",
            "Pentester",
            "Senior SOC Analyst",
            "Senior Pentester",
            "Threat Hunter",
            "Incident Responder"
        ]
    )

    # ------------------------------------------------------
    # ROLE GUIDE
    # ------------------------------------------------------

    st.markdown(
        """
        <div class="role-box">

        <div class="role-label">Role Guide</div>

        <table style="width:100%; border-collapse:collapse; color:white; font-size:0.95rem;">
            <tr>
                <td style="padding:6px 0;"><b>Student</b></td>
                <td style="padding:6px 0;">Basic cybersecurity awareness and terminology.</td>
            </tr>
            <tr>
                <td style="padding:6px 0;"><b>IT Support</b></td>
                <td style="padding:6px 0;">Basic troubleshooting and endpoint review.</td>
            </tr>
            <tr>
                <td style="padding:6px 0;"><b>Junior SOC Analyst</b></td>
                <td style="padding:6px 0;">Alert triage and initial investigation steps.</td>
            </tr>
            <tr>
                <td style="padding:6px 0;"><b>Junior Pentester</b></td>
                <td style="padding:6px 0;">Reconnaissance and basic attack understanding.</td>
            </tr>
            <tr>
                <td style="padding:6px 0;"><b>SOC Analyst</b></td>
                <td style="padding:6px 0;">Evidence analysis and incident investigation.</td>
            </tr>
            <tr>
                <td style="padding:6px 0;"><b>Pentester</b></td>
                <td style="padding:6px 0;">Attack path analysis and security testing.</td>
            </tr>
            <tr>
                <td style="padding:6px 0;"><b>Senior SOC Analyst</b></td>
                <td style="padding:6px 0;">Advanced incident analysis and containment.</td>
            </tr>
            <tr>
                <td style="padding:6px 0;"><b>Senior Pentester</b></td>
                <td style="padding:6px 0;">Advanced offensive security reasoning.</td>
            </tr>
            <tr>
                <td style="padding:6px 0;"><b>Threat Hunter</b></td>
                <td style="padding:6px 0;">Hypothesis-driven hunting and detection development.</td>
            </tr>
            <tr>
                <td style="padding:6px 0;"><b>Incident Responder</b></td>
                <td style="padding:6px 0;">Containment, eradication, and recovery decision-making.</td>
            </tr>
        </table>

        </div>
        """,
        unsafe_allow_html=True
    )

    # ------------------------------------------------------
    # GENERATE EXERCISE
    # ------------------------------------------------------

    if st.button("Generate Random Exercise"):

        selected = random.choice(techniques)

        st.session_state.exercise = {
            "technique": selected,
            "scenario": generate_scenario(selected),
            "quiz": generate_quiz(selected, role)
        }

    exercise = st.session_state.get("exercise")

    # ------------------------------------------------------
    # DISPLAY EXERCISE
    # ------------------------------------------------------

    if exercise:

        st.subheader("Incident Scenario")

        st.markdown(
            f"""
            <div class="scenario-box">
            {exercise["scenario"].replace("\n", "<br>")}
            </div>
            """,
            unsafe_allow_html=True
        )

        quiz = exercise["quiz"]

        st.markdown(
            f"""
            <div class="role-box">

                <div class="role-label">Training Role</div>
                <div class="role-value">{quiz['role']}</div>

                <div style="height:14px;"></div>

                <div class="role-label">Difficulty</div>
                <div class="role-value">{quiz['difficulty'].replace('_', ' ').title()}</div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.subheader("Analyst Decision")

        answer = st.radio(
            quiz["question"],
            quiz["options"],
            key="quiz_answer"
        )

        if st.button("Submit Answer"):

            if answer == quiz["answer"]:

                st.markdown(
                    """
                    <div class="report-box">
                    Correct. Threat assessment completed.
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    f"""
                    <div class="danger-card">
                    Incorrect.<br><br>
                    Correct answer:<br>
                    <b>{quiz['answer']}</b>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    else:

        st.markdown(
            """
            <div class="role-box">
            Select a training role and generate an exercise to begin the simulation.
            </div>
            """,
            unsafe_allow_html=True
        )
# ----------------------------------------------------------
# REPORTS
# ----------------------------------------------------------

elif page == "Reports":

    st.header("Reports")

    st.markdown(
        """
        <div class="report-box">
        Generated investigation reports will appear here.
        </div>
        """,
        unsafe_allow_html=True
    )