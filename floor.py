import streamlit as st
import urllib.parse

def share_selected_properties(selected_properties, custom_column_names, whatsapp_columns):
    # Prepare the message for multiple properties
    whatsapp_message = "Check out these Floors:\n\n"
    for row in selected_properties.values():
        property_details = "\n".join([f"{custom_column_names.get(col, col)}: {row.get(col, 'N/A')}" for col in whatsapp_columns])
        whatsapp_message += f"{property_details}\n\n"

    # Create the WhatsApp share URL
    whatsapp_url = f"https://wa.me/?text={urllib.parse.quote(whatsapp_message)}"

    # Display the URL to the user
    st.markdown(f"""
    <div style="background-color: #f0f0f0; padding: 10px; border-radius: 5px;">
        <p>Click the link below to share the selected properties on WhatsApp:</p>
        <a href="{whatsapp_url}" target="_blank" rel="noopener noreferrer">Share on WhatsApp</a>
    </div>
    """, unsafe_allow_html=True)

    st.info("If the link doesn't work, you can copy and paste it into your browser.")

def render_floor(df):
    st.markdown("<h2 class='sub-header'>FLOORS</h2>", unsafe_allow_html=True)

    # Initialize session state
    if 'filtered_df' not in st.session_state:
        st.session_state.filtered_df = df
    if 'filters_applied' not in st.session_state:
        st.session_state.filters_applied = False
    if 'selected_properties' not in st.session_state:
        st.session_state.selected_properties = {}

    # Create filters for specific columns
    specific_positions = [2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 17, 18, 21, 24]
    selected_columns = [df.columns[pos] for pos in specific_positions if pos < len(df.columns)]

    # Create columns for layout
    col1, col2, col3 = st.columns(3)
    filters = {}

    # Create filters only for the selected columns
    for i, column in enumerate(selected_columns):
        with [col1, col2, col3][i % 3]:
            unique_values = df[column].unique()
            filters[column] = st.multiselect(f"Filter by {column}", options=unique_values)

    custom_column_names = {
        df.columns[2]: "Location",
        df.columns[5]: "Size",
        df.columns[6]: "SQFT Built-Up Area",
        df.columns[7]: "Accommodation",
        df.columns[8]: "Type",
        df.columns[9]: "Description",
        df.columns[10]: "Purpose",
        df.columns[11]: "Facing",
        df.columns[12]: "Condition",
        df.columns[14]: "Lift",
        df.columns[15]: "STILT (Parking)",
        df.columns[16]: "PB (Power Backup)",
        df.columns[17]: "Floor available",
        df.columns[18]: "Rent",
    }

    # Specify the columns you want in the WhatsApp message
    whatsapp_columns = [df.columns[2], df.columns[5], df.columns[6], df.columns[7], df.columns[8], df.columns[9], df.columns[10], df.columns[11], df.columns[12], df.columns[14], df.columns[15], df.columns[16], df.columns[17], df.columns[18]]

    # Apply filters button
    if st.button("Apply Filters"):
        st.session_state.filtered_df = df.copy()
        for column, selected_values in filters.items():
            if selected_values:
                st.session_state.filtered_df = st.session_state.filtered_df[st.session_state.filtered_df[column].isin(selected_values)]
        st.session_state.filters_applied = True
        st.session_state.selected_properties = {}  # Reset selected properties when new filters are applied

    # Display results
    if st.session_state.filters_applied:
        st.markdown("<h3 class='sub-header'>Results</h3>", unsafe_allow_html=True)

        # Create a container for the cards
        st.markdown('<div class="card-container">', unsafe_allow_html=True)

        for index, row in st.session_state.filtered_df.iterrows():
            # Split columns into two groups
            half = len(df.columns) // 2
            left_columns = df.columns[1:half + 1]
            right_columns = df.columns[half + 1:]

            # Create a formatted message for WhatsApp with only selected columns and custom names
            property_details = "\n".join([f"{custom_column_names.get(col, col)}: {row.get(col, 'N/A')}" for col in whatsapp_columns])
            whatsapp_message = f"Check out this Floor:\n\n{property_details}"
            whatsapp_url = f"https://wa.me/?text={urllib.parse.quote(whatsapp_message)}"

            st.markdown(
                f"""
                <div class="property-card">
                    <div class="card-header">
                        <h3>{row.get(df.columns[2], 'N/A')}</h3>
                        <div class="whatsapp-share">
                            <a href="{whatsapp_url}" target="_blank" class="whatsapp-button">
                                Share WhatsApp
                            </a>
                        </div>
                    </div>
                    <div class="property-details">
                        <div class="property-column">
                            {''.join([f'<div class="property-item"><span class="property-label">{col}:</span> <span class="property-value">{row.get(col, "N/A")}</span></div>' for col in left_columns])}
                        </div>
                        <div class="property-column">
                            {''.join([f'<div class="property-item"><span class="property-label">{col}:</span> <span class="property-value">{row.get(col, "N/A")}</span></div>' for col in right_columns])}
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            # Add a checkbox for property selection without count number
            is_selected = st.checkbox("Select Property", key=f"select_{index}", value=index in st.session_state.selected_properties)
            if is_selected and index not in st.session_state.selected_properties:
                st.session_state.selected_properties[index] = row
            elif not is_selected and index in st.session_state.selected_properties:
                del st.session_state.selected_properties[index]

        # Close the container
        st.markdown('</div>', unsafe_allow_html=True)

        # Add a button to share selected properties
        if st.button("Share Selected Properties on WhatsApp"):
            if st.session_state.selected_properties:
                share_selected_properties(st.session_state.selected_properties, custom_column_names, whatsapp_columns)
            else:
                st.warning("Please select at least one property to share.")

        # Display a message if no results
        if st.session_state.filtered_df.empty:
            st.warning("No properties match the selected filters.")
