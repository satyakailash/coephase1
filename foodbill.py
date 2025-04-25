import streamlit as  st
st.title("FOOD BILL")
tip=0
bill=st.number_input("Enter bill amount",min_value=0,step=1)
if bill<=1000:
    tip=(bill*2)/100
    st.write("You got tip of :",tip)
elif bill>=5000:
    tip=(bill*7)/100
    st.write("You got tip of :",tip)
else:
    tip=(bill*5)/100
    st.write("You got tip of :",tip)
