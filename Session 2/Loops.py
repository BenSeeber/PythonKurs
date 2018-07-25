#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Eine Schleife ist unter anderem dazu da, durch ein Objekt wie einen String, 
#eine Liste oder ein Array zu iterieren

#Das erste Beispiel ist eine einfache For-Schleife, welche über einen String iteriert
#Die einzelnen Zeichen werden mittels der print() Funktion ausgegeben.
#Alle Funktionen und Operationen, welche in einer Schleife ausgeführt werden sollen,
#sind mit einem TAB eingerückt.

Satz = 'Drei Billionen Tonnen antarktisches Eis haben sich seit 1992 verflüssigt.'

for Zeichen in Satz:
    print(Zeichen)

#Eine Schleife kann aber nicht nur darzu genutzt werden einen String Zeichenweise
#Auszugeben. Es können genausogut komplexere Operationen erfolgen. Im folgenden wird
#der Sting in seine Einzelteile Zerlegt. Dann wird er mithilfe einer Schleife wieder
#zusammengesetzt

#Zerlege Satz in einzelne Worte. Diese sind in einer Liste gespeichert
Worte = Satz.split(' ')

#Erstelle einen leeren String
Zusammengesetzter_Satz = ''

#Schleife um den Satz wieder zusammenzusetzten
for Wort in Worte:
    #Der folgende Befehlt fürgt das Wort und ein Leerzeichen zu dem String
    #Zusammengesetzter_Satz hinzu
    Zusammengesetzter_Satz += Wort + ' '

#Jetzt muss nur noch das letzte Leerzeichen hinter dem Punkt entfernt werden
Zusammengesetzter_Satz = Zusammengesetzter_Satz[:-1]

#Neben der FOR Schleife gibt es auch die WHILE Schleife. Diese Iteriert bis eine
#Bestimmte Bedingugn erfüllt ist. 
#Als Beispiel werden die Zahlen 1:10 ausgegeben.

#Definition von i als Ganzzahl mit denm Wert 1
i = 1
while i<=10: #Die Bedingung für die Schleife ist, das die Variable kleiner oder gleich 10 ist
    #Aufgabe von i
    print(i)
    #hinzuzählen von 1 zur Zahl mit der Referenz i
    i = i+1
    
    
Date=[1,31,2,3,4,5,6,7]
Kuendigungen=[50,10,60,29,48,59,17]

i = 0
while Date[i] <= 3:
    print(Kuendigungen[i])
    i=i+1