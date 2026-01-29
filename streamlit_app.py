import streamlit as st

# 1. BEAUTIFUL STYLING (The CSS)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0e1117 0%, #1a1c24 100%);
    }
    h1 {
        color: #00FFC8;
        text-shadow: 0px 0px 15px #00FFC8;
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
    }
    .stButton>button {
        background-color: #00FFC8 !important;
        color: #000000 !important;
        border-radius: 25px !important;
        border: none !important;
        font-weight: bold !important;
        width: 100%;
        transition: 0.3s;
    }
    .stButton>button:hover {
        box-shadow: 0px 0px 20px #00FFC8 !important;
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

# 2. THE APP CONTENT
st.title("💎 TradeSmartWith_Vicki")

# Login Check (This keeps your password working)
def check_password():
    if "password_correct" not in st.session_state:
        st.text_input("Approved Email", key="email")
        st.text_input("Password", type="password", key="password")
        if st.button("🚀 Enter Dashboard"):
            if st.session_state["vickynwa98@gmail.com"] in st.secrets["Nneoma1998*"] and \
               st.session_state["password"] == st.secrets["passwords"][st.session_state["email"]]:
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("❌ Access Denied")
        return False
    return True

if check_password():
    st.success("✅ Neural Link Established: Welcome Vicki")
    st.write("### 📈 Live Scanner Dashboard")
    st.info("Scanner is active. Looking for high-probability setups...")

