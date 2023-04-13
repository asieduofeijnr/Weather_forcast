import streamlit as st
import plotly.express as px
import backend as bk

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider(
    "Forcast Days", min_value=1, max_value=5, help="Select the number of forcasted days"
)
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")


data = bk.get_data(place, days, option)


d, t = bk.get_data(days)

fig = px.line(x=d, y=t, labels={"x": "Dates", "y": "Temperature (C)"})
st.plotly_chart(fig)
