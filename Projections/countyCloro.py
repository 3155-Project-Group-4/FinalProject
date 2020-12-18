# GEO JSON FOR COUNTIES https://opendata.arcgis.com/datasets/34acbf4a26784f189c9528c1cf317193_0.geojson

import pandas as pd
import plotly.express as px
import plotly.offline as pyo
import plotly.graph_objects as go
from urllib.request import urlopen
import json
with urlopen('https://opendata.arcgis.com/datasets/34acbf4a26784f189c9528c1cf317193_0.geojson') as response:
    counties = json.load(response)


df = pd.read_csv('../DataPrep/presidentByCountyWin.csv')

fig = px.choropleth(df, geojson=counties, color='candidate', locations='county', featureidkey='properties.CO_NAME', color_discrete_map={'Donald Trump':'red', 'Joe Biden':'blue'}, hover_data=['total_votes'])
fig.update_geos(fitbounds='locations', visible=False)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


figCholoro = fig