#!/bin/usr/python3

'''
randomlinks.py - scrapes a random link off of a list of websites.

Prompt from:
https://www.reddit.com/r/PythonProjects2/comments/81ejxo/march_madness_testing_your_connections/

'''

import requests, bs4, random

def get_the_links(site):

    # site - assumed to be a str passed into it from print_a_link

    headers = {

    'user-agent': 'python-requests/4.8.2 (Compatible; PCoyle;)'

    }

    try:

        r = requests.get(site, headers=headers)

    except requests.exceptions.ConnectionError:

        #Error if the script couldn't connect to the website.

        print('Could not connect website')

        return 'No link to return'

    try:

        r.raise_for_status()

    except requests.exceptions.HTTPError:

        #Handles error codes that aren't successful. 200 means everything is good

        print('Problem connecting to {}! Status Code: {}'.format(
              site, r.status_code))

        return 'No link to return'


    else:

        all_links = []

        site_text = r.text

        soup = bs4.BeautifulSoup(site_text, 'html.parser')

        all_tagged_a = soup.find_all('a')

        #If there is an a in the html, it means there is a link

        for link in all_tagged_a:

            found = link.get('href')

            #finds the url of the link, not just the html tags.

            try:

                if found.startswith('http'):

                    all_links.append(found)

            except AttributeError:

                #Sometimes objects of the None type are found, not str
                #This is to catch those since .startswith can't be run on them

                pass

        return all_links

def print_a_link(websites):

    # websites - assumed to be a list of websites stored as strings.
    #            'https://www.google.com'

    for site in websites:

        links = get_the_links(site)

        if links != 'No link to return':

            random_link = random.choice(links)

            print('Link from {}:'.format(site))
            print(random_link)

        else:

            print('Could not get a link from {}.'.format(site))


if __name__ == '__main__':

    to_search = ['https://www.washingtonpost.com',
                 'https://www.reddit.com',
                 'http://www.psu.edu']

    print_a_link(to_search)

