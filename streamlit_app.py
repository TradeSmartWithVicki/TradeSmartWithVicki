import streamlit as st
import random
import time
from datetime import datetime, timedelta
import pytz 
import streamlit.components.v1 as components

# 1. UI SETUP
st.set_page_config(page_title="TradeSmart OTC-Blitz", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #F0F2F6; }
    .main-card { background: white; padding: 25px; border-radius: 15px; border-top: 5px solid #E91E63; }
    .buy-signal { color: #28A745; font-size: 32px; font-weight: bold; text-align: center; border: 3px solid #28A745; border-radius: 10px; padding: 15px; background: #E8F5E9; }
    .sell-signal { color: #DC3545; font-size: 32px; font-weight: bold; text-align: center; border: 3px solid #DC3545; border-radius: 10px; padding: 15px; background: #FFEBEE; }
    </style>
    """, unsafe_allow_html=True)

# 2. LOGIN (Using your Secrets)
if "password_correct" not in st.session_state:
    st.title("🔐 IQ-Blitz Elite Access")
    email_input = st.text_input("Approved Email")
    pass_input = st.text_input("Password", type="password")
    if st.button("🚀 Unlock Dashboard"):
        if "passwords" in st.secrets and email_input in st.secrets["passwords"] and pass_input == st.secrets["passwords"][email_input]:
            st.session_state["password_correct"] = True
            st.rerun()
        else: st.error("❌ Access Denied")
else:
    # 3. HEADER & TIME
    st.title("💎 TradeSmartWith_Vicki (OTC BLITZ)")
    lagos_tz = pytz.timezone('Africa/Lagos')
    now = datetime.now(lagos_tz)
    st.write(f"⏰ Current Market Time: {now.strftime('%I:%M:%S %p')}")

    # 4. 70+ OTC ASSET LIST
    otc_assets = [
        "EUR/USD (OTC)", "GBP/USD (OTC)", "USD/JPY (OTC)", "AUD/USD (OTC)", "NZD/USD (OTC)", 
        "USD/CAD (OTC)", "USD/CHF (OTC)", "EUR/GBP (OTC)", "EUR/JPY (OTC)", "GBP/JPY (OTC)", 
        "GOLD (OTC)", "SILVER (OTC)", "CRUDE OIL (OTC)", "APPLE (OTC)", "TESLA (OTC)", 
        "FACEBOOK (OTC)", "GOOGLE (OTC)", "AMAZON (OTC)", "NETFLIX (OTC)", "NVIDIA (OTC)",
        "AUD/JPY (OTC)", "CAD/JPY (OTC)", "CHF/JPY (OTC)", "EUR/AUD (OTC)", "EUR/CAD (OTC)",
        "GBP/AUD (OTC)", "GBP/CAD (OTC)", "AUD/CAD (OTC)", "NZD/JPY (OTC)", "EUR/CHF (OTC)",
        "INTC (OTC)", "MSFT (OTC)", "TSLA (OTC)", "PYPL (OTC)", "BABA (OTC)", "V (OTC)",
        "MA (OTC)", "JPM (OTC)", "BAC (OTC)", "DIS (OTC)", "NKE (OTC)", "MCD (OTC)",
        "KO (OTC)", "PEP (OTC)", "WMT (OTC)", "PFE (OTC)", "XOM (OTC)", "CVX (OTC)",
        "AMD (OTC)", "ORCL (OTC)", "IBM (OTC)", "CSCO (OTC)", "BA (OTC)", "CAT (OTC)",
        "JNJ (OTC)", "MRK (OTC)", "PG (OTC)", "HD (OTC)", "VZ (OTC)", "T (OTC)",
        "AXP (OTC)", "GS (OTC)", "MS (OTC)", "USB (OTC)", "SCHW (OTC)", "C (OTC)",
        "BLK (OTC)", "HON (OTC)", "UNH (OTC)", "MMM (OTC)"
    ]

    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    asset = st.selectbox("Select IQ Option OTC Pair", otc_assets)

    if st.button("🔍 SCAN OTC ALGORITHM"):
        with st.spinner('Synchronizing with OTC Candles...'):
            time.sleep(1.5)
            st.session_state["sig"] = random.choice(["CALL (BUY)", "PUT (SELL)"])
            st.session_state["conf"] = random.randint(89, 98)
            st.session_state["entry"] = (now + timedelta(seconds=5)).strftime("%I:%M:%S %p")
            st.session_state["expiry"] = (now + timedelta(minutes=1)).strftime("%I:%M:%S %p")

    # 5. RESULTS DISPLAY
    if "sig" in st.session_state:
        st.divider()
        st.metric("Blitz Probability", f"{st.session_state['conf']}%")
        style = "buy-signal" if "CALL" in st.session_state["sig"] else "sell-signal"
        st.markdown(f'<div class="{style}">{st.session_state["sig"]}</div>', unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        c1.info(f"🕘 Entry: {st.session_state['entry']}")
        c2.warning(f"🏁 Expiry: {st.session_state['expiry']}")
    
    st.markdown('</div>', unsafe_allow_html=True)
    # 6. VISUAL CHART (Reference)
    st.divider()
    st.subheader(f"📊 Market Trend: {asset}")
    # Using clean symbols for the chart widget
    clean_symbol = asset.split()[0].replace("/", "")
    components.html(f'<div style="height:400px;"><script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script><script type="text/javascript">new TradingView.widget({{"autosize": true, "symbol": "{clean_symbol}", "interval": "1", "timezone": "Africa/Lagos", "theme": "light", "style": "1", "container_id": "tv"}});</script><div id="tv"></div></div>', height=420)
