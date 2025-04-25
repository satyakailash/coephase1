import streamlit as st
min_value=0
st.title("This is a sample program")
num1=st.number_input("Enter a number",min_value,step=1)
num2=st.number_input("Enter a number",min_value,step=1)
if st.button("ADD"):
    st.write("TOTAL",num1+num2)
dob=st.date_input("Select DOB")
st.success("")
st.error("")