import streamlit as st
import requests
import json
from datetime import datetime
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Global Weather Forecast",
    page_icon="🌤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# API configuration
API_KEY = "demo"  # Using demo mode for this example
BASE_URL = "http://api.openweathermap.org/data/2.5"

def get_weather_data(city_name):
    """Fetch current weather data for a city"""
    try:
        # For demo purposes, we'll simulate API responses
        # In production, you would use: f"{BASE_URL}/weather?q={city_name}&appid={API_KEY}&units=metric"
        
        # Simulated weather data for demo
        demo_data = {
            "London": {
                "name": "London",
                "country": "GB",
                "temp": 15.2,
                "feels_like": 14.1,
                "humidity": 72,
                "pressure": 1013,
                "wind_speed": 3.5,
                "description": "Partly cloudy",
                "icon": "02d"
            },
            "New York": {
                "name": "New York",
                "country": "US",
                "temp": 22.8,
                "feels_like": 24.1,
                "humidity": 65,
                "pressure": 1018,
                "wind_speed": 4.2,
                "description": "Clear sky",
                "icon": "01d"
            },
            "Tokyo": {
                "name": "Tokyo",
                "country": "JP",
                "temp": 18.5,
                "feels_like": 19.2,
                "humidity": 78,
                "pressure": 1015,
                "wind_speed": 2.8,
                "description": "Light rain",
                "icon": "10d"
            },
            "Paris": {
                "name": "Paris",
                "country": "FR",
                "temp": 16.7,
                "feels_like": 15.9,
                "humidity": 68,
                "pressure": 1012,
                "wind_speed": 3.1,
                "description": "Overcast",
                "icon": "04d"
            },
            "Sydney": {
                "name": "Sydney",
                "country": "AU",
                "temp": 25.3,
                "feels_like": 26.8,
                "humidity": 58,
                "pressure": 1020,
                "wind_speed": 5.2,
                "description": "Sunny",
                "icon": "01d"
            }
        }
        
        # Check if city exists in demo data
        for city_key in demo_data.keys():
            if city_name.lower() in city_key.lower():
                return demo_data[city_key], None
        
        # If city not found, return a generic response
        return {
            "name": city_name.title(),
            "country": "Unknown",
            "temp": 20.0,
            "feels_like": 21.0,
            "humidity": 60,
            "pressure": 1013,
            "wind_speed": 3.0,
            "description": "Clear sky",
            "icon": "01d"
        }, None
        
    except Exception as e:
        return None, str(e)

def get_forecast_data(city_name):
    """Fetch 5-day forecast data for a city"""
    try:
        # Simulated 5-day forecast data
        import random
        forecast_data = []
        base_temp = 20
        
        for i in range(5):
            date = datetime.now()
            date = date.replace(day=date.day + i)
            
            temp_variation = random.randint(-5, 8)
            forecast_data.append({
                "date": date.strftime("%Y-%m-%d"),
                "day": date.strftime("%A"),
                "temp_max": base_temp + temp_variation + 3,
                "temp_min": base_temp + temp_variation - 2,
                "description": random.choice(["Sunny", "Partly cloudy", "Cloudy", "Light rain", "Clear sky"]),
                "humidity": random.randint(45, 85),
                "wind_speed": round(random.uniform(2.0, 6.0), 1)
            })
        
        return forecast_data, None
        
    except Exception as e:
        return None, str(e)

def display_current_weather(weather_data):
    """Display current weather information"""
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.subheader(f"🌍 {weather_data['name']}, {weather_data['country']}")
        st.metric("Temperature", f"{weather_data['temp']:.1f}°C", 
                 delta=f"Feels like {weather_data['feels_like']:.1f}°C")
        st.write(f"**Condition:** {weather_data['description'].title()}")
    
    with col2:
        st.metric("Humidity", f"{weather_data['humidity']}%")
        st.metric("Pressure", f"{weather_data['pressure']} hPa")
    
    with col3:
        st.metric("Wind Speed", f"{weather_data['wind_speed']} m/s")
        st.write(f"**Updated:** {datetime.now().strftime('%H:%M')}")

