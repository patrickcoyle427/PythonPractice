#!usr/bin/python3

'''
ask

You are given a string S. Your task is to print all possible size k
replacement combinations of the string in lexicographic sorted order.

Input Format

A single line containing the string S and integer value k
separated by a space.

Output Format

Print the combinations with their replacements of string S on separate lines.

Sample Input

HACK 2

Sample Output

AA
AC
AH
AK
CC
CH
CK
HH
HK
KK

'''

from itertools import combinations_with_replacement

word, size = input().split()

word = list(word)

word.sort()

combos = list(combinations_with_replacement(word, int(size)))

for combo in combos:

    for i in combo:
        print(i, end='')

    print()
