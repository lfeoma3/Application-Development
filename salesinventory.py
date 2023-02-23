import streamlit as st

st.title ("DAILY SALES APP")

st.text_input("Name of Customer")

st.number_input("Phone Number of the Customer")

st.selectbox("What is your choice of room",["single =10,000","suites = 25,000","penthouse = 50,000"]
x = st.number_input("Room Choices",step = 1)       
             
            
st.selectbox("What is your choice",["Breakfast = 5,000","Lunch = 10,000","Dinner = 10,000"])
y = st.number_input("Food Choices",step = 1)
            
             
if st.button("Calculate"):
    Daily_sales = (x+y)
    st.write("Daily_sales",{Daily_sales})
   