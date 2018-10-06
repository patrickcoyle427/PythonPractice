# Practice obtained from:
# https://www.python-course.eu/sql_python.php

import sqlite3

connection = sqlite3.connect('company.db')

cursor = connection.cursor()

cursor.execute("SELECT * FROM employee")

print('Fetchall:')

result = cursor.fetchall()

for r in result:

    print(r)

cursor.execute('SELECT * FROM employee')

print('\nfetch one:')

result = cursor.fetchone()

print(result)
