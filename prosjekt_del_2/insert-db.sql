/*Innsetting av teaterstykkene*/
INSERT INTO Teaterstykke (StykkeID, Stykketittel, VarighetMinutt)
VALUES 
(1, 'Størst av alt er kjærligheten', 90),
(2, 'Kongsemnene', 240);


/*Fremvisninger Størst av alt er kjærligheten, pass på at TeaterID og StykkeID er riktig*/
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


