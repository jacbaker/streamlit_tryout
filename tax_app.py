import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

income = st.sidebar.slider('income (aussie dollars)', 10000, 400000, 100000)
exchange_rate = st.sidebar.slider('exchange rate £ to $', 1.5, 2.5, 2.05)

uk_equivalent = income / exchange_rate

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

x_axis_series = [i for i in range(0, 400000, 10000)]
aussie_tax_series = map(calc_aussie_tax, x_axis_series)
uk_tax_series = map(calc_uk_tax, map(lambda inc: inc / exchange_rate, x_axis_series))

comparison_data_aussie = pd.DataFrame({
    '$ tax': aussie_tax_series,
    'income': x_axis_series
})

fig1 = px.scatter(comparison_data_aussie, x='income', y='$ tax')
fig1.add_trace(
    go.Scatter(x=[income], y=[austax], mode='markers', marker_symbol='star', marker_size=15, showlegend=False)
)

comparison_data_uk = pd.DataFrame({
    '£ tax': uk_tax_series,
    'income': x_axis_series
})

fig2 = px.scatter(comparison_data_uk, x='income', y='£ tax')
fig2.add_trace(
    go.Scatter(x=[income], y=[uktax], mode='markers', marker_symbol='star', marker_size=15, showlegend=False)
)

col1, col2 = st.columns(2)
col1.subheader('Aussie tax')
col2.subheader('UK tax')
col1.plotly_chart(fig1, use_container_width=True)
col2.plotly_chart(fig2, use_container_width=True)