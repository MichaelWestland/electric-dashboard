import streamlit as st
from streamlit_folium import folium_static

import cumsum
import chargermap
import hist

# Page config
st.set_page_config(
  page_title='Dashboard elektrische auto\'s',
  layout='wide',
  menu_items={
    'Get Help': None,
    'Report a bug': None
  }
)

st.markdown("## Dashboard elektrische auto's")
st.caption(" Door Boaz Geelhoed (500825279), Karlijn Huissen (500889478), Michael Westland (500889605) en Tessa Troostheide (500799202) - Groep 8")

col1, col2 = st.columns(2)

with col1:
  st.plotly_chart(cumsum.createCumSum(), use_container_width=True)
with col2:
  st.plotly_chart(hist.createHist(), use_container_width=True)

st.image('regression.png')

gemeente = st.selectbox('Selecteer regio', ('Amsterdam', 'Utrecht', 'Den Haag', 'Rotterdam'))

def getLonLat(gemeente):
  if gemeente == 'Amsterdam':
    return { 'latitude': 52.3777303, 'longitude': 4.8991132 }
  elif gemeente == 'Utrecht':
    return { 'latitude': 52.089479223083025, 'longitude': 5.109103972999964 }
  elif gemeente == 'Den Haag':
    return { 'latitude': 52.0811417352647, 'longitude': 4.324177288201205 }
  elif gemeente == 'Rotterdam':
    return { 'latitude': 51.92528749996545, 'longitude': 4.467948131552581 }

col1, col2 = st.columns([1.2, 1])

with col1:
  folium_static(chargermap.createMap({
    'maxresults': 250,
    'countrycode': 'nl',
    'distanceunit': 'KM',
    'latitude': getLonLat(gemeente)['latitude'],
    'longitude': getLonLat(gemeente)['longitude']
  }))
with col2:
  html_string = f"""
  <h3>Locatie van laadpalen rondom {gemeente}</h3>
  <h5>Legenda</h5>

  <p><span style='color: rgb(159, 50, 54)'>⬤</span> 1 oplader</p>
  <p><span style='color: rgb(207, 60, 41)'>⬤</span> 2 opladers</p>
  <p><span style='color: rgb(255, 141, 126)'>⬤</span> 3 opladers</p>
  <p><span style='color: rgb(245, 150, 48)'>⬤</span> 4 of 5 opladers</p>
  <p><span style='color: rgb(187, 249, 112)'>⬤</span> 6, 7 of 8 opladers</p>
  <p><span style='color: rgb(111, 171, 37)'>⬤</span> 9, 10 of 11 opladers</p>
  <p><span style='color: rgb(112, 128, 35)'>⬤</span> Meer dan 11 opladers</p>
  """

  st.markdown(html_string, unsafe_allow_html=True)