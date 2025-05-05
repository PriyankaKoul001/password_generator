import streamlit as st
import requests
import webbrowser

# --- Sidebar content ---
st.sidebar.title("🔐 About This App")
st.sidebar.markdown("""
Welcome to the Advanced Password Generator!  
Customize the type and strength of your password by selecting how many uppercase, lowercase, digits, and special characters you want.

Built using **FastAPI** + **Streamlit**.
""")

# --- Profile Links in Sidebar ---
st.sidebar.markdown("### Connect with Me:")
st.sidebar.markdown("""
<a href="https://www.linkedin.com/in/priyanka-koul-a5b1a5361/" target="_blank">
    <button style="background-color:#e63946; color:white; padding:8px 16px; border:none; border-radius:5px; margin-bottom:10px; width:100%;">
        🌐 LinkedIn
    </button>
</a>
<a href="https://github.com/PriyankaKoul001" target="_blank">
    <button style="background-color:#e63946; color:white; padding:8px 16px; border:none; border-radius:5px; width:100%;">
        💻 GitHub
    </button>
</a>
""", unsafe_allow_html=True)
# --- Footer ---
st.sidebar.markdown("""
    <hr style="margin-top: 50px;">
    <div style="text-align: center; color: grey; font-size: 0.9em;">
        Made with 💖 by <a href="https://www.linkedin.com/in/priyanka-koul-a5b1a5361/" target="_blank" style="text-decoration: none; color: #e63946;"><strong>Priyanka Koul</strong></a>
    </div>
""", unsafe_allow_html=True)


# --- Main content ---
st.title("Advanced Password Generator 🔑")
st.header("🔧 Customize Your Password")

# --- Inputs ---
length = st.number_input("Total Password Length", min_value=4, value=12)
uppercase = st.number_input("Uppercase Letters", min_value=0, value=2)
lowercase = st.number_input("Lowercase Letters", min_value=0, value=2)
digits = st.number_input("Digits", min_value=0, value=2)
special = st.number_input("Special Characters", min_value=0, value=2)

# --- Generate Password Button ---
if st.button("Generate Password"):
    params = {
        "length": length,
        "uppercase": uppercase,
        "lowercase": lowercase,
        "digits": digits,
        "special": special
    }

    try:
        response = requests.get("https://password-generator-n53d.onrender.com/generate-password", params=params)
        if response.status_code == 200:
            st.session_state.password = response.json()["password"]
        else:
            st.error(response.json()["detail"])
    except Exception as e:
        st.error(f"Something went wrong: {e}")

# --- Show Password if Available ---
if "password" in st.session_state:
    st.code(st.session_state.password, language="text")

