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
