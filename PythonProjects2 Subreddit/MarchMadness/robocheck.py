#!/usr/bin/python3

'''
robocheck.py - checks a list of websites'robots.txt files and
tells the user if they are allowed to scrape from their page.
Currently only checks for 'user-agent: *' and 'Disallow /'

prompt from: https://www.reddit.com/r/PythonProjects2/comments/81ejxo/march_madness_testing_your_connections/?st=jf2y1u2e&sh=0af618a2
This is for the bonus questions.
'''

import requests, pprint, http.client

http.client.MAXHEADERS = 1000

# If a site tries to return too many headers, the script will crash.
# Adding this line prevents that crash.

# requests uses http.client for receiving headers

def scrape_check(to_check):

    header = {

    'user-agent': 'python-requests/4.8.2 (Compatible; PCoyle;)'

    }

    try:

        r = requests.get(to_check + '/robots.txt', header)
        # adds robots.txt to the URL being checked.

    except requests.exceptions.ConnectionError:

        return 'Does not exist'

    try:

        r.raise_for_status()
        # Raises an exception if the .get request to robots.txt is not successful

    except requests.exceptions.HTTPError:

        return False

    else:
        
        robo_text = r.text.split('\n')
        # robots.txt files are separated by 
        for line in robo_text:

            if 'User-agent: *' in line or 'User-Agent: *' in line or 'user-agent: *' in line:

                user_agent_line = robo_text.index(line)

                for i in robo_text[user_agent_line:]:


                    if 'Disallow: /' in i and i[-1] == '/' and i[-2] == ' ':
                        
                        # if the site Disallowed all webscraping, False is returned
                        
                        # conditions are to make sure the string says exactly 'Disallow: /'
                        # this means it will skip lines that say something like
                        # 'Disallow: /calendar/feeds/

                        return False

                    elif i == ' ':

                        return True

                        # If a break is found, that means the script is no longer looking
                        # at 'User-agent: *', which means no Disallow was found, so webscraping
                        # is indeed allowed.

                return True

            #If True is returned, it means the site is able to be scraped.

def build_scrape_dict(scrape_list):

    scrape_status = {}

    for site in scrape_list:

        can_scrape = scrape_check(site)

        scrape_status[site] = can_scrape

    return scrape_status

if __name__ == '__main__':

    possible_scraping = [
        
        'https://www.google.com',
        'https://heyidontexist.com',
        'https://www.washingtonpost.com',
        'https://www.reddit.com',

    ]

    #Add websites you wish to check to this list.

    can_scrape = build_scrape_dict(possible_scraping)

    pprint.pprint(can_scrape)
