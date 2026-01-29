import streamlit as st
import random
import time
from datetime import datetime, timedelta
import pytz 
import streamlit.components.v1 as components

# All code must start at the very edge of the left side (no spaces)
st.set_page_config(page_title="TradeSmart Martingale-Elite", layout="wide")

if "password_correct" not in st.session_state:
    st.title("🔐 IQ-Blitz Elite Access")
    # ... (rest of your login code)
