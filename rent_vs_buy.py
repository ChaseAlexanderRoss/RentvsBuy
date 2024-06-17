import streamlit as st
import numpy as np

# Function to calculate monthly mortgage payment
def calculate_mortgage_payment(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    num_payments = years * 12
    mortgage_payment = (principal * monthly_rate * (1 + monthly_rate)**num_payments) / ((1 + monthly_rate)**num_payments - 1)
    return mortgage_payment

# Function to calculate total cost of buying
def calculate_buying_cost(home_price, down_payment_percent, loan_term, interest_rate, property_tax_rate):
    down_payment = home_price * (down_payment_percent / 100)
    loan_amount = home_price - down_payment
    monthly_mortgage_payment = calculate_mortgage_payment(loan_amount, interest_rate, loan_term)
    monthly_property_tax = home_price * (property_tax_rate / 100) / 12
    total_monthly_cost = monthly_mortgage_payment + monthly_property_tax
    return total_monthly_cost

# Function to calculate total cost of renting
def calculate_renting_cost(rent_amount, annual_rent_increase_rate, years):
    total_rent_cost = 0
    for year in range(years):
        total_rent_cost += rent_amount * 12
        rent_amount *= (1 + annual_rent_increase_rate / 100)
    return total_rent_cost / years / 12

# Streamlit app
st.title("Rent vs Buy Calculator")

st.sidebar.header("User Inputs")
home_price = st.sidebar.number_input("Home Price ($)", value=300000)
down_payment_percent = st.sidebar.slider("Down Payment (%)", min_value=0, max_value=100, value=20)
loan_term = st.sidebar.slider("Loan Term (years)", min_value=1, max_value=30, value=30)
interest_rate = st.sidebar.number_input("Interest Rate (%)", value=3.0)
property_tax_rate = st.sidebar.number_input("Property Tax Rate (%)", value=1.25)
rent_amount = st.sidebar.number_input("Monthly Rent ($)", value=1500)
annual_rent_increase_rate = st.sidebar.number_input("Annual Rent Increase Rate (%)", value=2.0)
years = st.sidebar.slider("Comparison Period (years)", min_value=1, max_value=30, value=30)

total_monthly_buying_cost = calculate_buying_cost(home_price, down_payment_percent, loan_term, interest_rate, property_tax_rate)
total_monthly_renting_cost = calculate_renting_cost(rent_amount, annual_rent_increase_rate, years)

st.write("### Total Monthly Costs")
st.write(f"Buying: ${total_monthly_buying_cost:,.2f}")
st.write(f"Renting: ${total_monthly_renting_cost:,.2f}")

if total_monthly_buying_cost < total_monthly_renting_cost:
    st.write("### Buying is more cost-effective over the specified period.")
else:
    st.write("### Renting is more cost-effective over the specified period.")

st.write("### Detailed Breakdown")
st.write(f"**Home Price:** ${home_price:,.2f}")
st.write(f"**Down Payment:** {down_payment_percent}%")
st.write(f"**Loan Term:** {loan_term} years")
st.write(f"**Interest Rate:** {interest_rate}%")
st.write(f"**Property Tax Rate:** {property_tax_rate}%")
st.write(f"**Monthly Rent:** ${rent_amount:,.2f}")
st.write(f"**Annual Rent Increase Rate:** {annual_rent_increase_rate}%")
st.write(f"**Comparison Period:** {years} years")
