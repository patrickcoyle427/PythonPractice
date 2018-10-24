#!usr/bin/python3

def alphabet_rangoli(size):

    alpha = 'abcdefghijklmnopqrstuvwxyz'

    middle = ''
    # The middle line is created first
    # This is used to determine the length to fill with .center()

    for i in range(size - 1, -1, -1):

        # loop to create the middle of the rangoli

        middle += alpha[i]

        if i != 0:

            middle += '-'

    for j in range(1, size):
        
        middle += ('-' + alpha[j])

    top = alpha[size-1]
    # create the top point of the rangoli

    topL = top + '-'
    topR = '-' + top
    # starts the top left and right sides of each line

    to_bottom = [top]
    # creates a list that will become the bottom of the rangoli.
    # the top point is added to the list to start as it will also
    # be the bottom point of the rangoli
    
    print(top.center(len(middle), '-'))
    # prints the top point of the rangoli

    for j in range(size - 2, -1, -1):

        # loop prints each line of the rangoli. It does this by
        # saving the top-left side and top-right side and building
        # upon them with each loop
        
        top = topL + alpha[j] + topR
        to_bottom.append(top)
        topL += alpha[j] + '-'
        topR = '-' + alpha[j] + topR
        
        print(top.center(len(middle), '-'))

    if len(to_bottom) > 1:
    # if to_bottom has 1 or less items, the next section is skipped.
    # appends the bottom point of the rangoli to to_bottom

        for i in range(2, len(to_bottom) + 1):
            # prints the rows created in top in reverse order
            # starts at 2 so the middle row isn't repeated

            print(to_bottom[-i].center(len(middle), '-'))           

if __name__ == '__main__':

    size = 6

    alphabet_rangoli(size)

