# 5. ANALYSIS PANEL
    if "sig" in st.session_state:
        st.divider()
        colA, colB, colC = st.columns(3)
        with colA: st.markdown(f'<div class="stat-box">AI Confidence<br><h2 style="color:#007BFF;">{st.session_state["conf"]}%</h2></div>', unsafe_allow_html=True)
        with colB: st.markdown(f'<div class="stat-box">Signal Strength<br><h2 style="color:#FFD700;">{st.session_state["strength"]}</h2></div>', unsafe_allow_html=True)
        with colC: st.markdown(f'<div class="stat-box">Market Trend<br><h2 style="color:#00ff88;">STABLE</h2></div>', unsafe_allow_html=True)

        st.write("")
        style = "buy-signal" if "CALL" in st.session_state["sig"] else "sell-signal"
        st.markdown(f'<div class="{style}">{st.session_state["sig"]}</div>', unsafe_allow_html=True)
        
        # 6. SCHEDULE & MARTINGALE
        st.subheader("⏰ Trading Schedule (2-Min Expiry)")
        t1, t2 = st.columns(2)
        t1.info(f"🔔 Get Ready Time: {st.session_state['ready_t']}")
        t2.success(f"🚀 First Entry (2m): {st.session_state['entry_t']}")
        
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
