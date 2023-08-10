#!/usr/bin/python3

import sqlite3

conn = sqlite3.connect('miniproject_database2.db')

# Create a cursor object to execute SQL commands
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Best_Doggos (ranking Integer, name TEXT)''')

c.execute("INSERT INTO Best_Doggos (ranking, name) VALUES (1, 'Golden Retriever.')")
c.execute("INSERT INTO Best_Doggos (ranking, name) VALUES (2, 'Poodle')")
c.execute("INSERT INTO Best_Doggos (ranking, name) VALUES (3, 'Akita')")
c.execute("INSERT INTO Best_Doggos (ranking, name) VALUES (4, 'Boxer')")
c.execute("INSERT INTO Best_Doggos (ranking, name) VALUES (5, 'Pitbull')")
c.execute("INSERT INTO Best_Doggos (ranking, name) VALUES (6, 'Dashund')")

# Commit changes and close the connection
conn.commit()
conn.close()


