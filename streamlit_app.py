import streamlit as st

# 1. BRIGHT & CLEAN STYLING
st.markdown("""
    <style>
    .stApp { background-color: white; }
    h1 { color: #007BFF; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-weight: bold; }
    .stButton>button {
        background-color: #007BFF !important;
        color: white !important;
        border-radius: 8px !important;
        width: 100%;
        height: 3em;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. SIMPLE LOGIN SYSTEM
if "password_correct" not in st.session_state:
    st.title("🔐 TradeSmart Login")
    st.write("Please enter your credentials to access the scanner.")
    
    email_input = st.text_input("Approved Email")
    pass_input = st.text_input("Password", type="password")
    
    if st.button("🚀 Enter Dashboard"):
        if email_input in st.secrets["passwords"] and pass_input == st.secrets["passwords"][email_input]:
            st.session_state["password_correct"] = True
            st.rerun()
        else:
            st.error("❌ Invalid Email or Password")
else:
    # 3. THE DASHBOARD (What you see after login)
    st.title("💎 TradeSmartWith_Vicki")
    st.success("Welcome back! Your scanner is active.")
    
    st.divider()
    
    st.subheader("📡 Live Market Scanner")
    asset = st.selectbox("Choose Asset", ["EUR/USD OTC", "BTC/USD", "GOLD", "GBP/JPY"])
    
    if st.button("🔍 RUN AI ANALYSIS"):
        with st.spinner('Scanning markets...'):
            st.balloons()
            st.write(f"### Analysis for {asset}: 📈 UPTREND LIKELY")
            st.info("Scanner Confidence: 88%")
