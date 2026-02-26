import streamlit as st
from utils.state import get_state

st.set_page_config(page_title="Settings", page_icon="⚙️")
app_state = get_state()

st.title("⚙️ Settings")
st.caption("Manage user and theme. (Theme changes reflect after rerun)")

username = st.text_input("Username", value=app_state['username'] or "guest")
theme = st.selectbox("Theme", options=["light", "dark"], index=0 if app_state['theme']=="light" else 1)

if st.button("Save Settings"):
    app_state['username'] = username.strip() or "guest"
    app_state['theme'] = theme
    st.success("Settings saved.")

st.button("Reset Session", on_click=lambda: st.session_state.clear())