def display_forecast(forecast_data):
    """Display 5-day weather forecast"""
    st.subheader("📅 5-Day Forecast")
    
    # Create columns for each day
    cols = st.columns(5)
    
    for i, day_data in enumerate(forecast_data):
        with cols[i]:
            st.write(f"**{day_data['day'][:3]}**")
            st.write(day_data['date'][5:])  # MM-DD format
            st.metric("High/Low", 
                     f"{day_data['temp_max']}°/{day_data['temp_min']}°")
            st.write(f"💧 {day_data['humidity']}%")
            st.write(f"💨 {day_data['wind_speed']} m/s")
            st.write(f"_{day_data['description']}_")

def main():
    # Header
    st.title("🌤️ Global Weather Forecast")
    st.markdown("Get real-time weather information for cities around the world")
    
    # Sidebar for popular cities
    st.sidebar.header("🏙️ Popular Cities")
    popular_cities = ["London", "New York", "Tokyo", "Paris", "Sydney", "Berlin", "Mumbai", "São Paulo"]
    
    selected_popular = st.sidebar.selectbox(
        "Quick select a city:",
        [""] + popular_cities
    )
    
    # Main search input
    col1, col2 = st.columns([3, 1])
    
    with col1:
        city_input = st.text_input(
            "🔍 Enter city name:",
            value=selected_popular if selected_popular else "",
            placeholder="e.g., London, New York, Tokyo..."
        )
    
    with col2:
        search_button = st.button("Get Weather", type="primary")
    
    # Search functionality
    if search_button or city_input:
        if city_input.strip():
            with st.spinner(f"Fetching weather data for {city_input}..."):
                # Get current weather
                weather_data, weather_error = get_weather_data(city_input)
                
                if weather_error:
                    st.error(f"Error fetching weather data: {weather_error}")
                elif weather_data:
                    # Display current weather
                    st.markdown("---")
                    display_current_weather(weather_data)
                    
                    # Get and display forecast
                    forecast_data, forecast_error = get_forecast_data(city_input)
                    
                    if forecast_error:
                        st.warning(f"Could not fetch forecast data: {forecast_error}")
                    elif forecast_data:
                        st.markdown("---")
                        display_forecast(forecast_data)
                    
                    # Additional information
                    st.markdown("---")
                    st.info("💡 **Tip:** Try searching for major cities like London, New York, Tokyo, Paris, or Sydney for demo data!")
                else:
                    st.error("Could not fetch weather data. Please try again.")
        else:
            st.warning("Please enter a city name to search for weather information.")
    
    # Instructions
    if not city_input:
        st.markdown("---")
        st.markdown("""
        ### 🌟 How to use:
        1. **Type a city name** in the search box above
        2. **Click "Get Weather"** or press Enter
        3. **View current conditions** and 5-day forecast
        4. **Use the sidebar** to quickly select popular cities
        
        ### 📍 Supported locations:
        - Major cities worldwide
        - Use format: "City" or "City, Country"
        - Examples: London, New York, Tokyo, Paris, Sydney
        """)
        
        # Sample weather cards for demonstration
        st.markdown("### 🌍 Sample Weather Data")
        sample_cols = st.columns(3)
        
        sample_cities = [
            {"name": "London", "temp": "15°C", "desc": "Partly cloudy", "emoji": "⛅"},
            {"name": "New York", "temp": "23°C", "desc": "Clear sky", "emoji": "☀️"},
            {"name": "Tokyo", "temp": "19°C", "desc": "Light rain", "emoji": "🌧️"}
        ]
        
        for i, city in enumerate(sample_cities):
            with sample_cols[i]:
                st.markdown(f"""
                <div style="padding: 1rem; border-radius: 10px; background-color: #f0f2f6; text-align: center;">
                    <h3>{city['emoji']} {city['name']}</h3>
                    <h2>{city['temp']}</h2>
                    <p>{city['desc']}</p>
                </div>
                """, unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666;">
        <p>🌤️ Global Weather Forecast | Built with Streamlit</p>
        <p><small>Note: This is a demo version with simulated data. In production, this would connect to a real weather API.</small></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()