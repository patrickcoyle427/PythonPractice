#!/usr/bin/python3

'''
invert.py - takes in an image and inverts the colors, then saves it to
            the user's current working directory
'''

import sys, os.path
import numpy as np
import matplotlib.image as mpimg

def get_user_choice():

    while True:

        print('Enter the path for the image')
        print('If the image is in the same location as this program,')
        print('you can just enter the name and the file type (example.png)')
            
        choice = input('> ')

        if choice.endswith(('.png', '.jpg', '.jpeg')) != True:

            print('File must be PNG, JPG, or JPEG! Please try another file')
            # Checks the file type to make sure it can be inverted

            continue

        else:

            return choice

def invert_and_save(image):

    # Image is a string that references a file path

    while True:

        try:

            img = mpimg.imread(image)

        except FileNotFoundError:

            print('\nCould not find file. Please try another path\n')

            image = get_user_choice()

            # Lets the user enter another image if their first one couldn't
            # be found.

            continue

    file_name = image.split('.')[0]
    # Grabs the name of the file to be used in the inverted image's name

    if img.dtype == 'float32' or img.dtype == 'float64':

        # Checks the type of the file. If the image is a float,
        # Then then to invert the colors we just have to subtract
        # them from 1. This is because the colors are stored as
        # a number from 0 to 1.

        inverted = 1 - img

        # Creates a numpy ndarray

    elif img.dtype == 'uint8':

        # If the image is unt8, the colors are stored from 0-255
        # and the array's values can just be subtracted them from 255

        inverted = 255 - img

        # Creates a numpy ndarray

    else:

        print('Type not supported')
        
        sys.exit()

        # Exits if the file can't be inverted

    new_file_name = '{}_inverted.png'.format(file_name)

    mpimg.imsave(new_file_name, inverted)

    print('Image saved as {}.'.format(new_file_name))
    
if __name__ == '__main__':

    image = get_user_choice()
    invert_and_save(image)
