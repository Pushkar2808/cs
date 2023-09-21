import streamlit as st
import mysql.connector
from page import *

page=st.session_state.get("page","login")
if page == "login":
            login()
elif page == "op":
        op()
elif page == "add stock":
        addstock()
elif page == "show stock":
        showstock()
elif page == "remove stock":
        removestock()
