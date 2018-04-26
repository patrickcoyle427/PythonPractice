#!/usr/bin/python3

# TODO:
# When create draft pods isn't selected, Play Within Pods should be grayed out
# Hookup anything signals that might be needed
# Add section to set rounds, or let the software calculate rounds
# Add 'Create Event' and 'Cancel' buttons
# Make them green and red?
# Make this write an XML file after everything is filled in
# Make the layout look nice!!!

import sys

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

        # Tournament Type Section

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

        # Games Played Section

        self.gamesPlayedGroup = QGroupBox('Games in Match')

        self.games_played = (QRadioButton('Best of 1'), QRadioButton('Best of 3'))

        games_played_layout = QHBoxLayout()
        games_played_layout.addWidget(self.games_played[0])
        games_played_layout.addWidget(self.games_played[1])

        self.gamesPlayedGroup.setLayout(games_played_layout)

        layout.addWidget(self.gamesPlayedGroup, 2, 1)

        # Create Draft Pods Section

        self.draftPodGroup = QGroupBox('Draft Pods')

        self.create_draft_pods = QCheckBox('Create Draft Pods')
        self.play_within_pods = QCheckBox('Play Within Pods')

        draft_pod_layout = QHBoxLayout()
        draft_pod_layout.addWidget(self.create_draft_pods)
        draft_pod_layout.addWidget(self.play_within_pods)

        self.draftPodGroup.setLayout(draft_pod_layout)

        layout.addWidget(self.draftPodGroup, 3, 0)

        self.setWindowTitle('Create New Tournament')
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        # Sets it so the user can only close the window, not minimize or maximize

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    create_tournament = CreateTournament()
    sys.exit(app.exec_())
