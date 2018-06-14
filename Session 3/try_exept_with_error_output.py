#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 08:29:59 2018

@author: f095
"""

logf = open("test_log.log", "w")   
try:
    df = pd.read_csv('pandas_dataframe_importing_csv/example.csv')
except Exception as e:
    logf.write("Failed to compare {0}\n".format(str(e)))