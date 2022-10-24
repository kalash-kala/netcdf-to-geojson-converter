import datetime
from time import time
import pandas as pd
import csv, json
from geojson import Feature, FeatureCollection, Point
import numpy as np

df = pd.read_csv('enter the path of cleaned or uncleaned csv')

print(df['time'].value_counts())

# Creates a dataframe consisting of data at a particular date and time
df = df[df['time']=="2022-03-17 00:00:00"]

print(df.info())
print(df.describe())

print(df.sample(5))

features = []

for ind in df.index:
    features.append(
            Feature(
                geometry=Point([df.loc[ind,'lon'],df.loc[ind,'lat']]),
                properties = {
                    # added the parameters associated with the geometry (Point)
                    'time' : df.loc[ind,'time'],
                    'uwnd' : df.loc[ind,'uwnd'],
                    'vwnd' : df.loc[ind,'vwnd'],
                    'dir' : df.loc[ind,'dir'],
                }
            )
        )

collection  = FeatureCollection(features)
with open("Enter the location of destination json file", "w") as f:
    f.write('%s' % collection)
