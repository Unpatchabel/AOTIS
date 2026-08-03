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
    page_title="AOTIS",
    page_icon="🛡️",
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
                background:
                    linear-gradient(
                        rgba(5,10,25,0.75),
                        rgba(5,10,25,0.88)
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
# HEADER
# ----------------------------------------------------------

st.markdown(
    """
    <h1 style='margin-bottom:0;'>🛡️ TALOS</h1>

    <p style='font-size:1.1rem;color:#cbd5e1;'>
    AI-Driven OSINT Threat Awareness & Tabletop Platform
    </p>
    """,
    unsafe_allow_html=True
)

# ----------------------------------------------------------
# SIDEBAR
# ----------------------------------------------------------

logo_path = Path("assets/logo.png")

if logo_path.exists():
    st.sidebar.image(str(logo_path), width=120)

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

    st.header("Threat Awareness Dashboard")

    st.write(
        """
        Welcome to **TALOS**, an AI-driven OSINT threat awareness
        and tabletop exercise platform powered by MITRE ATT&CK.
        """
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("ATT&CK Techniques", get_technique_count())

    with col2:
        st.metric("Exercises Generated", "0")

    with col3:
        st.metric("Training Score", "0%")

    st.divider()

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

elif page == "Tabletop Simulator":

    st.header("Tabletop Simulator")

    techniques = get_all_techniques()

    if st.button("Generate Random Exercise"):

        selected = random.choice(techniques)

        st.session_state.exercise = {
            "technique": selected,
            "scenario": generate_scenario(selected),
            "quiz": generate_quiz(selected)
        }

    exercise = st.session_state.get("exercise")

    if exercise:

        st.subheader("🚨 Incident Scenario")

        st.markdown(
            f"""
            <div class="scenario-box">
            {exercise["scenario"].replace("\n", "<br>")}
            </div>
            """,
            unsafe_allow_html=True
        )

        quiz = exercise["quiz"]

        st.subheader("🧠 Analyst Decision")

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
                    ✅ Correct! Threat assessment completed.
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    f"""
                    <div class="danger-card">
                    ❌ Incorrect.<br><br>
                    Correct answer:<br>
                    <b>{quiz['answer']}</b>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    else:
        st.info("Generate an exercise to begin the simulation.")

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