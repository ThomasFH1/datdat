import sqlite3

con = sqlite3.connect("Theatre.db")
cursor = con.cursor()

cursor.execute("INSERT INTO Teaterstykke (StykkeTittel, VarighetMinutt) VALUES (?, ?)", ("Største av alt er kjærlighet whatever", 10))

#cursor.execute("INSERT INTO forestilling VALUES (?, ?, ?, ?)", ("2024-02-03", "Gamle Scene", 1, 1 ))

"""

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

"""