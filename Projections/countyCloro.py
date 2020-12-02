# GEO JSON FOR COUNTIES https://opendata.arcgis.com/datasets/34acbf4a26784f189c9528c1cf317193_0.geojson

import pandas as pd
import plotly.express as px
import plotly.offline as pyo
import plotly.graph_objects as go
from urllib.request import urlopen
import json
with urlopen('https://opendata.arcgis.com/datasets/34acbf4a26784f189c9528c1cf317193_0.geojson') as response:
    counties = json.load(response)

df = pd.read_csv('../Data/testData.csv')

fig = px.choropleth(df, geojson=counties, color='County', locations='County', featureidkey='properties.CO_NAME')
fig.update_geos(fitbounds='locations', visible=False)
fig.update_traces(zauto=True)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()