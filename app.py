import streamlit as st

st.title("My First ML App")
st.write("Welcome to my deployed Streamlit project!")

name = st.text_input("Enter your name")

if name:
    st.success(f"Hello {name} 👋")

