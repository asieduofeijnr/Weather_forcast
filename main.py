import streamlit as st
import plotly.express as px
from backend import get_data

# Setting the title of the web application
st.title("Weather Forecast for the Next Days")

# Creating a text input box for the user to enter a location
place = st.text_input("Place: ")

# Creating a slider for the user to select the number of days to forecast
days = st.slider(
    "Forcast Days", min_value=1, max_value=5, help="Select the number of forcasted days"
)

# Creating a dropdown menu for the user to select which type of data to view
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

# Setting a subheader to display the selected option (either "Temperature" or "Sky"), the selected number of days, and the selected location
st.subheader(f"{option} for the next {days} days in {place}")

# Fetching the weather forecast data for the selected location and number of days using the get_data() function
# A try-except block is used to handle the case where the location is not found
try:
    filtered_data = get_data(place, days)
except KeyError:
    st.error("You typed a non existing place. Please correct and try again")

# Displaying the weather forecast data based on the selected option
if place:
    if option == "Temperature":
        # Extracting the temperature data from the forecast data
        temperatures = [(dict["main"]["temp"]) / 10 for dict in filtered_data]
        # Extracting the date data from the forecast data
        dates = [dict["dt_txt"] for dict in filtered_data]
        # Creating a line plot of temperature vs. date using Plotly Express
        fig = px.line(
            x=dates, y=temperatures, labels={"x": "Dates", "y": "Temperature (C)"}
        )
        # Displaying the plot using Streamlit
        st.plotly_chart(fig)

    if option == "Sky":
        # Mapping the sky conditions to their corresponding image paths
        images = {
            "Clear": "images/clear.png",
            "Clouds": "images/cloud.png",
            "Rain": "images/rain.png",
            "Snow": "images/snow.png",
        }
        # Extracting the sky condition data from the forecast data
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        # Extracting the date data from the forecast data
        dates = [dict["dt_txt"] for dict in filtered_data]
        # Mapping the sky conditions to their corresponding image paths
        image_paths = [images[conditions] for conditions in sky_conditions]
        # Displaying the images using Streamlit
        st.image(image_paths, width=115, caption=dates)
