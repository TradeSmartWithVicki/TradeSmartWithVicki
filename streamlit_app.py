import streamlit as st

# Beautiful Styling
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0e1117 0%, #1a1c24 100%); }
    h1 { color: #00FFC8; text-shadow: 0px 0px 15px #00FFC8; text-align: center; }
    .stButton>button { background-color: #00FFC8 !important; color: black !important; border-radius: 20px; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("💎 TradeSmartWith_Vicki")

# Check if the "passwords" section even exists in Secrets
if "passwords" not in st.secrets:
    st.error("🚨 System Error: The 'passwords' section is missing from your Streamlit Secrets box.")
    st.info("Go to Streamlit Settings > Secrets and make sure it starts with [passwords]")
else:
    if "password_correct" not in st.session_state:
        email_input = st.text_input("Approved Email")
        pass_input = st.text_input("Password", type="password")
        
        if st.button("🚀 Enter Dashboard"):
            # Check if email exists in our secrets list
            if email_input in st.secrets["passwords"]:
                if pass_input == st.secrets["passwords"][email_input]:
                    st.session_state["password_correct"] = True
                    st.rerun()
                else:
                    st.error("❌ Incorrect Password")
            else:
                st.error("❌ Email not recognized")
    else:
        st.success("✅ Welcome back, Vicki!")
        st.write("### 📈 Live Scanner Active")
