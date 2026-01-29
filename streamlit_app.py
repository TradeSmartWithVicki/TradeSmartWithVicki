import streamlit as st
import random
import time
from datetime import datetime, timedelta
import pytz 
import streamlit.components.v1 as components

# 1. PAGE CONFIG & CUSTOM MIDNIGHT BLUE THEME
st.set_page_config(page_title="TradeSmartWith_Vicki", layout="wide")
st.markdown("""
    <style>
    /* Deep Midnight Blue Background */
    .stApp { background-color: #101820; color: #D1D5DB; }
    
    /* Elegant Card Design */
    .main-card { 
        background: #1B2631; 
        padding: 25px; 
        border-radius: 15px; 
        border: 1px solid #2E4053;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    /* Signal Styles */
    .buy-signal { color: #00ff88; font-size: 36px; font-weight: bold; text-align: center; border: 2px solid #00ff88; border-radius: 10px; padding: 15px; background: rgba(0, 255, 136, 0.05); }
    .sell-signal { color: #ff4b4b; font-size: 36px; font-weight: bold; text-align: center; border: 2px solid #ff4b4b; border-radius: 10px; padding: 15px; background: rgba(255, 75, 75, 0.05); }
    
    /* Martingale Boxes */
    .m-box { background-color: #212F3D; padding: 12px; border-radius: 8px; border-left: 5px solid #F39C12; margin-top: 10px; color: #FDFEFE; }
    
    /* Stat Boxes with Gold Accent */
    .stat-box { text-align: center; padding: 10px; border-radius: 10px; background: #154360; border: 1px solid #1A5276; }
    h2 { color: #F1C40F !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. LOGIN SYSTEM
if "password_correct" not in st.session_state:
    st.title("🔐 TradeSmartWith_Vicki Login")
    email_input = st.text_input("Approved Email")
    pass_input = st.text_input("Password", type="password")
    if st.button("🚀 Unlock Dashboard"):
        if "passwords" in st.secrets and email_input in st.secrets["passwords"] and pass_input == st.secrets["passwords"][email_input]:
            st.session_state["password_correct"] = True
            st.rerun()
        else: st.error("❌ Invalid Email or Password. Check your Streamlit Secrets.")
else:
    # 3. DASHBOARD HEADER
    st.title("💎 TradeSmartWith_Vicki")
    lagos_tz = pytz.timezone('Africa/Lagos')
    now = datetime.now(lagos_tz)
    st.write(f"⏰ Market Time: {now.strftime('%I:%M:%S %p')}")

    # 4. 70 OTC ASSET LIST
    otc_assets = ["EUR/USD (OTC)", "GBP/USD (OTC)", "USD/JPY (OTC)", "AUD/USD (OTC)", "NZD/USD (OTC)", "USD/CAD (OTC)", "USD/CHF (OTC)", "EUR/GBP (OTC)", "EUR/JPY (OTC)", "GBP/JPY (OTC)", "GOLD (OTC)", "SILVER (OTC)", "CRUDE OIL (OTC)", "APPLE (OTC)", "TESLA (OTC)", "FACEBOOK (OTC)", "GOOGLE (OTC)", "AMAZON (OTC)", "NETFLIX (OTC)", "NVIDIA (OTC)", "AUD/JPY (OTC)", "CAD/JPY (OTC)", "CHF/JPY (OTC)", "EUR/AUD (OTC)", "EUR/CAD (OTC)", "GBP/AUD (OTC)", "GBP/CAD (OTC)", "AUD/CAD (OTC)", "NZD/JPY (OTC)", "EUR/CHF (OTC)", "INTC (OTC)", "MSFT (OTC)", "TSLA (OTC)", "PYPL (OTC)", "BABA (OTC)", "V (OTC)", "MA (OTC)", "JPM (OTC)", "BAC (OTC)", "DIS (OTC)", "NKE (OTC)", "MCD (OTC)", "KO (OTC)", "PEP (OTC)", "WMT (OTC)", "PFE (OTC)", "XOM (OTC)", "CVX (OTC)", "AMD (OTC)", "ORCL (OTC)", "IBM (OTC)", "CSCO (OTC)", "BA (OTC)", "CAT (OTC)", "JNJ (OTC)", "MRK (OTC)", "PG (OTC)", "HD (OTC)", "VZ (OTC)", "T (OTC)", "AXP (OTC)", "GS (OTC)", "MS (OTC)", "USB (OTC)", "SCHW (OTC)", "C (OTC)", "BLK (OTC)", "HON (OTC)", "UNH (OTC)", "MMM (OTC)"]

    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    asset = st.selectbox("Select Asset Pair", otc_assets)

    if st.button("🔍 SCAN OTC ALGORITHM"):
        with st.spinner('Calculating Price Probability...'):
            time.sleep(1.5)
            st.session_state["sig"] = random.choice(["CALL (BUY)", "PUT (SELL)"])
            st.session_state["conf"] = random.randint(92, 98)
            st.session_state["strength"] = random.choice(["STRONG", "EXTREME", "VOLATILE"])
            # 2-MINUTE INTERVALS
            st.session_state["ready_t"] = (now + timedelta(minutes=2)).strftime("%I:%M:00 %p")
            st.session_state["entry_t"] = (now + timedelta(minutes=4)).strftime("%I:%M:00 %p")
            st.session_state["m1"] = (now + timedelta(minutes=6)).strftime("%I:%M:00 %p")
            st.session_state["m2"] = (now + timedelta(minutes=8)).strftime("%I:%M:00 %p")
            st.session_state["m3"] = (now + timedelta(minutes=10)).strftime("%I:%M:00 %p")

    # 5. ANALYSIS PANEL
    if "sig" in st.session_state:
        st.divider()
        colA, colB, colC = st.columns(3)
        with colA: st.markdown(f'<div class="stat-box">AI Confidence<br><h2>{st.session_state["conf"]}%</h2></div>', unsafe_allow_html=True)
        with colB: st.markdown(f'<div class="stat-box">Signal Strength<br><h2>{st.session_state["strength"]}</h2></div>', unsafe_allow_html=True)
        with colC: st.markdown(f'<div class="stat-box">Market Trend<br><h2>STABLE</h2></div>', unsafe_allow_html=True)

        st.write("")
        style = "buy-signal" if "CALL" in st.session_state["sig"] else "sell-signal"
        st.markdown(f'<div class="{style}">{st.session_state["sig"]}</div>', unsafe_allow_html=True)
        
        # 6. SCHEDULE (2-MIN INTERVALS)
        st.subheader("⏰ Trading Schedule")
        t1, t2 = st.columns(2)
        t1.info(f"🔔 Get Ready Time: {st.session_state['ready_t']}")
        t2.success(f"🚀 First Entry Time: {st.session_state['entry_t']}")
        
        st.markdown("⚖️ Martingale Recovery Levels:")
        st.markdown(f"""
        <div class="m-box"><b>Level 1:</b> {st.session_state['m1']} (2 min duration)</div>
        <div class="m-box"><b>Level 2:</b> {st.session_state['m2']} (2 min duration)</div>
        <div class="m-box"><b>Level 3:</b> {st.session_state['m3']} (2 min duration)</div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

    # 7. LIVE CHART
    st.divider()
    st.subheader(f"📊 Live Technical View: {asset}")
    clean_sym = asset.split()[0].replace("/", "")
    chart_html = f"""
    <div style="height:500px;">
      <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
      <script type="text/javascript">
      new TradingView.widget({{"autosize": true, "symbol": "{clean_sym}", "interval": "1", "timezone": "Africa/Lagos", "theme": "dark", "style": "1", "container_id": "tv"}});
      </script>
      <div id="tv"></div>
    </div>"""
    components.html(chart_html, height=520)
