#!/usr/bin/python3

'''

currencyExchangeRate.py - Lets the user specify the currency they have an an amount.
                          They can then select which currencies they would like to see
                          their original amount converted to.

                          Scrapes x-rates.com for up to date exchage information and
                          displays it to the user.

Prompt from: https://www.reddit.com/r/PythonProjects2/
             comments/81rvtt/make_a_currency_exchange_rate_calculator/

'''

import requests, bs4

#requests - used to download the html of the table page on x-rates.com
#bs4 - used to parse the downloaded html from x-rates.com

def ask_user():

    to_find = []
    
    while True:

        print('Which currency do you want to excange?')
        print('Type code to see all the currency codes')

        to_exchange = input('> ').upper()

        if to_exchange == 'CODE':

            display_currency('print')

        elif currencies(to_exchange) == None:

            #Checks to see if the currency the user entered exists

            print('\nThat is not a valid currency! If you are unsure of the 3 letter')
            print('code you are looking for, type code to see all options.\n')

        else:

            break

    while True:

        print('\nHow much currency do you have in {}?'.format(to_exchange))

        try:

            amount = int(input('> '))

            if amount > 0:

                break

            else:

                print('\nPlease enter a number above 0.')

        except ValueError:

            print('\nThat is not a number! Please only enter a number')

            #Prevents user from crashing the program by entering a non-number
            
            continue

    while True:

        print('\nEnter in a currency to find.')
        print('Type stop to convert to the specified currencies.')
        print('Type all to see all currency conversions.')
        print('Type code to see all options.')

        choice = input('> ').upper()

        if choice == 'CODE':

            display_currency('print')

        elif choice == 'STOP':

            if len(to_find) == 0:

                print('\nYou have not chosen any currencies!')
                print('Please choose a currency before typing stop.')

            else:

                get_exchange(to_exchange, amount, set(to_find))
                #A set is passed into the function here in case the user enters any duplicates
                
                break

        elif choice == 'ALL':

            all_currencies = display_currency('all valid')

            get_exchange(to_exchange, amount, all_currencies)

            break

        elif currencies(choice) != None:

            print('You have selected {}'.format(choice))

            to_find.append(choice)

        else:

            print('\nSorry, that was not a valid choice. Please enter either')
            print('a currency, stop, all, or code.')

            
def currencies(currency):

    #currency - string - 3 letter code for a country's currency
    #Used for printing and validating whether the country the user picked exists or not.

    currency_origin = {'AED': 'Emirati Dirham',
                       'ARS': 'Argentine Peso',
                       'AUD': 'Australian Dollar',
                       'BHD': 'Bahraini Dinar',
                       'BWP': 'Botswana Pula',
                       'BND': 'Bruneian Dollar',
                       'BRL': 'Brazilian Real',
                       'CAD': 'Canadian Dollar',
                       'CLP': 'Chilean Peso',
                       'CNY': 'Chinese Yuan Renminbi',
                       'COP': 'Colombian Peso',
                       'HRK': 'Croatian Kuna',
                       'HUF': 'Hungarian Forint',
                       'ISK': 'Icelandic Krona',
                       'INR': 'Indian Rupee',
                       'IRR': 'Iranian Rial',
                       'ILS': 'Israeli Shekel',
                       'JPY': 'Japanese Yen',
                       'KZT': 'Kazakhstani Tenge',
                       'KRW': 'South Korean Won',
                       'LYD': 'Libyan Dinar',
                       'MYR': 'Malaysian Ringgit',
                       'MUR': 'Mauritian Rupee',
                       'MXN': 'Mexican Peso',
                       'NPR': 'Nepalese Rupee',
                       'NZD': 'New Zealand Dollar',
                       'NOK': 'Norwegian Krone',
                       'OMR': 'Omani Rial',
                       'PKR': 'Pakistani Rupee',
                       'PHP': 'Philippine Peso',
                       'PLN': 'Polish Zloty',
                       'QAR': 'Qatari Riyal',
                       'RON': 'Romanian New Leu',
                       'RUB': 'Russian Ruble',
                       'SAR': 'Saudi Arabian Riyal',
                       'SGD': 'Singapore Dollar',
                       'ZAR': 'South American Rend',
                       'LKR': 'Sri Lankan Rupee',
                       'SEK': 'Swedish Krona',
                       'CHF': 'Swiss Franc',
                       'TWD': 'Taiwan New Dollar',
                       'THB': 'Thai Baht',
                       'TTD': 'Trinidadian Dollar',
                       'TRY': 'Turkish Lyra',
                       'AED': 'Emirati Dirham',
                       'GBP': 'British Pound',
                       'VEF': 'Venezuelan Boliva',
                       'EUR': 'Euro',
                       'USD': 'United States Dollar',
                       'DKK': 'Danish Krone',
                       'CZK': 'Czech Koruna',
                       'IDR': 'Indonesian Rupiah',
                       'HKD': 'Hong Kong Dollar'
                       }

    return currency_origin.get(currency)
    #Returns None if nothing is found.

