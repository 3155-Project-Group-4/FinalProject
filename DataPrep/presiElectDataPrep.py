import pandas as pd


# Read in CSV of precinct data
df = pd.read_csv('../Data/results_by_precinct.csv')

# Filter to needed columns
filteredDF = df[['County', 'Contest Name', 'Choice', 'Election Day',
                 'One Stop', 'Absentee by Mail', 'Provisional', 'Total Votes']]

# Filter to presidential election
presFilteredDF = filteredDF[filteredDF['Contest Name'] == 'US PRESIDENT']

# Sort by county alpha
presFilteredDF = presFilteredDF.sort_values('County')

# Group By Choice
presFilteredDF = presFilteredDF.groupby(['County', 'Choice']).sum().reset_index()

# Data is now in the form

# ------    -------    --------------      --------    ----------------    -----------     ------------
# County    Choice      Election Day       One Stop    Absentee by Mail    Provisional     Total Votes
# ------    -------    --------------      --------    ----------------    -----------     ------------

