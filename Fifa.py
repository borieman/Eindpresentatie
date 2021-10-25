import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
import requests
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.io as pio
pio.templates.default = 'seaborn'
import statsmodels.api as sm


st.beta_set_page_config(layout = "wide")

#Titel van de pagina
st.title("Fifa")

st.write("""
***
""")

# De rijen verwijderen waar kolom 9, 10 en 11 missende waardes zijn.
FIFA15['club_name'] = FIFA15['club_name'].fillna('No club')
FIFA15['league_name'] = FIFA15['league_name'].fillna('No league')
FIFA15['club_position'] = FIFA15['club_position'].fillna('No position')
FIFA16['club_name'] = FIFA16['club_name'].fillna('No club')
FIFA16['league_name'] = FIFA16['league_name'].fillna('No league')
FIFA16['club_position'] = FIFA16['club_position'].fillna('No position')
FIFA17['club_name'] = FIFA17['club_name'].fillna('No club')
FIFA17['league_name'] = FIFA17['league_name'].fillna('No league')
FIFA17['club_position'] = FIFA17['club_position'].fillna('No position')
FIFA18['club_name'] = FIFA18['club_name'].fillna('No club')
FIFA18['league_name'] = FIFA18['league_name'].fillna('No league')
FIFA18['club_position'] = FIFA18['club_position'].fillna('No position')
FIFA19['club_name'] = FIFA19['club_name'].fillna('No club')
FIFA19['league_name'] = FIFA19['league_name'].fillna('No league')
FIFA19['club_position'] = FIFA19['club_position'].fillna('No position')
FIFA20['club_name'] = FIFA20['club_name'].fillna('No club')
FIFA20['league_name'] = FIFA20['league_name'].fillna('No league')
FIFA20['club_position'] = FIFA20['club_position'].fillna('No position')
FIFA21['club_name'] = FIFA21['club_name'].fillna('No club')
FIFA21['league_name'] = FIFA21['league_name'].fillna('No league')
FIFA21['club_position'] = FIFA21['club_position'].fillna('No position')
FIFA22['club_name'] = FIFA22['club_name'].fillna('No club')
FIFA22['league_name'] = FIFA22['league_name'].fillna('No league')
FIFA22['club_position'] = FIFA22['club_position'].fillna('No position')

FIFA15['fifa_jaar'] = 'FIFA15'
FIFA16['fifa_jaar'] = 'FIFA16'
FIFA17['fifa_jaar'] = 'FIFA17'
FIFA18['fifa_jaar'] = 'FIFA18'
FIFA19['fifa_jaar'] = 'FIFA19'
FIFA20['fifa_jaar'] = 'FIFA20'
FIFA21['fifa_jaar'] = 'FIFA21'
FIFA22['fifa_jaar'] = 'FIFA22'

FIFA22_map = pd.DataFrame(FIFA22.groupby(['fifa_jaar', 'nationality'])['overall'].mean())

df = gpd.GeoDataFrame(pd.merge(FIFA22_map, countries, how = 'left', on = 'nationality'))

fig = folium.Map(location=[0, 0],
               zoom_start=2)

folium.Choropleth(geo_data=df,
                  name='geometry',
                  data=df,
                  columns=['nationality','overall'],
                  key_on='feature.properties.nationality', 
                  fill_color='YlGn', 
                  fill_opacity=0.9, 
                  line_opacity=0.3,
                  legend_name='Lagenda: Rating', 
                  nan_fill_color='black').add_to(m)

st.plotly_chart(fig)
