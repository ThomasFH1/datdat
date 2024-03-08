CREATE TABLE
    Teater (
        TeaterID INT NOT NULL PRIMARY KEY,
        Teaternavn VARCHAR(128) NOT NULL
    );

CREATE TABLE
    Sal (
        Salnavn VARCHAR(128) NOT NULL,
        TeaterID INT NOT NULL,
        PRIMARY KEY (Salnavn, TeaterID),
        FOREIGN KEY (TeaterID) REFERENCES Teater (TeaterID) ON UPDATE CASCADE ON DELETE CASCADE
    );

CREATE TABLE
    Område (
        Områdenummer INT NOT NULL,
        Områdenavn VARCHAR(128) NOT NULL,
        Salnavn VARCHAR(128) NOT NULL,
        TeaterID INT NOT NULL,
        PRIMARY KEY (Områdenummer, Salnavn, TeaterID),
        FOREIGN KEY (Salnavn, TeaterID) REFERENCES Sal (Salnavn, TeaterID) ON UPDATE CASCADE ON DELETE CASCADE
    );

CREATE TABLE
    Rad (
        Radnummer SMALLINT NOT NULL,
        Områdenummer INT NOT NULL,
        Salnavn VARCHAR(128) NOT NULL,
        TeaterID INT NOT NULL,
        PRIMARY KEY (Radnummer, Områdenummer, Salnavn, TeaterID),
        FOREIGN KEY (Områdenummer, Salnavn, TeaterID) REFERENCES Område (Områdenummer, Salnavn, TeaterID) ON UPDATE CASCADE ON DELETE CASCADE
    );

CREATE TABLE
    Stol (
        Kolonnenummer SMALLINT NOT NULL,
        Radnummer SMALLINT NOT NULL,
        Områdenummer INT NOT NULL,
        Salnavn VARCHAR(128) NOT NULL,
        TeaterID INT NOT NULL,
        Handicapstol BOOLEAN NOT NULL,
        PRIMARY KEY (
            Kolonnenummer,
            Radnummer,
            Områdenummer,
            Salnavn,
            TeaterID
        ) FOREIGN KEY (Radnummer, Områdenummer, Salnavn, TeaterID) REFERENCES Rad (Radnummer, Områdenummer, Salnavn, TeaterID) ON UPDATE CASCADE ON DELETE CASCADE
    );

CREATE TABLE
    Teaterstykke (
        StykkeID INT NOT NULL,
        Stykketittel VARCHAR(128) NOT NULL,
        VarighetMinutt SMALLINT NOT NULL,
        PRIMARY KEY (StykkeID)
    );

CREATE TABLE
    Akt (
        Aktnummer INT NOT NULL,
        Aktnavn VARCHAR(128) NOT NULL,
        StykkeID INT NOT NULL,
        PRIMARY KEY (Aktnummer, StykkeID) FOREIGN KEY (StykkeID) REFERENCES Teaterstykke (StykkeID) ON UPDATE CASCADE ON DELETE CASCADE
    );

CREATE TABLE
    Fremvisning (
        Fremvisningstidspunkt DATETIME NOT NULL,
        Salnavn VARCHAR(128) NOT NULL,
        TeaterID INT NOT NULL,
        StykkeID INT NOT NULL,
        PRIMARY KEY (
            Fremvisningstidspunkt,
            Salnavn,
            TeaterID,
            StykkeID
        ),
        FOREIGN KEY (Salnavn, TeaterID) REFERENCES Sal (Salnavn, TeaterID) ON UPDATE CASCADE ON DELETE CASCADE,
        FOREIGN KEY (StykkeID) REFERENCES Teaterstykke (StykkeID) ON UPDATE CASCADE ON DELETE CASCADE
    );

CREATE TABLE
    BillettPris (
        Prisgruppe VARCHAR(128) NOT NULL,
        StykkeID INT NOT NULL,
        Pris SMALLINT NOT NULL,
        PRIMARY KEY (Prisgruppe, StykkeID),
        FOREIGN KEY (StykkeID) REFERENCES Teaterstykke (StykkeID) ON UPDATE CASCADE ON DELETE CASCADE
    );

