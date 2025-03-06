import streamlit as st

st.title('Streamlit Abdallah')
st.write('Welcome to my first Streamlit app!')

ap = st.text_input('Enter your name')
st.write('Hello', ap)