import streamlit as st
import urllib.parse


def render_plot(df):
    st.markdown("<h2 class='sub-header'>PLOTS</h2>", unsafe_allow_html=True)

    # Create filters for each column
    specific_positions = [2, 3, 5, 6, 7, 8, 11, 12, 13]

    # Select only the columns at the specified positions
    selected_columns = [df.columns[pos] for pos in specific_positions if pos < len(df.columns)]

    # Create columns for layout
    col1, col2, col3 = st.columns(3)
    filters = {}

    # Create filters only for the selected columns
    for i, column in enumerate(selected_columns):
        with [col1, col2, col3][i % 3]:
            unique_values = df[column].unique()
            filters[column] = st.multiselect(f"Filter by {column}", options=unique_values)

    # Apply filters
    filtered_df = df.copy()
    for column, selected_values in filters.items():
        if selected_values:
            filtered_df = filtered_df[filtered_df[column].isin(selected_values)]

    custom_column_names = {
        df.columns[2]: "Location",
        df.columns[5]: "Size",
        df.columns[6]: "Description",
        df.columns[7]: "Facing",
        df.columns[8]: "Road width",
    }

    # Submit button
    if st.button("Apply Filters"):
        # Display results
        st.markdown("<h3 class='sub-header'>Results</h3>", unsafe_allow_html=True)

        # Create a container for the cards
        st.markdown('<div class="card-container">', unsafe_allow_html=True)

        for _, row in filtered_df.iterrows():
            # Split columns into two groups
            half = len(df.columns) // 2
            left_columns = df.columns[1:half + 1]
            right_columns = df.columns[half + 1:]

            # Specify the columns you want in the WhatsApp message
            whatsapp_columns = [df.columns[2], df.columns[5], df.columns[6], df.columns[7], df.columns[8]]  # Custom columns for WhatsApp message


            # Create a formatted message for WhatsApp with only selected columns and custom names
            property_details = "\n".join([f"{custom_column_names.get(col, col)}: {row.get(col, 'N/A')}" for col in whatsapp_columns])
            whatsapp_message = f"Check out this Plot:\n\n{property_details}"
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

            # Close the container
        st.markdown('</div>', unsafe_allow_html=True)

        # Display a message if no results
        if filtered_df.empty:
            st.warning("No properties match the selected filters.")