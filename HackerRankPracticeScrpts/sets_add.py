#!/usr/bin/python3

'''
Rupal has a huge collection of country stamps. She decided to count the
total number of distinct country stamps in her collection. She asked for your
help. You pick the stamps one by one from a stack of N country stamps.

Find the total number of distinct country stamps.

Input Format

The first line contains an integer N, the total number of country stamps.
The next lines N contains the name of the country where the stamp is from.

Output Format

Output the total number of distinct country stamps on a single line.

Sample Input

7
UK
China
USA
France
New Zealand
UK
France 

Sample Output

5
'''

if __name__ == '__main__':

    total_stamps = int(input())

    dist_stamps = set()

    for _ in range(total_stamps):

        dist_stamps.add(input())

    print(len(dist_stamps))
