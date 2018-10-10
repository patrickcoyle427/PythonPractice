import textwrap

def wrap(string, max_length):

    return '\n'.join(textwrap.wrap(string, max_length))

if __name__ == '__main__':

    to_wrap = 'abcdefghijklmnopqrstuvwxyz'
    wrap_len = 4
    print(wrap(to_wrap, 4))
