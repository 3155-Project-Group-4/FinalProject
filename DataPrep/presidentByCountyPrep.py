import pandas as pd


# Read in CSV of precinct data
df = pd.read_csv('../Data/president_county_candidate.csv')

filteredByStateDF = df[df['state'] == 'North Carolina']

filteredByStateDF.to_csv('../DataPrep/testFilter.csv')

filteredByWinDF = filteredByStateDF[filteredByStateDF['won'] == True].reset_index()

filteredByWinDF['county'] = filteredByWinDF['county'].str.upper()

filteredByWinDF['county'] = filteredByWinDF['county'].str.replace(' COUNTY', '')

filteredByWinDF.to_csv('../DataPrep/presidentByCountyWin.csv')

