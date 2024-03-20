/*SAAEK=Størst av alt er kjærligheten*/
/*Innsetting av teaterstykkene*/
INSERT INTO Teater (TeaterID, Teaternavn)
VALUES
(1, "Trøndelag Teater");

INSERT INTO Teaterstykke (StykkeID, Stykketittel, VarighetMinutt)
VALUES 
(1, 'Størst av alt er kjærligheten', 90),
(2, 'Kongsemnene', 240);

/*Akter kongsemnene*/
INSERT INTO Akt (Aktnummer, StykkeID, Aktnavn)
VALUES 
(1, 2, 'akt_1'),
(2, 2, 'akt_2'),
(3, 2, 'akt_3'),
(4, 2, 'akt_4'),
(5, 2, 'akt_5');

/*Akter SAAEK*/
INSERT INTO Akt (Aktnummer, StykkeID, Aktnavn)
VALUES 
(1, 1, 'akt_1');


/*Setter inn skuespillere kongsemnene først som brukere, så ansatte*/
INSERT INTO Bruker (Fornavn, Etternavn, Telefonnummer, Adresse)
VALUES 
('Arturo', 'Scotti', '+47000001', 'Slottsplassen 1, 0010 Oslo'),
('Haakon', 'Haakonssønn', '+47000002', 'Slottsplassen 1, 0010 Oslo'),
('Ingunn Beate', 'Strige Øyen', '+47000003', 'Slottsplassen 1, 0010 Oslo'),
('Hans Petter', 'Nilsen', '+47000004', 'Slottsplassen 1, 0010 Oslo'),
('Madeleine Brandtzæg', 'Nilsen', '+47000005', 'Slottsplassen 1, 0010 Oslo'),
('Synnøve Fossum', 'Eriksen', '+47000006', 'Slottsplassen 1, 0010 Oslo'),
('Emma Caroline', 'Deichmann', '+47000007', 'Slottsplassen 1, 0010 Oslo'),
('Thomas Jensen', 'Takyi', '+47000008', 'Slottsplassen 1, 0010 Oslo'),
('Per Bogstad', 'Gulliksen', '+47000009', 'Slottsplassen 1, 0010 Oslo'),
('Isak Holmen', 'Sørensen', '+47000010', 'Slottsplassen 1, 0010 Oslo'),
('Fabian Heidelberg', 'Lunde', '+47000011', 'Slottsplassen 1, 0010 Oslo'),
('Emil', 'Olafsson', '+47000012', 'Slottsplassen 1, 0010 Oslo'),
('Snorre Ryen', 'Tøndel', '+47000013', 'Slottsplassen 1, 0010 Oslo');


INSERT INTO Ansatt (Personnummer, BrukerID)
VALUES 
(00000000001, 1),
(00000000002, 2),
(00000000003, 3),
(00000000004, 4),
(00000000005, 5),
(00000000006, 6),
(00000000007, 7),
(00000000008, 8),
(00000000009, 9),
(00000000010, 10),
(00000000011, 11),
(00000000012, 12),
(00000000013, 13);

/*Setter inn skuespillere SAAEK først som brukere, så ansatte*/
INSERT INTO Bruker (Fornavn, Etternavn, Telefonnummer, Adresse)
VALUES 
('Sunniva Du Mond', 'Nordal', '+47000014', 'Slottsplassen 1, 0010 Oslo'),
('Jo', 'Saberniak', '+47000015', 'Slottsplassen 1, 0010 Oslo'),
('Marte M.', 'Steinholt', '+47000016', 'Slottsplassen 1, 0010 Oslo'),
('Tor Ivar', 'Hagen', '+47000017', 'Slottsplassen 1, 0010 Oslo'),
('Tor Ivar', 'Hagen', '+47000017', 'Slottsplassen 1, 0010 Oslo'),
('Trond-Ove', 'Skrødal', '+47000018', 'Slottsplassen 1, 0010 Oslo'),
('Natalie Grøndahl', 'Tangen', '+47000019', 'Slottsplassen 1, 0010 Oslo'),
('Åsmund', 'Flaten', '+47000020', 'Slottsplassen 1, 0010 Oslo');

INSERT INTO Ansatt (Personnummer, BrukerID)
VALUES 
('00000000014', 14),
('00000000015', 15),
('00000000016', 16),
('00000000017', 17),
('00000000018', 18),
('00000000019', 19),
('00000000020', 20);

/*Setter inn kunstnerisk lag til kongsemnene først som brukere, så ansatte*/
INSERT INTO Bruker (Fornavn, Etternavn, Telefonnummer, Adresse)
VALUES 
('Yury', 'Butusov', '+47000021', 'Slottsplassen 1, 0010 Oslo'),
('Aleksandr', 'Shishkin-Hokusai', '+47000022', 'Slottsplassen 1, 0010 Oslo'),
('Eivind', 'Myren', '+47000023', 'Slottsplassen 1, 0010 Oslo'),
('Mina', 'Rype Stokke', '+47000024', 'Slottsplassen 1, 0010 Oslo');

INSERT INTO Ansatt (Personnummer, BrukerID)
VALUES 
('00000000021', 21),
('00000000022', 22),
('00000000023', 23),
('00000000024', 24);

