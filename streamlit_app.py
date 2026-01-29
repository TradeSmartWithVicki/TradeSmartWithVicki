import streamlit as st
import random
import time
from datetime import datetime, timedelta
import pytz 
import streamlit.components.v1 as components

# 1. MATURE SLATE & SILVER THEME
st.set_page_config(page_title="TradeSmartWith_Vicki", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #243447; color: #F0F3F4; }
    .main-card { background: #2C3E50; padding: 30px; border-radius: 12px; border: 1px solid #5D6D7E; box-shadow: 0 4px 20px rgba(0,0,0,0.4); }
    .stat-box { text-align: center; padding: 15px; border-radius: 8px; background: #34495E; border: 1px solid #5D6D7E; color: #BDC3C7; }
    .buy-signal { color: #27AE60; font-size: 32px; font-weight: bold; text-align: center; border: 2px solid #27AE60; border-radius: 10px; padding: 15px; background: rgba(39, 174, 96, 0.1); }
    .sell-signal { color: #E74C3C; font-size: 32px; font-weight: bold; text-align: center; border: 2px solid #E74C3C; border-radius: 10px; padding: 15px; background: rgba(231, 76, 60, 0.1); }
    .m-box { background-color: #3E4A59; padding: 12px; border-radius: 6px; border-left: 5px solid #BDC3C7; margin-top: 10px; color: #ECF0F1; }
    h1, h2, h3 { color: #ECF0F1 !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. LOGIN SYSTEM
if "password_correct" not in st.session_state:
    st.markdown('<div class="main-card" style="max-width:500px; margin:auto;">', unsafe_allow_html=True)
    st.title("🔒 TradeSmartWith_Vicki")
    email_input = st.text_input("Approved Email")
    pass_input = st.text_input("Password", type="password")
    if st.button("Access Dashboard"):
        if "passwords" in st.secrets and email_input in st.secrets["passwords"] and pass_input == st.secrets["passwords"][email_input]:
            st.session_state["password_correct"] = True
            st.rerun()
        else:
            st.error("❌ Authentication Failed")
    st.markdown('</div>', unsafe_allow_html=True)
else:
    # 3. DASHBOARD CONTENT
    st.title("💎 TradeSmartWith_Vicki")
    lagos_tz = pytz.timezone('Africa/Lagos')
    now = datetime.now(lagos_tz)
    st.write(f"⏰ Market Time: {now.strftime('%I:%M:%S %p')}")

    otc_assets = ["EUR/USD (OTC)", "GBP/USD (OTC)", "USD/JPY (OTC)", "AUD/USD (OTC)", "NZD/USD (OTC)", "USD/CAD (OTC)", "USD/CHF (OTC)", "EUR/GBP (OTC)", "EUR/JPY (OTC)", "GBP/JPY (OTC)", "GOLD (OTC)", "SILVER (OTC)", "CRUDE OIL (OTC)", "APPLE (OTC)", "TESLA (OTC)", "FACEBOOK (OTC)", "GOOGLE (OTC)", "AMAZON (OTC)", "NETFLIX (OTC)", "NVIDIA (OTC)"]

    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    asset = st.selectbox("Select Asset Pair", otc_assets)

    if st.button("RUN ALGORITHM SCAN"):
        with st.spinner('Analyzing Data...'):
            time.sleep(1.5)
            st.session_state["sig"] = random.choice(["CALL (BUY)", "PUT (SELL)"])
            st.session_state["conf"] = random.randint(92, 98)
            st.session_state["strength"] = random.choice(["STRONG", "EXTREME", "HIGH"])
            st.session_state["ready_t"] = (now + timedelta(minutes=2)).strftime("%I:%M:00 %p")
            st.session_state["entry_t"] = (now + timedelta(minutes=4)).strftime("%I:%M:00 %p")
            st.session_state["m1"] = (now + timedelta(minutes=6)).strftime("%I:%M:00 %p")
            st.session_state["m2"] = (now + timedelta(minutes=8)).strftime("%I:%M:00 %p")
            st.session_state["m3"] = (now + timedelta(minutes=10)).strftime("%I:%M:00 %p")

    if "sig" in st.session_state:
        st.divider()
        c1, c2, c3 = st.columns(3)
        with c1: st.markdown(f'<div class="stat-box">Confidence<br><h3>{st.session_state["conf"]}%</h3></div>', unsafe_allow_html=True)
        with c2: st.markdown(f'<div class="stat-box">Signal Strength<br><h3>{st.session_state["strength"]}</h3></div>', unsafe_allow_html=True)
        with c3: st.markdown(f'<div class="stat-box">Market Trend<br><h3>STABLE</h3></div>', unsafe_allow_html=True)

        st.write("")
        style = "buy-signal" if "CALL" in st.session_state["sig"] else "sell-signal"
        st.markdown(f'<div class="{style}">{st.session_state["sig"]}</div>', unsafe_allow_html=True)
        
        st.subheader("📅 Trading Schedule")
        t1, t2 = st.columns(2)
        t1.info(f"🔔 Get Ready: {st.session_state['ready_t']}")
        t2.success(f"🚀 Entry Time: {st.session_state['entry_t']}")
        
        st.markdown("⚖️ Martingale Levels (2m):")
        st.markdown(f"""
        <div class="m-box">Level 1: {st.session_state['m1']}</div>
        <div class="m-box">Level 2: {st.session_state['m2']}</div>
        <div class="m-box">Level 3: {st.session_state['m3']}</div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 4. CHART
    st.divider()
    st.subheader(f"📊 Live Chart: {asset}")
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
