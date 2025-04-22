import streamlit as st
import requests
import webbrowser

# --- Sidebar content ----
st.sidebar.title("🔐 About This App")
st.sidebar.markdown("""
Welcome to the Advanced Password Generator!  
Customize the type and strength of your password by selecting how many uppercase, lowercase, digits, and special characters you want.

Built using **FastAPI** + **Streamlit**.
""")

# --- Profile Links in Sidebar ---
st.sidebar.markdown("### Connect with Me:")
if st.sidebar.button("🌐 LinkedIn"):
    webbrowser.open_new_tab("https://www.linkedin.com/in/priyanka-koul-a5b1a5361/")

if st.sidebar.button("💻 GitHub"):
    webbrowser.open_new_tab("https://github.com/PriyankaKoul001")

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
        response = requests.get("http://localhost:8000/generate-password", params=params)
        if response.status_code == 200:
            st.session_state.password = response.json()["password"]
        else:
            st.error(response.json()["detail"])
    except Exception as e:
        st.error(f"Something went wrong: {e}")

# --- Show Password if Available ---
if "password" in st.session_state:
    st.code(st.session_state.password, language="text")

