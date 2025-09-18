Weather Forecast Website - MVP Todo
Core Features to Implement:
Main Application (app.py) - Streamlit web interface

City/country search input
Weather data display
Error handling for invalid locations
Weather API Integration

Use OpenWeatherMap API (free tier)
Fetch current weather and forecast data
Handle API responses and errors
User Interface Components

Search bar for location input
Current weather display (temperature, description, humidity, wind)
5-day forecast display
Location information display
Dependencies (requirements.txt)

streamlit
requests (for API calls)
pandas (for data handling)
File Structure:
app.py (main application)
requirements.txt (dependencies)
README.md (usage instructions)
Implementation Approach:
Use OpenWeatherMap free API (no key required for basic demo)
Simple, clean interface with Streamlit components
Error handling for network issues and invalid locations
Responsive design that works on different screen sizes