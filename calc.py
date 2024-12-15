import streamlit as st

st.title("My calc")

def squared(x):
    return x*x 


number = st.number_input("Insert a number")


if st.button("Get squared"):
    res = squared(number)

    st.write(res)