# This script is designed to run in a Streamlit environment.
# If you're running it in an environment without Streamlit installed, this fallback will show a CLI-based simulation instead.

try:
    import streamlit as st
    import os

    env = os.getenv("ENV", "production")
    mode = st.sidebar.radio("Select Mode", ["Live", "Test"])
    is_test = (mode == "Test")

    st.markdown(f"""
        <div style='padding: 1rem; background-color: {'#ffdd57' if is_test else '#2ecc71'}; color: black; text-align: center; border-radius: 8px;'>
            <strong>{'TEST MODE - SIMULATION ONLY' if is_test else 'LIVE MODE - ACTIVE PREDICTIONS'}</strong>
        </div>
    """, unsafe_allow_html=True)

    st.title("AI Betting System Dashboard")

    tabs = st.tabs(["MLB", "NBA", "NFL", "NHL", "UFC", "Soccer"])

    for tab, sport in zip(tabs, ["MLB", "NBA", "NFL", "NHL", "UFC", "Soccer"]):
        with tab:
            st.subheader(f"{sport} Predictions")
            st.write("⚠️ This is a test run. No alerts will be sent." if is_test else "✅ Live predictions in effect.")
            st.dataframe({
                "Team": ["Team A", "Team B"],
                "Odds": ["+150", "-130"],
                "Win Probability": [0.63, 0.57],
                "Edge %": [6.2, 3.4],
                "Bet": ["Yes", "No"]
            })

    st.markdown("---")
    st.markdown("Made with 💡 for high-performance sports analytics.")

except ModuleNotFoundError:
    import os
    print("Streamlit is not installed. Running in fallback CLI mode.")
    print("ENV:", os.getenv("ENV", "production"))
    print("MODE: Test")
    print("---")
    sports = ["MLB", "NBA", "NFL", "NHL", "UFC", "Soccer"]
    for sport in sports:
        print(f"{sport} Predictions (TEST MODE)")
        print("Team A vs Team B | Odds: +150 / -130 | Win Prob: 63% / 57% | Edge: 6.2% / 3.4% | Bet: Yes / No")
        print("---")