import streamlit as st
import mysql.connector
from page import *
db=mysql.connector.connect(host="bakgs4ewc5wjhjigbt9w-mysql.services.clever-cloud.com",user="u6yovg764kskss2z",password="iWSZjK9HdgGfMmdZEUJp",database="bakgs4ewc5wjhjigbt9w")
c=db.cursor()
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
