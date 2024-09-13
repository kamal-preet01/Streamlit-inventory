import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from rented import render_rented
from kothi import render_kothi
from apartment import render_apartment
from floor import render_floor
from plot import render_plot
from office import render_office
from retail import render_retail

# Set up Google Sheets credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_file('keys.json', scopes=scope)
client = gspread.authorize(creds)

# Open the specific Google Sheet
SHEET_ID = '1yz74MaxJ-C5OfoSxfCQ7A9wtdlY-53PyBV3OmDiR0i8'
sheet = client.open_by_key(SHEET_ID)


def fetch_data(worksheet_name):
    worksheet = sheet.worksheet(worksheet_name)
    data = worksheet.get_all_values()
    df = pd.DataFrame(data[1:], columns=data[0])
    return df


def main():
    st.set_page_config(page_title="Aadhunik Property Finder", layout="wide")

    # Load custom CSS
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Enhanced App header
    st.markdown("""
    <header class="app-header">
        <h1 class="main-title">Aadhunik Property Finder</h1>
        <p class="subtitle">Discover Your Dream Property</p>
    </header>
    """, unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.markdown("<h2 style='text-align: center; color: #1f487e;'>Filters</h2>", unsafe_allow_html=True)
        sheet_option = st.selectbox(
            "Select Property Type",
            ["Rented", "Kothi", "Apartment", "Floor", "Plot", "Office", "Retail"]
        )

    # Render the appropriate sheet based on selection
    if sheet_option == "Rented":
        render_rented(fetch_data("Rented"))
    elif sheet_option == "Kothi":
        render_kothi(fetch_data("Kothi"))
    elif sheet_option == "Apartment":
        render_apartment(fetch_data("Apartment"))
    elif sheet_option == "Floor":
        render_floor(fetch_data("Floor"))
    elif sheet_option == "Plot":
        render_plot(fetch_data("Plot"))
    elif sheet_option == "Office":
        render_office(fetch_data("Office"))
    elif sheet_option == "Retail":
        render_retail(fetch_data("Retail"))


if __name__ == "__main__":
    main()