#!/usr/bin/python3'
'''
Task

Take in a list of Fractions, then find and return their product

Input Format

First line contains n, the number of rational numbers.
The ith of next n lines contain two integers each, the numerator(Ni)
and denominator(Di) of the rational number in the list.

Sample Input 0

3
1 2
3 4
10 6

Sample Output 0

5 8


'''

from fractions import Fraction
from functools import reduce

def product(fracs):
    
    t = reduce(lambda x, y: x * y, fracs)
    
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    
    for _ in range(int(input())):
        
        fracs.append(Fraction(*map(int, input().split())))
        
    result = product(fracs)
    
    print(*result)
