import streamlit as st
import config
import pandas as pd
from config import fetch_orders
from config import insert_data_sql
import extra_streamlit_components as stx
import datetime
import time
from streamlit_local_storage import LocalStorage

localS = LocalStorage()


# Read
user_id = localS.getItem("user_id")
storename = localS.getItem("storename")
st.write(f"Welcome User {user_id}")
st.write(f"Store Name: {storename}")



if st.button("Logout"):
    localS.deleteItem("user_id", key="user_id_storage")
    localS.deleteItem("storename", key="storename_storage")
    time.sleep(1)
    st.switch_page("app.py")





# conn = sqlite3.connect("app.db")
# cur = conn.cursor()

# cur.execute("""
# CREATE TABLE IF NOT EXISTS session_data (
#     key TEXT PRIMARY KEY,
#     value TEXT
# )
# """)



# st.title("Dashboard")
# if "user_id" in st.session_state:
#     st.write(f"Welcome User {st.session_state.user_id}")
#     user_id = st.session_state.user_id
#     cur.execute(
#     "INSERT OR REPLACE INTO session_data VALUES (?, ?)",
#         ("username", user_id)
#     )
#     conn.commit()
#     st.write(f"The store name is {st.session_state.store_name}")
    












# if st.button("Load"):
#     cur.execute(
#         "SELECT value FROM session_data WHERE key=?",
#         ("username",)
#     )
#     row = cur.fetchone()
#     if row:
#         st.write(row[0])

# conn.close()































# with st.container():
#     st.write("-----")
#     left_column, right_column = st.columns(2)
#     with left_column:
#         st.header("About Me")
#         st.write("Hi! I'm a passionate developer and data scientist. I enjoy working on projects that involve data analysis, machine learning, and web development.")
#     with right_column:
#         st.header("My Interests")
#         st.write("I am interested in data science, machine learning, and web development.")
#     #st.write("I am a data enthusiast who loves creating interactive web applications using Streamlit. I enjoy exploring data and sharing insights through visualizations.")


