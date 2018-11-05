#!/bin/usr/python3

'''
Task
Given sets of integers, N and M, print their symmetric difference in ascending
order. The term symmetric difference indicates those values that exist in
either or but do not exist in both.

Input Format

The first line of input contains an integer, N.
The second line contains N space-separated integers.
The third line contains an integer, M.
The fourth line contains M space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.
'''

def sym_diff(g1, g2):

    set1, set2 = set(g1), set(g2)

    diff1 = set1.difference(set2)
    diff2 = set2.difference(set1)

    diff1.update(diff2)

    diff1 = list(diff1)

    diff1.sort()

    return diff1

if __name__ == '__main__':

    n_lines = int(input())
    n_values = list(map(int, input().split()))

    m_lines = int(input())
    m_values = list(map(int, input().split()))

    for value in sym_diff(n_values, m_values):

        print(value)

