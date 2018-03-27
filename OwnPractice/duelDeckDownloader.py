#!/usr/bin/python3

import bs4, requests

duel_decks = ('jace-vs-chandra', 'garruk-vs-liliana', 'elspeth-vs-tezzeret',
              'ajani-vs-nicol-bolas', 'venser-vs-koth', 'sorin-vs-tibalt',
              'jace-vs-vraska', 'elspeth-vs-kiora', 'nissa-vs-ob-nixilis',
              'elves-vs-goblins', 'divine-vs-demonic', 'phyrexia-vs-coalition',
              'knights-vs-dragons', 'izzet-vs-golgari', 'heroes-vs-monsters',
              'speed-vs-cunning', 'blessed-vs-cursed',
              'merfolk-vs-goblins')

for decks in duel_decks:

    deck_names = decks.split('-')
    deck1 = deck_names[0].upper()
    deck2 = deck_names[-1].upper()
    
    res = requests.get('https://magic.wizards.com/en/content/duel-decks-{}'.format(decks))
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    deck_quantities = soup.select('.card-count')
    deck_card = soup.select('.card-name')

    decklists = []
    decklist_1_last_card = ''

    print(deck1)
    
    for i in range(len(deck_quantities)):
        
        decklist_line = '{} {}'.format(deck_quantities[i].getText(), deck_card[i].getText())
        
        if decklist_line not in decklists:
            
            decklists.append(decklist_line)
            
        elif decklist_1_last_card == '':
            
            decklist_1_last_card = '{} {}'.format(deck_quantities[i-1].getText(), deck_card[i-1].getText())

    for line in decklists:
        
        print(line)

        if line == decklist_1_last_card:
            
            print()
            print(deck2)

    del decklists[:]
    decklist_1_last_card = ''
    print()
