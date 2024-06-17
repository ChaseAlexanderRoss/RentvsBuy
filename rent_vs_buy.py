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

    # Input fields for user data
    home_price = st.number_input("Home Price", value=300000)
    down_payment_percentage = st.slider("Down Payment Percentage", 0.0, 1.0, value=0.20)
    loan_term = st.number_input("Loan Term (years)", value=30)
    interest_rate = st.slider("Interest Rate", 0.0, 0.10, value=0.04)
    property_tax_rate = st.slider("Property Tax Rate", 0.0, 0.05, value=0.01)
    insurance_annual = st.number_input("Homeowners Insurance (annual)", value=1000)
    maintenance_percentage = st.slider("Maintenance Cost Percentage", 0.0, 0.05, value=0.01)
    monthly_rent = st.number_input("Monthly Rent", value=1500)
    rent_inflation_rate = st.slider("Rent Inflation Rate", 0.0, 0.10, value=0.03)
    investment_rate = st.slider("Investment Rate (annual)", 0.0, 0.10, value=0.05)
    duration_years = st.number_input("Duration of Stay (years)", value=10)
    selling_cost_percentage = st.slider("Selling Cost Percentage", 0.0, 0.10, value=0.06)

    if st.button("Calculate"):
        buying_cost = calculate_buying_cost(home_price, down_payment_percentage, loan_term, interest_rate, property_tax_rate, insurance_annual, maintenance_percentage, duration_years, selling_cost_percentage)
        renting_cost = calculate_renting_cost(monthly_rent, rent_inflation_rate, insurance_annual, duration_years)
        opportunity_cost = down_payment_percentage * home_price * (1 + investment_rate)**duration_years
        net_benefit = buying_cost - renting_cost + opportunity_cost

        st.write(f"Total Buying Cost: ${buying_cost:,.2f}")
        st.write(f"Total Renting Cost: ${renting_cost:,.2f}")
        st.write(f"Opportunity Cost of Down Payment: ${opportunity_cost:,.2f}")
        st.write(f"Net Financial Benefit: ${net_benefit:,.2f}")

if __name__ == "__main__":
    rent_vs_buy_calculator()
