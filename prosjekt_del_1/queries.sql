SELECT
    Teaterstykke.StykkeID,
    Teaterstykke.Stykketittel,
    Fremvisning.Fremvisningstidspunkt,
    COUNT(Billett.BillettID) AS AntallSolgteBilletter
FROM
    Fremvisning
JOIN Teaterstykke ON Fremvisning.StykkeID = Teaterstykke.StykkeID
JOIN Billett ON 
    Fremvisning.Fremvisningstidspunkt = Billett.Fremvisningstidspunkt AND
    Fremvisning.Salnavn = Billett.Salnavn AND
    Fremvisning.TeaterID = Billett.TeaterID AND
    Fremvisning.StykkeID = Billett.StykkeID
GROUP BY
    Fremvisning.Fremvisningstidspunkt, Teaterstykke.Stykketittel
ORDER BY
    AntallSolgteBilletter DESC;