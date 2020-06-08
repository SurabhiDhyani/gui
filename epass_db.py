import sqlite3

conn=sqlite3.connect("epass.db")
print("Database opened")

def create_record(applicant, age, phone, autorizedId, foreignTravled, zone, symptoms, reason, validate):
    conn.execute(''' CREATE TABLE IF NOT EXISTS
                    EPass_Records(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    Applicant TEXT NOT NULL,
                    Age TEXT NOT NULL,
                    PhoneNumber TEXT NOT NULL,
                    AuthorizedID TEXT NOT NULL,
                    ForeignTravled TEXT NOT NULL,
                    Zone TEXT NOT NULL,
                    Symptoms TEXT NOT NULL,
                    Reason TEXT NOT NULL,
                    Validate INT NOT NULL)''')

    conn.execute("INSERT INTO EPass_Records(Applicant, Age, PhoneNumber, AuthorizedID, ForeignTravled, Zone, Symptoms, Reason,Validate) VALUES(?,?,?,?,?,?,?,?,?)", (applicant,age,phone,autorizedId,foreignTravled,zone,symptoms,reason,validate))
    conn.commit()