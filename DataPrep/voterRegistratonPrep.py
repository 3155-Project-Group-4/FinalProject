import plotly.express as px
import codecs
import pandas as pd

doc = codecs.open('../Data/ncvoter_Statewide.txt', 'rU', 'UTF-16')

df = pd.read_csv(doc, sep='\t')

dfFilteredCounty = df['county_id', 'voter_reg_num']

dfFilteredCounty = dfFilteredCounty.groupBy(['county_id'])

dfFilteredCounty.to_csv('testout.csv')
