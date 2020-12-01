import pandas as pd
import plotly.offline as pyo
import plotly.graph_objects as go

# Read in CSV of precinct data
df = pd.read_csv('../Data/results_by_precinct.csv')

# Filter to needed columns
filteredDF = df[['County', 'Contest Name', 'Choice', 'Election Day',
                 'One Stop', 'Absentee by Mail', 'Provisional', 'Total Votes']]

# Filter to presidential election
presFilteredDF = filteredDF[filteredDF['Contest Name'] == 'US PRESIDENT']


#Test Data output
presFilteredDF.to_csv(r'../Data/testData.csv')