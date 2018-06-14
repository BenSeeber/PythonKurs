# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Um Objekte einer Variablen zuzuweisen, wird in Pyhton das = verwendet.
a='Hello World'

#In diesem Beispiel wurde der Variablen a der String 'Hello World' zugewiesen.
#Dieser kann mit der print() Funktion ausgegeben werden.
#Dabei ist a der Parameter, welcher an die Printfunktion übergeben wird.
print(a)

#In Pyhton gibt es verscheidene Basis Datentypen.

#Ganzzahl
integer_type = 5

#Fließkommazahl
float_type = 1.5

#Eine Fließkommazhal kann auch als Bruch dargestellt werden
bruch = 5/6

#Jetzt kommen wir zu Objekent über die Iteriert werden kann. D.h. über ein Index können bestimme
#Tiele des Objekts mitels [...] selektiert werden. Dazu geleich.

#Der Einfachste Type ist ein String. Also eine Folge von Zeichen. Diser kann mit
#einfachen Hochkommata
string = 'Hello World'

#und doppelten Hochkommata geschrieben werden.
string2 = "Hello World"

#Aufgepasst werden muss nur, wenn im String ein Hochkommata vorkommt.
#string3 = 'I'm a programmer' #Das ist falsch

#dann kann man über den \ markieren, dass das Hochkomata ein Zeichen ist
string4 = 'I\'m a programmer'

#Oder der String wird mit doppelten Hochkommata geschrieben
string5 = "I'm a programmer"

#Jetzt definieren wir einmal einen String, welcher eine ID darstellen soll.
string6ID = "ABD5764#irfj"

#Aus diesem sollen die ersten 3 Zeichen selektiert werden. Dazu kann ein Index in [...] verwendet werden.

#Zählen in interierbaren Variablen
#Gezählt wird von 0 an
#Der Letzte Index ist nicht mit dabei , d.h. für das Beispiel
#0:3 ist nicht ABD5 sondern ABD

#Für die ersten 3 Zeichen muss der String wie folgt aufgerufen werden
string6ID[0:3]

#Rückwärts Zählen (String ohne letztes Objekt)
string6ID[0:-1]
string6ID[:-1]

#nur die letzten zwei Einträge
string6ID[-2:]

string6ID[0:-1]

#Nachdem wir gesehen haben, wie einzelne Zeichen selektiert werden können, 
#gehen wir ein schritt weiter und suchen bestimmte Zeichenketten in einem String.
#Als Beispiel nutzen wir eine Mail adresse.
eMail = 'ben.seeber@five1.de'

#Um zu prüfen ob es sich um eine deutsche Mailadresse handelt, kann die find() Funktion
#Aus dem str Packet genutzt werden.
str.find(eMail, '.de')
#Wenn die Ausgabe größer -1 ist, wurde die Zeichenkette gefunden. Ist die Ausgabe -1,
#dann wurde das zeichen nicht gefunden. Die Ausgabe der letzten Suche war 16. 16 ist der Anfang 
#der Zeichenkette '.de'

#Versucht man die Suche nach eine .com Endung, so ist das Ergebniss -1. Mit einem Logischen Test ob
#Das Ergebniss der Suche ungleich -1 ist, sollt diese den Wert FALS liefern.

#Ist eMail eine Adresse mit einer .com Endung?
str.find(eMail,'.com') != -1

#Mithilfe des Wissens, das der Firmenname zwischen einem @ und der Endung .de Kodiert ist,
#kann der Firmenname aus der Mailadresse extrahiert werden

#Finde Anfang der .de Endung
Ende = str.find(eMail, '.de')
#Finde Position des @ Zeichens
Anfang = str.find(eMail,'@')

#Nutze die Information über Anfang und Ende um den Firmennamen zu extrahieren.
eMail[Anfang+1:Ende]

#Nachem Strings ausführlich beschrieben wurden kommen wir jetzt zu den Objetkten Tupel und Liste.
#Der Hauptunterschied ist, das Tupel, nachdem sie erstellt wurden, nicht veränderbar sind.
#Listen hingegen sind veränderbar. So können z.B. neue Einträge hinzugefügt werden.
#Beide Objekte können mit unterscheidlichen Objeklten befüllt werden.

#Datentype Tupel
MailTuple = ('ben.seeber@five1.de', 'Heike@python-beispiel.de', 'Horst@python-beispiel.de')

#Datentype Liste
eMailList = ['ben.seeber@five1.de', 'Heike@python-beispiel.de', 'Horst@python-beispiel.de']

#Liste mit unterschiedlichen Eeinträgen
InhomogeneListe = [1,10.5,'Ich bin ein String']

#Um aus einer Liste einen Eintrag abzurufen, können wie bei String Indizes verwedent werden.
#Für die Selektion der zweiten Mailadressen nutzt man den Index [1]
eMailList[1]

#Für die Selektion der ersten zwei Einträge
eMailList[:2]

#Listen bringen die Methode append() um einträge hinzuzufügen.

#Eintrag Hinzufügen
eMailList.append('neue_adresse@test.de')
print(eMailList)

#Mithilfe einer FOR Schleife kann durch Listen iteriert werden

for eMailAdresse in eMailList:
    #Setzte string zusammen
    Ausgabe = 'Die Mail Adresse ist ' + eMailAdresse
    #Gib den String aus
    print(Ausgabe)

#Dies kann genutzt werden um z.B. nur eMail Adressen der Firma python-beispiel auszugeben
for i in eMailList:
    if str.find(i,'python-beispiel') != -1:
        print(i)

#Oder es werden die Firmen extrahiert       
for i in eMailList:
    anfang = str.find(i,'@')
    ende = str.find(i, '.de')
    print(i[anfang+1:ende])

#Listen  können für auch Verschachtelt werden. Dies kann zu Tabellenähnlichen Strukturen führen.

#Verschachtelung
Liste1 = [1,5,10]
Liste2 = ["A","B","C"]

#Listen Zusammenhängen
Liste3 = [Liste1,Liste2]

#Um einzelne Werte aus Liste2 Abzufragen muss aus Liste3 erst mal die Liste2 ausgewählt werden
Liste3[1]
#Um eine das zweite Element der List2 auszuwählen muss noch eine Ebene tiefer Selektiert werden
Liste3[1][1]

#Der letzte relevante native Datentyp in Python soll das Dictionary sein. Es ist eine Sammlung von Key - Value paaren.
#D.h. wie in einem Wörterbuch kann man nach Keys Suchen und bekommt den Wert zurück.

Dict1 = {'Frankreich':'Paris' , 'Deutschland':'Berlin'}

Dict1['Frankreich']
Dict1['Deutschland']

