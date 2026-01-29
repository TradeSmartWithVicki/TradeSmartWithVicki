import streamlit as st
import random
import time
from datetime import datetime, timedelta

# 1. STYLE SETTINGS
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
    .buy-signal { color: #28A745; font-size: 32px; font-weight: bold; text-align: center; border: 3px solid #28A745; border-radius: 10px; padding: 15px; background: #E8F5E9; }
    .sell-signal { color: #DC3545; font-size: 32px; font-weight: bold; text-align: center; border: 3px solid #DC3545; border-radius: 10px; padding: 15px; background: #FFEBEE; }
    .time-box {
        background-color: #F8F9FA;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        border: 1px solid #DEE2E6;
    }
    .stButton>button {
        background-color: #007BFF !important;
        color: white !important;
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
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
    # 3. BRANDING & LIVE CLOCK
    st.title("💎 TradeSmartWith_Vicki")
    
    now = datetime.now()
    st.markdown(f"<h4 style='text-align:center; color:#1E3A8A;'>Market Time: {now.strftime('%H:%M:%S')}</h4>", unsafe_allow_html=True)

    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('<div class="signal-header">📡 AI OTC Scanner</div>', unsafe_allow_html=True)
        st.write("⏱ 2 Minutes Standard Signal")
        
        otc_pairs = [
            "EUR/USD OTC", "GBP/USD OTC", "USD/JPY OTC", "AUD/USD OTC", "NZD/USD OTC", 
            "USD/CAD OTC", "USD/CHF OTC", "EUR/GBP OTC", "EUR/JPY OTC", "GBP/JPY OTC", 
            "AUD/JPY OTC", "CHF/JPY OTC", "CAD/JPY OTC", "NZD/JPY OTC", "EUR/AUD OTC", 
            "EUR/CAD OTC", "GBP/AUD OTC", "GBP/CAD OTC", "AUD/CAD OTC", "AUD/NZD OTC", 
            "XAU/USD OTC", "XAG/USD OTC", "XRP/USD OTC", "BTC/USD OTC", "ETH/USD OTC", 
            "LTC/USD OTC", "BCH/USD OTC", "SOL/USD OTC", "MATIC/USD OTC", "DOT/USD OTC", 
            "Apple OTC", "Amazon OTC", "Google OTC", "Microsoft OTC", "Facebook OTC", 
            "Tesla OTC", "Netflix OTC", "Boeing OTC", "Disney OTC", "Intel OTC", 
            "McDonalds OTC", "Nike OTC", "Pfizer OTC", "Visa OTC", "Walmart OTC", 
            "Exxon OTC", "CocaCola OTC", "Pepsi OTC", "Chevron OTC", "JPMorgan OTC"
        ]
        asset = st.selectbox("Market Asset", otc_pairs)

    with col2:
        st.write("")
        st.write("")
        if st.button("🔍 RUN ANALYSIS"):
            conf = random.randint(70, 99)
            if conf >= 90: strength = "STRONG"
            elif conf >= 80: strength = "MODERATE"
            else: strength = "WEAK"
            
            st.session_state["conf"] = conf
            st.session_state["strength"] = strength
            st.session_state["last_signal"] = random.choice(["CALL (BUY)", "PUT (SELL)"])
            
            # TIME CALCULATIONS
            st.session_state["ready_t"] = (now + timedelta(seconds=15)).strftime("%H:%M:%S")

st.session_state["entry_t"] = (now + timedelta(minutes=2)).strftime("%H:%M:00")
            st.session_state["m1_t"] = (now + timedelta(minutes=4)).strftime("%H:%M:00")
            st.session_state["m2_t"] = (now + timedelta(minutes=6)).strftime("%H:%M:00")
            st.session_state["m3_t"] = (now + timedelta(minutes=8)).strftime("%H:%M:00")
    # 4. RESULTS DISPLAY
    if "last_signal" in st.session_state:
        st.divider()
        m_col1, m_col2 = st.columns(2)
        m_col1.metric("AI Confidence", f"{st.session_state['conf']}%")
        m_col2.metric("Signal Strength", st.session_state['strength'])
        
        signal_text = st.session_state["last_signal"]
        style = "buy-signal" if "BUY" in signal_text else "sell-signal"
        st.markdown(f'<div class="{style}">{signal_text}</div>', unsafe_allow_html=True)

        st.write("---")
        t_col1, t_col2 = st.columns(2)
        with t_col1:
            st.markdown(f'<div class="time-box"><p style="color:grey;margin:0;">Get Ready</p><h3>{st.session_state["ready_t"]}</h3></div>', unsafe_allow_html=True)
        with t_col2:
            st.markdown(f'<div class="time-box" style="border-color:#28A745;"><p style="color:grey;margin:0;">Entry Time</p><h3>{st.session_state["entry_t"]}</h3></div>', unsafe_allow_html=True)

        st.subheader("⚖️ Martingale Levels")
        st.write(f"Level 1: {st.session_state['m1_t']}")
        st.write(f"Level 2: {st.session_state['m2_t']}")
        st.write(f"Level 3: {st.session_state['m3_t']}") # FIXED: Level 3 is back!
    
    st.markdown('</div>', unsafe_allow_html=True)

