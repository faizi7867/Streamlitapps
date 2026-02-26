import streamlit as st

def get_state():
    if 'app' not in st.session_state:
        st.session_state.app = {
            'theme': 'light',
            'username': None,
            'filters': {},
            'data': None,
        }
    return st.session_state.app