#!/usr/bin/python3
'''
Task

You are given a date. Your task is to find what the day is on that date.

Input Format

A single line of input containing the space separated month, day and year,
respectively, in MM DD YYYY format.

Output Format

Output the correct day in capital letters.


'''
import calendar

def day_of_week(to_check):
    # to_check: list of integers that correspond to dates in
    # month, day, year order

    month, day, year = to_check

    return calendar.day_name[calendar.weekday(year, month, day)].upper()

if __name__ == '__main__':

    date = list(map(int, input().split()))

    print(day_of_week(date))
