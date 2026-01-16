import streamlit as st

st.header('st.button')

if st.button('say hello'):
     st.write('why hello?')
else:
     st.write('goodbye')
     
import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

st.write('Your favorite color is ', option)