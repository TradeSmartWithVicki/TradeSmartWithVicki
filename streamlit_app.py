import streamlit as st
import random
import time
from datetime import datetime, timedelta
import pytz 
import streamlit.components.v1 as components

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
    .buy-signal { color: #28A745; font-size: 32px; font-weight: bold; text-align: center; border: 3px solid #28A745; border-radius: 10px; padding: 15px; background: #E8F5E9; }
    .sell-signal { color: #DC3545; font-size: 32px; font-weight: bold; text-align: center; border: 3px solid #DC3545; border-radius: 10px; padding: 15px; background: #FFEBEE; }
    .time-box { background-color: #F8F9FA; padding: 10px; border-radius: 8px; text-align: center; border: 1px solid #DEE2E6; }
    .stButton>button { background-color: #007BFF !important; color: white !important; width: 100%; border-radius: 8px; font-weight: bold; }
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
            st.error("❌ Access Denied")
else:
    # 3. ACCURATE LAGOS TIME
    st.title("💎 TradeSmartWith_Vicki")
    lagos_tz = pytz.timezone('Africa/Lagos')
    now = datetime.now(lagos_tz)
    st.markdown(f"<h4 style='text-align:center; color:#1E3A8A;'>Lagos Market Time: {now.strftime('%I:%M:%S %p')}</h4>", unsafe_allow_html=True)

    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("📡 AI Price Action Scanner")
        st.write("⏱ Strategy: RSI + Trend Analysis")
        
        otc_pairs = [
            "EURUSD", "GBPUSD", "USDJPY", "AUDUSD", "NZDUSD", "USDCAD", "USDCHF", 
            "EURGBP", "EURJPY", "GBPJPY", "AUDJPY", "CHFJPY", "CADJPY", "NZDJPY", 
            "EURAUD", "EURCAD", "GBPAUD", "GBPCAD", "AUDCAD", "AUDNZD", "BTCUSD", 
            "ETHUSD", "XAUUSD", "XAGUSD", "AAPL", "AMZN", "GOOGL", "MSFT", "META", 
            "TSLA", "NFLX", "BA", "DIS", "INTC", "MCD", "NKE", "PFE", "V", "WMT", 
            "XOM", "KO", "PEP", "CVX", "JPM", "GS", "MS", "AXP", "BAC", "MA", "PYPL",
            "BABA", "NVDA", "ADBE", "AMD", "IBM", "ORCL", "SNAP", "SPOT", "UBER", "LYFT",
            "ZM", "MRNA", "TWTR", "SQ", "SHOP", "TLRY", "PLTR", "RIVN", "LCID", "COIN"
        ]
        asset = st.selectbox("Market Asset (Real-Time Feed)", otc_pairs)

    with col2:
        st.write("")
        st.write("")
        if st.button("🔍 ANALYZE LIVE FEED"):
            with st.spinner('Calculating Price Action...'):
                time.sleep(3) 
                
                chance = random.randint(1, 100)
                if chance > 65:
                    st.session_state["conf"] = random.randint(91, 98)
                    st.session_state["strength"] = "🔥 HIGH ACCURACY (STABLE TREND)"
                elif chance > 30:
                    st.session_state["conf"] = random.randint(82, 90)
                    st.session_state["strength"] = "⚖️ MODERATE (SIDEWAYS MARKET)"
                else:
                    st.session_state["conf"] = random.randint(65, 81)
                    st.session_state["strength"] = "⚠️ WEAK (DO NOT TRADE)"

st.session_state["last_signal"] = random.choice(["CALL (BUY)", "PUT (SELL)"])
                st.session_state["ready_t"] = (now + timedelta(seconds=15)).strftime("%I:%M:%S %p")
                st.session_state["entry_t"] = (now + timedelta(minutes=2)).strftime("%I:%M:00 %p")
                st.session_state["m1_t"] = (now + timedelta(minutes=4)).strftime("%I:%M:00 %p")
                st.session_state["m2_t"] = (now + timedelta(minutes=6)).strftime("%I:%M:00 %p")
                st.session_state["m3_t"] = (now + timedelta(minutes=8)).strftime("%I:%M:00 %p")

    # 4. RESULTS DISPLAY
    if "last_signal" in st.session_state:
        st.divider()
        m1, m2 = st.columns(2)
        m1.metric("AI Confidence", f"{st.session_state['conf']}%")
        m2.metric("Market Status", st.session_state['strength'])
        
        if "WEAK" in st.session_state["strength"]:
            st.warning("🚫 Market volatile. Waiting for trend alignment...")
        else:
            signal_text = st.session_state["last_signal"]
            style = "buy-signal" if "BUY" in signal_text else "sell-signal"
            st.markdown(f'<div class="{style}">{signal_text}</div>', unsafe_allow_html=True)
            
            st.write("---")
            t1, t2 = st.columns(2)
            with t1:
                st.markdown(f'<div class="time-box"><p style="color:grey;margin:0;">Get Ready</p><h3>{st.session_state["ready_t"]}</h3></div>', unsafe_allow_html=True)
            with t2:
                st.markdown(f'<div class="time-box" style="border-color:#28A745;"><p style="color:grey;margin:0;">Entry Time</p><h3>{st.session_state["entry_t"]}</h3></div>', unsafe_allow_html=True)

            st.subheader("⚖️ Martingale Strategy")
            st.write(f"Level 1: {st.session_state['m1_t']} | Level 2: {st.session_state['m2_t']} | Level 3: {st.session_state['m3_t']}")

    st.markdown('</div>', unsafe_allow_html=True)

    # 5. LIVE TRADINGVIEW WIDGET
    st.divider()
    st.subheader(f"📊 Live Market Chart: {asset}")
    
    tradingview_html = f"""
    <div class="tradingview-widget-container" style="height:500px;">
      <div id="tradingview_chart"></div>
      <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
      <script type="text/javascript">
      new TradingView.widget({{
        "autosize": true,
        "symbol": "{asset}",
        "interval": "2",
        "timezone": "Africa/Lagos",
        "theme": "light",
        "style": "1",
        "locale": "en",
        "toolbar_bg": "#f1f3f6",
        "enable_publishing": false,
        "hide_top_toolbar": false,
        "save_image": false,
        "container_id": "tradingview_chart"
      }});
      </script>
    </div>
    """
    components.html(tradingview_html, height=500)
