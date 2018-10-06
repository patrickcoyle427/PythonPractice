# Practice obtained from:
# https://www.python-course.eu/sql_python.php

import sqlite3

connection = sqlite3.connect('company.db')

cursor = connection.cursor()

staff_data = [ ('Pat', 'Coyle', 'm', '1988-04-27'),
               ('Mitty', 'Coyle', 'f', '1992-08-20'),
               ('Jane', 'Wall', 'f', '1989-03-14') ]

for p in staff_data:

    format_str = '''INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
                    VALUES (NULL, "{first}", "{last}", "{gender}", "{birthdate}");'''

    sql_command = format_str.format(first=p[0], last=p[1], gender=p[2], birthdate=p[3])

    cursor.execute(sql_command)

connection.commit()
connection.close()
