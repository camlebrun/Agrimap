import pandas as pd
import streamlit as st
import joblib as jbl
import plotly.express as px
import geopandas as gpd


def config():
    return st.set_page_config(layout="wide", page_title="AgriMap")

config()
df = pd.read_csv('data/data_ble.csv')

st.markdown(
    "<h1 style='text-align: center'> AgriMap </h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h3 style='text-align: center'> SIRE cultivons un avenir fertile </h3>",
    unsafe_allow_html=True,
)

france_geojson_url = "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements.geojson"
gdf_france = gpd.read_file(france_geojson_url)

df['geome'] = df['geome'].apply(eval)

# Create a scatter map with Plotly Express
fig = px.scatter_mapbox(
    df,
    lat=df['geome'].apply(lambda x: x['coordinates'][0]),
    lon=df['geome'].apply(lambda x: x['coordinates'][1]),
    color='norm',
    color_continuous_scale=['blue', 'green', 'red'],
    animation_frame='annee',
    opacity=0.5,
    mapbox_style="open-street-map",  # Utiliser la vue satellite
    center={"lat": 48, "lon": 40},
    zoom=2.3,
)

# Mise à jour des paramètres de la mise en page
fig.update_layout(
    transition={'duration': 1},  # Durée de transition
    width=1000,
    height=500,


)
st.plotly_chart(fig, use_container_width=True)

with st.expander("Dataset"):
    st.dataframe(df)