/*Setter inn kunstnerisk lag til SAAEK først som brukere, så ansatte*/
INSERT INTO Bruker (Fornavn, Etternavn, Telefonnummer, Adresse)
VALUES 
('Jonas', 'Corell Petersen', '+47000025', 'Slottsplassen 1, 0010 Oslo'),
('David', 'Gehrt', '+47000026', 'Slottsplassen 1, 0010 Oslo'),
('Gaute', 'Tønder', '+47000027', 'Slottsplassen 1, 0010 Oslo'),
('Magnus', 'Mikaelsen', '+47000028', 'Slottsplassen 1, 0010 Oslo'),
('Kristoffer', 'Spender', '+47000029', 'Slottsplassen 1, 0010 Oslo');

INSERT INTO Ansatt (Personnummer, BrukerID)
VALUES 
('00000000025', 25),
('00000000026', 26),
('00000000027', 27),
('00000000028', 28),
('00000000029', 29);

/*Fremvisninger SAAEK, pass på at TeaterID og StykkeID er riktig*/
INSERT INTO Fremvisning (Fremvisningstidspunkt, Salnavn, TeaterID, StykkeID)
VALUES 
('2024-03-18 19:30', 'Gamle Scene', 1, 1),
('2024-03-19 19:30', 'Gamle Scene', 1, 1),
('2024-04-02 19:30', 'Gamle Scene', 1, 1),
('2024-04-03 19:30', 'Gamle Scene', 1, 1),
('2024-04-23 19:30', 'Gamle Scene', 1, 1);

/*Fremvisninger Kongsemnene, pass på at TeaterID og StykkeID er riktig*/
INSERT INTO Fremvisning (Fremvisningstidspunkt, Salnavn, TeaterID, StykkeID)
VALUES 
('2024-03-19 18:30', 'Hovedscenen', 1, 2),
('2024-04-02 18:30', 'Hovedscenen', 1, 2),
('2024-04-03 18:30', 'Hovedscenen', 1, 2),
('2024-04-11 18:30', 'Hovedscenen', 1, 2),
('2024-04-12 18:30', 'Hovedscenen', 1, 2);

/*Lagene til begge teaterstykker */
INSERT INTO Lag (Lagnavn, StykkeID)
VALUES 
('Medvirkende', '1'),
('Kunstnerisk lag', '1'),
('Medvirkende', '2'),
('Kunstnerisk lag', '2');

INSERT INTO Oppgaver (OppgaveID, Oppgavenavn, StykkeID, Lagnavn)
VALUES 
(1, 'Håkon Håkonson', 2, 'Medvirkende'),
(2, 'Dagfinn Bonde', 2, 'Medvirkende'),
(3, 'Jatgeir Skald', 2, 'Medvirkende'),
(4, 'Sigrid', 2, 'Medvirkende'),
(5, 'Ingeborg', 2, 'Medvirkende'),
(6, 'Guttorm Ingesson', 2, 'Medvirkende'),
(7, 'Skule Jarl', 2, 'Medvirkende'),
(8, 'Inga frå Varteig', 2, 'Medvirkende'),
(9, 'Paal Flida', 2, 'Medvirkende'),
(10, 'Ragnhild', 2, 'Medvirkende'),
(11, 'Gregorius Jonsson', 2, 'Medvirkende'),
(12, 'Margrete', 2, 'Medvirkende'),
(13, 'Biskop Nikolas', 2, 'Medvirkende'),
(14, 'Peter', 2, 'Medvirkende');

INSERT INTO Deltar (Aktnummer, StykkeID, OppgaveID)
VALUES 
(1, 2, 1), (2, 2, 1), (3, 2, 1), (4, 2, 1), (5, 2, 1), -- Håkon Håkonson i alle akter
(1, 2, 2), (2, 2, 2), (3, 2, 2), (4, 2, 2), (5, 2, 2), -- Dagfinn Bonde i alle akter
(4, 2, 3), -- Jatgeir Skald i akt 4
(1, 2, 4), (2, 2, 4), (5, 2, 4), -- Sigrid i aktene 1, 2 og 5
(4, 2, 5), -- Ingeborg i akt 4
(1, 2, 6), -- Guttorm Ingesson i akt 1
(1, 2, 7), (2, 2, 7), (3, 2, 7), (4, 2, 7), (5, 2, 7), -- Skule Jarl i alle akter
(1, 2, 8), (3, 2, 8), -- Inga frå Varteig i akt 1 og 3
(1, 2, 9), (2, 2, 9), (3, 2, 9), (4, 2, 9), (5, 2, 9), -- Paal Flida i alle akter
(1, 2, 10), (5, 2, 10), -- Ragnhild i akt 1 og 5
(1, 2, 11), (2, 2, 11), (3, 2, 11), (4, 2, 11), (5, 2, 11), -- Gregorius Jonsson i alle akter
(1, 2, 12), (2, 2, 12), (3, 2, 12), (4, 2, 12), (5, 2, 12); -- Margrete i alle


/*Brukerhistorie 3, fiktiv kunde*/
INSERT INTO Bruker (Fornavn, Etternavn, Telefonnummer, Adresse)
VALUES
('Kong', 'Harald', '+47000030', 'Kongens gate 1, 0153 Oslo');

INSERT INTO Kunde (KundeID, BrukerID)
VALUES
(30, 30);