#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 10:06:29 2018

@author: f095
"""

county_name = "CLAY COUNTY"
 
#Filtere das erste Wort 

#Variante 1: mit dem Index
count_part = county_name[0:4]
print(count_part) 

#Variante 2: mit der str.find() Funktion
ende = str.find(county_name,' ')
count_part = county_name[0:ende]

#Variante 3: split funktion
Split_result = county_name.split(' ')
Erstes_Wort = Split_result[0]

#Weise die Liste aus der Mail einer Variablen county zu
county = ['CLAY COUNTY', 'SUWANNEE COUNTY', 'NASSAU COUNTY',
       'COLUMBIA COUNTY', 'ST  JOHNS COUNTY', 'BAKER COUNTY',
       'BRADFORD COUNTY', 'HAMILTON COUNTY', 'UNION COUNTY',
       'MADISON COUNTY', 'LAFAYETTE COUNTY', 'FLAGLER COUNTY',
       'DUVAL COUNTY', 'LAKE COUNTY', 'VOLUSIA COUNTY', 'PUTNAM COUNTY',
       'MARION COUNTY', 'SUMTER COUNTY', 'LEON COUNTY', 'FRANKLIN COUNTY',
       'LIBERTY COUNTY', 'GADSDEN COUNTY', 'WAKULLA COUNTY',
       'JEFFERSON COUNTY', 'TAYLOR COUNTY', 'BAY COUNTY', 'WALTON COUNTY',
       'JACKSON COUNTY', 'CALHOUN COUNTY', 'HOLMES COUNTY',
       'WASHINGTON COUNTY', 'GULF COUNTY', 'ESCAMBIA COUNTY',
       'SANTA ROSA COUNTY', 'OKALOOSA COUNTY', 'ALACHUA COUNTY',
       'GILCHRIST COUNTY', 'LEVY COUNTY', 'DIXIE COUNTY',
       'SEMINOLE COUNTY', 'ORANGE COUNTY', 'BREVARD COUNTY',
       'INDIAN RIVER COUNTY', 'MIAMI DADE COUNTY', 'BROWARD COUNTY',
       'MONROE COUNTY', 'PALM BEACH COUNTY', 'MARTIN COUNTY',
       'HENDRY COUNTY', 'PASCO COUNTY', 'GLADES COUNTY',
       'HILLSBOROUGH COUNTY', 'HERNANDO COUNTY', 'PINELLAS COUNTY',
       'POLK COUNTY', 'North Fort Myers', 'Orlando', 'HIGHLANDS COUNTY',
       'HARDEE COUNTY', 'MANATEE COUNTY', 'OSCEOLA COUNTY', 'LEE COUNTY',
       'CHARLOTTE COUNTY', 'COLLIER COUNTY', 'SARASOTA COUNTY',
       'DESOTO COUNTY', 'CITRUS COUNTY']

#Nutze eine FOR Schleife um die Elemente der Liste auszugeben
for county_name in county:
    print(county_name)

#Nutze die Split Funktion um das erste Wort 
#der County Strings auszugeben
for i in county:
    Split_result = i.split(' ')
    Erstes_Wort = Split_result[0]
    print(Erstes_Wort)
#Statt die County Strings auszugeben, erstelle eine neue Liste 
#mit dem Namen count_part_list

#Leere Liste anlegen
Ich_bin_eine_Liste = []
#Neues Element zu Liste hinzufügen
Ich_bin_eine_Liste.append(Erstes_Wort)

county_part_list = []]
for i in county:
    Split_result = i.split(' ')
    Erstes_Wort = Split_result[0]
    county_part_list.append(Erstes_Wort)
    

    
    
    