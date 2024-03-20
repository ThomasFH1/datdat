import sqlite3

def hent_akter_og_skuespillere(db_path="Theatre.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    query = """
    SELECT b.Fornavn || ' ' || b.Etternavn AS SkuespillerNavn, ts.Stykketittel, ak.Aktnavn, ak.Aktnummer, ak.StykkeID
    FROM Ansatt a
    JOIN Bruker b ON a.BrukerID = b.BrukerID
    JOIN HarOppgaver ho ON a.AnsattID = ho.AnsattID
    JOIN Deltar d ON ho.OppgaveID = d.OppgaveID AND ho.StykkeID = d.StykkeID
    JOIN Akt ak ON d.Aktnummer = ak.Aktnummer AND d.StykkeID = ak.StykkeID
    JOIN Teaterstykke ts ON ak.StykkeID = ts.StykkeID
    ORDER BY ts.Stykketittel, ak.Aktnummer;
    """
    
    cursor.execute(query)
    resultater = cursor.fetchall()
    conn.close()
    return resultater

def finn_medskuespillere(skuespillernavn, alle_data):
    deltakelser = {}
    for skuespiller, stykketittel, aktnavn, aktnummer, stykkeID in alle_data:
        nøkkel = (stykketittel, aktnummer, aktnavn)
        if nøkkel not in deltakelser:
            deltakelser[nøkkel] = set()
        deltakelser[nøkkel].add(skuespiller)

    stykke_akter = {}

    for (stykketittel, aktnummer, aktnavn), skuespillere in deltakelser.items():
        if skuespillernavn in skuespillere:
            if stykketittel not in stykke_akter:
                stykke_akter[stykketittel] = []
            stykke_akter[stykketittel].append((aktnavn, skuespillere))

    for stykketittel, akter in stykke_akter.items():
        print(f"\n{skuespillernavn} har spilt i '{stykketittel}':")
        for aktnavn, skuespillere in sorted(akter, key=lambda x: x[0]):
            medskuespillere = skuespillere - {skuespillernavn}
            if medskuespillere:
                print(f"  I {aktnavn}, med: {', '.join(sorted(medskuespillere))}")

alle_data = hent_akter_og_skuespillere()
finn_medskuespillere("Arturo Scotti", alle_data)

