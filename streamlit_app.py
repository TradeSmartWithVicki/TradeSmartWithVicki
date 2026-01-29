import streamlit as st

# 1. STYLE SETTINGS (Keeping your matured light theme)
st.markdown("""
    <style>
    .stApp { background-color: #F0F2F6; }
    .main-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border-top: 5px solid #007BFF;
    }
    .signal-header { color: #1E3A8A; font-weight: bold; font-size: 24px; }
    .time-box {
        background-color: #F8F9FA;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        border: 1px solid #DEE2E6;
    }
    .martingale-row {
        display: flex;
        justify-content: space-between;
        padding: 8px 0;
        border-bottom: 1px solid #EEE;
    }
    /* Login Button Styling */
    .stButton>button {
        background-color: #007BFF !important;
        color: white !important;
        width: 100%;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. THE LOGIN DETAILS (Brought back as requested)
if "password_correct" not in st.session_state:
    st.title("🔐 TradeSmart Elite Login")
    
    email_input = st.text_input("Approved Email")
    pass_input = st.text_input("Password", type="password")
    
    if st.button("🚀 Enter Dashboard"):
        # This checks the [passwords] section in your Streamlit Secrets
        if "passwords" in st.secrets and email_input in st.secrets["passwords"]:
            if pass_input == st.secrets["passwords"][email_input]:
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("❌ Incorrect Password")
        else:
            st.error("❌ Email not recognized in Secrets")
else:
    # 3. YOUR PERFECTED DASHBOARD (Untouched)
    st.title("💎 TradeSmart Professional")

    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('<div class="signal-header">📡 AI OTC Scanner</div>', unsafe_allow_html=True)
        st.write("⏱ 2 Minutes Standard Signal")
        asset = st.selectbox("Market Asset", ["XRP/USD OTC", "EUR/USD OTC", "GBP/JPY", "GOLD"])
        m1, m2 = st.columns(2)
        m1.metric("AI Confidence", "84%")
        m2.metric("Signal Strength", "STRONG")

    with col2:
        if st.button("🔍 RUN SCAN"):
            st.balloons()
    
    st.divider()

    # Time Tracking Section
    s_col1, s_col2 = st.columns(2)
    with s_col1:
        st.markdown('<div class="time-box"><p style="margin:0; color:grey;">Get Ready</p><h3 style="margin:0; color:#1E3A8A;">06:20:34</h3></div>', unsafe_allow_html=True)
    with s_col2:
        st.markdown('<div class="time-box" style="border-color: #28A745;"><p style="margin:0; color:grey;">Entry Time</p><h3 style="margin:0; color:#28A745;">06:22:40</h3></div>', unsafe_allow_html=True)

    st.write("---")
    st.subheader("⚖️ Martingale Levels")
    levels = [("Level 1", "06:24:03"), ("Level 2", "06:26:45"), ("Level 3", "06:28:10")]
    
    for lvl, tm in levels:
        st.markdown(f'<div class="martingale-row"><span>{lvl}</span><span style="font-weight:bold;">{tm}</span></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
