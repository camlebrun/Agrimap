import streamlit as st
import pandas as pd
import joblib as jbl
import plotly.express as px
import geopandas as gpd

# Function to configure Streamlit page
def config():
    return st.set_page_config(
        layout="wide",
        page_title="AgriMap"
    )

config()

# Load the .pickle file using joblib
df = jbl.load("Bio_indices(1).pickle")

# Convert the joblib file to a pandas DataFrame
df_pandas = pd.DataFrame(df)

# Display the title and additional information using markdown
st.markdown(
    "<h1 style='text-align: center'> AgriMap : SIRE cultivons</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h3 style='text-align: center'> Add info</h3>",
    unsafe_allow_html=True,
)

# Load the geographical boundaries of France
france_geojson_url = "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements.geojson"
gdf_france = gpd.read_file(france_geojson_url)

# Use st.slider instead of st.select_slider
year_option = list(range(2000, 2024))
year = st.slider("**Select year**", min_value=min(year_option), max_value=max(year_option))

# Create a choropleth map with Plotly Express
fig = px.choropleth_mapbox(
    gdf_france,
    geojson=gdf_france.geometry,
    locations=gdf_france.index,
    color_continuous_scale="reds",
    color=gdf_france.index,
    range_color=(gdf_france.index.min(), gdf_france.index.max()),
    mapbox_style="carto-positron",
    center={"lat": 46.6031, "lon": 1.8883},
    zoom=4.5
)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.update_layout(width=1100, height=500)

# Display the map in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Use st.expander to create an expandable section for the dataset
with st.expander("Dataset"):
    st.dataframe(df_pandas)
