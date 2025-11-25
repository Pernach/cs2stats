import streamlit as st
from streamlit.web.server import Server
from datetime import datetime

st.subheader(body=str(datetime.now()))