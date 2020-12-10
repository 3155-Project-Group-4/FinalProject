# GEO JSON FOR COUNTIES https://opendata.arcgis.com/datasets/34acbf4a26784f189c9528c1cf317193_0.geojson

import pandas as pd
import plotly.express as px

# Cant use this unless you wanna download the 3 gig statewide file
# df = pd.read_csv('../Data/ncvoter_Statewide.csv', dtype={'voter_reg_number': int, 'birth_year': int})
#
# filteredDF = df[['county_desc', 'ncid']]
#
# print(filteredDF)
#
# filteredDF.to_csv('../Data/ncvoter_StatewideFiltered.csv')


# df = pd.read_csv('../Data/ncvoter_StatewideFiltered.csv')
#
# countedOutDf = df.groupby(['county_desc']).agg(['mean', 'count'])
# countedOutDf.columns = countedOutDf.columns.droplevel(0)
# countedOutDf.to_csv('../Data/outByCounty.csv')

countedOutDf = pd.read_csv('../Data/outByCounty.csv')

figBarRegisteredVoters = px.bar(countedOutDf, x='county_desc', y='count', labels = {'county_desc' : 'County', 'count' : 'Number Of Registered Voters'}, title = 'Number of Registered Voters by County in North Carolina')



