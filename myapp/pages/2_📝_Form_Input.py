import streamlit as st
from utils.state import get_state
import pandas as pd

st.set_page_config(page_title="Form Input", page_icon="📝", layout="centered")
app_state = get_state()

st.title("📝 Form Input")
st.caption("Submit a record; it persists in the session until app reload.")

with st.form("record_form", clear_on_submit=True):
    name = st.text_input("Name", value=app_state['username'] or "")
    category = st.selectbox("Category", options=list("ABCDE"))
    value = st.number_input("Value", min_value=0.0, max_value=1000.0, value=100.0, step=1.0)
    submitted = st.form_submit_button("Save")

if submitted:
    app_state['username'] = name or "guest"
    row = {"name": app_state['username'], "category": category, "value": value}
    if app_state['data'] is None:
        app_state['data'] = pd.DataFrame(columns=row.keys())
    app_state['data'] = pd.concat([app_state['data'], pd.DataFrame([row])], ignore_index=True)
    st.success("Saved!")

st.markdown("---")
st.subheader("Session Data")
st.dataframe(app_state['data'] if app_state['data'] is not None else pd.DataFrame(), use_container_width=True)