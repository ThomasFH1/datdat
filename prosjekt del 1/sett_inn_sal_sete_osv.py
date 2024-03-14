import sqlite3
import sys

def les_sal(salfil):
    områder = {}
    with open(salfil, "r") as f:
        dato = f.readline().strip()

        for line in f:
            if not line[0].isdigit():
                last_område = line.strip()
                områder[last_område] = []
            else:
                områder[last_område].append(line.strip())
    return områder, dato

con = sqlite3.connect("Theatre.db")
cursor = con.cursor()


områder, dato = les_sal(f"{sys.argv[1]}.txt")
teater_id = 1
salnavn = " ".join([word.capitalize() for word in sys.argv[1].split("-")])
cursor.execute("INSERT INTO Sal VALUES (?, ?)", (salnavn, teater_id))

#billett_id = 0
områdenummer = 0
for områdenavn, rader in områder.items():
    områdenummer += 1
    cursor.execute("INSERT INTO Område VALUES (?, ?, ?, ?)", (områdenummer, områdenavn, salnavn, teater_id))
    for i, rad in enumerate(reversed(rader)):
        radnummer = i + 1
        cursor.execute("INSERT INTO Rad VALUES (?, ?, ?, ?)", (radnummer, områdenummer, salnavn, teater_id))
        for j, kjøpt in enumerate(rad):
            kolonnenummer = j + 1
            cursor.execute("INSERT INTO Stol VALUES (?, ?, ?, ?, ?)", (kolonnenummer, radnummer, områdenummer, salnavn, teater_id))
            # billett_id += 1
            # cursor.execute("INSERT INTO Billett VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            #                (billett_id, kolonnenummer, radnummer, områdenummer, salnavn, teater_id, hovedscenen_dato, stykke_id))

con.commit() 
con.close()
