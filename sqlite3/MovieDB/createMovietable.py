#! usr/bin/python3

import DbManage

def create_table():
    
    with DbManage.DbManage('Movies.db') as movies:

        column_info = """
            MovieID INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            Year INTEGER NOT NULL,
            Director TEXT,
            Genre TEXT,
            Format TEXT
            """

        # MovieID - Primary key, number is the ROWID
        # Name - Name of the movie
        # Year - Year of release
        # Director - Director the movie
        # Genre - Type of movie (Horror, Comedy, ect')
        # Format - Type of media (VHS, DVD, Blu-Ray)

        movies.execute('CREATE TABLE IF NOT EXISTS Movies({})'.
                       format(column_info))

if __name__ == '__main__':

    create_table()
