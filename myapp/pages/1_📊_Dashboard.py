import streamlit as st
from utils.state import get_state
import pandas as pd
import numpy as np

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")
app_state = get_state()

st.title("📊 Dashboard")
st.caption(f"Hello, **{app_state['username']}**!")

@st.cache_data(show_spinner=False)
def load_data(rows=2000, seed=42):
    rng = np.random.default_rng(seed)
    df = pd.DataFrame({
        "category": rng.choice(list("ABCDE"), size=rows),
        "value": rng.normal(100, 15, size=rows).round(2),
        "score": rng.uniform(0, 1, size=rows).round(3),
    })
    return df

df = load_data()

# Apply a simple filter from global state
active_cats = app_state['filters'].get('categories', list("ABCDE"))

left, right = st.columns([2, 5])
with left:
    st.subheader("Filters")
    selected = st.multiselect("Categories", options=list("ABCDE"), default=active_cats)
    if st.button("Apply Filters"):
        app_state['filters']['categories'] = selected
        st.success("Filters updated.")

with right:
    st.subheader("Overview")
    filtered = df[df['category'].isin(active_cats)]
    st.metric("Rows", len(filtered))
    st.bar_chart(filtered.groupby('category')['value'].mean())

    with st.expander("Data Preview"):
        st.dataframe(filtered.head(20), use_container_width=True)