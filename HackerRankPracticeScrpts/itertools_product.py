#!usr/bin/python3

# You are given two lists a and b. Your task is to compute their
# cartesian product a * b.

from itertools import product

a = list(map(int, input().split()))

b = list(map(int, input().split()))

axb = list(product(a,b))

for line in axb:
    print(line, end=' ')
