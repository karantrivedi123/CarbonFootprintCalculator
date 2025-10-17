import streamlit as st
import pandas as pd

# Set the title and a small introduction for your app
st.title('Portfolio Carbon Footprint Calculator 🌍')
st.write("""
This tool calculates the total carbon footprint of your investment portfolio.
It uses a dataset of company financials and ESG metrics, with missing emissions data
predicted by a machine learning model.
""")

# --- Function to Perform the Calculation ---
# We put our main logic inside a function to keep the code clean.
def calculate_footprint(portfolio_df, company_data):
    # Get the latest data for each company
    company_data_latest = company_data.sort_values('Year').drop_duplicates('CompanyName', keep='last')

    # Merge portfolio with company data
    portfolio_complete = pd.merge(
        portfolio_df,
        company_data_latest,
        on='CompanyName',
        how='left'
    )

    # Clean data and calculate financed emissions
    portfolio_complete.dropna(subset=['MarketCap', 'CarbonEmissions'], inplace=True)
    
    # Avoid division by zero if MarketCap is 0
    portfolio_complete = portfolio_complete[portfolio_complete['MarketCap'] > 0]

    portfolio_complete['OwnershipFraction'] = portfolio_complete['Investment'] / portfolio_complete['MarketCap']
    portfolio_complete['FinancedEmissions'] = portfolio_complete['OwnershipFraction'] * portfolio_complete['CarbonEmissions']
    
    total_emissions = portfolio_complete['FinancedEmissions'].sum()
    
    return total_emissions, portfolio_complete

# --- Load the Main Company Dataset ---
# We use @st.cache_data to make the app faster by loading the data only once.
@st.cache_data
def load_data():
    try:
        data = pd.read_csv('companies_with_full_emissions_data.csv')
        return data
    except FileNotFoundError:
        return None

company_data = load_data()

if company_data is None:
    st.error("Error: The main data file ('companies_with_full_emissions_data.csv') was not found.")
else:
    # --- The User Interface ---
    st.header("Upload Your Portfolio CSV File")
    
    # Create the file uploader widget
    uploaded_file = st.file_uploader(
        "Your portfolio should have two columns: 'CompanyName' and 'Investment'",
        type="csv"
    )

    if uploaded_file is not None:
        # Load the user's uploaded portfolio
        user_portfolio = pd.read_csv(uploaded_file)
        st.success("Portfolio uploaded successfully!")

        # Calculate the footprint
        total_emissions, result_df = calculate_footprint(user_portfolio, company_data)

        # Display the results
        st.subheader("Results")
        st.metric(
            label="Total Portfolio Carbon Footprint",
            value=f"{total_emissions:,.2f} tons of CO₂e"
        )

        st.write("---")
        st.write("Calculation Breakdown:")
        st.dataframe(result_df[['CompanyName', 'Investment', 'MarketCap', 'CarbonEmissions', 'FinancedEmissions']])

# Add a small footer
st.info("To use the app, create a CSV file named `my_portfolio.csv` with 'CompanyName' and 'Investment' columns.")
