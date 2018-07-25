#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 08:31:20 2018

@author: f095
"""
#Mit den standardt Datentypen in Python sind Tabellenstrukturen relativ kompliziert umzusetzten.
#Aus diesem Gerund verwenden wir als Einfache Tabelle ein ARRAY. Dieses ist wird im Packet NumPy 
#mitgeliefert und stellt eine verschachtelte Liste mit zusätztlichen Funktionen dar.

#zuerste wird das Packet NumPy geladen und kann später mit dem Kürzel np angesprochen werden.
import numpy as np

#Definition von zwei Listen (Liste1 besteht aus zwei verschachtelten Listen)
Liste = [[1, 5, 10],[7,20,80]]
Liste2 = ['a',5,20]

#Konvertieren der Liste in ein Array
Array = np.array(Liste)

#Zeile zu Array hinzufügen (Achtung! In Liste2 ist eins String -> Datentyp der Liste ändert
#sich von Interger zu String)

Array2 = np.vstack([Array,Liste2])

Array[1,1]

#Array mit 3 Dimensionen
Array4 = np.array([[['a','b','c'],['a','b','c']],[[1,4,5],[6,7,8] ]])

#Jetzt definieren wir ein Array, welches aus Tupeln besteht. Die Tupel stellen die einzelnen Zeilen
#einer Tabelle dar. Diese werden in ein Listenobjekt [...]  gepackt und mit der np.array Funktion
#in ein Array transformiert. Um später die spalten ähnlich zu SQL abrufen zu können,
#wirden noch die Spaltennamen und Datentypen festgelegt. Dabei ist die Spalte1 eine Ganzzahl (np.int) 
#und die Spalte2 ein String mit max. 10 Zeichen (S10). Sollen längere Strings abgespeichert werden,
#kann die Zahl auf z.B. S20 erhöht werden. Damit können dann Strings mit bis zu 20 Zeichen gespeichert
#werden.

Array1 = np.array([(1,'A'),(5,'B'),(10,'C')],dtype = [('Spalte1',np.float),('Spalte2','S10')])

#Wenn das Array gespeichert wurde, können mit der Methode dtype die Spaltennamen und Datentypen abgerufen werden.
Array1.dtype

#Mit der Spaltenbezeichnung in eckigen Klammer kann die passende Spalte aufgerufen werden.
Array1['Spalte2']

#Oder mit dem Index die Passende Zeile
Array1[1]




