#!/usr/bin/python3

'''
Task

You have a non-empty set
, and you have to execute commands given in

lines.

The commands will be pop, remove and discard.

Input Format

The first line contains integer n, the number of elements in the set .
The second line contains n space separated elements of set s. All of the
elements are non-negative integers, less than or equal to 9.
The third line contains integer N, the number of commands.
The next N lines contains either pop, remove and/or discard commands followed
by their associated value.

Output Format

Print the sum of the elements of set s on a single line.

Sample Input

9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5

Sample Output

4
'''

def remaining_elms(to_mod, commands):

    for command in commands:

        if len(command[0]) == 1:
            
            try:

                exec('to_mod.{}()'.format(command[0]))

            except ValueError:

                pass
        
        else:

            try:

                exec('to_mod.{}({})'.format(command[0], int(command[1])))

            except ValueError:

                pass

    return sum(to_mod)

if __name__ == '__main__':
   
    n = int(input())
    s = set(map(int, input().split()))

    total_commands = int(input())

    commands = []

    for _ in range(total_commands):

        commands.append(input().split())

    print(remaining_elms(s, commands))    
