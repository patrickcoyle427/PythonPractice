#!/usr/bin/python3

'''
enroll_player.py - Lets the user add players to an enrollment list using
                   their first and last name, plus an ID number. When
                   the user is done, their enrolled players are exported
                   to an XML file.

'''

import xml.etree.ElementTree as ET
import sys


def enroll_players():
    
    current_enrolled = []
    # Holds the players that are being enrolled

    all_enrolled = ET.Element('Participants')
    # Creates a the root of the xml document

    temp_id_num = 0
    # Used for setting up temporary IDs

    # Note: tempIDs are usually used to get a tournament up and running without
    # having to worry about giving each player ID numbers.

    while True:

        print('Enroll players? Press q to quit, enter to continue.')
        continue_enrollment = input('> ')
        # Lets the user decide when to stop entering in players.

        if continue_enrollment.lower() == 'q':

            if len(current_enrolled) == 0:
                # Doesn't bother to try to write to file if there is nothing there

                sys.exit(0)

            else:

                for id_num, first_name, last_name in current_enrolled:
                    # these entries are created below if the user decided
                    # they want to enroll a player.

                    current_player = ET.SubElement(all_enrolled, 'Player',
                                                   {'id': id_num})

                    # Creates a new entry for a player

                    add_first_name = ET.SubElement(current_player, 'FirstName')
                    add_first_name.text = first_name
                    # Sets their first name

                    add_last_name = ET.SubElement(current_player, 'LastName')
                    add_last_name.text = last_name
                    # Sets their last name

                    status = ET.SubElement(current_player, 'Status')
                    status.text = 'Enrolled'
                    
                    
                to_write = ET.ElementTree(all_enrolled)
                to_write.write('enrolled.xml', encoding='utf-8',
                               xml_declaration=True)
                # Everything is written to the XML file all at once, this way,
                # when I add the ability to remove players before the tournament
                # starts, the XML document wont have to be constantly accessed
                # and updated every time you add/remove a player.

                print('File written! Have a nice day!')
                sys.exit(0)

        else:

            first_name = input('Please enter your first name: ')
            last_name = input('Please enter your last name: ')
            id_num = input('Enter an ID number: ')
            # ID number can be left blank to use a temp ID.
            # Something that says this should be added.

            if id_num == '':
              
                temp_id_num += 1
                temp_template = 'TEMP{}'.format(str(temp_id_num).zfill(4))
                # Creates a temporary ID
              
                id_num = temp_template
      
            current_enrolled.append((id_num, first_name, last_name))
            # Creates tuples that will be iterated over when the XML doc is
            # being written.
            
if __name__ == '__main__':

    enroll_players()
