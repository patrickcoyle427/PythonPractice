#!/usr/bin/python3

'''

testXMLloadAndWrite.py - practicing with loading and writing to an xml file.

'''

import xml.etree.ElementTree as  ET

folder = 'Tournaments\\'

file = 'test ID6354692.xml'

infile = folder + file

tree = ET.parse(infile)

tournament = tree.getroot()

players = tournament[1]

to_enroll = [('IDNUM1', 'Patrick', 'Coyle'), ('IDNUM2', 'Mitty', 'Coyle')]

for child in tournament:

    print(child)

players = tournament[1]

for idnum, first, last in to_enroll:

    player = ET.SubElement(players, 'Player')

    idNumber = ET.SubElement(player, 'IDNumber')
    idNumber.text = idnum
    
    firstName = ET.SubElement(player, 'firstName')
    firstName.text = first
    
    lastName = ET.SubElement(player, 'lastName')
    lastName.text = last

    wins = ET.SubElement(player, 'Wins')
    wins.text = '0'

    draws = ET.SubElement(player, 'Draws')
    draws.text = '0'

for child in players:

    print('{}, {} ({})'.format(child[2].text, child[1].text, child[0].text))

to_write = tree

new_file = '{}testing {}'.format(folder, file)

to_write.write(new_file,
               encoding = 'utf-8',
               xml_declaration = True)

print('Successfuly Saved File')

newTree = ET.parse(new_file)

newTournament = newTree.getroot()

newPlayers = newTournament[1]

for child in newPlayers:

    print('{}, {} ({})'.format(child[2].text, child[1].text, child[0].text))
