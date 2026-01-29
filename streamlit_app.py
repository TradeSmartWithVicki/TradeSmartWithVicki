import streamlit as st

# 1. BRIGHTER, VIBRANT STYLING (No more "too dark")
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; } /* Slightly lighter deep navy */
    h1 { color: #00FFC8; text-shadow: 0px 0px 10px #00FFC8; text-align: center; }
    
    /* Neon Cards for readability */
    .metric-container {
        background: #1A1C24;
        border-radius: 15px;
        padding: 20px;
        border: 1px solid #00FFC8;
        box-shadow: 0px 0px 15px rgba(0, 255, 200, 0.2);
    }
    
    /* Bright Button */
    .stButton>button {
        background: linear-gradient(90deg, #00FFC8, #00D1FF) !important;
        color: #000 !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        height: 3.5em !important;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. APP LOGIC
if "password_correct" not in st.session_state:
    st.title("🔐 ELITE ACCESS")
    # ... (Login check remains the same)
else:
    st.title("💎 TradeSmart Elite Scanner")
    
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("📡 AI OTC SCANNER")
        
        # Adding Timeframes as requested
        m_asset = st.selectbox("Market Asset", ["XRP/USD OTC", "EUR/USD OTC", "BTC/USD", "GOLD"])
        t_frame = st.selectbox("Timeframe", ["1-Minute", "5-Minute", "15-Minute", "1-Hour"])
        
        if st.button("🚀 START SCAN"):
            st.balloons()
            st.write(f"### Result: {m_asset} ({t_frame})")
            st.success("🎯 SIGNAL FOUND: STRONG BUY")

    with col2:
        st.subheader("⚖️ Martingale Levels")
        base = st.number_input("Base Stake", value=100.0) # Removed $ sign label
        
        # Displaying amounts clearly without the $ sign
        for i in range(1, 4):
            amt = base * (2.2 ** (i-1))
            st.markdown(f"""
                <div style="background:#1A1C24; padding:10px; border-radius:10px; margin-bottom:10px; border-left: 4px solid #FFD700;">
                    <span style="color:grey">Level {i}</span><br>
                    <span style="color:#00FFC8; font-size:20px; font-weight:bold;">{amt:,.0f}</span>
                </div>
            """, unsafe_allow_html=True)
