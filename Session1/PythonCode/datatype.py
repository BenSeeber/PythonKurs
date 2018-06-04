# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a='Hello World'

print(a)

integer_type = 5

float_type = 1.5

bruch = 5/6 #@Tomas: Warum hast du das so gemacht?

string = 'Hello World'

string2 = "Hello World"

string3 = 'I'm a programmer' #Das ist falsch

string4 = 'I\'m a programmer'

string5 = "I'm a programmer"

string6ID = "ABD5764#irfj"

#Zählen in interierbaren Variablen
#Gezählt wird von 0 an
#Der Letzte Index ist nicht mit dabei , d.h. für das Beispiel
#0:3 ist nicht ABD5 sondern ABD

string6ID[0:3]

#Rückwärts Zählen (String ohne letztes Objekt)
string6ID[0:-1]
string6ID[:-1]

#nur die letzten zwei Einträge
string6ID[-2:]

string6ID[0:-1]

eMail = 'ben.seeber@five1.de'
#Find in String
ende = str.find(eMail, '.de')
anfang = str.find(eMail,'@')

eMail[anfang+1:ende]

#Ist .com in der Mailadresse?
str.find(eMail,'.de') != -1

1 == 1

#Datentype Tupel
MailTuple = ('ben.seeber@five1.de', 'meltem@eprimo.de', 'anja@eprimo.de')

#Datentype Liste
eMailList = ['ben.seeber@five1.de', 'meltem@eprimo.de', 'anja@eprimo.de']

#Objekt Abrufen
eMailList[0:2]

#Eintrag Hinzufügen
eMailList.append('zweiteMail@test.de')

for i in eMailList:
    if str.find(i,'eprimo') != -1:
        print(i)
        
for i in eMailList:
    anfang = str.find(i,'@')
    ende = str.find(i, '.de')
    print(i[anfang+1:ende])

#Verschachtelung
Liste1 = [1,5,10]
Liste2 = ["A","B","C"]

#Listen Zusammenhängen
Liste3 = [Liste1,Liste2]

#Abfragen von einzelnen Werten
Liste3[1][2]


#Nutzung von Arrays
import numpy as np

Array1 = np.array([(1,'A'),(5,'B'),(10,'C')],dtype = [('Spalte1',np.int),('Spalte2','S10')])
Array1.dtype

Array1['Spalte2']

Array1['Spalte1']

Array1[:,0:2]

#ioder
Array1[0,0:2]


#DICT
Dict1 = {'Frankreich':'Paris' , 'Deutschland':(1,2,4)}

Dict1['Frankreich']
Dict1['Deutschland']

