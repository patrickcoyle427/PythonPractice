#!usr/bin/python3

'''
Task:

You are given a string S. 
Your task is to print all possible combinations, up to size k,
of the string in lexicographic sorted order.

Input Format:

A single line containing the string S and integer value k separated by a space.


Output Format:

Print the different combinations of string S on separate lines.

Sample Input

HACK 2

Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK

'''

from itertools import combinations

word, size = input().split()

word = list(word)

word.sort()

combos = []

for i in range(1, int(size) + 1):

    combos.append(list(combinations(word, i)))

for combo in combos:

    for tup in combo:

        for letter in tup:

            if len(tup) > 1:

                print(letter, end='')

            else:

                print(letter)
                
        if len(tup) > 1:
            print()
