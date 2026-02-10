import streamlit as st
st.title("Addition App")
a=st.number_input("Enter first number:")
b=st.number_input("Enter second number:")
if st.button('Addtion'):
    c=a+b
    st.success(f'{a}+{b}={c}')