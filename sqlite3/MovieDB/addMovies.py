#!usr/bin/python3

import DbManage as dbm

# DbManage is a class I wrote to automatically create the db connection, cursor, and to commit
# any changes made to the data base.

def add_movies(mov_list):

    with dbm.DbManage('Movies.db') as movies:

        movies.executemany('INSERT INTO Movies(Name, Year, Director, Genre, Format)\
                           VALUES(?, ?, ?, ?, ?)', mov_list)

if __name__ == '__main__':

    to_insert = [('12 Angry Men', '1957', 'Sidney Lumet', 'Crime Drama', 'DVD'),
                 ('Scream For Help', '1985', 'Michael Winner', 'Horror', 'VHS'),
                 ('40 Year Old Virgin, The', '2005', 'Judd Apatow', 'Comedy', 'DVD'),
                 ('500 Days of Summer', '2009', 'Richard McGonagle', 'Romance Drama', 'DVD'),
                 ('Across The Universe', '2007', 'Julie Taymor', 'Musical', 'DVD'),
                 ('Airplane!', '1980', 'Jim Abrahams, David Zucker, Jerry Zucker', 'Comedy', 'DVD'),
                 ('Alien', '1979', 'Ridley Scott', 'Horror', 'Blu-Ray'),
                 ('Aliens', '1986', 'Ridley Scott', 'Action', 'Blu-Ray'),
                 ('Altered States', '1980', 'Ken Russell', 'Horror', 'DVD'),
                 ('Amelie', '2001', 'Jean-Pierre Jeunet', 'Romantic Comedy', 'DVD'),
                 ('American Psycho', '2000', 'Mary Harron', 'Horror', 'DVD')]

    add_movies(to_insert)


    
