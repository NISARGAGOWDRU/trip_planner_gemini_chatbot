import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import random
import urllib.parse

# Load the data
file_path = r"C:\Users\gowdr\OneDrive\Desktop\chatbot\tourist.csv"
data = pd.read_csv(file_path)

# Function to get unique countries from the data
def get_unique_countries():
    return data['Country'].unique()

# Function to generate random country suggestion
def get_random_country():
    countries = get_unique_countries()
    return random.choice(countries)

# Main app
def main():
    st.title("Tourist Recommendation System")

    option = st.radio("Would you like to specify a location or get a random suggestion?", 
                      ("Specify Location", "Get Random Suggestion"))

    if option == "Specify Location":
        countries = get_unique_countries()
        selected_country = st.selectbox("Choose a Country", countries)
    else:
        selected_country = get_random_country()
        st.write(f"Randomly selected country: {selected_country}")

    if selected_country:
        # Fixed coordinates for demonstration; replace with actual coordinates as needed
        country_coordinates = {
            "Belgium": (50.8503, 4.3517),
            "Australia": (-25.2744, 133.7751),
            "Canada": (56.1304, -106.3468),
            "Bengaluru": (12.9716, 77.5946),  # Example for Bengaluru
            # Add more countries and their coordinates here
        }

        location = country_coordinates.get(selected_country, (0, 0))

        # Create a map centered on the selected country
        map_ = folium.Map(location=location, zoom_start=5)
        folium.Marker(location, tooltip=selected_country).add_to(map_)

        # User query for recommendations
        user_query = st.text_input("Ask for travel recommendations (e.g., 'Find hotels and activities in this area')")

        if st.button("Get Recommendations"):
            if user_query:
                # Encode user query for URL
                query_encoded = urllib.parse.quote(user_query)
                google_maps_url = f"https://www.google.com/maps/search/?api=1&query={query_encoded}"

                st.write(f"**Here are some recommendations based on your query:**")
                st.write(f"[Click here to view on Google Maps]({google_maps_url})")

        # Display the map using st_folium
        st_folium(map_)

# Run the main function
if __name__ == "__main__":
    main()
