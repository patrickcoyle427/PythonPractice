#!usr/bin/python3
'''
Raghu is a shoe shop owner. His shop has X number of shoes. 
He has a list containing the size of each shoe he has in his shop. 
There are N number of customers who are willing to pay Xi amount
of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.
'''

from collections import Counter

def money_earned(shoe_inv, cust_buys):
    
    # Create a dict with shoe_inv. Subtracts the sizes that 
    # customers want from inventory, and calculates the total
    # earned.

    # shoe_inv: list, contains the current sizes in stock
    # cust_buys: list, contains 2 element lists.
    #   [0]: customer's shoe size
    #   [1]: price of the shoe

    # returns the total amount earned from shoe sales

    inventory = Counter(shoe_inv)

    total_earned = 0

    for purchase in cust_buys:

        size = purchase[0]
        price = purchase[1]

        if inventory[size] > 0:

            inventory[size] -= 1
            total_earned += price

    return total_earned


if __name__ == '__main__':

    '''
    The first line contains x, the number of shoes. 
    The second line contains the space separated list of all
    the shoe sizes in the shop.
    The third line contains n, the number of customers. 
    The next n lines contain the space separated values of the
    shoe size desired by the customer and Xi, the price of the shoe.

    Sample Input

    10
    2 3 4 5 6 8 7 6 5 18
    6
    6 55
    6 45
    6 55
    4 40
    18 60
    10 50

    Sample Output:

    200
    '''

    total_shoes = int(input('Total shoes: '))
    
    shoe_inv = [int(x) for x in input('Shoe inventory: ').split(' ')]
    # takes in a space separated list and uses list comprehension to turn
    # all the input into ints
    
    total_customers = int(input('Total customers: '))
    
    cust_purchase = []

    for _ in range(total_customers):
        cust_purchase.append(list(map(
            int, input('Shoe Size and Price: ').strip().split())))
        # Takes in the shoe size and price separated by space, turns them
        # into integers and lists and then adds them to the cust_purchase list

    print('Money earned: ' + money_earned(shoe_inv, cust_purchase))
