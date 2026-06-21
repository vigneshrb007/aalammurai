import streamlit as st
import config
import pandas as pd
from config import fetch_orders
from config import insert_data_sql
import extra_streamlit_components as stx
import datetime
import time


cookie_manager = stx.CookieManager()


st.set_page_config(
    page_title="My App",
    initial_sidebar_state="collapsed"
)



# Page setup
# st.set_page_config(page_title="Web Layout Demo", layout="wide")




st.set_page_config(page_title="Login System")

if "user_id" in st.session_state:
    st.write(f"Welcome User {st.session_state.user_id}")



st.title("Login")
username = st.text_input("Mobile No.")
password = st.text_input("Password", type="password")



if st.button("Login"):

    if not username or not password:
        st.error("Please enter both username and password")
    else:
        # # Call the function
        qurry = f"SELECT ID, STORENAME FROM USERS WHERE MOBILENO = '{username}' AND PASSWORD = '{password}'"
        df = fetch_orders(qurry)

        # Display results
        if not df.empty and df.iloc[0, 0] > 0:
            st.session_state.logged_in = True
            st.session_state.user_id = username
            st.session_state.store_name = df.iloc[0, 1]  # Assuming STORENAME is the second column
            st.success("Login successful!")
                # Redirect to another page
            st.switch_page("pages/page_2.py")
        else:
            st.error("Invalid credentials")
















# if st.button("Login"):

#     if not username or not password:
#         st.error("Please enter both username and password")
#     else:
#         # # Call the function
#         qurry = f"SELECT ISNULL(ID,0) AS RST FROM USERS WHERE MOBILENO = '{username}' AND PASSWORD = '{password}'"
#         df = fetch_orders(qurry)

#         # Display results
#         if not df.empty and df.iloc[0, 0] > 0:
#             cookie_manager.set("user_id",username)
#             st.success("Login successful!")
#                 # Redirect to another page
#             st.switch_page("pages/page_2.py")
            
#         else:
#             st.error("Invalid credentials")





# qurry = "SELECT ID FROM USERS WHERE MOBILENO = '9791037237' AND PASSWORD = '12345'"
# df = fetch_orders(qurry)
# st.write(df)




# st.title("Products Page")
# if st.button("Go to Cart"):
#     st.switch_page("pages/page_2.py")






# st.image("D:\python\surya\images\AM_Kaali_page-0001.jpg")










# # Call the function
# qurryu = "INSERT INTO TEST_INSERT (SOME_TEXT) VALUES('GRAPE')"
# #qurryu = "UPDATE TEST_INSERT SET SOME_TEXT = 'CAHNGE' WHERE SOME_TEXT = 'APPLE'"
# dfu = insert_data_sql(qurryu)
# # Display results


# --------------------------------

# # Call the function
# qurry = "SELECT TOP 10 ID, NAME FROM ORDERS ORDER BY ID"
# df = fetch_orders(qurry)
# # Display results
# st.dataframe(df)


# # Call the function
# qurryu = "SELECT * FROM TEST_INSERT ORDER BY ID"
# dfu = fetch_orders(qurryu)
# # Display results
# st.dataframe(dfu)





















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



# with st.container():
#     st.write("-----")
#     st.header("My Projects")
#     st.write("##")
#     image_column, text_column = st.columns((1, 8))
#     with image_column:
#         st.image("D:\python\surya\images\AM_Kaali_page-0001.jpg")

#     with text_column:
#         st.subheader("Project 1: Data Analysis with Python")
#         st.write("In this project, I analyzed a dataset using Python libraries such as Pandas and Matplotlib. I explored the data, performed cleaning and preprocessing, and created visualizations to uncover insights.")

