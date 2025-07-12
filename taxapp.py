import streamlit as st
import pandas as pd

def uktaxcalc(inc):
    uktax = 0
    if inc > 125140:
        uktax += (inc - 125140) * 0.45
        inc = 125140
    if inc > 50271:
        uktax += (inc - 50271) * 0.4
        inc = 50271
    if inc > 12570:
        uktax += (inc - 12570) * 0.2
    return uktax

def austaxcalc(inc):
    austax = 0
    if inc > 180000:
        austax += (inc - 180000) * 0.45
        inc = 180000
    if inc > 120000:
        austax += (inc - 120000) * 0.37
        inc = 120000
    if inc > 45000:
        austax += (inc - 45000) * 0.325
        inc = 45000
    if inc > 18200:
        austax += (inc - 18200) * 0.16
    return austax

income = st.sidebar.slider('Income £ ', 0, 400000, 50000)
exchangerate = st.sidebar.slider('Exchange rate £1 in $', 1.5, 2.5, 2.05)
uktax = uktaxcalc(income)
austax = austaxcalc(income * exchangerate)


st.subheader(f'Your income is £{income:,.2f}')

st.subheader(f'Your tax is £{uktax:,.2f}')

st.subheader(f'Aussie dollars equivalents')
st.subheader(f'Your income would be ${income * exchangerate:,.2f}')
st.subheader(f'You would be taxed ${austax:,.2f} = £{austax / exchangerate:,.2f}')

st.write('In the UK you don\'t pay capital gains tax on your primary residence')
st.write('In Australia you pay capital gains tax on investment income')

ukincomeseries = [i * 1000 for i in range(0, 400, 10)]
ausincomeseries = map(lambda x: x * exchangerate, ukincomeseries)
uktaxseries = map(uktaxcalc, ukincomeseries)
austaxseries = map(austaxcalc, ausincomeseries)
taxdataframe = pd.DataFrame({
    '$ AUD': austaxseries,
    '£ GBP': uktaxseries
})
st.line_chart(taxdataframe)