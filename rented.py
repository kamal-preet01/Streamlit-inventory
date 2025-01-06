import streamlit as st
from utils import get_google_sheet_data
import pandas as pd


def apply_premium_ui_styles():
    st.markdown("""
    <style>
    /* Premium Color Scheme */
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

/* Additional Details Section */
.additional-details {
    font-size: 0.85rem;
    margin-top: 8px;
    padding-top: 8px;
    border-top: 1px solid var(--border);
}

.additional-details p {
    margin: 4px 0;
    display: flex;
    justify-content: space-between;
    gap: 8px;
}

.additional-details strong {
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

# Rest of the code remains the same...


def display_rented_data():
    # Apply premium styling
    apply_premium_ui_styles()


    # Fetch data
    data = get_google_sheet_data("Rented")
    if data:
        df = pd.DataFrame(data[1:], columns=data[0])

        st.markdown('<div class="filter-panel">', unsafe_allow_html=True)

        # Price Filters
        col1, col2 = st.columns(2)
        with col1:
            df['PRICE'] = pd.to_numeric(df.iloc[:, 12], errors='coerce')
            min_price = int(df['PRICE'].min())
            max_price = int(df['PRICE'].max())

            price_col1, price_col2 = st.columns(2)
            with price_col1:
                min_price_input = st.number_input("Min Price (PSF) (₹)",
                                                  min_value=min_price,
                                                  max_value=max_price,
                                                  value=min_price)
            with price_col2:
                max_price_input = st.number_input("Max Price (PSF) (₹)",
                                                  min_value=min_price,
                                                  max_value=max_price,
                                                  value=max_price)

        # Property Filters
        col3, col4 = st.columns(2)
        with col3:
            category_options = ["All"] + list(df.iloc[:, 0].dropna().unique())
            selected_category = st.selectbox("Category", category_options)
            type_options = ["All"] + list(df.iloc[:, 3].dropna().unique())
            selected_type = st.selectbox("Property Type", type_options)
        with col4:
            configuration_options = ["All"] + list(df.iloc[:, 6].dropna().unique())
            selected_configuration = st.selectbox("Configuration", configuration_options)
            facing_options = ["All"] + list(df.iloc[:, 7].dropna().unique())
            selected_facing = st.selectbox("Facing", facing_options)

        # Location and Reference Filters
        col5, col6 = st.columns(2)
        with col5:
            location_options = ["All"] + list(df.iloc[:, 2].dropna().unique())
            selected_location = st.selectbox("Location", location_options)
        with col6:
            ref_options = ["All"] + list(df.iloc[:, 14].dropna().unique())
            selected_ref = st.selectbox("Reference", ref_options)

        st.markdown('</div>', unsafe_allow_html=True)

        # Filtering Logic
        filtered_data = df.copy()

        # Apply Filters
        if selected_category != "All":
            filtered_data = filtered_data[filtered_data.iloc[:, 0] == selected_category]
        if selected_location != "All":
            filtered_data = filtered_data[filtered_data.iloc[:, 2] == selected_location]
        if selected_type != "All":
            filtered_data = filtered_data[filtered_data.iloc[:, 3] == selected_type]
        if selected_configuration != "All":
            filtered_data = filtered_data[filtered_data.iloc[:, 6] == selected_configuration]
        if selected_facing != "All":
            filtered_data = filtered_data[filtered_data.iloc[:, 7] == selected_facing]
        if selected_ref != "All":
            filtered_data = filtered_data[filtered_data.iloc[:, 14] == selected_ref]

        # Price Filtering
        filtered_data = filtered_data[
            (filtered_data['PRICE'] >= min_price_input) &
            (filtered_data['PRICE'] <= max_price_input)
            ]

        # Results Counter
        st.markdown(f"""
            <div class="results-counter">
                {len(filtered_data)} Premium Properties Found
            </div>
        """, unsafe_allow_html=True)

        # Display Property Cards
        for _, row in filtered_data.iterrows():
            st.markdown(f"""
            <div class="property-card">
                <div class="property-header">
                    <div class="property-title">{row['COMPANY NAME']} - {row['BUILDING']}</div>
                    <div class="property-price">₹{row['PRICE']:,.2f}</div>
                </div>
                <div class="property-details">
                    <div class="detail-item">
                        <span>📏</span>
                        <span>{row['AREA (IN SQ.FT.) (A/T)']} sq.ft.</span>
                    </div>
                    <div class="detail-item">
                        <span>🏢</span>
                        <span>{row['UNIT NO.']} | Floor {row['FLOOR']}</span>
                    </div>
                    <div class="detail-item">
                        <span>📍</span>
                        <span>{row['LOCATION']}</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Expandable Details
            with st.expander("View Complete Details"):
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"""
                        <div class="detail-section">
                            <p><strong>Date:</strong> {row['DATE']}</p>
                            <p><strong>Building:</strong> {row['BUILDING']}</p>
                            <p><strong>Location:</strong> {row['LOCATION']}</p>
                            <p><strong>Company:</strong> {row['COMPANY NAME']}</p>  
                            <p><strong>Commencement:</strong> {row['COMMENCEMENT']}</p> 
                        </div>
                    """, unsafe_allow_html=True)
                with col2:
                    st.markdown(f"""
                        <div class="detail-section">
                            <p><strong>Rent PSF:</strong> ₹{row['RENT PSF']}</p>
                            <p><strong>Lease Rent:</strong> ₹{row['LEASE RENT']}</p>
                            <p><strong>Security:</strong> {row['SECURITY']}</p>
                            <p><strong>Term:</strong> {row['TERM']}</p>
                        </div>
                    """, unsafe_allow_html=True)
                st.markdown(f"""
                    <div class="additional-details">
                        <p><strong>Lock-in Period:</strong> {row['LOCKIN']}</p>
                        <p><strong>Increment:</strong> {row['INCREMENT']}</p>
                        <p><strong>Return:</strong> {row['RETURN']}</p>
                        <p><strong>Offered By:</strong> {row['OFFERED BY']}</p>
                    </div>
                """, unsafe_allow_html=True)

    else:
        st.error("Unable to load rented property data. Please try again later.")
