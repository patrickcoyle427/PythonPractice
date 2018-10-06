#!usr/bin/python3

# Given the participants' score sheet for your University Sports Day, 
# you are required to find the runner-up score. You are given scores. 
# Store them in a list and find the score of the runner-up.


def next_lowest(case):

    case.sort()

    case_len = len(case)

    for i in range(1, case_len+1):

        if case[-i] < case[-1]:

            return case[-1]

if __name__ == '__main__':

    test_cases = [[2, 3, 6, 6, 5], [10, 19, 3, 7, 8, 4], [1, 7, 15, 10, 63, 20, 43]]

    for case in test_cases:

        print(next_lowest(case))