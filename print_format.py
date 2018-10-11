#!usr/bin/python3
'''
Print n lines where each line n (in the range 1 < i < n)
contains the respective decimal, octal, capitalized
hexadecimal, and binary values of n. Each printed
value must be formatted to the width of the binary
value of n.
'''

def print_formatted(number):

    bin_num = len('{:b}'.format(number))

    for i in range(1, number + 1):

        for base in 'doXb':

            print('{i:{width}{base}}'.format(width=bin_num, i=i, base=base), end=' ')

        print()

if __name__ == '__main__':
    
    n = int(input('Enter a number: '))
    print_formatted(n)
