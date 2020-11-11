import numpy as np
import pandas as pd

#Attibutes that will be used:

columns = [
    'Crossing', 'Finishing','HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling', 'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration', 'SprintSpeed', 'Agility', 'Reactions', 'Balance', 'ShotPower', 'Jumping', 'Stamina', 'Strength', 'LongShots', 'Aggression', 'Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure', 'Marking', 'StandingTackle', 'SlidingTackle', 'GKDiving', 'GKHandling', 'GKKicking', 'GKPositioning', 'GKReflexes','Weak Foot','Work Rate', 'Position'
]

#Opening the dataset
data = pd.read_csv('data.csv'
           , usecols = columns
           )
