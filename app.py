import streamlit as st
import requests

st.set_page_config(page_title="Currency Converter", page_icon="💱")

st.title("💱 Currency Converter")

# Expanded currency list
currencies = [
    "USD",  # US Dollar
    "PKR",  # Pakistani Rupee
    "EUR",  # Euro
    "GBP",  # British Pound
    "INR",  # Indian Rupee
    "CNY",  # Chinese Yuan
    "JPY",  # Japanese Yen
    "AED",  # UAE Dirham
    "SAR",  # Saudi Riyal
    "CAD",  # Canadian Dollar
    "AUD"   # Australian Dollar
]

amount = st.number_input("Enter amount", min_value=0.0, value=1.0)
from_currency = st.selectbox("From Currency", currencies)
to_currency = st.selectbox("To Currency", currencies)

def get_rate(from_curr, to_curr):
    url = f"https://v6.exchangerate-api.com/v6/ebcc4c338e9fdf7ff02d04c5/latest/{from_curr}"
    response = requests.get(url)
    data = response.json()
    return data["conversion_rates"][to_curr]

if st.button("Convert"):
    rate = get_rate(from_currency, to_currency)
    result = amount * rate
    st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")