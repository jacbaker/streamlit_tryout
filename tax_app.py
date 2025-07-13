import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.sidebar.subheader('Adjust income and exchange rate using the sliders')
income = st.sidebar.slider('income (aussie dollars)', 10000, 400000, 100000)
exchange_rate = st.sidebar.slider('exchange rate £ to $', 1.5, 2.5, 2.05)

uk_equivalent = income / exchange_rate

st.sidebar.write(f'income: ${income:,.2f}')
st.sidebar.write(f'uk equivalent: £{uk_equivalent:,.2f}')
st.sidebar.write(f'at exchange rate £1 = ${exchange_rate:.2f}')


def calc_aussie_tax(income):
    austax = 0
    if income > 180000:
        austax += (income - 180000) * 0.45
        income = 180000
    if income > 120000:
        austax += (income - 120000) * 0.37
        income = 120000
    if income > 45000:
        austax += (income - 45000) * 0.325
        income = 45000
    if income > 18200:
        austax += (income - 18200) * 0.16
    return austax

austax = calc_aussie_tax(income)
st.subheader(f'Australian tax: ${austax:,.2f}')

def calc_uk_tax(uk_equivalent):
    uktax = 0
    if uk_equivalent > 125140:
        uktax += (uk_equivalent - 125140) * 0.45
        uk_equivalent = 125140
    if uk_equivalent > 50271:
        uktax += (uk_equivalent - 50271) * 0.4
        uk_equivalent = 50271
    if uk_equivalent > 12571:
        uktax += (uk_equivalent - 12571) * 0.2
    return uktax

uktax = calc_uk_tax(uk_equivalent)
aud_equivalent_uktax = uktax * exchange_rate

st.subheader(f'UK tax: £{uktax:,.2f} which is equivalent to ${aud_equivalent_uktax:,.2f}')

x_axis_series = [i for i in range(0, 410000, 10000)]
aussie_tax_series = list(map(calc_aussie_tax, x_axis_series))
uk_tax_series = list(map(calc_uk_tax, map(lambda inc: inc / exchange_rate, x_axis_series)))

fig = make_subplots(rows=1, cols=1, shared_yaxes=True)
fig.update_yaxes(title_text="Tax in $ for Aussie tax and £ for UK tax", range=[0, 170000], dtick=20000)
fig.update_xaxes(title_text="Income", dtick=50000)
fig.add_trace(
    go.Scatter(x=x_axis_series, y=uk_tax_series, name="UK tax"),
    row=1, col=1
)
fig.add_trace(
    go.Scatter(x=x_axis_series, y=aussie_tax_series, name="Aussie tax"),
    row=1, col=1
)
fig.add_trace(
    go.Scatter(x=[income], y=[uktax], mode='markers', marker_symbol='star', marker_size=15, showlegend=False)
)
fig.add_trace(
    go.Scatter(x=[income], y=[austax], mode='markers', marker_symbol='star', marker_size=15, showlegend=False)
)
fig.update_layout(title_text="Aussie tax vs UK tax")
# fig.show()
st.plotly_chart(fig, use_container_width=True)