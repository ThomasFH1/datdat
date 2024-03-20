SELECT
    Teaterstykke.Stykketittel,
    Bruker.Fornavn || ' ' || Bruker.Etternavn AS Fullt_navn,
    Rolle.Oppgavenavn
FROM
    Bruker
    JOIN Ansatt ON Ansatt.BrukerID = Bruker.BrukerID
    JOIN HarOppgaver ON Ansatt.AnsattID = HarOppgaver.AnsattID
    JOIN Rolle ON HarOppgaver.OppgaveID = Rolle.OppgaveID
    AND HarOppgaver.StykkeID = Rolle.StykkeID
    JOIN Teaterstykke ON Rolle.StykkeID = Teaterstykke.StykkeID;