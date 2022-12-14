import datetime
from time import time
import pandas as pd
import csv, json
from geojson import Feature, FeatureCollection, Point
import numpy as np

df = pd.read_csv('Enter your file location here')

# to see what all columns are present in the csv file and information related to it
df.info()
df.decsribe()

features = []

for ind in df.index:
    features.append(
            Feature(
                geometry=Point([df.loc[ind,'lon'],df.loc[ind,'lat']]),
                properties = {
                    'time' : df.loc[ind,'time'],
                    # like the above key value pair 
                    # you can add many other pairs based on the properties you want from the csv
                }
            )
        )

collection  = FeatureCollection(features)
with open("Enter the json file location where this geoJSON should be stored", "w") as f:
    f.write('%s' % collection)
