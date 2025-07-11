import streamlit as st
import numpy as np
import pandas as pd

st.write('Hello from Streamlit')
# df = pd.DataFrame({
#     'first col': [1, 2, 3, 4],
#     'second col': [10, 20, 30, 40]
# })

# st.write(df)

# st.table(df)

if st.checkbox('Show randomized dataframe example'):
    my_dataframe = pd.DataFrame(
        np.random.randn(10, 20),
        columns=('col %d' % i for i in range(20))
    )
    st.dataframe(my_dataframe.style.highlight_max(axis=0))


# my_chart_data = pd.DataFrame(
#     np.random.randn(10, 3),
#     columns=['a', 'b', 'c']
# )
st.write('Here is a line chart for two made up currency values')
bitcoin = [5, 8, 19, 12, 13, 17, 21]
gbp = [12, 11, 13, 12, 12, 12, 14]
my_chart_data = pd.DataFrame(
    {'bitcoin': bitcoin,
     'gbp': gbp}
)
st.line_chart(my_chart_data)

st.sidebar.write('Here is a widget for showing x squared')
x = st.sidebar.slider('x', 1, 10, 2)
st.sidebar.write('x', 'squared is', x * x)

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Mobile', 'Never')
)

my_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

st.sidebar.write('your chosen values: ', my_slider)