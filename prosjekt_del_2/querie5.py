import sqlite3
con = sqlite3.connect("Theatre.db")
cursor = con.cursor()


query = """
    SELECT
    Fornavn,
    Etternavn,
    Teaterstykke.Stykketittel,
    Rolle.Oppgavenavn
FROM
    Ansatt
    JOIN Bruker ON Ansatt.BrukerID = Bruker.BrukerID
    JOIN HarOppgaver ON Ansatt.AnsattID = HarOppgaver.AnsattID
    JOIN Rolle ON HarOppgaver.OppgaveID = Rolle.OppgaveID
    AND HarOppgaver.StykkeID = Rolle.StykkeID
    JOIN Teaterstykke ON Rolle.StykkeID = Teaterstykke.StykkeID
"""
cursor.execute(query)
row = cursor.fetchall()
print("Navn på skuespillere og roller som opptrer i teaterstykkene:", row)
con.close()