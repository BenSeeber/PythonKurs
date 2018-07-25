#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 10:57:11 2018

@author: f095
"""

import pandas
from pandas import DataFrame
import pyodbc

#Finde SQL Treiber
pyodbc.drivers()

#Stelle Verbindung her
cnxn = pyodbc.connect(
    r'DRIVER={FreeTDS};'
    r'SERVER=127.0.0.1,32774;'
    r'DATABASE=master;'
    r'UID=sa;'
    r'PWD=Pa$$w0rd'
    )

#Mache Abfrage
sql = "Select * From dbo.MSreplication_options"
data = pandas.read_sql(sql,cnxn)

#Bekomme die erste Spalte
data.optname