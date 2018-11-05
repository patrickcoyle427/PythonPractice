#!/usr/bin/python3

'''
There is an list of n integers. There are also 2 disjoint sets, A and B,
each containing m integers. You like all the integers in set A and dislike all
the integers in set B. Your initial happiness is 0. For each integer in the
array, if i in A, you add 1 to your happiness. If i in b, you add -1
to your happiness. Otherwise, your happiness does not change.
Output your final happiness at the end.

Note: Since A and B and are sets, they have no repeated elements.
However, the list might contain duplicate elements.

Input Format

The first line contains integers n and m and separated by a space.
The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers, A and B, respectively.

Output Format

Output a single integer, your total happiness.
'''

def happiness(to_check, happy_up, happy_down):

    happy_points = 0

    for i in to_check:

        if i in happy_up:

            happy_points += 1

        elif i in happy_down:

            happy_points -= 1

    return happy_points

if __name__ == '__main__':

    m, n = list(map(int, input().split()))

    happy_check = list(map(int, input().split()))

    happy = set(map(int, input().split()))
    unhappy = set(map(int, input().split()))

    print(happiness(happy_check, happy, unhappy))
