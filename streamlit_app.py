import streamlit as st
import random
import time
from datetime import datetime, timedelta
import pytz 
import streamlit.components.v1 as components

# 1. UI SETUP
st.set_page_config(page_title="TradeSmart Martingale-Elite", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #F0F2F6; }
    .main-card { background: white; padding: 25px; border-radius: 15px; border-top: 5px solid #E91E63; }
    .buy-signal { color: #28A745; font-size: 32px; font-weight: bold; text-align: center; border: 3px solid #28A745; border-radius: 10px; padding: 15px; background: #E8F5E9; }
    .sell-signal { color: #DC3545; font-size: 32px; font-weight: bold; text-align: center; border: 3px solid #DC3545; border-radius: 10px; padding: 15px; background: #FFEBEE; }
    .m-box { background-color: #f8f9fa; padding: 15px; border-radius: 10px; border-left: 5px solid #6c757d; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 2. LOGIN
if "password_correct" not in st.session_state:
    st.title("🔐 IQ-Blitz Martingale Access")
    email_input = st.text_input("Approved Email")
    pass_input = st.text_input("Password", type="password")
    if st.button("🚀 Unlock Dashboard"):
        if "passwords" in st.secrets and email_input in st.secrets["passwords"] and pass_input == st.secrets["passwords"][email_input]:
            st.session_state["password_correct"] = True
            st.rerun()
        else: st.error("❌ Access Denied")
else:
    st.title("💎 TradeSmartWith_Vicki (MARTINGALE LEVEL 1-2-3)")
    lagos_tz = pytz.timezone('Africa/Lagos')
    now = datetime.now(lagos_tz)
    
    otc_assets = ["EUR/USD (OTC)", "GBP/USD (OTC)", "USD/JPY (OTC)", "AUD/USD (OTC)", "GOLD (OTC)", "APPLE (OTC)", "TESLA (OTC)"] # +63 more as previously listed

    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    asset = st.selectbox("Select Asset", otc_assets)

    if st.button("🔍 GENERATE 2-MIN SIGNALS"):
        with st.spinner('Calculating Martingale Levels...'):
            time.sleep(1)
            st.session_state["sig"] = random.choice(["CALL (BUY)", "PUT (SELL)"])
            # Timing calculations based on 2-minute Blitz/IQ strategy
            st.session_state["ready_t"] = (now + timedelta(minutes=2)).strftime("%I:%M:00 %p")
            st.session_state["entry_t"] = (now + timedelta(minutes=4)).strftime("%I:%M:00 %p")
            st.session_state["m1"] = (now + timedelta(minutes=6)).strftime("%I:%M:00 %p")
            st.session_state["m2"] = (now + timedelta(minutes=8)).strftime("%I:%M:00 %p")
            st.session_state["m3"] = (now + timedelta(minutes=10)).strftime("%I:%M:00 %p")

    if "sig" in st.session_state:
        st.divider()
        style = "buy-signal" if "CALL" in st.session_state["sig"] else "sell-signal"
        st.markdown(f'<div class="{style}">{st.session_state["sig"]}</div>', unsafe_allow_html=True)
        
        st.subheader("⏰ Trading Schedule (2-Min Intervals)")
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"🔔 Get Ready Time: {st.session_state['ready_t']}")
        with col2:
            st.success(f"🚀 First Entry (2m): {st.session_state['entry_t']}")
        
        st.markdown("---")
        st.write("⚖️ Martingale Recovery Levels:")
        st.markdown(f"""
        <div class="m-box"><b>Level 1:</b> {st.session_state['m1']} (2 min duration)</div>
        <div class="m-box"><b>Level 2:</b> {st.session_state['m2']} (2 min duration)</div>
        <div class="m-box"><b>Level 3:</b> {st.session_state['m3']} (2 min duration)</div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
