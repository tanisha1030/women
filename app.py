import streamlit as st
import folium
from streamlit_folium import st_folium
from folium.plugins import HeatMap

st.set_page_config(page_title="Women Safety Map", layout="wide")

st.title("🚨 Women Safety - Danger Zones Map")

# Base map centered at New Delhi
m = folium.Map(location=[28.6139, 77.2090], zoom_start=12, tiles="CartoDB positron")

# Define danger zones
danger_zones = [
    {
        "name": "Zone A - High Risk",
        "coordinates": [[28.62, 77.20], [28.63, 77.21], [28.62, 77.22], [28.61, 77.21]],
        "color": "red"
    },
    {
        "name": "Zone B - Moderate Risk",
        "coordinates": [[28.60, 77.18], [28.61, 77.19], [28.60, 77.20], [28.59, 77.19]],
        "color": "orange"
    },
    {
        "name": "Zone C - Low Risk",
        "coordinates": [[28.58, 77.22], [28.59, 77.23], [28.58, 77.24], [28.57, 77.23]],
        "color": "green"
    }
]

# Add polygons for danger zones
for zone in danger_zones:
    folium.Polygon(
        locations=zone["coordinates"],
        color=zone["color"],
        fill=True,
        fill_color=zone["color"],
        fill_opacity=0.5,
        tooltip=zone["name"]
    ).add_to(m)

# Optionally add heatmap (simulated points)
crime_points = [
    [28.6139, 77.2090],
    [28.6145, 77.2100],
    [28.6120, 77.2080],
    [28.6100, 77.2060],
    [28.6110, 77.2075],
    [28.6150, 77.2110]
]

HeatMap(crime_points).add_to(m)

# Display the map
st_data = st_folium(m, width=900, height=600)
