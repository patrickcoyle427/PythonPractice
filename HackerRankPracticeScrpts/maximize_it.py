#!/bin/usr/python3

'''

You are given a function f(X) = X**2. You are also given K lists. The ith list
consists of Ni elements.

You have to pick one element from each list so that the value from the equation
below is maximized:

S = (f(X1) + f(X2) + ... _ f(Xk)) % M

Xi denotes the element picked from the ith list. Find the maximized value S-max
% denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily
the largest element. You add the squares of the chosen elements and perform
the modulo operation. The maximum value that you can obtain, will be the answer
to the problem.

Input Format

The first line contains 2 space separated integers K and M.
The next lines each contains an integer Ni, denoting the number of elements
in the list, followed by space separated integers denoting the elements in
the list.

Output Format

Output a single integer denoting the value S-max

Sample Input

3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10

Sample Output

206

Also try:

3 998
6 67828645 425092764 242723908 669696211 501122842 438815206
4 625649397 295060482 262686951 815352670
3 100876777 196900030 523615865

'''

from itertools import product

'''
To solve this problem, need to figure out all combinations when picking 1 item
from each list, then do the required calculations, and return the largest
value found. Since modulous is involved, the the combo that returns the greatest
number is not going to be whatever value is found by max() each time.
'''

def maximize_it(lists, modulous):

    for group in lists:

        group.pop(0)
        # first number is discarded, it is just the number of elements
        # in each list

    possible_combos = product(*lists)
    # by using * before lists, lists are fed into product individually

    maximum = 0

    for nums in possible_combos:

        total = 0

        for num in nums:

            total += num ** 2

        total %= modulous

        if total > maximum:

            maximum = total

    return maximum
    

if __name__ == '__main__':

    lines, modulo_num = list(map(int, input().split()))

    num_lists = []

    for i in range(lines):

        num_lists.append(list(map(int, input().split())))

    print(maximize_it(num_lists, modulo_num))




