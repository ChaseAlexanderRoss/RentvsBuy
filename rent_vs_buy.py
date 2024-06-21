import streamlit as st

# Function to calculate buying cost
def calculate_buying_cost(home_price, down_payment_percentage, loan_term, interest_rate, property_tax_rate, insurance_annual, maintenance_percentage, duration_years, selling_cost_percentage):
    down_payment = home_price * down_payment_percentage
    loan_amount = home_price - down_payment
    monthly_interest_rate = interest_rate / 12
    number_of_payments = loan_term * 12
    mortgage_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate)**number_of_payments) / ((1 + monthly_interest_rate)**number_of_payments - 1)
    total_mortgage_payment = mortgage_payment * 12 * duration_years
    total_property_tax = home_price * property_tax_rate * duration_years
    total_insurance = insurance_annual * duration_years
    total_maintenance = home_price * maintenance_percentage * duration_years
    selling_costs = home_price * selling_cost_percentage
    total_buying_cost = total_mortgage_payment + total_property_tax + total_insurance + total_maintenance + down_payment + selling_costs
    return total_buying_cost

# Function to calculate renting cost
def calculate_renting_cost(monthly_rent, rent_inflation_rate, insurance_annual, duration_years):
    total_rent = sum([monthly_rent * (1 + rent_inflation_rate)**year for year in range(duration_years)]) * 12
    total_insurance = insurance_annual * duration_years
    total_renting_cost = total_rent + total_insurance
    return total_renting_cost

# Main function to run the Streamlit app
def rent_vs_buy_calculator():
    st.title("Rent vs. Buy Calculator")

    st.sidebar.header("Input Parameters")
    st.sidebar.markdown("### Home Purchase Details")
    home_price = st.sidebar.number_input("Home Price ($)", value=300000, step=10000)
    down_payment_percentage = st.sidebar.slider("Down Payment Percentage", 0.0, 1.0, value=0.20)
    loan_term = st.sidebar.number_input("Loan Term (years)", value=30, step=1)
    interest_rate = st.sidebar.slider("Interest Rate (%)", 0.0, 10.0, value=4.0) / 100
    property_tax_rate = st.sidebar.slider("Property Tax Rate (%)", 0.0, 5.0, value=1.0) / 100
    insurance_annual = st.sidebar.number_input("Homeowners Insurance (annual $)", value=1000, step=100)
    maintenance_percentage = st.sidebar.slider("Maintenance Cost Percentage", 0.0, 5.0, value=1.0) / 100
    selling_cost_percentage = st.sidebar.slider("Selling Cost Percentage", 0.0, 10.0, value=6.0) / 100

    st.sidebar.markdown("### Renting Details")
    monthly_rent = st.sidebar.number_input("Monthly Rent ($)", value=1500, step=50)
    rent_inflation_rate = st.sidebar.slider("Rent Inflation Rate (%)", 0.0, 10.0, value=3.0) / 100
    insurance_annual_rent = st.sidebar.number_input("Renter's Insurance (annual $)", value=200, step=50)

    st.sidebar.markdown("### General")
    investment_rate = st.sidebar.slider("Investment Rate (%)", 0.0, 10.0, value=5.0) / 100
    duration_years = st.sidebar.number_input("Duration of Stay (years)", value=10, step=1)

    if st.button("Calculate"):
        buying_cost = calculate_buying_cost(home_price, down_payment_percentage, loan_term, interest_rate, property_tax_rate, insurance_annual, maintenance_percentage, duration_years, selling_cost_percentage)
        renting_cost = calculate_renting_cost(monthly_rent, rent_inflation_rate, insurance_annual_rent, duration_years)
        opportunity_cost = (home_price * down_payment_percentage) * (1 + investment_rate)**duration_years
        net_benefit = buying_cost - renting_cost + opportunity_cost

        st.subheader("Results")
        st.write(f"Total Buying Cost: ${buying_cost:,.2f}")
        st.write(f"Total Renting Cost: ${renting_cost:,.2f}")
        st.write(f"Opportunity Cost of Down Payment: ${opportunity_cost:,.2f}")
        st.write(f"Net Financial Benefit: ${net_benefit:,.2f}")

if __name__ == "__main__":
    rent_vs_buy_calculator()
