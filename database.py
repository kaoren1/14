import sqlite3

conn = sqlite3.connect("database2.db")
cursor = conn.cursor()
cursor.execute('''
        CREATE TABLE IF NOT EXISTS Service(
            ID_Service INTEGER PRIMARY KEY,
            NameService TEXT NOT NULL,
            Price FLOAT NOT NULL 
        )
''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS Master(
            ID_Master INTEGER PRIMARY KEY,
            SurnameMaster TEXT NOT NULL,
            NameMaster TEXT NOT NULL
        )
''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS SessionTime(
            ID_SessionTime INTEGER PRIMARY KEY,
            Duration FLOAT NOT NULL
        )
''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS Building(
            ID_Building INTEGER PRIMARY KEY,
            Street TEXT NOT NULL
        )
''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS Difficulty(
            ID_Building INTEGER PRIMARY KEY,
            Difficulty_level TEXT NOT NULL
        )
''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS Tatoo_parlour(
            ID_Tatoo INTEGER PRIMARY KEY,
            Service_ID INT NOT NULL,
            Master_ID INT NOT NULL,
            SessionTime_ID INT NOT NULL,
            Building_ID INT NOT NULL,
            FOREIGN KEY (Service_ID) REFERENCES Service(ID_Service),
            FOREIGN KEY (Master_ID) REFERENCES Master(ID_Master),
            FOREIGN KEY (SessionTime_ID) REFERENCES SessionTime(ID_SessionTime),
            FOREIGN KEY (Building_ID) REFERENCES Building(ID_Building)
        )
''')

value = "Нанесение татуировки"
value_price = 2000
cursor.execute("INSERT INTO Service (NameService, Price) VALUES (?,?)", (value, value_price))
conn.commit()

surname = "Петров"
name = "Пётр"
cursor.execute("INSERT INTO Master (SurnameMaster, NameMaster) VALUES (?, ?)", (surname, name))
conn.commit()

duration_value = 2
cursor.execute("INSERT INTO SessionTime (Duration) VALUES (?)", (duration_value,))
conn.commit()

street_value = "ул. Петровская д.28"
cursor.execute("INSERT INTO Building (Street) VALUES (?)", (street_value,))
conn.commit()

conn.commit()
conn.close()
