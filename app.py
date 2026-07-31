import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AOTIS",
    page_icon="🛡️",
    layout="wide"
)

# Header
st.title("🛡️ AOTIS")
st.subheader("AI-Driven OSINT Threat Awareness & Tabletop Platform")

# Sidebar navigation
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

# Pages
if page == "Dashboard":

    st.header("Dashboard")

    st.info("Welcome to AOTIS.")

    st.write("This platform will provide:")
    st.write("- MITRE ATT&CK exploration")
    st.write("- Threat awareness briefings")
    st.write("- Interactive tabletop exercises")
    st.write("- MCQ-based cyber training")
    st.write("- Downloadable reports")

elif page == "ATT&CK Explorer":

    st.header("ATT&CK Explorer")

    st.write("Search MITRE ATT&CK techniques here.")

elif page == "Tabletop Simulator":

    st.header("Tabletop Simulator")

    st.write("Interactive tabletop exercises will appear here.")

elif page == "Reports":

    st.header("Reports")

    st.write("Generated reports will appear here.")