#!/usr/bin/python3

'''
Task

You are given two values a and n.
Perform integer division and print a // b.

Input Format

The first line contains T, the number of test cases.
The next lines each contain the space separated values of a and b.

Output Format

Print the value of a //b.
In the case of ZeroDivisionError or ValueError, print the error code.

Sample Input

3
1 0
2 $
3 1

Sample Output

Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3

'''

def divide(x,y):

    try:

        x, y = int(x), int(y)
        print(x//y)

    # Exceptions are caught individually
    # Not a good practice to catch all exceptions

    except ValueError as e:

        print('Error Code:', e)

    except ZeroDivisionError as e:

        print('Error Code:', e)
        
if __name__ == '__main__':

    tests = int(input('Number of test cases: 's))

    for _ in range(tests):

        a, b = input('Input 2 values, space separated: ').split()
        
        divide(a,b)






