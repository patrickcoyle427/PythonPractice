#!/usr/bin/python3

# TODO:
# Hookup anything signals that might be needed
# Add section to set rounds, or let the software calculate rounds
# Make this write an XML file after everything is filled in
# Make the layout look nice!!!

import sys

import xml.etree.ElementTree as ET

from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication,
                             QCheckBox, QRadioButton, QLabel,
                             QGridLayout, QLineEdit, QHBoxLayout,
                             QGroupBox)

from PyQt5.QtCore import Qt

class CreateTournament(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        layout = QGridLayout()
        self.setLayout(layout)
        # Sets up a grid layout for the window.

        # Event Name Section

        self.event_name_label = QLabel('Event Name:', self)
        # Creates the label for event name

        self.enter_event_name = QLineEdit()
        # Creates a LineEdit object for the user to enter the event's name

        layout.addWidget(self.event_name_label, 0, 0)
        layout.addWidget(self.enter_event_name, 0, 1)

        ### Tournament Type Section ###

        self.tournamentTypeGroup = QGroupBox('Tourament Type:')
        # Creates a group of radio button. This one is for the tournament type
        
        self.tournament_type = (QRadioButton('Swiss'), QRadioButton('Single Elimination'))
        # Tuple of the different types of tournaments
        self.tournament_type[0].setChecked(True)
        # Sets 'Swiss' to be checked by default

        tournament_type_layout = QHBoxLayout()
        tournament_type_layout.addWidget(self.tournament_type[0])
        tournament_type_layout.addWidget(self.tournament_type[1])

        self.tournamentTypeGroup.setLayout(tournament_type_layout)

        layout.addWidget(self.tournamentTypeGroup, 2, 0)

        ### Games Played Section ###

        self.gamesPlayedGroup = QGroupBox('Games in Match')

        self.games_played = (QRadioButton('Best of 1'), QRadioButton('Best of 3'))

        # In a tuple together for organization purposes

        games_played_layout = QHBoxLayout()
        games_played_layout.addWidget(self.games_played[0])
        games_played_layout.addWidget(self.games_played[1])

        self.games_played[0].setChecked(True)

        self.gamesPlayedGroup.setLayout(games_played_layout)

        layout.addWidget(self.gamesPlayedGroup, 2, 1)

        ### Create Draft Pods Section ###

        self.draftPodGroup = QGroupBox('Draft Pods')

        self.create_draft_pods = QCheckBox('Create Draft Pods')
        self.create_draft_pods.stateChanged.connect(self.draft_settings)
        
        self.play_within_pods = QCheckBox('Play Within Pods')
        self.play_within_pods.setEnabled(False)

        draft_pod_layout = QHBoxLayout()
        draft_pod_layout.addWidget(self.create_draft_pods)
        draft_pod_layout.addWidget(self.play_within_pods)

        self.draftPodGroup.setLayout(draft_pod_layout)

        layout.addWidget(self.draftPodGroup, 3, 0)

        ### Create Tournament and Cancel Section ###

        self.create_event = QPushButton('Create Event', self)
        self.cancel = QPushButton('Cancel', self)

        self.create_event.clicked.connect(self.write_tournament_xml_file)
        self.cancel.clicked.connect(self.close)

        self.create_event.setStyleSheet('background-color: green; color: white')
        self.cancel.setStyleSheet('background-color: red; color: white')

        layout.addWidget(self.create_event, 4, 0)
        layout.addWidget(self.cancel, 4, 1)

        self.setWindowTitle('Create New Tournament')
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        # Sets it so the user can only close the window, not minimize or maximize

        self.show()

    def draft_settings(self):

        if self.create_draft_pods.isChecked() == True:

            self.play_within_pods.setEnabled(True)
            self.play_within_pods.toggle()

        else:
            
            self.play_within_pods.toggle()
            self.play_within_pods.setEnabled(False)

    def write_tournament_xml_file(self):

        root = ET.Element('Tournament')

        tournamentSetup = ET.SubElement(root, 'TournamentSetup')

        eventName = ET.SubElement(tournamentSetup, 'EventName')
        eventName.text = self.enter_event_name.text()

        structure = ET.SubElement(tournamentSetup, 'Structure')

        style = ET.SubElement(structure, 'Style')

        if self.tournament_type[0].isChecked() == True:

            style.text = 'Swiss'

        else:

            style.text = 'SingleElimination'

        gamesPlayedInMatch = ET.SubElement(structure, 'GamesPlayedInMatch')

        if self.games_played[0].isChecked() == True:
            
            gamesPlayedInMatch.text = '1'

        else:

            gamesPlayedInMatch.text = '3'

        # TODO: Continue building XML doc

        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    create_tournament = CreateTournament()
    sys.exit(app.exec_())
