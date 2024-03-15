CREATE TABLE
    Teater (
        TeaterID INT PRIMARY KEY,
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
        StykkeID INT PRIMARY KEY,
        Stykketittel VARCHAR(128) NOT NULL,
        VarighetMinutt SMALLINT NOT NULL
    );

CREATE TABLE
    Akt (
        Aktnummer INT NOT NULL,
        StykkeID INT NOT NULL,
        Aktnavn VARCHAR(128) NOT NULL,
        PRIMARY KEY (Aktnummer, StykkeID) FOREIGN KEY (StykkeID) REFERENCES Teaterstykke (StykkeID) ON UPDATE CASCADE ON DELETE CASCADE
    );


CREATE TABLE
    BillettPris (
        Prisgruppe VARCHAR(128) NOT NULL,
        StykkeID INT NOT NULL,
        Pris SMALLINT NOT NULL,
        Minimumsantall SMALLINT NOT NULL CHECK(Minimumsantall >= 1),
        PRIMARY KEY (Prisgruppe, StykkeID),
        FOREIGN KEY (StykkeID) REFERENCES Teaterstykke (StykkeID) ON UPDATE CASCADE ON DELETE CASCADE
    );

CREATE TABLE
    Billett (
        BillettID INT PRIMARY KEY,
        Kolonnenummer SMALLINT NOT NULL,
        Radnummer SMALLINT NOT NULL,
        Områdenummer INT NOT NULL,
        Salnavn VARCHAR(128) NOT NULL,
        TeaterID INT NOT NULL,
        Fremvisningstidspunkt DATETIME NOT NULL,
        StykkeID INT NOT NULL,
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
        AnsattID INT PRIMARY KEY,
        Personnummer INT NOT NULL UNIQUE,
        BrukerID INT NOT NULL UNIQUE,
        FOREIGN KEY (BrukerID) REFERENCES Bruker (BrukerID)
    );

CREATE TABLE
    Kunde (
        KundeID INT PRIMARY KEY,
        BrukerID INT NOT NULL UNIQUE,
        FOREIGN KEY (BrukerID) REFERENCES Bruker (BrukerID)
    );

CREATE TABLE
    Kjøp (
        KjøpID INT PRIMARY KEY,
        KundeID INT NOT NULL,
        BillettID INT NOT NULL  UNIQUE,
        Kjøpstidspunkt DATETIME NOT NULL,
        FOREIGN KEY (KundeID) REFERENCES Kunde (KundeID),
        FOREIGN KEY (BillettID) REFERENCES Billett (BillettID)
    );

CREATE TABLE
    Lag (
        Lagnavn VARCHAR(128) NOT NULL,
        StykkeID INT NOT NULL,
        PRIMARY KEY (Lagnavn, StykkeID),
        FOREIGN KEY (StykkeID) REFERENCES Teaterstykke (StykkeID) ON UPDATE CASCADE ON DELETE CASCADE
    );

CREATE TABLE
    Oppgaver (
        OppgaveID INT,
        Oppgavenavn VARCHAR(128) NOT NULL,
        StykkeID INT NOT NULL,
        Lagnavn VARCHAR(128) NOT NULL,
        PRIMARY KEY (OppgaveID, StykkeID)
        FOREIGN KEY (StykkeID) REFERENCES Teaterstykke (StykkeID) ON UPDATE CASCADE ON DELETE CASCADE
        FOREIGN KEY (Lagnavn, StykkeID) REFERENCES Lag(Lagnavn, StykkeID)
    );

CREATE TABLE
    Rolle (
        OppgaveID INT,
        StykkeID INT NOT NULL,
        Oppgavenavn VARCHAR(128) NOT NULL,
        PRIMARY KEY (OppgaveID, StykkeID)
        FOREIGN KEY (OppgaveID, StykkeID) REFERENCES Oppgaver(OppgaveID, StykkeID)

    );

CREATE TABLE
    Deltar (
        Aktnummer SMALLINT NOT NULL,
        StykkeID INT NOT NULL, 
        OppgaveID INT NOT NULL,
        PRIMARY KEY (Aktnummer, StykkeID, OppgaveID) 
        FOREIGN KEY (Aktnummer, StykkeID) REFERENCES Akt(Aktnummer, StykkeID)
        FOREIGN KEY (OppgaveID, StykkeID) REFERENCES Rolle(OppgaveID, StykkeID)
    );

CREATE TABLE
    Status (Statusnavn VARCHAR(128) PRIMARY KEY);

CREATE TABLE Kontrakt (
    KontraktID INTEGER PRIMARY KEY,
    Signeringsdato DATE NOT NULL,
    Statusnavn VARCHAR(128) NOT NULL,
    KontraktType VARCHAR(50) NOT NULL,
    FOREIGN KEY (Statusnavn) REFERENCES Status (Statusnavn),
    CHECK (KontraktType IN ('Ansatt', 'Direktør'))
);


CREATE TABLE
    Direktørkontrakt (
        DirektørkontraktID INTEGER,
        TeaterID INT NOT NULL UNIQUE,
        FOREIGN KEY (TeaterID) REFERENCES Teater(TeaterID)
        FOREIGN KEY (DirektørkontraktID) REFERENCES Kontrakt (KontraktID)
    );

CREATE TABLE
    AnsattKontrakt (
        AnsattkontraktID INTEGER,
        TeaterID INT NOT NULL,
        Jobbtittel VARCHAR(128) NOT NULL,
        FOREIGN KEY (TeaterID) REFERENCES Teater(TeaterID),
        FOREIGN KEY (AnsattkontraktID) REFERENCES Kontrakt (KontraktID),
        FOREIGN KEY (Jobbtittel) REFERENCES Jobbtittel(Jobbtittel)
    );

CREATE TABLE
    Jobbtittel (Jobbtittel VARCHAR(128) NOT NULL);

CREATE TABLE 
    HarOppgaver (
        AnsattID INT NOT NULL,
        OppgaveID INT NOT NULL,
        StykkeID INT NOT NULL, 
        PRIMARY KEY (AnsattID, OppgaveID),
        FOREIGN KEY (AnsattID) REFERENCES Ansatt(AnsattID),
        FOREIGN KEY (OppgaveID, StykkeID) REFERENCES Oppgaver(OppgaveID, StykkeID)
    );