import sqlite3

# Koble til databasen
conn = sqlite3.connect('teater.db')
cursor = conn.cursor()

def hent_akter_for_skuespillere():
    # SQL-forespørsel for å hente alle akter skuespillere har deltatt i
    sql_query = """
        SELECT DISTINCT Deltar.Aktnummer, Deltar.StykkeID, Oppgaver.Oppgavenavn, Teaterstykke.Stykketittel
        FROM Deltar
        JOIN Oppgaver ON Deltar.OppgaveID = Oppgaver.OppgaveID AND Deltar.StykkeID = Oppgaver.StykkeID
        JOIN Teaterstykke ON Deltar.StykkeID = Teaterstykke.StykkeID;
    """
    # Utfør SQL-forespørselen
    cursor.execute(sql_query)
    result = cursor.fetchall()

    # Organiser resultatene i en nested liste
    akter_liste = {}
    for row in result:
        aktnummer = row[0]
        stykke_id = row[1]
        oppgave_navn = row[2]
        stykke_tittel = row[3]
        if stykke_id not in akter_liste:
            akter_liste[stykke_id] = {'Stykke tittel': stykke_tittel, 'Akt': []}
        akter_liste[stykke_id]['Akt'].append({'Aktnummer': aktnummer, 'Oppgave navn': oppgave_navn})

    return akter_liste

def finn_akter_for_skuespiller(skuespiller_navn):
    akt_liste = hent_akter_for_skuespillere()
    skuespillere = set()
    for stykke_id, data in akt_liste.items():
        for akt in data['Akt']:
            sql_query = """
                SELECT COUNT(*)
                FROM Deltar
                JOIN Oppgaver ON Deltar.OppgaveID = Oppgaver.OppgaveID AND Deltar.StykkeID = Oppgaver.StykkeID
                WHERE Oppgaver.Oppgavenavn = ? AND Deltar.Aktnummer = ? AND Deltar.StykkeID = ?;
            """
            cursor.execute(sql_query, (skuespiller_navn, akt['Aktnummer'], stykke_id))
            count = cursor.fetchone()[0]
            if count > 0:
                skuespiller_query ="""
                    SELECT Ansatt.Fornavn, Ansatt.Etternavn FROM """
                skuespillere.add(stykke_id)
    return 0 # bare satte 0

# Testfunksjonen med et skuespillernavn
skuespiller_navn = input("Vennligst skriv inn skuespillernavnet: ")
akter = finn_akter_for_skuespiller(skuespiller_navn)

if akter:
    print(f"Skuespilleren {skuespiller_navn} har deltatt i følgende akter:")
    for akt in akter:
        print(f"- Akt {akt['Aktnummer']} i skuespillet '{akt['Stykke tittel']}'")
else:
    print(f"Ingen data funnet for skuespilleren {skuespiller_navn}.")

# Lukk databaseforbindelsen
conn.close()