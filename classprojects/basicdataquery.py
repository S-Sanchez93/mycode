#!/usr/bin/env/python3

import sqlite3  

connection = sqlite3.connect('miniproject_database2.db')

cursor = connection.cursor()

query = "SELECT * FROM Best_Doggos"

cursor.execute(query)

results = cursor.fetchall()

for row in results:
    print(row)

cursor.close()

connection.commit()
connection.close()

