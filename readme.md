# Portfolio Carbon Footprint Calculator

**[Live App Demo Link - You will add this later]**

## 🚀 Project Overview

This project is an interactive web application that calculates the carbon footprint of an investment portfolio. It addresses the real-world challenge of incomplete ESG data by using a machine learning model to estimate carbon emissions for companies that do not report them.

This tool allows an investor to upload their portfolio and receive an immediate, data-driven estimate of their "financed emissions" in tons of CO₂e.

---

## 🛠️ Tech Stack

* **Language:** Python
* **Data Analysis:** Pandas
* **Machine Learning:** Scikit-learn (Linear Regression)
* **Web App Framework:** Streamlit
* **IDE:** Visual Studio Code

---

## ✨ Features

* **Interactive UI:** A simple and clean user interface built with Streamlit.
* **File Upload:** Allows users to upload their own portfolio in CSV format.
* **ML-Powered Estimation:** Fills missing emissions data using a regression model trained on company revenue and industry sector.
* **Financed Emissions Calculation:** Implements the standard formula to calculate the user's share of corporate emissions.
* **Clear Results:** Displays the total portfolio footprint and a detailed breakdown per holding.

---

## 🔧 How to Run Locally

1.  Clone the repository: `git clone [your-repo-url]`
2.  Navigate to the project directory: `cd CarbonProject`
3.  Install the required libraries: `pip install -r requirements.txt`
4.  Run the Streamlit app: `streamlit run app.py`