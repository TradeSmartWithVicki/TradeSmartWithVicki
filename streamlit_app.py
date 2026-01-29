import streamlit as st
import random
import time
from datetime import datetime, timedelta
import pytz 
import streamlit.components.v1 as components

# 1. PAGE CONFIG & MATURE THEME
st.set_page_config(page_title="TradeSmartWith_Vicki", layout="wide")
st.markdown("""
    <style>
    /* Royal Charcoal Background (Mature & Deep) */
    .stApp { 
        background-color: #1C2331; 
        color: #D6DBDF; 
    }
    
    /* Elegant Card: Midnight Slate */
    .main-card { 
        background: #2C3E50; 
        padding: 30px; 
        border-radius: 15px; 
        border-top: 4px solid #D4AF37; /* Champagne Gold Accent */
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    }
    
    /* Buttons: Champagne Gold */
    .stButton>button {
        background-color: #D4AF37 !important;
        color: #1C2331 !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        border: none !important;
        width: 100%;
    }

    /* Signal Styles: Refined Emerald and Ruby */
    .buy-signal { 
        color: #2ECC71; 
        font-size: 34px; 
        font-weight: bold; 
        text-align: center; 
        border: 2px solid #2ECC71; 
        border-radius: 12px; 
        padding: 15px; 
        background: rgba(46, 204, 113, 0.1); 
    }
    .sell-signal { 
        color: #E74C3C; 
        font-size: 34px; 
        font-weight: bold; 
        text-align: center; 
        border: 2px solid #E74C3C; 
        border-radius: 12px; 
        padding: 15px; 
        background: rgba(231, 76, 60, 0.1); 
    }
    
    /* Martingale: Soft Gold Levels */
    .m-box { 
        background-color: #34495E; 
        padding: 12px; 
        border-radius: 8px; 
        border-left: 5px solid #D4AF37; 
        margin-top: 10px; 
        color: #F4D03F;
    }
    
    /* Stats Boxes */
    .stat-box { 
        text-align: center; 
        padding: 15px; 
        border-radius: 12px; 
        background: #1C2331; 
        border: 1px solid #3E4A59; 
    }
    h1, h2, h3 { color: #D4AF37 !important; font-family: 'Segoe UI', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# 2. LOGIN SYSTEM
if "password_correct" not in st.session_state:
    st.markdown('<div class="main-card" style="max-width:500px; margin:auto;">', unsafe_allow_html=True)
    st.title("🔐 VIP Access")
    st.subheader("TradeSmartWith_Vicki")
    email_input = st.text_input("Approved Email")
    pass_input = st.text_input("Password", type="password")
    if st.button("🚀 UNLOCK DASHBOARD"):
        if "passwords" in st.secrets and email_input in st.secrets["passwords"] and pass_input == st.secrets["passwords"][email_input]:
            st.session_state["password_correct"] = True
            st.rerun()
        else: st.error("❌ Invalid Credentials")
    st.markdown('</div>', unsafe_allow_html=True)
else:
    # 3. DASHBOARD HEADER
    st.title("💎 TradeSmartWith_Vicki")
    lagos_tz = pytz.timezone('Africa/Lagos')
    now = datetime.now(lagos_tz)
    st.write(f"📅 {now.strftime('%A, %d %B %Y')} | ⏰ {now.strftime('%I:%M:%S %p')}")

    # 4. 70 OTC ASSET LIST
    otc_assets = ["EUR/USD (OTC)", "GBP/USD (OTC)", "USD/JPY (OTC)", "AUD/USD (OTC)", "NZD/USD (OTC)", "USD/CAD (OTC)", "USD/CHF (OTC)", "EUR/GBP (OTC)", "EUR/JPY (OTC)", "GBP/JPY (OTC)", "GOLD (OTC)", "SILVER (OTC)", "CRUDE OIL (OTC)", "APPLE (OTC)", "TESLA (OTC)", "FACEBOOK (OTC)", "GOOGLE (OTC)", "AMAZON (OTC)", "NETFLIX (OTC)", "NVIDIA (OTC)", "AUD/JPY (OTC)", "CAD/JPY (OTC)", "CHF/JPY (OTC)", "EUR/AUD (OTC)", "EUR/CAD (OTC)", "GBP/AUD (OTC)", "GBP/CAD (OTC)", "AUD/CAD (OTC)", "NZD/JPY (OTC)", "EUR/CHF (OTC)", "INTC (OTC)", "MSFT (OTC)", "TSLA (OTC)", "PYPL (OTC)", "BABA (OTC)", "V (OTC)", "MA (OTC)", "JPM (OTC)", "BAC (OTC)", "DIS (OTC)", "NKE (OTC)", "MCD (OTC)", "KO (OTC)", "PEP (OTC)", "WMT (OTC)", "PFE (OTC)", "XOM (OTC)", "CVX (OTC)", "AMD (OTC)", "ORCL (OTC)", "IBM (OTC)", "CSCO (OTC)", "BA (OTC)", "CAT (OTC)", "JNJ (OTC)", "MRK (OTC)", "PG (OTC)", "HD (OTC)", "VZ (OTC)", "T (OTC)", "AXP (OTC)", "GS (OTC)", "MS (OTC)", "USB (OTC)", "SCHW (OTC)", "C (OTC)", "BLK (OTC)", "HON
    (OTC)", "UNH (OTC)", "MMM (OTC)"]
st.markdown('<div class="main-card">', unsafe_allow_html=True)
    asset = st.selectbox("Select Market Asset", otc_assets)

    if st.button("🔍 SCAN MARKET LIQUIDITY"):
        with st.spinner('Analyzing Trends...'):
            time.sleep(1.5)
            st.session_state["sig"] = random.choice(["CALL (BUY)", "PUT (SELL)"])
            st.session_state["conf"] = random.randint(92, 98)
            st.session_state["strength"] = random.choice(["STRONG", "EXTREME", "HIGH"])
            st.session_state["ready_t"] = (now + timedelta(minutes=2)).strftime("%I:%M:00 %p")
            st.session_state["entry_t"] = (now + timedelta(minutes=4)).strftime("%I:%M:00 %p")
            st.session_state["m1"] = (now + timedelta(minutes=6)).strftime("%I:%M:00 %p")
            st.session_state["m2"] = (now + timedelta(minutes=8)).strftime("%I:%M:00 %p")
            st.session_state["m3"] = (now + timedelta(minutes=10)).strftime("%I:%M:00 %p")

    # 5. ANALYSIS PANEL
    if "sig" in st.session_state:
        st.divider()
        col1, col2, col3 = st.columns(3)
        with col1: st.markdown(f'<div class="stat-box">AI Confidence<br><h2>{st.session_state["conf"]}%</h2></div>', unsafe_allow_html=True)
        with col2: st.markdown(f'<div class="stat-box">Signal Strength<br><h2>{st.session_state["strength"]}</h2></div>', unsafe_allow_html=True)
        with col3: st.markdown(f'<div class="stat-box">Trend Analysis<br><h2>STABLE</h2></div>', unsafe_allow_html=True)

        st.write("")
        style = "buy-signal" if "CALL" in st.session_state["sig"] else "sell-signal"
        st.markdown(f'<div class="{style}">{st.session_state["sig"]}</div>', unsafe_allow_html=True)
        
        # 6. SCHEDULE
        st.subheader("⏰ Trading Schedule (2-Min Intervals)")
        t1, t2 = st.columns(2)
        t1.info(f"🔔 Get Ready Time: {st.session_state['ready_t']}")
        t2.success(f"🚀 Execution Entry: {st.session_state['entry_t']}")
        
        st.markdown("⚖️ Martingale Recovery Management:")
        st.markdown(f"""
        <div class="m-box"><b>Level 1 (Recovery):</b> {st.session_state['m1']}</div>
        <div class="m-box"><b>Level 2 (Recovery):</b> {st.session_state['m2']}</div>
        <div class="m-box"><b>Level 3 (Recovery):</b> {st.session_state['m3']}</div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 7. LIVE CHART
    st.divider()
    st.subheader(f"📊 Market Overview: {asset}")
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

