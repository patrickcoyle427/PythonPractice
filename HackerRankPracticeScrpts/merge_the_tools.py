#!bin/usr/python3

'''
Split a string into equal parts, and print the unique letters in those mini
strings in the order they appear.

Example:

AABCAAADA split into 3 parts gives
['AAB', 'CAA', 'ADA']

What to print:
'AB'
'CA'
'AD'

Strings are always split into equal lengths.

'''

import textwrap

def merge_the_tools(string, k):
    
    split_string = textwrap.wrap(string, k)

    distinct_char = ''

    for string in split_string:

        for letter in string:

            if letter not in distinct_char:

                distinct_char += letter

        print(distinct_char)
        distinct_char = ''

if __name__ == '__main__':
    
    string, k = input('Enter a string: '), int(input('Enter a number that equally divides the string: '))
    merge_the_tools(string, k)

    # Test case to try:
    # AFJALKDELVNEFLAKSDFJIWELAJFLFJAJEUINVMASSSWOEIRANCNASSFJOWEIMLLOIENAFMAAYYU'
    # 5
