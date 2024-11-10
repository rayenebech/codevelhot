import streamlit as st

st.set_page_config(
    page_title="CodeVelhot Junction 2024",
    page_icon="📜",
    layout= "wide",
    )

st.title("Zero Friction powered by CodeVelhot.")
st.sidebar.success('Solutions to empower digital democracy.')

st.image('pages/background.jpeg')
# tab1, tab2 = st.tabs(["📈 Multimodal Polis", "🗃 Data"])

st.page_link("pages/Multimodal_Polis.py", label='Start!')