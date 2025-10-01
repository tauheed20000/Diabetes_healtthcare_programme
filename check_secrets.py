import streamlit as st

st.write("Testing Streamlit secrets...")

# Print only whether the key exists (not the value, for safety)
if "GEMINI_API_KEY" in st.secrets:
    st.success("✅ GEMINI_API_KEY found in secrets.toml!")
else:
    st.error("❌ GEMINI_API_KEY NOT found. Check your .streamlit/secrets.toml file.")
