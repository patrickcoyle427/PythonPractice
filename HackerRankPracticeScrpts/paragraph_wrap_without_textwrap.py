#!usr/bin/python3

def wrap(string, max_width):

    x_len_str = ''
    # string to be appended
    to_print = []
    # holds words for each line
    
    for i in range(len(string)):
        
        x_len_str += string[i]
        # adds the current character to the string to be appended
        
        if len(x_len_str) == max_width:
            # once the string to be appended hits the max len, it is
            # appended to the list that will be printed.
            
            to_print.append(x_len_str)
            
            x_len_str = ''

        elif i + 1 == len(string):
            # if the end of the string is reached, the remaining characters
            # are appended to the list to print.

            to_print.append(x_len_str)

    return '\n'.join(to_print)

if __name__ == '__main__':

    word = 'abcdefghijklmnopqrstuvwxyz'
    wrap_len = 4
    print(wrap(word, 4))
    
