# Jetzt schreiben wir eine Funktion, welche einen Hashwert welche eine CSV Datei ausliest,
# eine Spalte hased und dann wieder als CSV Datei speichert.

import hashlib
df[column] = [base64.b64encode(hashlib.sha1(str(val).encode("UTF-8")).digest()).decode('utf-8') for val in df[column]]