# The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# Import Libraries
import pandas as pd
import numpy as np

# Read in data
football = pd.read_csv('football.csv')

# Parse data
football['Goal Difference'] = abs(football['Goals'] - football['Goals Allowed'])
min_difference = football['Goal Difference'].min()
football.set_index('Team', inplace = True)
team_min_difference = football.where(football['Goal Difference'] == min_difference).dropna().index[0]

print(team_min_difference)
