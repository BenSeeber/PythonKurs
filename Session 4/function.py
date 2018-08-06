# Programmcode, welcher oft verwendet wird kann in Funktionen zusammengefügt werden.
# Z.B. print() eine Funktion.
# Diese können auch selber erstellt werden

# Der Code sieht dann in etwa so aus:

# def functio-name(parameters):
#    statement

# Ein einfaches Beispiel ist das Quadrieren einer Zahl

def quadriere(x):
    return x*2

# mit return kann das Ergebniss einer Funktion ausgegeben werden

# Jetzt Schreiben wir eine Funktion mit zwei Parametern. y hat hier eine default Value.
def f(x, y=[]):
    y.append(x)
    return(y)

# Alle Variablen, welche in einer Funktion definiert sind, sind lokale Variablen. 
# D.h. sie leben nur in der Funktion
# Testen wir das mal

def lokale_variablen():
    x=5
    print(x)

# Rufen wir die Funktion einmal auf

lokale_variablen()

# und jetzt versuchen wir x auszugeben
print(x)

# Um Variablen auch Global verfügbar zu machen muss dies explizit definiert werden
def globale_variablen():
    global x
    x=5
    print(x)

globale_variablen()
print(x)

# Jetzt mal eine komplexere Funktion, welche ein JSON Objekt verarbeitet.
# Dazu definieren wir eine Variable event, welcher wir ein JSON Objekt übergeben.
event = {
  "Records": [
    {
      "eventVersion": "2.0",
      "eventSource": "aws:s3",
      "awsRegion": "eu-central-1",
      "eventTime": "2018-07-19T14:49:56.324Z",
      "eventName": "ObjectCreated:Put",
      "s3": {
        "s3SchemaVersion": "1.0",
        "configurationId": "mytest",
        "bucket": {
          "name": "test-bucket",
          "ownerIdentity": {
            "principalId": "atvg5324"
          },
          "arn": "arn:aws:s3:::bse-clearing-test-input"
        },
        "object": {
          "key": "my_file.csv",
          "size": 4767,
          "eTag": "tesdget",
          "sequencer": "afeg2gfr"
        }
      }
    }
  ]
}

# Dann wird die Funktion definiert, welche zwei Werte ausgibt, einmal den Key und einmal das Bucket.
def get_info(event):
    Key=event['Records'][0]['s3']['object']['key']
    Bucket=event['Records'][0]['s3']['bucket']['name']
    return Key, Bucket
    
# Wenn eine Funktion zwei Werte ausgibt, können diese mit Komma getrennt in 
# zwei Variablen geschrieben werden.
Key, Bucket = get_info(event)


# Jetzt schreiben wir eine Funktion, welche einen Hashwert welche eine CSV Datei ausliest,
# eine Spalte hased und dann wieder als CSV Datei speichert.

import hashlib
df[column] = [base64.b64encode(hashlib.sha1(str(val).encode("UTF-8")).digest()).decode('utf-8') for val in df[column]]

