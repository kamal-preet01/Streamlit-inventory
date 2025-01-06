import streamlit as st
from kothi import display_kothi_data
from apartment import display_apartment_data
from floor import display_floor_data
from plot import display_plot_data
from rented import display_rented_data
from retail import display_retail_data
from office import display_office_data
from sheet_viewer import display_sheet_viewer


def apply_professional_ui_styles():
    st.markdown("""
    <style>
    /* Modern Professional Color Palette */
/* Modern Professional Color Palette */
:root {
    --primary-color: #2c3e50;
    --secondary-color: #3498db;
    --background-light: #f4f6f9;
    --background-white: #ffffff;
    --text-dark: #2c3e50;
    --text-muted: #7f8c8d;
    --border-color: #e2e6ea;
}

/* Global Typography and Reset */
* {
    font-family: 'Inter', 'Roboto', 'Segoe UI', sans-serif;
    box-sizing: border-box;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

/* Responsive Base Styling */
.reportview-container {
    background-color: var(--background-light);
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 8px;
}

/* Enhanced Sidebar Styling */
.sidebar .sidebar-content {
    background: var(--background-white);
    border-right: 1px solid var(--border-color);
    padding: 15px;
}

/* Modern Navigation Styling */
.stRadio > div {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    justify-content: flex-start;
    width: 100%;
}

.stRadio label {
    background-color: var(--background-white);
    border: 1px solid var(--border-color);
    border-radius: 6px;
    padding: 8px 12px;
    font-weight: 500;
    font-size: 0.9em;
    flex: 1 1 auto;
    min-width: 120px;
    text-align: center;
}

/* Mobile-Optimized Main Title */
h1 {
    color: var(--primary-color);
    text-align: center;
    font-weight: 600;
    font-size: 1.5em;
    margin: 12px 0;
    padding: 8px 0;
    background: linear-gradient(135deg, #3498db, #2980b9);
    -webkit-background-clip: text;
    color: transparent;
}

h1::after {
    content: '';
    width: 60px;
    height: 3px;
    margin: 8px auto;
}

/* Compact Subheading */
h2 {
    text-align: center;
    font-size: 1em;
    color: var(--text-muted);
    font-weight: 400;
    margin: 10px 0;
}

/* Mobile-Optimized Property Cards */
.property-card {
    background: var(--background-white);
    border-radius: 8px;
    padding: 12px;
    margin-bottom: 12px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    border: 1px solid var(--border-color);
}

.property-header {
    display: flex;
    flex-direction: column;
    gap: 8px;
    margin-bottom: 8px;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--border-color);
}

.property-title {
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--primary-color);
}

.property-price {
    font-size: 1.1rem;
    font-weight: 600;
    color: #48bb78;
    padding: 4px 8px;
    background: #f0fff4;
    border-radius: 4px;
    align-self: flex-start;
}

.property-details {
    display: grid;
    grid-template-columns: 1fr;
    gap: 8px;
    margin-top: 8px;
}

.detail-item {
    display: flex;
    align-items: center;
    gap: 6px;
    color: var(--text-secondary);
    font-size: 0.9rem;
}

/* Compact Filter Panel */
.filter-panel {
    background: var(--background-white);
    padding: 12px;
    border-radius: 8px;
    margin-bottom: 16px;
}

/* Mobile-Optimized Form Elements */
.stTextInput > div > div > input,
.stNumberInput > div > div > input,
.stSelectbox > div > div > div {
    border-radius: 6px;
    padding: 8px 12px;
    font-size: 0.9rem;
}

/* Compact Results Counter */
.results-counter {
    background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
    color: white;
    padding: 8px;
    border-radius: 6px;
    text-align: center;
    font-weight: 500;
    font-size: 0.9rem;
    margin: 12px 0;
}

/* Mobile-Optimized Expandable Content */
.streamlit-expanderHeader {
    padding: 8px;
    font-size: 0.9rem;
}

.streamlit-expanderContent {
    padding: 12px;
}

/* Extra Small Screen Optimizations */
@media (max-width: 360px) {
    h1 {
        font-size: 1.3em;
    }

    .property-title {
        font-size: 1rem;
    }

    .property-price {
        font-size: 1rem;
    }

    .detail-item {
        font-size: 0.85rem;
    }
}

/* Small Screen Optimizations */
@media (max-width: 480px) {
    .reportview-container {
        padding: 0 4px;
    }

    .property-card {
        padding: 10px;
    }

    .filter-panel {
        padding: 10px;
    }

    .stRadio label {
        padding: 6px 10px;
        font-size: 0.85em;
    }
}
    </style>
    """, unsafe_allow_html=True)


def main():
    # Professional Page Configuration
    st.set_page_config(
        page_title="Aadhunik Estates | Real Estate Solutions",
        page_icon="🏢",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # Apply Professional UI Styles
    apply_professional_ui_styles()

    # Professional Header
    st.markdown("""
    <h1>AADHUNIK ESTATES</h1>
    <h2>Real Estate Intelligence</h2>
    """, unsafe_allow_html=True)

    # Professional Sidebar Navigation
    st.sidebar.markdown("## P.R.I.S.M- Personalized Realestate Interactive Search Machine")

    # Precise Menu Configuration
    menu_config = {
        "Kothi": "🏘️",
        "Apartment": "🏢",
        "Floor": "🏬",
        "Plot": "🌳",
        "Rented": "🔑",
        "Retail": "🛍️",
        "Office": "💼",
        "View Sheets": "📊"
    }

    menu = list(menu_config.keys())

    # Precise Radio Button Selection
    choice = st.sidebar.radio(
        "Select Property Type",
        menu,
        format_func=lambda x: f"{menu_config[x]} {x}"
    )

    # Dynamic Content Display
    display_functions = {
        "Kothi": display_kothi_data,
        "Apartment": display_apartment_data,
        "Floor": display_floor_data,
        "Plot": display_plot_data,
        "Rented": display_rented_data,
        "Retail": display_retail_data,
        "Office": display_office_data,
        "View Sheets": display_sheet_viewer  # Add this line
    }

    # Execute Selected Property Type Display
    display_functions[choice]()

    # Compact Professional Footer
    st.markdown("""
    <div class="footer">
    © 2024 Aadhunik Estates | Real Estate Solutions | P.R.I.S.M
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
