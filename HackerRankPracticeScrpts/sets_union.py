#/usr/bin/python3

'''
Task

The students of District College have subscriptions to English and French
newspapers. Some students have subscribed only to English, some have
subscribed to only French and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to
the English newspaper, and the other set is subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.

Input Format

The first line contains an integer, n, the number of students who have
subscribed to the English newspaper.
The second line contains n space separated roll numbers of those students.
The third line contains b, the number of students who have subscribed to the
French newspaper.
The fourth line contains b space separated roll numbers of those students.

Output Format

Output the total number of students who have at least one subscription.

Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

Sample Output

13

'''

def min_1_sub(group1, group2):

    return len((group1.union(group2)))

if __name__ == '__main__':

    n_eng = int(input())

    eng_subs = set(map(int, input().split()))

    n_frn = int(input())

    frn_subs = set(map(int, input().split()))
    
    print(min_1_sub(eng_subs, frn_subs))
