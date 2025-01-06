import streamlit as st
from utils import get_google_sheet_data
import pandas as pd


def apply_premium_ui_styles():
    st.markdown("""
    <style>
    /* Mobile-First Base Variables */
    :root {
        --primary: #1a365d;
        --secondary: #00a0dc;
        --accent: #48bb78;
        --background: #f7fafc;
        --surface: #ffffff;
        --text-primary: #2d3748;
        --text-secondary: #4a5568;
        --border: #e2e8f0;
    }

    /* Global Mobile Optimizations */
    .stApp {
        max-width: 100%;
        padding: 0.5rem;
    }

    /* Radio Button Group Optimization - Fixed Equal Widths */
/* Radio Button Group Optimization - Fixed Equal Widths */
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

    /* Filter Panel */
    .filter-panel {
        background: var(--surface);
        padding: 12px 8px;
        border-radius: 8px;
        margin-bottom: 12px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }

    /* Input Fields */
    .stNumberInput > div > div > input {
        padding: 4px 8px;
        font-size: 0.9rem;
        height: 36px;
    }

    .stSelectbox > div > div {
        padding: 4px 8px;
        font-size: 0.9rem;
        height: 36px;
    }

    /* Labels */
    .stNumberInput label, .stSelectbox label {
        font-size: 0.85rem;
        margin-bottom: 2px;
    }

    /* Results Counter */
    .results-counter {
        background: var(--primary);
        color: white;
        font-size: 0.85rem;
        padding: 8px;
        border-radius: 6px;
        text-align: center;
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
        color: var(--text-secondary);
        background: #f8fafc;
        padding: 2px 6px;
        border-radius: 4px;
        font-size: 0.85rem;
        white-space: nowrap;
    }

    /* Expandable Details */
    .streamlit-expanderHeader {
        font-size: 0.85rem;
        padding: 6px 8px;
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
    }

    .detail-section strong {
        color: var(--text-primary);
        flex-shrink: 0;
    }

    /* Extra Small Screen Optimizations */
    @media (max-width: 350px) {
        .property-header {
            grid-template-columns: 1fr;
        }

        .property-price {
            justify-self: start;
        }

        .detail-item {
            font-size: 0.8rem;
        }

        .stRadio label {
            font-size: 0.85rem;
            padding: 4px 6px;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def display_retail_data():
    # Apply mobile-optimized styling
    apply_premium_ui_styles()

    # Fetch data
    data = get_google_sheet_data("Retail")
    if data:
        df = pd.DataFrame(data[1:], columns=data[0][:22])

        st.markdown('<div class="filter-panel">', unsafe_allow_html=True)

        # Property type filter - Mobile optimized
        filter_option = st.radio(
            "RETAIL OPTIONS",
            ("Retail for Sale", "Retail for Rent"),
            horizontal=True,
            label_visibility="collapsed"
        )

        # Size Filter - Single column for mobile
        df['SIZE'] = pd.to_numeric(df.iloc[:, 4], errors='coerce')
        min_size = int(df['SIZE'].min())
        max_size = int(df['SIZE'].max())

        st.markdown("##### Size Range (sq. ft.)")
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

        # Price Filter - Single column for mobile
        st.markdown("##### Price Range (₹)")
        if filter_option == "Retail for Rent":
            df['PRICE'] = pd.to_numeric(df.iloc[:, 12], errors='coerce')
            min_price = int(df['PRICE'].min())
            max_price = int(df['PRICE'].max())
        else:
            df['SALE_PRICE'] = pd.to_numeric(df.iloc[:, 13], errors='coerce')
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

        # Location and Project Filters
        location_options = ["All"] + list(df.iloc[:, 2].dropna().unique())
        selected_location = st.selectbox("Location", location_options)

        type_options = ["All"] + list(df.iloc[:, 3].dropna().unique())
        selected_type = st.selectbox("Project", type_options)

        # Profile and Reference Filters
        profile_options = ["All"] + list(df.iloc[:, 21].dropna().unique())
        selected_profile = st.selectbox("Profile", profile_options)

        reference_options = ["All"] + list(df.iloc[:, 22].dropna().unique())
        selected_reference = st.selectbox("Reference", reference_options)

        st.markdown('</div>', unsafe_allow_html=True)

        # Filtering Logic
        if filter_option == "Retail for Sale":
            filtered_data = df[df.iloc[:, 11] == "SALE"]
        else:
            filtered_data = df[df.iloc[:, 11] == "RENT"]

        # Apply filters
        if selected_location != "All":
            filtered_data = filtered_data[filtered_data.iloc[:, 2] == selected_location]
        if selected_type != "All":
            filtered_data = filtered_data[filtered_data.iloc[:, 3] == selected_type]
        if selected_profile != "All":
            filtered_data = filtered_data[filtered_data.iloc[:, 21] == selected_profile]
        if selected_reference != "All":
            filtered_data = filtered_data[filtered_data.iloc[:, 22] == selected_reference]

        filtered_data = filtered_data[
            (filtered_data['SIZE'] >= min_size_input) &
            (filtered_data['SIZE'] <= max_size_input)
        ]

        if filter_option == "Retail for Rent":
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
                {len(filtered_data)} Premium Retail Spaces Found
            </div>
        """, unsafe_allow_html=True)

        # Display Property Cards
        for _, row in filtered_data.iterrows():
            price_display = row['PRICE'] if filter_option == "Retail for Rent" else row['SALE_PRICE']

            st.markdown(f"""
            <div class="property-card">
                <div class="property-header">
                    <div class="property-title">{row['PROJECT']} - {row['LOCATION']}</div>
                    <div class="property-price">₹{price_display:,.2f}</div>
                </div>
                <div class="property-details">
                    <div class="detail-item">📏 {row['SIZE']} sq.ft.</div>
                    <div class="detail-item">🏬 {row['FLOOR']}</div>   
                    <div class="detail-item">📍 {row['UNIT NO.']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Mobile-Optimized Expandable Details
            with st.expander("View Details"):
                st.markdown(f"""
                    <div class="detail-section">
                        <p><strong>Date:</strong> {row['DATE']}</p>
                        <p><strong>Project:</strong> {row['PROJECT']}</p>
                        <p><strong>Location:</strong> {row['LOCATION']}</p>
                        <p><strong>Size:</strong> {row['SIZE']} sq.ft.</p>
                        <p><strong>Floor:</strong> {row['FLOOR']}</p>
                        <p><strong>Unit:</strong> {row['UNIT NO.']}</p>
                        <p><strong>Tower:</strong> {row['TOWER/BLOCK']}</p>
                        <p><strong>Maintenance:</strong> {row['MAINTENANCE']}</p>
                        <p><strong>Description:</strong> {row['DESCRIPTION']}</p>
                        <p><strong>Offered By:</strong> {row['OFFERED BY']}</p>
                        <p><strong>Profile:</strong> {row['PROFILE']}</p>
                        <p><strong>Reference:</strong> {row['REF']}</p>
                    </div>
                """, unsafe_allow_html=True)

    else:
        st.error("Unable to load retail data. Please try again later.")
