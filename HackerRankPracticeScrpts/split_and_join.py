#!usr/bin/python3

'''
You are given a string. Split the string on a " " (space)
delimiter and join using a - hyphen.
'''

def split_and_join(line):
    
    split = line.split(' ')
    
    return '-'.join(split)

if __name__ == '__main__':

    input_string = 'this is a string'

    print(split_and_join(input_string))