CREATE TABLE
    Billett (
        BillettID INT NOT NULL,
        Kolonnenummer SMALLINT NOT NULL,
        Radnummer SMALLINT NOT NULL,
        Områdenummer INT NOT NULL,
        Salnavn VARCHAR(128) NOT NULL,
        TeaterID INT NOT NULL,
        Fremvisningstidspunkt DATETIME NOT NULL,
        StykkeID INT NOT NULL,
        PRIMARY KEY (BillettID),
        FOREIGN KEY (
            Kolonnenummer,
            Radnummer,
            Områdenummer,
            Salnavn,
            TeaterID
        ) REFERENCES Stol (
            Kolonnenummer,
            Radnummer,
            Områdenummer,
            Salnavn,
            TeaterID
        ),
        FOREIGN KEY (
            Fremvisningstidspunkt,
            Salnavn,
            TeaterID,
            StykkeID
        ) REFERENCES Fremvisning (
            Fremvisningstidspunkt,
            Salnavn,
            TeaterID,
            StykkeID
        )
    );

CREATE TABLE
    Bruker (
        BrukerID INT AUTO_INCREMENT PRIMARY KEY,
        Fornavn VARCHAR(128) NOT NULL,
        Etternavn VARCHAR(128) NOT NULL,
        Telefonnummer VARCHAR(14) NOT NULL,
        Adresse VARCHAR(128) NOT NULL
    );

CREATE TABLE
    Ansatt (
        AnsattID INT AUTO_INCREMENT PRIMARY KEY,
        Personnummer INT NOT NULL UNIQUE,
        BrukerID INT NOT NULL UNIQUE,
        FOREIGN KEY (BrukerID) REFERENCES Bruker (BrukerID)
    );

CREATE TABLE
    Kunde (
        KundeID INT AUTO_INCREMENT PRIMARY KEY,
        BrukerID INT NOT NULL UNIQUE,
        FOREIGN KEY (BrukerID) REFERENCES Bruker (BrukerID)
    );

CREATE TABLE
    Kjøp (
        KjøpID INT AUTO_INCREMENT PRIMARY KEY,
        KundeID INT NOT NULL,
        BillettID INT NOT NULL,
        Kjøpstidspunkt DATETIME NOT NULL,
        FOREIGN KEY (KundeID) REFERENCES Kunde (KundeID),
        FOREIGN KEY (BillettID) REFERENCES Billett (BillettID)
    );

CREATE TABLE
    Oppgaver (
        OppgaveID INT AUTO_INCREMENT PRIMARY KEY,
        Oppgavenavn VARCHAR(128) NOT NULL,
        StykkeID INT NOT NULL,
        FOREIGN KEY (StykkeID) REFERENCES Teaterstykke (StykkeID) ON UPDATE CASCADE ON DELETE CASCADE
    );

CREATE TABLE
    Lag (
        Lagnavn VARCHAR(128) NOT NULL,
        StykkeID INT NOT NULL,
        PRIMARY KEY (Lagnavn, StykkeID),
        FOREIGN KEY (StykkeID) REFERENCES Teaterstykke (StykkeID) ON UPDATE CASCADE ON DELETE CASCADE
    );

CREATE TABLE
    Rolle (
        RolleID INT AUTO_INCREMENT PRIMARY KEY,
        Rollenavn VARCHAR(128) NOT NULL
    );

CREATE TABLE
    Deltar (
        RolleID INT NOT NULL,
        Aktnummer SMALLINT NOT NULL,
        StykkeID INT NOT NULL, 
        PRIMARY KEY (RolleID, Aktnummer, StykkeID) 
    );

CREATE TABLE
    Status (Statusnavn VARCHAR(128) PRIMARY KEY);

CREATE TABLE
    Kontrakt (
        KontraktID INTEGER PRIMARY KEY,
        Signeringsdato DATE NOT NULL,
        Statusnavn VARCHAR(128) NOT NULL,
        KontraktType VARCHAR(50) NOT NULL, -- 'Ansatt' eller 'Direktør'
        FOREIGN KEY (Statusnavn) REFERENCES Status (Statusnavn)
    );

CREATE TABLE
    DirektorKontrakt (
        DirektorkontraktID INTEGER,
        FOREIGN KEY (DirektorkontraktID) REFERENCES Kontrakt (KontraktID)
    );

CREATE TABLE
    AnsattKontrakt (
        AnsattkontraktID INTEGER,
        FOREIGN KEY (AnsattkontraktID) REFERENCES Kontrakt (KontraktID)
    );

CREATE TABLE
    Jobbtittel (Jobbtittel VARCHAR(128) NOT NULL);

CREATE TABLE 
    HarOppgaver (
        AnsattID INT NOT NULL,
        OppgaveID INT NOT NULL,
        PRIMARY KEY (AnsattID, OppgaveID),
        FOREIGN KEY (AnsattID) REFERENCES Ansatt(AnsattID),
        FOREIGN KEY (OppgaveID) REFERENCES Oppgaver(OppgaveID)
    );