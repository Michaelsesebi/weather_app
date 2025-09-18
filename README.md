Global Weather Forecast Website
A Python-based web application built with Streamlit that allows users to view weather forecasts for cities around the world.

Features
🌍 Global Coverage: Search for weather in any city worldwide
🌤️ Current Weather: Real-time temperature, humidity, pressure, and wind data
📅 5-Day Forecast: Extended weather predictions
🏙️ Popular Cities: Quick access to major cities
📱 Responsive Design: Works on desktop and mobile devices
How to Use
Search for a City: Enter any city name in the search box
View Current Weather: See temperature, conditions, and atmospheric data
Check Forecast: View the 5-day weather prediction
Quick Select: Use the sidebar to quickly select popular cities
Installation & Setup
Clone or download this project
Install dependencies:
pip install -r requirements.txt
Run the application:
streamlit run app.py
Open your browser and navigate to the provided local URL (usually http://localhost:8501)
Demo Data
This version includes demo data for popular cities including:

London, UK
New York, USA
Tokyo, Japan
Paris, France
Sydney, Australia
Production Setup
For production use, you would need to:

Sign up for a weather API service (e.g., OpenWeatherMap)
Get an API key
Replace the demo data with actual API calls
Add error handling for API rate limits
Technologies Used
Streamlit: Web framework for Python
Requests: HTTP library for API calls
Pandas: Data manipulation and analysis
License
This project is open source and available under the MIT License.

Editor
