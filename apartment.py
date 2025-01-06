import streamlit as st
from utils import get_google_sheet_data
import pandas as pd


def apply_premium_ui_styles():
    st.markdown("""
    <style>
    /* Mobile-First Base Variables */
    :root {
        --primary: #1a365d;
        --primary-light: #2c5282;
        --secondary: #00a0dc;
        --accent: #48bb78;
        --background: #f7fafc;
        --surface: #ffffff;
        --text-primary: #2d3748;
        --text-secondary: #4a5568;
        --border: #e2e8f0;
    }

    /* Global Mobile Optimizations */
    .main {
        padding: 0.5rem;
        max-width: 100%;
    }

    /* Filter Panel */
    .filter-panel {
        background: var(--surface);
        padding: 16px 12px;
        border-radius: 8px;
        margin-bottom: 12px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }

    /* Radio Button Group Optimization */
    .stRadio > div {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
        gap: 8px;
        margin: 0;
        padding: 0;
    }

    .stRadio > div > div {
        display: flex;
        flex-direction: column;
        width: 100%;
        gap: 8px;
    }

    .stRadio label {
        width: 100%;
        padding: 8px 16px;
        font-size: 0.95rem;
        border: 1px solid var(--border);
        border-radius: 8px;
        text-align: center;
        cursor: pointer;
        transition: all 0.2s ease;
        margin: 0;
        background: var(--surface);
        color: var(--text-primary);
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 40px;
    }

    .stRadio label:hover {
        background-color: #f8fafc;
        border-color: var(--primary);
    }

    /* Radio Button Selected State */
    .stRadio label[data-checked="true"] {
        background-color: var(--primary-light);
        color: white;
        border-color: var(--primary);
    }

    /* Options Header */
    .stRadio > label {
        font-size: 1rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 8px;
        text-align: center;
        display: block;
    }

    /* Input Fields */
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > div {
        padding: 6px 8px;
        font-size: 0.9rem;
        height: 36px;
        border-radius: 6px;
    }

    .stNumberInput label,
    .stSelectbox label {
        font-size: 0.85rem;
        margin-bottom: 2px;
    }

    /* Results Counter */
    .results-counter {
        background: var(--primary);
        color: white;
        padding: 8px;
        border-radius: 6px;
        text-align: center;
        font-size: 0.85rem;
        margin: 8px 0;
    }

    /* Property Cards */
    .property-card {
        background: var(--surface);
        border-radius: 8px;
        padding: 8px;
        margin-bottom: 8px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        border: 1px solid var(--border);
    }

    .property-header {
        display: grid;
        grid-template-columns: 1fr auto;
        gap: 4px;
        align-items: center;
        margin-bottom: 6px;
        padding-bottom: 6px;
        border-bottom: 1px solid var(--border);
    }

    .property-title {
        font-size: 0.95rem;
        font-weight: 600;
        color: var(--primary);
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    .property-price {
        font-size: 0.9rem;
        font-weight: 600;
        color: var(--accent);
        padding: 2px 6px;
        background: #f0fff4;
        border-radius: 4px;
        white-space: nowrap;
    }

    .property-details {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
    }

    .detail-item {
        display: inline-flex;
        align-items: center;
        gap: 4px;
        background: #f8fafc;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 0.85rem;
        color: var(--text-secondary);
        white-space: nowrap;
    }

    /* Expandable Content */
    .streamlit-expanderHeader {
        font-size: 0.85rem;
        padding: 8px;
    }

    .streamlit-expanderContent {
        padding: 8px;
    }

    .detail-section {
        font-size: 0.85rem;
    }

    .detail-section p {
        margin: 4px 0;
        display: flex;
        justify-content: space-between;
        gap: 8px;
        line-height: 1.4;
    }

    .detail-section strong {
        color: var(--text-primary);
        flex-shrink: 0;
    }

    /* Extra Small Screen Optimizations */
    @media (max-width: 350px) {
        .property-header {
            text-align: left;
        }

        .property-title {
            font-size: 0.95rem;
        }

        .property-price {
            font-size: 0.9rem;
        }

        .detail-item {
            font-size: 0.8rem;
            padding: 2px 6px;
        }

        .stRadio label {
            font-size: 0.85rem;
            padding: 6px;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def display_apartment_data():
    # Apply mobile-optimized styling
    apply_premium_ui_styles()

    # Fetch data
    data = get_google_sheet_data("Apartment")
    if data:
        df = pd.DataFrame(data[1:], columns=data[0])

        st.markdown('<div class="filter-panel">', unsafe_allow_html=True)

        # Property type filter
        filter_option = st.radio(
            "APARTMENT OPTIONS",
            ("Apartments for Sale", "Apartments for Rent"),
            horizontal=True,
            label_visibility="collapsed"
        )

        # Create dynamic columns based on indices
        df['SIZE'] = pd.to_numeric(df.iloc[:, 5], errors='coerce')
        df['PRICE'] = pd.to_numeric(df.iloc[:, 15], errors='coerce')
        df['SALE_PRICE'] = pd.to_numeric(df.iloc[:, 17], errors='coerce')

        # Size Filter - Single column for mobile
        st.markdown("##### Size Range (sq. ft.)")
        min_size = int(df['SIZE'].min())
        max_size = int(df['SIZE'].max())

        size_col1, size_col2 = st.columns(2)
        with size_col1:
            min_size_input = st.number_input("Min",
                                             min_value=min_size,
                                             max_value=max_size,
                                             value=min_size)
        with size_col2:
            max_size_input = st.number_input("Max",
                                             min_value=min_size,
                                             max_value=max_size,
                                             value=max_size)

        # Price Filter
        st.markdown("##### Price Range (₹)")
        if filter_option == "Apartments for Rent":
            min_price = int(df['PRICE'].min())
            max_price = int(df['PRICE'].max())
        else:
            min_price = int(df['SALE_PRICE'].min())
            max_price = int(df['SALE_PRICE'].max())

        price_col1, price_col2 = st.columns(2)
        with price_col1:
            min_price_input = st.number_input("Min Price",
                                              min_value=min_price,
                                              max_value=max_price,
                                              value=min_price)
        with price_col2:
            max_price_input = st.number_input("Max Price",
                                              min_value=min_price,
                                              max_value=max_price,
                                              value=max_price)

        # Project and Accommodation
        micro_market_options = ["All"] + list(df.iloc[:, 2].dropna().unique())  # Column C
        selected_micro_market = st.selectbox("Micro Market", micro_market_options)

        location_options = ["All"] + list(df.iloc[:, 3].dropna().unique())  # Column D
        selected_location = st.selectbox("Location", location_options)

        project_options = ["All"] + list(df.iloc[:, 4].dropna().unique())
        selected_project = st.selectbox("Project", project_options)

        accommodation_options = ["All"] + list(df.iloc[:, 6].dropna().unique())
        selected_accommodation = st.selectbox("Accommodation", accommodation_options)

        # Reference and Profile
        reference_options = ["All"] + list(df.iloc[:, 22].dropna().unique())
        selected_reference = st.selectbox("Reference", reference_options)

        profile_options = ["All"] + list(df.iloc[:, 21].dropna().unique())
        selected_profile = st.selectbox("Profile", profile_options)

        st.markdown('</div>', unsafe_allow_html=True)

        # Filtering Logic
        if filter_option == "Apartments for Sale":
            filtered_data = df[df.iloc[:, 14] == "SALE"]
        else:
            filtered_data = df[df.iloc[:, 14] == "RENT"]

        # Apply filters
        if selected_micro_market != "All":
            filtered_data = filtered_data[filtered_data.iloc[:, 2] == selected_micro_market]
        if selected_location != "All":
            filtered_data = filtered_data[filtered_data.iloc[:, 3] == selected_location]
        if selected_project != "All":
            filtered_data = filtered_data[filtered_data.iloc[:, 4] == selected_project]
        if selected_accommodation != "All":
            filtered_data = filtered_data[filtered_data.iloc[:, 6] == selected_accommodation]
        if selected_reference != "All":
            filtered_data = filtered_data[filtered_data.iloc[:, 22] == selected_reference]
        if selected_profile != "All":
            filtered_data = filtered_data[filtered_data.iloc[:, 21] == selected_profile]

        filtered_data = filtered_data[
            (filtered_data['SIZE'] >= min_size_input) &
            (filtered_data['SIZE'] <= max_size_input)
            ]

        if filter_option == "Apartments for Rent":
            filtered_data = filtered_data[
                (filtered_data['PRICE'] >= min_price_input) &
                (filtered_data['PRICE'] <= max_price_input)
                ]
        else:
            filtered_data = filtered_data[
                (filtered_data['SALE_PRICE'] >= min_price_input) &
                (filtered_data['SALE_PRICE'] <= max_price_input)
                ]

        # Results Counter
        st.markdown(f"""
            <div class="results-counter">
                {len(filtered_data)} Properties Found
            </div>
        """, unsafe_allow_html=True)

        # Display Property Cards
        for _, row in filtered_data.iterrows():
            price_display = row['PRICE'] if filter_option == "Apartments for Rent" else row['SALE_PRICE']

            st.markdown(f"""
            <div class="property-card">
                <div class="property-header">
                    <div class="property-title">{row.iloc[4]} | {row.iloc[6]}</div>
                    <div class="property-price">₹{price_display:,.2f}</div>
                </div>
                <div class="property-details">
                    <div class="detail-item">📏 {row.iloc[5]} sq.ft.</div>
                    <div class="detail-item">🏢 Tower {row["TOWER"]}</div>
                    <div class="detail-item">📍 Floor {row["FLOOR"]}</div>
                    <div class="detail-item"> {row["AVAILABLE / UNAVAILABLE"]}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Mobile-Optimized Expandable Details
            with st.expander("View Details"):
                st.markdown(f"""
                    <div class="detail-section">
                        <p><strong>Date:</strong> {row["DATE"]}</p>
                        <p><strong>Location:</strong> {row["LOCATION"]}</p>
                        <p><strong>Size:</strong> {row.iloc[5]} sq.ft.</p>
                        <p><strong>Unit:</strong> {row["UNIT NO."]}</p>
                        <p><strong>Description:</strong> {row["DESCRIPTION"]}</p>
                        <p><strong>Parking:</strong> {row["CAR PARKING"]}</p>
                        <p><strong>Maintenance:</strong> {row["MAINTENANCE"]}</p>
                        <p><strong>Offered By:</strong> {row["OFFERED BY"]}</p>
                        <p><strong>Profile:</strong> {row["PROFILE"]}</p>
                        <p><strong>Reference:</strong> {row.iloc[22]}</p>
                        <p><strong>Status:</strong> {row["AVAILABLE / UNAVAILABLE"]}</p>
                    </div>
                """, unsafe_allow_html=True)

    else:
        st.error("Unable to load apartment data. Please try again later.")
