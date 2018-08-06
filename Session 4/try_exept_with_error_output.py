#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 08:29:59 2018

@author: f095
"""

import pandas as pd
import datetime as dt

try:
    df = pd.read_csv('pandas_dataframe_importing_csv/example.csv')
except Exception as e:
    with open("test_log.log", "a") as the_log:
        the_log.write("Failed to read file: {0}\n".format(str(e)))
