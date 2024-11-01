Tourist Recommendation System 🌍
Overview
This project is a Tourist Recommendation System web app built using Streamlit, Folium, and Pandas. It helps users explore tourist destinations by specifying a location or receiving a random country suggestion. The app also provides the ability to request travel recommendations and view results via an interactive map interface.

Features
User Interaction: Choose a country from a dropdown or get a random suggestion.
Map Visualization: Display an interactive map centered on the selected location with a marker.
Travel Recommendations: Accepts user queries for travel-related suggestions and provides a link to view results directly on Google Maps.
Dynamic UI: Uses Streamlit for an intuitive and responsive user interface.
Country Selection: Utilizes a CSV file with country data for location selection.
How It Works
Specify Location: The user can choose a country from a dropdown list populated with unique country names from the dataset.
Random Country Suggestion: The app can also suggest a random country for users who are undecided.
Map Generation: A Folium map is created and displayed, centered on the selected country's coordinates.
Recommendations: Users can input a travel query, such as "Find hotels and activities in this area," and receive a Google Maps link to explore further.
Technologies Used
Streamlit: For building the web application.
Folium: For creating and displaying interactive maps.
Pandas: For data handling and processing.
Python Standard Libraries: random, urllib.parse.
Installation
Clone this repository:
bash
Copy code
git clone https://github.com/yourusername/tourist-recommendation-system.git
Navigate to the project directory:
bash
Copy code
cd tourist-recommendation-system
Install required packages:
bash
Copy code
pip install streamlit pandas folium streamlit-folium
Run the application:
bash
Copy code
streamlit run app.py
Data Requirement
Ensure you have a CSV file containing country data at the specified file path (C:\Users\gowdr\OneDrive\Desktop\chatbot\tourist.csv), with a column named Country.

Usage
Run the app and open the web page.
Choose a country or let the app suggest one randomly.
View the map with the selected location.
Enter a travel query to receive recommendations and click on the link to view more details on Google Maps.
Example Coordinates
Pre-defined country coordinates are used for demonstration:

Belgium: (50.8503, 4.3517)
Australia: (-25.2744, 133.7751)
Canada: (56.1304, -106.3468)
Bengaluru: (12.9716, 77.5946)
(More can be added as needed)
Future Enhancements
Integrate APIs for real-time travel data and recommendations.
Enhance the dataset with more countries and coordinates.
Add advanced features like hotel and restaurant search, activity suggestions, etc.
License
This project is open-source and available under the MIT License.
