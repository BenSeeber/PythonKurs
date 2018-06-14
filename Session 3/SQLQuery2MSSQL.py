#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 08:29:12 2018

@author: f095
"""

import pandas
from pandas import DataFrame
import pyodbc

cnxn = pyodbc.connect('DSN=MYMSSQL;UID=sa;PWD=Pa$$w0rd')
crsr = cnxn.cursor()
for table_name in crsr.tables(tableType='TABLE'):
    print(table_name)
cursor = cnxn.cursor()
sql = "Select * From dbo.MSreplication_options"
data = pandas.read_sql(sql,cnxn)