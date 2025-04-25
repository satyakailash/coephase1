import streamlit as st
st.title("Welcome to ACE travels")
model=st.selectbox("Choose",["Bike","Auto","Car"])
distance=st.slider("Enter distance in Kilometers",0,100)
if st.button("submit"):
    if model=="Bike":
        rup=distance*10
        st.write("Rupees :",rup)
        st.write("HAVE A NICE BIKE RIDE")
    elif model=="Auto":
        rup=distance*20
        st.write("Rupees :",rup)
        st.write("HAVE A NICE AUTO RIDE")
    else:
        rup=distance*40
        st.write("Rupees :",rup)
        st.write("HAVE A NICE CAR RIDE")
