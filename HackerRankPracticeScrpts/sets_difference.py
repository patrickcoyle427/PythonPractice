#!/bin/usr/python3

'''
Task
Students of District College have a subscription to English and French
newspapers. Some students have subscribed to only the English newspaper,
some have subscribed to only the French newspaper, and some have subscribed
to both newspapers.

You are given two sets of student roll numbers. One set has subscribed
to the English newspaper, and one set has subscribed to the French newspaper.
Your task is to find the total number of students who have subscribed to
only English newspapers.

Input Format

The first line contains n, the number of students who have subscribed
to the English newspaper. 
The second line contains the n space separated list of student roll
numbers who have subscribed to the English newspaper.
The third line contains b, the number of students who have subscribed
to the French newspaper. 
The fourth line contains the b space separated list of student roll
numbers who have subscribed to the French newspaper.

Output Format

Output the total number of students who are subscribed to the English newspaper only.

Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

Sample Output

4
'''

def total_dif(group1, group2):

    return len(group1.difference(group2))

if __name__ == '__main__':

    n_eng = int(input())
    eng_subs = set(map(int, input().split()))

    b_frn = int(input())
    frn_subs = set(map(int, input().split()))

    print(total_dif(eng_subs, frn_subs))
