import streamlit as st
from utils.state import get_state

st.set_page_config(page_title="MultiApp Demo", page_icon="🧭", layout="wide")

app_state = get_state()

st.title("🧭 Streamlit Multipage App")
st.write("Welcome! Use the left sidebar to navigate between pages.")

# Quick links to pages via query params (optional)
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Go to Dashboard"):
        st.switch_page("pages/1_📊_Dashboard.py")
with col2:
    if st.button("Go to Form"):
        st.switch_page("pages/2_📝_Form_Input.py")
with col3:
    if st.button("Go to Settings"):
        st.switch_page("pages/3_⚙️_Settings.py")

# Example: Set a default username once
if app_state['username'] is None:
    app_state['username'] = "guest"
    st.info("Default user set to 'guest' (change it in Settings).")

st.markdown("---")
st.subheader("Tips")
st.markdown("""
- Edit files in the `pages/` folder to add new pages.
- Use `st.session_state` (or a helper) to share state.
- Cache expensive operations with `@st.cache_data`.
""")