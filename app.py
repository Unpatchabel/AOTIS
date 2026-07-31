import streamlit as st

from core.attack_search import (
    search_by_id,
    search_by_keyword,
    get_attack_id,
    get_tactics,
    get_technique_count
)

# ----------------------------------------------------------
# Page setup
# ----------------------------------------------------------

st.set_page_config(
    page_title="AOTIS",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ AOTIS")
st.subheader("AI-Driven OSINT Threat Awareness & Tabletop Platform")

# ----------------------------------------------------------
# Sidebar
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
# Dashboard
# ----------------------------------------------------------

if page == "Dashboard":

    st.header("Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("ATT&CK Techniques", get_technique_count())

    with col2:
        st.metric("Reports Generated", "0")

    st.success("Connected to the official MITRE ATT&CK dataset.")

# ----------------------------------------------------------
# ATT&CK Explorer
# ----------------------------------------------------------

elif page == "ATT&CK Explorer":

    st.header("ATT&CK Explorer")

    mode = st.radio(
        "Search Mode",
        ["Technique ID", "Keyword"],
        horizontal=True
    )

    query = st.text_input("Enter search term")

    if st.button("Search") and query:

        if mode == "Technique ID":
            results = search_by_id(query)
        else:
            results = search_by_keyword(query)

        if not results:
            st.warning("No techniques found.")

        else:
            st.success(f"Found {len(results)} result(s)")

            for tech in results[:10]:

                attack_id = get_attack_id(tech)
                tactics = get_tactics(tech)

                st.markdown(f"## {attack_id} - {tech.get('name', 'Unknown')}")

                if tactics:
                    st.markdown(
                        "**Tactics:** " + ", ".join(tactics)
                    )

                with st.expander("View Description"):
                    st.write(
                        tech.get("description", "No description available.")
                    )

                st.divider()

# ----------------------------------------------------------
# Tabletop Simulator
# ----------------------------------------------------------

elif page == "Tabletop Simulator":

    st.header("Tabletop Simulator")

    st.info("Coming next: randomized scenarios and MCQ exercises.")

# ----------------------------------------------------------
# Reports
# ----------------------------------------------------------

elif page == "Reports":

    st.header("Reports")

    st.info("Generated reports will appear here.")