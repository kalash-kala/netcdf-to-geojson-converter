import datetime
from time import time
import pandas as pd
import csv, json
from geojson import Feature, FeatureCollection, Point
import numpy as np


df = pd.read_csv('add the path of the converted CSV file')

df = df.sample(20000)

print(df.index.size)

df.index = range(df.index.size)

print(df.head())

# converting the data type as int64 is not an acceptable JSON format
df['elevation'] = df['elevation'].astype('float64')

features = []

for ind in df.index:
    features.append(
            Feature(
                geometry=Point([df.loc[ind,'lon'],df.loc[ind,'lat']]),
                properties = {
                    'elevation' : df.loc[ind,'elevation']
                }
            )
        )

collection  = FeatureCollection(features)
with open("add the destination json file location here", "w") as f:
    f.write('%s' % collection)
