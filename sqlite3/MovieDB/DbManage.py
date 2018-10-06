#!bin/usr/python3
"""
DbManage - Class to help manage sqlite databases.
           To be used with With to automatically create the connection
           and cursor, and to close the cursor and commit the changes"""

import sqlite3

class DbManage(object):

    def __init__(self, dbName):

        # dbName: string that has the name of the database

        self.dbName = dbName   
        self.conn = None
        self.cursor = None

        # Creates the variables that will be used for the connection
        # object and the cursor.

    def __enter__(self):

        # When using a With statement, returns the database cursor

        self.conn = sqlite3.connect(self.dbName)
        self.cursor = self.conn.cursor()

        return self.cursor

    def __exit__(self, dbType, dbValue, dbTb):

        # dbType, dbValue, dbTb are exception values passed to
        # __exit__

        # closes the cursor and saves any changes to the database
        # when the With statement is finished.
        
        self.conn.commit()
        self.conn.close()

        

            

            
        
