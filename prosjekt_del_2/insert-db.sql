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

INSERT INTO Ansatt (AnsattID, Personnummer, BrukerID)
VALUES 
(1, 00000000001, 1),
(2, 00000000002, 2),
(3, 00000000003, 3),
(4, 00000000004, 4),
(5, 00000000005, 5),
(6, 00000000006, 6),
(7, 00000000007, 7),
(8, 00000000008, 8),
(9, 00000000009, 9),
(10, 00000000010, 10),
(11, 00000000011, 11),
(12, 00000000012, 12),
(13, 00000000013, 13);

/*Setter inn skuespillere SAAEK først som brukere, så ansatte*/
INSERT INTO Bruker (Fornavn, Etternavn, Telefonnummer, Adresse)
VALUES 
('Sunniva Du Mond', 'Nordal', '+47000014', 'Slottsplassen 1, 0010 Oslo'),
('Jo', 'Saberniak', '+47000015', 'Slottsplassen 1, 0010 Oslo'),
('Marte M.', 'Steinholt', '+47000016', 'Slottsplassen 1, 0010 Oslo'),
('Tor Ivar', 'Hagen', '+47000017', 'Slottsplassen 1, 0010 Oslo'),
('Trond-Ove', 'Skrødal', '+47000018', 'Slottsplassen 1, 0010 Oslo'),
('Natalie Grøndahl', 'Tangen', '+47000019', 'Slottsplassen 1, 0010 Oslo'),
('Åsmund', 'Flaten', '+47000020', 'Slottsplassen 1, 0010 Oslo');

INSERT INTO Ansatt (AnsattID, Personnummer, BrukerID)
VALUES 
(14, '00000000014', 14),
(15, '00000000015', 15),
(16, '00000000016', 16),
(17, '00000000017', 17),
(18, '00000000018', 18),
(19, '00000000019', 19),
(20, '00000000020', 20);



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

