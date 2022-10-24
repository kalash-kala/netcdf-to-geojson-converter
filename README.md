# Netcdf4 to geoJSON

## What is this about :

- I have created a Python script which converts netcdf4 files to geoJSON very easily and quickly.
- I have used the novel approach to do this. First we convert netcdf4 to csv and then we use inbuilt python libraries to convert the csv file to geoJSON.

## Why convert the netcdf4 file to csv first ?

- CSV has a lot of benefits in python
- Using pandas library, one can manipulate the csv data in plethora of ways
- This makes it great to create geoJson files of different types consisting of different data
- We can not only adjust the number of columns required but also change the number of data rows
- using the csv we can make multiple dataframes consisting of different combinations of data, hence making it very versatile

## Prerequisites :

- Strong knowledge of Pandas and Numpy library
    - must know how to merge dataframes
    - must know how to slice the dataframe
    - must know how add new columns and apply broadcasting features
    - must know how to use map and apply functions
    - must know how to change data types of the coulmns

## Prerequisite packages :

- The packages below are used for converting netcdf4 file to csv

```python
import csv
import netCDF4 as nc
from netcdf2csv import convert_dir

netcdf_dir_route = "" # contains the netcdf file location
cleaned_csv_route = "" # this contains the file route where you want the CSV to be stored
csv_route = "" #contains the route where the uncleaned csv files will be stored

convert_dir(netcdf_dir=netcdf_dir_route,csv_dir=csv_route,cleaned_csv_dir=cleaned_csv_route,clean_choice=1)
```

- netcdf2csv is a third party open source package, so to install this click on → [LINK](https://pypi.org/project/netcdf2csv/)

<aside>
⚠️ Please keep in mind to use regular python environment and not the one provided by anaconda as this package can only be downloaded using the pip command and not conda command

</aside>

- The packages below are used for converting csv to geoJSON

```python
import pandas as pd
import numpy as np
import csv, json
from geojson import Feature, FeatureCollection, Point
```

The code files in this repo will contain :

- General code structure
- few examples

## The errors you might face :

- For numeric valued columns, keep their data type as float64, if it is something else like int64 then it will throw an error saying that the following data type is not acceptable by JSON
- For columns whose data type are not so common like date time, convert them to object type data, otherwise it will throw an error saying  that the following data type is not acceptable by JSON

### In short do the following with the data :

- convert numeric type columns to → float64
- convert categorical type columns to → object