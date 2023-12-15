import streamlit as st
import time
st.set_page_config(layout="wide", page_title="AgriMap")

st.markdown(
    "<h1 style='text-align: center'> AgriMap </h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h3 style='text-align: center'> Amélioration : utilisez vos données </h3>",
    unsafe_allow_html=True,
)
with st.form("Ajouter vos données"):
   txt = st.code(
"""    wheat_requirements = {
    'mean_temperature': 291.761,
    'Maximum_temperature_of_warmest_month': 298.15,
    'Minimum_temperature_of_coldest_month': 268.15,
    'Precipitation_of_driest_month': 1.52e-07,
    'Precipitation_of_wettest_month':2.28e-07,
    'Annual_precipitation': 4.253e-07,
    }"""
    )   
   submitted = st.form_submit_button("Envoyer")
if submitted:
        with st.spinner('Veuillez patienter...'):
            time.sleep(5)
            st.success('Fini !')
            st.write("C'est une démo, rien n'a été envoyé !")