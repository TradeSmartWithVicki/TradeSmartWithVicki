import streamlit as st
import random

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
    .buy-signal { color: #28A745; font-size: 30px; font-weight: bold; text-align: right; }
    .sell-signal { color: #DC3545; font-size: 30px; font-weight: bold; text-align: right; }
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
    .stButton>button {
        background-color: #007BFF !important;
        color: white !important;
        width: 100%;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. LOGIN SYSTEM
if "password_correct" not in st.session_state:
    st.title("🔐 TradeSmart Elite Login")
    email_input = st.text_input("Approved Email")
    pass_input = st.text_input("Password", type="password")
    if st.button("🚀 Enter Dashboard"):
        if "passwords" in st.secrets and email_input in st.secrets["passwords"]:
            if pass_input == st.secrets["passwords"][email_input]:
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("❌ Incorrect Password")
else:
    # 3. REBRANDED HEADER
    st.title("💎 TradeSmartWith_Vicki")

    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('<div class="signal-header">📡 AI OTC Scanner</div>', unsafe_allow_html=True)
        st.write("⏱ 2 Minutes Standard Signal")
        
        # 4. ADDED 70+ OTC ASSETS
        otc_pairs = [
            "EUR/USD OTC", "GBP/USD OTC", "USD/JPY OTC", "AUD/USD OTC", "NZD/USD OTC", "USD/CAD OTC", "USD/CHF OTC",
            "EUR/GBP OTC", "EUR/JPY OTC", "GBP/JPY OTC", "AUD/JPY OTC", "CHF/JPY OTC", "CAD/JPY OTC", "NZD/JPY OTC",
            "EUR/AUD OTC", "EUR/CAD OTC", "GBP/AUD OTC", "GBP/CAD OTC", "AUD/CAD OTC", "AUD/NZD OTC", "XAU/USD OTC",
            "XAG/USD OTC", "XRP/USD OTC", "BTC/USD OTC", "ETH/USD OTC", "LTC/USD OTC", "BCH/USD OTC", "ADA/USD OTC",
            "SOL/USD OTC", "DOT/USD OTC", "AVAX/USD OTC", "LINK/USD OTC", "ATOM/USD OTC", "MATIC/USD OTC", "ALGO/USD OTC",
            "Apple OTC", "Amazon OTC", "Google OTC", "Microsoft OTC", "Facebook OTC", "Tesla OTC", "Netflix OTC",
            "Boeing OTC", "Disney OTC", "Intel OTC", "McDonalds OTC", "Nike OTC", "Pfizer OTC", "Visa OTC", "Walmart OTC",
            "Exxon OTC", "CocaCola OTC", "Pepsi OTC", "Chevron OTC", "Goldman OTC", "JPMorgan OTC", "AmericanExp OTC",
            "Alibaba OTC", "Nio OTC", "Baidu OTC", "TotalEnergies OTC", "BP OTC", "Shell OTC", "BMW OTC", "Volkswagen OTC",
            "Airbus OTC", "Siemens OTC", "HSBC OTC", "Barclays OTC", "Samsung OTC", "Sony OTC"
        ]
        asset = st.selectbox("Market Asset", otc_pairs)
        
        m1, m2 = st.columns(2)
        m1.metric("AI Confidence", f"{random.randint(80, 96)}%")
        # 5. SIGNAL STRENGTH LOGIC
        strength = random.choice(["STRONG", "MODERATE"])
        m2.metric("Signal Strength", strength)

    with col2:
        if st.button("🔍 RUN SCAN"):
            st.session_state["last_signal"] = random.choice(["CALL (BUY)", "PUT (SELL)"])
            st.balloons()
    
    st.divider()

    # 6. BUY / SELL TRADE RESULTS
        if "last_signal" in st.session_state:
        res_col1, res_col2 = st.columns(2)
        with res_col1:
            st.write(f"### Result for {asset}")
        with res_col2:
            signal_style = "buy-signal" if "BUY" in st.session_state["last_signal"] else "sell-signal"
            st.markdown(f'<div class="{signal_style}">{st.session_state["last_signal"]}</div>', unsafe_allow_html=True)

    # Time Tracking Section (Untouched)
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
