import streamlit as st
import pandas as pd

inc = st.sidebar.slider('Income $', 0, 400000, 50000)
exrate = st.sidebar.slider('Exchange rate £1 in $', 1.5, 2.5, 2.05)

auinc = [i * 10000 for i in range(0, 40)]
ukinc = map(lambda inc: inc / exrate, auinc)

st.line_chart(pd.DataFrame({'$': auinc, '£': ukinc}))