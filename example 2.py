# import csv
# import netCDF4 as nc
# from netcdf2csv import convert_dir

# convert_dir(netcdf_dir='/Users/kalashkala/Desktop/Python Code/nc-to-json/bathymetry',csv_dir='/Users/kalashkala/Desktop/Python Code/nc-to-json/csvfile',cleaned_csv_dir='/Users/kalashkala/Desktop/Python Code/nc-to-json/cleaned csv file',clean_choice=1)

import datetime
from time import time
import pandas as pd
import csv, json
from geojson import Feature, FeatureCollection, Point
import numpy as np

df = pd.read_csv('/Users/kalashkala/Desktop/Python Code/nc-to-json/cleaned csv file/cleaned_ww3_fcs_glo_1.0.csv')
# df['time'] = pd.to_datetime(df['time'],infer_datetime_format=True)

print(df['time'].value_counts())

#cd1 = datetime.datetime.strptime("2022-03-17 00:00:00",'%Y-%m-%d %H:%M:%S')
df = df[df['time']=="2022-03-17 00:00:00"]

for col in df.columns:
    print(col, " : ", df[col].isna().sum())


print(df.info())
print(df.iloc[0])

# features = []

# for ind in df.index:
#     features.append(
#             Feature(
#                 geometry=Point([df.loc[ind,'lon'],df.loc[ind,'lat']]),
#                 properties = {
#                     'time' : df.loc[ind,'time'],
#                     'uwnd' : df.loc[ind,'uwnd'],
#                     'vwnd' : df.loc[ind,'vwnd'],
#                     'hs' : df.loc[ind,'hs'],
#                     't0m1' : df.loc[ind,'t0m1'],
#                     'dir' : df.loc[ind,'dir'],
#                     'phs01' : df.loc[ind,'phs01'],
#                     'phs02' : df.loc[ind,'phs02'],
#                     'pdi01' : df.loc[ind,'pdi01'],
#                     'pdi02' : df.loc[ind,'pdi02'],
#                 }
#             )
#         )

# collection  = FeatureCollection(features)
# with open("/Users/kalashkala/Desktop/Python Code/nc-to-json/particular date GeoJSON.json", "w") as f:
#     f.write('%s' % collection)


# Bathymetry :

# df = df.sample(20000)

# print(df.index.size)

# df.index = range(df.index.size)

# print(df.head())
# df['elevation'] = df['elevation'].astype('float64')

# features = []

# for ind in df.index:
#     features.append(
#             Feature(
#                 geometry=Point([df.loc[ind,'lon'],df.loc[ind,'lat']]),
#                 properties = {
#                     'elevation' : df.loc[ind,'elevation']
#                 }
#             )
#         )

# collection  = FeatureCollection(features)
# with open("/Users/kalashkala/Desktop/Python Code/nc-to-json/bathymetry geoJSON.json", "w") as f:
#     f.write('%s' % collection)

# import csv, json
# from geojson import Feature, FeatureCollection, Point
# import numpy as np

# features = []
# with open('/Users/kalashkala/Desktop/Python Code/nc-to-json/cleaned csv file/cleaned_ww3_fcs_glo_1.0.csv',newline='') as csvfile:
#     reader = csv.reader(csvfile, delimiter=',')
#     for lon,lat,time,uwnd,vwnd,hs,t0m1,direction,phs01,phs02,pdi01,pdi02 in reader:
        
#         features.append(
#             Feature(
#                 geometry=Point([float(lat),float(lon)]),
#                 properties = {
#                     'time' : time,
#                     'uwnd' : uwnd,
#                     'vwnd' : vwnd,
#                     'hs' : hs,
#                     't0m1' : t0m1,
#                     'direction' : direction,
#                     'phs01' : phs01,
#                     'phs02' : phs02,
#                     'pdi01' : pdi01,
#                     'pdi02' : pdi02
#                 }   
#             )
#         )
        
        
# collection  = FeatureCollection(features)
# with open("/Users/kalashkala/Desktop/Python Code/nc-to-json/geojson.json", "w") as f:
#     f.write('%s' % collection)
