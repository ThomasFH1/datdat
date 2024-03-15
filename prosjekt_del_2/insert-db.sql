/*SAAEK=Størst av alt er kjærligheten*/
/*Innsetting av teaterstykkene*/
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
(1, 1, 'akt_1'),


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

