#!/usr/bin/python3
'''
You are given an integer N followed by N email addresses. Your task
is to print a list containing only valid email addresses in lexicographical
order.

Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores.
    The website name can only have letters and digits.
    The maximum length of the extension is 3

Input Format

The first line of input is the integer N, the number of email addresses.
N lines follow, each containing a string.

Constraints

Each line is a non-empty string.

Output Format

Output a list containing the valid email addresses in lexicographical order.
If the list is empty, just output an empty list, [].

Sample Input

3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com

Sample Output

['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
'''

def fun(s):

    at_index = 0
    dot_index = 0

    if s.count('@') != 1:

        return False

    else:

        at_index = s.index('@')

    if len(s[:at_index]) < 1:

        return False

    for letter in s[:at_index]:

        if letter not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_1234567890':
            return False

    if s.count('.') != 1:

        return False

    else:

        dot_index = s.index('.')

    if not s[at_index + 1:dot_index].isalnum():

        return False

    elif len(s[dot_index:]) > 4:

        return False 

    return True

def filter_mail(emails):
