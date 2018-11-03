#!/usr/bin/python3

'''
You have to generate a list of the first N fibonacci numbers, 0 being the first
number. Then, apply the map function and a lambda expressionto cube each
fibonacci number and print the list.
'''

cube = lambda x: x ** 3

def fibonacci(n):

    fib = []

    x, y = 0, 1
    
    for _ in range(n):

        fib.append(x)
        
        x, y = y, x + y

    return fib


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
