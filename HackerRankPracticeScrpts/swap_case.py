#!usr/bin/python3

'''
You are given a string and your task is to swap cases.
In other words, convert all lowercase letters to uppercase
letters and vice versa.
'''

def swap_case(string):

    return string.swapcase()

if __name__ == '__main__':

    to_switch = 'HackerRank.com presents "Pythonist 3"'

    print(swap_case(to_switch))
