#!bin/usr/python3
'''
Mr. Vincent works in a door mat manufacturing company.
One day, he designed a new door mat with the following specifications:

Mat size must be n X m. (n is an odd natural number, and m is 3 times n.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
'''

def matprint(num1):
    
    num2 = num1 * 3
    
    for i in range(1, num1, 2):
        print(('.|.' * i).center(num2, '-'))
        
    print('WELCOME'.center(num2, '-'))
    
    for j in range(num1 - 2, 0, -2):
        print(('.|.' * j).center(num2, '-'))


if __name__ == '__main__':

    num = int(input('Enter an odd number greater than 5: '))

    matprint(num)
