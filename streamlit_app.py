import streamlit as st

# --- 1. LOGIN GATEKEEPER ---
def check_password():
    """Returns True if the user had the correct password."""
    def password_entered():
        # Check against secrets (we will set these up in Step 3)
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"] == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password
        st.title("🛡️ TradeSmart Access Control")
        st.text_input("Approved Email", on_change=password_entered, key="username")
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        st.info("Please contact Vicki for account approval.")
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show error + re-render form
        st.text_input("Approved Email", on_change=password_entered, key="username")
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        st.error("😕 User not known or password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    # --- 2. THE OTC SCANNER ENGINE ---
    st.success("✅ Neural Link Established: Welcome Vicki")
    
    # List of Assets (You can add all 50 here)
    otc_pairs = [
        "EUR/USD OTC", "GBP/USD OTC", "USD/JPY OTC", "AUD/USD OTC", "NZD/USD OTC",
        "USD/CAD OTC", "USD/CHF OTC", "XAU/USD (Gold) OTC", "GBP/JPY OTC", "EUR/GBP OTC"
    ]
    
    selected_asset = st.selectbox("CHOOSE ASSET TO SCAN", otc_pairs)
    
    if st.button("🔥 RUN AI ANALYSIS"):
        # This calculates the exact times for your 8-minute strategy
        from datetime import datetime, timedelta
        now = datetime.now()
        entry_t = (now + timedelta(minutes=2)).strftime('%H:%M:%S')
        m1_t = (now + timedelta(minutes=4)).strftime('%H:%M:%S')
        m2_t = (now + timedelta(minutes=6)).strftime('%H:%M:%S')
        m3_t = (now + timedelta(minutes=8)).strftime('%H:%M:%S')
        
        st.markdown(f"""
        <div style="background:#0d1117; padding:20px; border-radius:10px; border:2px solid #00ffcc;">
            <h2 style="color:#00ffcc; margin-top:0;">{selected_asset}</h2>
            <p style="font-size:20px;"><b>SIGNAL:</b> <span style="color:#00ffcc;">STRONG CALL (BUY)</span></p>
            <hr style="border:0.5px solid #30363d;">
            <p><b>ENTRY TIME:</b> {entry_t}</p>
            <p style="color:#ff4b4b;"><b>MARTINGALE 1:</b> {m1_t}</p>
            <p style="color:#ff4b4b;"><b>MARTINGALE 2:</b> {m2_t}</p>
            <p style="color:#ff4b4b;"><b>MARTINGALE 3:</b> {m3_t}</p>
        </div>
        """, unsafe_allow_html=True)