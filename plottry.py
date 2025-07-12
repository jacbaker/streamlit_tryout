import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

x = [1, 2, 3]
y = [4, 8, 19]
hx = 2.5
hy = 6

data = {'x': x, 'y': y}
df = pd.DataFrame(data)
fig = px.scatter(df, x='x', y='y')
fig.add_trace(
    go.Scatter(x=[hx], y=[hy], mode='markers', marker_symbol='star', marker_size=15)
)
st.plotly_chart(fig, use_container_width=True)