def display_currency(to_do):

    #to_do - string - only ever 'print' or 'valid_currency'
    #print will display all the countries that the user can select from
    #valid_currency is used when selecting 'all' as which currencies you
    #  would like to convert to/

    valid_currency = ('AED', 'ARS', 'AUD', 'BHD', 'BND',
                      'BRL', 'BWP', 'CAD', 'CHF', 'CLP',
                      'CNY', 'COP', 'CZK', 'DKK', 'EUR',
                      'GBP', 'HKD', 'HRK', 'HUF', 'IDR',
                      'ILS', 'INR', 'IRR', 'ISK', 'JPY',
                      'KRW', 'KZT', 'LKR', 'LYD', 'MUR',
                      'MXN', 'MYR', 'NOK', 'NPR', 'NZD',
                      'OMR', 'PHP', 'PKR', 'PLN', 'QAR',
                      'RON', 'RUB', 'SAR', 'SEK', 'SGD',
                      'THB', 'TRY', 'TTD', 'TWD', 'USD',
                      'VEF', 'ZAR')


    if to_do == 'print':
        
        print('\nHere are the valid currencies:\n')

        for country in valid_currency:

            print('{} - {}'.format(country, currencies(country)))

    else:

        return valid_currency
                       
def get_exchange(to_convert, amount, conversions):

    #to_convert - string - currency the user wants to convert
    #amount - int - amount to convert
    #conversions - set or tuple - contains each country to convert the user's currency to.

    location = r'http://www.x-rates.com/table/?from={}&amount={}'.format(to_convert, amount)
    #sets up the location of webpage to scrape

    print('\nConverting {} {}:'.format(amount, to_convert))

    res = requests.get(location)
    #downloads html for scraping

    res.raise_for_status()
    #Checks to make sure download was successful

    to_parse = res.text
    #Saves the html to this variable to be parsed below

    soup = bs4.BeautifulSoup(to_parse, 'html.parser')
    #Sets up the html to be parsed

    findings = soup.find_all('td', class_ ='rtRates')
    #Finds all elements named td that contain a class named 'rtRates',
    #which is where the currency exchange info is saved.

    for line in findings[20:]:

        #Skips first 20 because they're part of the top 10 list.
        #Prevents duplicate info from being displayed

        currency_from = str(line)[42:45]
        #the country of origin of the currency is sliced out of the html.
                       
        currency_to = str(line)[53:56]
        #same for what the currency is being converted to

        exchange = line.getText()
        #Only contains the amount of the conversion

        if currency_from == to_convert and currency_to in conversions:

            #only displays currencies specified by the user.

            print('To: {} - {} ---> {}'.format(currency_to, currencies(currency_to), exchange))
       
if __name__ == '__main__':
    
    ask_user()
