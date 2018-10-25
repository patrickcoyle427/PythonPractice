#!/bin/usr/python3

'''
In this challenge, you will be given 2 integers, n and m. There are n words,
which might repeat, in word group A. There are m words belonging to word
group B. For each m words, check whether the word has appeared in group A or not.
Print the 1-indexed indices of each occurrence of m in group A. If it does not
appear, print -1.

Input Format

The first line contains integers, n and m separated by a space. 
The next n lines contains the words belonging to group A. 
The next m lines contains the words belonging to group B.

Output Format

Output m lines. 
The ith line should contain the 1-indexed positions of the occurrences of the ith
word separated by spaces.

Sample Input

5 2
a
a
b
a
b
a
b

Sample Output

1 2 4
3 5
'''

from collections import defaultdict

if __name__ == '__main__':

    group_a_len, group_b_len = [int(x) for x in input().split()]
    
    groups = defaultdict(list)

    for _ in range(group_a_len):

        groups['a'].append(input())

    for _ in range(group_b_len):

        groups['b'].append(input())

    indexes = ''

    for b_letter in groups['b']:
        
        for let_i in range(len(groups['a'])):

            if groups['a'][let_i] == b_letter:

                indexes += str(let_i + 1) + ' '

            elif let_i + 1 == len(groups['a']) and indexes == '':

                indexes += '-1'
        
        print(indexes.strip())
        indexes = ''
