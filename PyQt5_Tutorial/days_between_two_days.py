#!/usr/bin/python3

'''

days_between_two_days.py - Asks the user for two dates and tells them
                           the number of days in between.

'''

from PyQt5.QtCore import QDate, Qt

def ask_for_days():

    date1_split = None
    date2_split = None

    date_separators = ('/', '-', ' ')

    while True:
        
        print('Please enter a date, in DD MM YYYY format')
    
        date1 = input('> ')

        if len(date1) != 10:

            print('Invalid date! Please enter another.')

        else:

            break

    while True:
        
        print('Please enter a second date in DD MM YYYY format')
                
        date2 = input('> ')

        if len(date2) != 10:

            print('Invalid date! Please enter another.')

        else:

            break

    for spacer in date_separators:

        if spacer in date1:

            date1_split = date1.split(spacer)

        if spacer in date2:

            date2_split = date2.split(spacer)

    if date1_split == None or date2_split == None:

        # Raises an error if the script can't parse the dates.

        raise ValueError('No separator in your date!',
                         'Please use a space, / or - to separate the numbers')

    else:

        return (date1_split, date2_split)


def calculate_days_between(dates):

    # dates - assumed to be a tuple containing 2 lists with

    day1, month1, year1 = dates[0]
    day2, month2, year2 = dates[1]

    date1 = QDate(int(year1), int(month1), int(day1))
    date2 = QDate(int(year2), int(month2), int(day2))

    days_between = abs(date1.daysTo(date2))

    # Uses the absolute value because we only care the total number
    # of days between, and don't want to display a negative number

    print('Date 1: {}'.format(date1.toString(Qt.DefaultLocaleLongDate)))
    print('Date 2: {}'.format(date2.toString(Qt.DefaultLocaleLongDate)))

    if days_between == 1:

        print('There is 1 day between these two dates')

    else:

        print('There are {} days between these two dates'.format(days_between))

if __name__ == '__main__':

    dates = ask_for_days()

    calculate_days_between(dates)
                                           
