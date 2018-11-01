import numpy as np
import pandas as pd
from read_data import read_data
from sklearn import tree, preprocessing

# This is a project that will predict the success of
# a Fantasy Football player for the coming week.
# It will take into account position, average weekly score,
# last weeks score, rank of opposing defense
# vs. the run, rank of opposing defense vs. pass, points
# allowed by opposing defense and other things
# I think of
# edit:
# many more categories have been added to the data, including
# opponent offensive stats, whether or not it's a division matchup,
# and (simply enough) the player's own team.

# First retrieve the data for all past weeks of RB performance
train_link = "combined_rb_stats_2.csv"
rb_data = read_data(train_link)

# Separate the data from the targets
rb_data, rb_targets = rb_data.iloc[:, :-2], rb_data.iloc[:, -1]

# The following section will be encoding the categorical data into numerical data
# Encoding player NAMES
le_names = preprocessing.LabelEncoder()
le_names.fit(rb_data['Name'])
rb_names = list(le_names.classes_)
rb_data['Name'] = le_names.transform(rb_data['Name'])

# Encoding player POSITION
le_pos = preprocessing.LabelEncoder()
le_pos.fit(rb_data['Pos'])
rb_pos = list(le_pos.classes_)
rb_data['Pos'] = le_pos.transform(rb_data['Pos'])

# Encoding player OPPONENT
le_opp = preprocessing.LabelEncoder()
le_opp.classes_ = ['ARI', 'ATL', 'BAL', 'BUF', 'CAR', 'CHI', 'CIN', 'CLE',
                   'DAL', 'DEN', 'DET', 'GB', 'HOU', 'IND', 'JAX', 'KC',
                   'LAC', 'LAR', 'MIA', 'MIN', 'NE', 'NO', 'NYG', 'NYJ',
                   'OAK', 'PHI', 'PIT', 'SEA', 'SAN', 'TB', 'TEN', 'WAS',
                   'BYE']
rb_opp = list(le_opp.classes_)
rb_data['Opp'] = le_opp.transform(rb_data['Opp'])

# Encoding player TEAM
le_team = preprocessing.LabelEncoder()
rb_team = list(le_opp.classes_)
rb_data['Team'] = le_opp.transform(rb_data['Team'])

# Encoding DIVISION RIVAL
le_div = preprocessing.LabelEncoder()
le_div.fit(rb_data['Div Rival?'])
div_rival = list(le_div.classes_)
rb_data['Div Rival?'] = le_div.transform(rb_data['Div Rival?'])

# Now we're retrieving this weeks data
test_link = "fantasy_rb_week9_2.csv"
rb_data2 = read_data(test_link)

# Separate this data
rb_data2, rb_targets2 = rb_data2.iloc[:, :-2], rb_data2.iloc[:, -1]

# Encode this data
rb_data2['Name'] = le_names.transform(rb_data2['Name'])
rb_data2['Pos'] = le_pos.transform(rb_data2['Pos'])
rb_data2['Opp'] = le_opp.transform(rb_data2['Opp'])
rb_data2['Team'] = le_opp.transform(rb_data2['Team'])
rb_data2['Div Rival?'] = le_div.transform(rb_data2['Div Rival?'])

# Fill any NaN's with 0's
rb_data = rb_data.fillna(0)
rb_data2 = rb_data2.fillna(0)

# Create a list to hold the predictions
prediction_list = []

# Run a loop 1000 times, each time creating a new tree and getting it's
# predictions for each player
for x in range(0, 1000):
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(rb_data, rb_targets)
    weekly_predictions = clf.predict(rb_data2)
    prediction_list.append(weekly_predictions)

full_stats_list = []

# Now we're going to restructure the list so that we have a list of lists
# and the inner list's are player specific, each containing all of the
# predictions for that specific player
for y in range(0, len(weekly_predictions)):
    player_y_list = []
    z = 1
    for prediction in prediction_list:
        player_y_list.append(prediction[y])
        z += 1

    full_stats_list.append(player_y_list)

# De-encode the NAMES of the players, for display purposes
rb_data2['Name'] = le_names.inverse_transform(rb_data2['Name'])

# Now we're going to iterate through the list, getting a count
# of how many predictions for the player are yes, and how many are no.
# We will display this as a percentage, but whichever has the majority
# will be considered the prediction.
# We will display the player name, the percentage, and the prediction.
for index, row in rb_data2.iterrows():

    percent = (full_stats_list[index].count('Y')/10)
    predict = ""

    if percent < 50:
        predict = "will NOT"

    elif percent >= 50:
        predict = "WILL"

    print("\nOur confidence that {} will surpass 12 pts "
          "this week is {}%".format(rb_data2['Name'].loc[index], percent))
    print("Therefore, we predict that {} {} surpass 12 pts.".format(rb_data2['Name'].loc[index], predict))

