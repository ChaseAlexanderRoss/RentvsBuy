import streamlit as st

# Function to fetch real-world data
def get_real_world_data():
    # These values are examples and should be replaced with real-time data fetching in a production environment
    mortgage_rate = 6.87 / 100  # Example rate from FRED data
    annual_rent_increase = 0.03  # Example rent increase from market trends
    home_appreciation_rate = 0.07  # Example appreciation rate from FHFA
    down_payment_percentage = 0.136  # Example average down payment from NAR and Rocket Mortgage
    return mortgage_rate, annual_rent_increase, home_appreciation_rate, down_payment_percentage

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
    st.set_page_config(page_title="Rent vs. Buy Calculator", layout="centered")
    st.title("Rent vs. Buy Calculator")
    description_placeholder = st.empty()
    description_placeholder.markdown("## Compare the costs and benefits of renting versus buying a home.")
    
    st.sidebar.header("Input Parameters")
    
    duration_years = st.sidebar.number_input("Duration of Stay (years)", value=10, step=1)
    
    if st.sidebar.button("Use Real-World Data"):
        mortgage_rate, annual_rent_increase, home_appreciation_rate, down_payment_percentage = get_real_world_data()
        st.session_state['mortgage_rate'] = mortgage_rate
        st.session_state['annual_rent_increase'] = annual_rent_increase
        st.session_state['home_appreciation_rate'] = home_appreciation_rate
        st.session_state['down_payment_percentage'] = down_payment_percentage

    mortgage_rate = st.session_state.get('mortgage_rate', 0.0687)
    annual_rent_increase = st.session_state.get('annual_rent_increase', 0.03)
    home_appreciation_rate = st.session_state.get('home_appreciation_rate', 0.07)
    down_payment_percentage = st.session_state.get('down_payment_percentage', 0.20)
    
    with st.sidebar:
        st.markdown("### Home Purchase Details")
        home_price = st.number_input("Home Price ($)", value=300000, step=10000)
        down_payment_percentage = st.slider("Down Payment Percentage", 0.0, 1.0, value=down_payment_percentage)
        loan_term = st.number_input("Loan Term (years)", value=30, step=1)
        insurance_annual = st.number_input("Homeowners Insurance (annual $)", value=1000, step=100)
        maintenance_percentage = st.slider("Maintenance Cost Percentage", 0.0, 5.0, value=1.0) / 100
        property_tax_rate = st.slider("Property Tax Rate (%)", 0.0, 5.0, value=1.0) / 100
        selling_cost_percentage = st.slider("Selling Cost Percentage", 0.0, 10.0, value=6.0) / 100

        st.markdown("### Renting Details")
        monthly_rent = st.number_input("Monthly Rent ($)", value=1500, step=50)
        insurance_annual_rent = st.number_input("Renter's Insurance (annual $)", value=200, step=50)
        
        st.markdown("### Investment")
        investment_rate = st.slider("Investment Rate (%)", 0.0, 10.0, value=5.0) / 100

    if st.button("Calculate"):
        buying_cost = calculate_buying_cost(home_price, down_payment_percentage, loan_term, mortgage_rate, property_tax_rate, insurance_annual, maintenance_percentage, duration_years, selling_cost_percentage)
        renting_cost = calculate_renting_cost(monthly_rent, annual_rent_increase, insurance_annual_rent, duration_years)
        opportunity_cost = (home_price * down_payment_percentage) * (1 + investment_rate)**duration_years
        net_benefit = buying_cost - renting_cost + opportunity_cost

        if net_benefit > 0:
            description_placeholder.markdown("# It is better to buy a home based on the financial calculations.")
        else:
            description_placeholder.markdown("# It is better to rent based on the financial calculations.")
        
        st.subheader("Results")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Total Buying Cost")
            st.write(f"${buying_cost:,.2f}")
        with col2:
            st.markdown("### Total Renting Cost")
            st.write(f"${renting_cost:,.2f}")
        
        st.markdown("### Opportunity Cost of Down Payment")
        st.write(f"${opportunity_cost:,.2f}")

        st.markdown("### Net Financial Benefit")
        st.write(f"${net_benefit:,.2f}")

if __name__ == "__main__":
    rent_vs_buy_calculator()
