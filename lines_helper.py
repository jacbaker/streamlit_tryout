import streamlit as st

my_text = st.text_area('Enter text here')
my_lines = my_text.split('\n')

if 'maxlines' not in st.session_state:
    st.session_state.maxlines = 0

def incr():
    st.session_state.maxlines += 1
    
for i in range(min(st.session_state.maxlines, len(my_lines))):
    st.write(my_lines[i])

st.button('next line', on_click=incr)