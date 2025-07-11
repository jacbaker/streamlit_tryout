import streamlit as st

col1, col2 = st.columns(2)
   
the_text = st.text_area('Paste text here', value="")

lines = the_text.split('\n')

for i in range(len(lines)):
    col1.write('line ' + str(i))
    col2.write(lines[i])
  
