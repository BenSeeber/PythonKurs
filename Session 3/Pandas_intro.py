#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 08:03:49 2018

@author: f095
"""

import pandas as pd

#Read csv file
df = pd.read_csv("/Users/f095/FIVE1 GmbH & Co. KG/Analytics - Customer/EPRIMO_SCHULUNG/PYTHON_2/FL_insurance_sample.csv")

#Get columns
df.columns

#get different datatypes in table
df.dtypes

#get one column
df.point_longitude

#get more columns

df[['point_longitude','statecode']]

#get unique values
county = df.county.unique()
#group data
df.groupby(['county'])['point_longitude'].mean()

#filtern

df[["county","point_longitude"]].loc[df.county=='CLAY COUNTY']

#filter nach liste
some_values=('SUWANNEE COUNTY','NASSAU COUNTY')
df[["county","point_longitude"]].loc[df.county.isin(some_values)]

#und die negation mit einer Tilde ~
df[["county","point_longitude"]].loc[~df.county.isin(some_values)]