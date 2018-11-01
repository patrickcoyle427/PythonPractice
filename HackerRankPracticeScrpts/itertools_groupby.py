#!/usr/bin/python3
'''
You are given a string S. Suppose a character 'c' occurs consecutively
times in the string. Replace these consecutive occurrences of the character
'c' with (X, c) in the string.

All the characters of S denote integers between 0 and 9

Input Format

A single line of input consisting of the string S.

Output Format

A single line of output consisting of the modified string.

Sample Input

1222311

Sample Output

(1, 1) (3, 2) (1, 3) (2, 1)

'''

from itertools import groupby

S = input()

for letter, amt in groupby(S):

    print('({}, {})'.format(len(list(amt)), letter), end=' ')
