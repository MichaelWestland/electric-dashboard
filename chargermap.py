import requests
import streamlit as st
import folium
from branca.element import Template, MacroElement

config = {
  'baseUrl': 'https://api.openchargemap.io/v3',
  'apiKey': st.secrets["key"],
  'endpointPOI': '/poi'
}

def fetchPOI(payload):
  r = requests.get(f"{config['baseUrl']}{config['endpointPOI']}", params=payload, headers={'X-API-Key': config['apiKey']})
  return r.json()

def color_producer(len):
  if len == 1:
    return 'darkred'

  elif len == 2:
    return 'red'

  elif len == 3:
    return 'lightred'

  elif len <= 5:
    return 'orange'

  elif len <= 8:
    return 'lightgreen'

  elif len <= 11:
    return 'green'

  else:
    return 'darkgreen'

def createMap(args):
  data = fetchPOI(args)

  m = folium.Map(
    location=[args['latitude'], args['longitude']], 
    zoom_start=14, 
    tiles='CartoDB positron',
    width=800
  )

  for row in data:
    folium.Marker(
      location=[row['AddressInfo']['Latitude'], row['AddressInfo']['Longitude']],
      popup=folium.Popup(f"""
        <h4>{row['AddressInfo']['Title']}</h4>

        <b>{row['AddressInfo']['AddressLine1']}</b> <br>
        <b>{row['AddressInfo']['Town']}</b> <br>
        <b>{row['AddressInfo']['Postcode']}</b> <br>
        <b>{row['AddressInfo']['Country']['Title']}</b> <br>

        <p>Aantal opladers: {row['NumberOfPoints']}</p>
        """,
        min_width=200,
        max_width=1000
      ),
      
      icon=folium.Icon(color=color_producer(row['NumberOfPoints']), icon="plug", prefix='fa')
    ).add_to(m)

  return m