import plotly.express as px
import pandas as pd


# makes bar chart for total senate president and governor votes in north carolina

df = df = pd.read_csv('../Data/results_by_precinct.csv')

filteredDF = df.groupby(['Contest Name']).sum().reset_index()

filteredDF = filteredDF.loc[(filteredDF['Contest Name'] == 'US SENATE') | (filteredDF['Contest Name'] == 'US PRESIDENT') | (filteredDF['Contest Name'] == 'NC LIEUTENANT GOVERNOR')].reset_index()

filteredDF.to_csv('totalVotes.csv')

fig = px.bar(filteredDF, x='Contest Name', y='Total Votes')

fig.show()