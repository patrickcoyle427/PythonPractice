#!/bin/usr/python3

'''
president_ages.py - scrapes the ages of all of the US presidents in days from
                    wikipedia, calculates the number of years they were alive,
                    then displays the information using a pandas dataframe.

prompt from:

'''

import requests, bs4, pandas, numpy

headers = {

    'user-agent': 'python-requests/4.8.2(Compatible; pcoyle)'

    }

try:

    r = requests.get('https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States_by_age',
                     headers = headers)
    # Source of data scraping.

    
    r.raise_for_status()

except:

    print('There was an error! Error code: {}'.format(r.status_code))

    # If for some reason the data can't be pulled, the rest of the
    # script won't be run.

else:

    days_and_years = {

        'Days': [],
        'Years': []

        }
    #Dictionary to hold the results of the scraping
        
    site_text = r.text

    soup = bs4.BeautifulSoup(site_text, 'html.parser')

    finding_lifespan = soup.find_all('td')

    presidents = [
            
        'George Washington',
        'John Adams',
        'Thomas Jefferson',
        'James Madison',
        'James Monroe',
        'John Q. Adams',
        'Andrew Jackson',
        'Martin Van Buren',
        'William H. Harrison',
        'John Tyler', 
        'James K. Polk',
        'Zachary Taylor', 
        'Millard Fillmore',
        'Franklin Pierce',
        'James Buchanan',
        'Abraham Lincoln',
        'Andrew Johnson',
        'Ulysses S. Grant',
        'Rutherford B. Hays',
        'James A. Garfield',
        'Chester A. Arthur',
        'Grover Cleveland',
        'Benjamin Harrison',
        'Grover Cleveland (2nd term)',
        'William McKinley',
        'Theodore Roosevelt',
        'William H. Taft',
        'Woodrow Wilson',
        'Warren G. Harding',
        'Calivn Coolidge',
        'Herbert Hoover',
        'Franklin D. Roosevelt',
        'Harry S. Truman',
        'Dwight D. Eisenhower',
        'John F. Kennedy',
        'Lyndon B. Johnson',
        'Richard Nixon',
        'Gerald Ford',
        'Jimmy Carter',
        'Ronald Reagan',
        'George H. W. Bush',
        'Bill Clinton',
        'George W. Bush',
        'Barack Obama',
        'Donald Trump'

        ]

    # List of all president names.

    for line in finding_lifespan:

        line_text = line.get_text()

        line_len = len(line_text)
        #lines with the president's age in days are between 50 and 52 characters long.

        if line_len > 49 and line_len < 53 and  'days)' in line_text:

            split_num = line_text[-13:][1:7].split(',')

            days_alive = int(split_num[0] + split_num[1])

            years_alive = days_alive / 365.25
            #365.25 days in a year. Takes leap years into consideration

            days_and_years['Years'].append(years_alive)

            days_and_years['Days'].append(days_alive)

    df = pandas.DataFrame(days_and_years, index = presidents)

    print(df)
