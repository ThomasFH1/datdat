import sqlite3
con = sqlite3.connect("Theatre.db")
cursor = con.cursor()


query = "SELECT Ansatt.Navn, Teaterstykke.Stykketittel, Rolle.Oppgavenavn \
         FROM ansatt \
         JOIN Rolle ON Ansatt.AnsattID = Rolle.AnsattID \
         JOIN Teaterstykke ON Rolle.TeaterstykkeID = Teaterstykke.TeaterstykkeID"
cursor.execute(query)
row = cursor.fetchall()
print("Navn på skuespillere og roller som opptrer i teaterstykkene: ", row)