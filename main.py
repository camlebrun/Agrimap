import streamlit as st
import pandas as pd
import joblib as jbb
import plotly.express as px
import geopandas as gpd



def config():
    return st.set_page_config(
    layout="wide",
    page_title="Visualisation Hackathon"
    )

config()

# Chargez le fichier .pickle avec joblib
df = jbb.load("C:/Users/anton/Desktop/Data/Master2/hackaton/Bio_indices(1).pickle")

# Convertissez le fichier joblib en un df pandas
df_pandas = pd.DataFrame(df)

st.title('Hackathon Groupe 6')

dataset, carte_france = st.tabs(['Dataset', 'Carte de France'])

with dataset:
    st.dataframe(df_pandas)

with carte_france:
    # Charger les limites géographiques de la France
    france_geojson_url = "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements.geojson"
    gdf_france = gpd.read_file(france_geojson_url)

    # Création de la carte avec Plotly Express
    fig = px.choropleth_mapbox(
        gdf_france,
        geojson=gdf_france.geometry,
        locations=gdf_france.index,
        color_discrete_map={0: 'gray'},  # Utilisation d'une seule couleur (gris dans cet exemple)
        mapbox_style="carto-positron",
        center={"lat": 46.6031, "lon": 1.8883},
        zoom=5,
    )

    # Affichage de la carte dans Streamlit
    st.plotly_chart(fig)