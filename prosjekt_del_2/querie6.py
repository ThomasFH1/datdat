"""Vi ønsker å lage et query i SQL som finner hvilke forestillinger som har solgt
best. Skriv ut navn på forestilling og dato og antall solgte plasser sortert på
antall plasser i synkende rekkefølge"""

import sqlite3
con = sqlite3.connect("Theatre.db")
cursor = con.cursor()


query = """
   SELECT Stykketittel, Fremvisningstidspunkt, COUNT(BillettID) as AntallSolgteBilletter
   FROM Fremvisning
   JOIN Teaterstykke on Fremvisning.StykkeID = Teaterstykke.StykkeID
   JOIN Billett on Fremvisning.FremvisningID = Billett.FremvisningID
   GROUP BY Fremvisning.FremvisningID
   ORDER BY AntallSolgteBilletter DESC
"""
cursor.execute(query)
row = cursor.fetchall()
print("Dato og stykketittel på best solgte forestillinger, sortert i synkende rekkefølge:", row)
con.close()