#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 08:03:49 2018

@author: f095
"""

import pandas as pd
print(1)

#Read csv file
df = pd.read_csv("/Users/f095/OneDrive - FIVE1 GmbH & Co. KG/Code/PythonKurs/Session 3/FL_insurance_sample.csv")

#Get columns
df.columns

#get different datatypes in table
df.dtypes

df.iloc[0]

#get one column
df.point_longitude

#get more columns
spalten_von_interesse = ['point_longitude','statecode']
df[spalten_von_interesse]

#get unique values
county = df.county.unique()
print(county)

#group data with one KPI
df.groupby(['county'])['point_longitude'].mean()

#group data with more then one KPI
df.groupby(['county']).agg({'point_longitude':'mean','point_latitude':'mean','eq_site_limit':'max'}).iloc[0]

#filtern nach Wert

df[df.county=='CLAY COUNTY'][["county","point_longitude"]]


#filtern nach ersten Buchstaben einer Spalte
df[df.county.str.slice(0,1)=='L'][["county","point_longitude"]].county.unique()

#filter nach liste
some_values=('SUWANNEE COUNTY','NASSAU COUNTY')
df[df.county.isin(some_values)][["county","point_longitude"]]

#und die negation mit einer Tilde ~
df[~df.county.isin(some_values)][["county","point_longitude"]].groupby(['county'])['county'].count()