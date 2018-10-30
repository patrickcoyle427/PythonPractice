#!usr/bin/python3

'''
You are given a string S.
Your task is to print all possible permutations of size k
of the string in lexicographic sorted order.

Input Format

A single line containing the space separated string S
and the integer value k.

Output Format

Print the permutations of the string
on separate lines. 
'''

from itertools import permutations

word, size = input().split()

combos = list(permutations(word, int(size)))

combos.sort()

for combo in combos:

    for i in combo:

        print(i, end='')

    print()
