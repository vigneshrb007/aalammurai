import streamlit as st
# from PIL import Image
# import pandas as pd
# import config
# from config import fetch_orders
# from config import insert_data_sql
# import base64



# if not st.session_state.get("logged_in", False):
#     st.switch_page("app.py")

st.title("Dashboard")
if "user_id" in st.session_state:
    st.write(f"Welcome User {st.session_state.user_id}")


if st.button("Logout"):
    st.session_state.clear()
    st.switch_page("app.py")



with st.container():
    st.write("-----")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About Me")
        st.write("Hi! I'm a passionate developer and data scientist. I enjoy working on projects that involve data analysis, machine learning, and web development.")
    with right_column:
        st.header("My Interests")
        st.write("I am interested in data science, machine learning, and web development.")
    #st.write("I am a data enthusiast who loves creating interactive web applications using Streamlit. I enjoy exploring data and sharing insights through visualizations.")


