#!/usr/bin/python3

'''
testtable.py - A test of the table GUI available in PyQt5.
               This is set up as a way to enter players into a tournament.
               I plan to use this and other code I've written to make
               my own tournamnet software.

'''

import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QGridLayout,
                             QApplication, QLineEdit, QPushButton,
                             QTableWidgetItem, QHeaderView, QAbstractItemView,
                             QLabel,)

from PyQt5.QtCore import Qt

class Window(QWidget):

    currentIDNum = 0

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        self.firstNameLabel = QLabel('First Name:', self)
        self.lastNameLabel = QLabel('Last Name:', self)

        self.playerFirstName = QLineEdit()
        self.playerFirstName.returnPressed.connect(self.addText)
        # When return is pressed while this QLineEdit is selected it will run the addText function
        
        self.playerLastName = QLineEdit()
        self.playerLastName.returnPressed.connect(self.addText)
        # When return is pressed while this QLineEdit is selected it will run the addText function

        self.tableWidget = QTableWidget()
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Prevents the user from editing the cells directly
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # When the user clicks a cell, it will select the whole row
        self.tableWidget.verticalHeader().hide()
        # Hides the row headers
        
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem('ID'))
        # Makes column 1's header ID
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem('Player'))
        # Makes coumn 2's header Player
        self.tableWidget.setColumnWidth(1, 175)
        # Sets the 2nd column's length
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode(2))
        # Resize mode 2 is fixed, meaning the user can't change the size of the headers

        self.addPlayerButton = QPushButton('Add Player', self)
        # Creates the Add Player button
        self.addPlayerButton.clicked.connect(self.addText)
        # Connects it to the addText function
        self.addPlayerButton.setAutoDefault(True)
        # Runs the Add Text function if enter is pressed while the button is selected.

        grid = QGridLayout()
        # Creates a grid layout
        grid.setVerticalSpacing(5)
        
        grid.addWidget(self.firstNameLabel, 0, 0)
        grid.addWidget(self.playerFirstName, 0, 1)
        grid.addWidget(self.lastNameLabel, 1, 0)
        grid.addWidget(self.playerLastName, 1, 1)
        grid.addWidget(self.addPlayerButton, 2, 0)
        grid.addWidget(self.tableWidget, 3, 0, 4, 2)
        # Each of these adds the objects to the grid layout. The first 2 numbers determine the position,
        # the next two are which cells it extends to.

        self.setLayout(grid)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Testing Tables')

        self.show()


    def addText(self):

        if self.playerFirstName.text() != '' or self.playerLastName.text() != '':
            # Check to make sure there are no blanks.

            self.currentIDNum += 1

            self.tableWidget.insertRow(self.tableWidget.rowCount())

            self.tableWidget.setItem(self.tableWidget.rowCount()-1, 0, QTableWidgetItem(str(self.currentIDNum)))
            # Sets the first cell to the player's ID Number. For now it just increments.
            self.tableWidget.setItem(self.tableWidget.rowCount()-1, 1, QTableWidgetItem('{}, {}'.format(self.playerLastName.text(),
                                                                                                        self.playerFirstName.text())))
            # Sets the player's name. Last name is dispalyed first
            
            self.playerFirstName.setText('')
            self.playerLastName.setText('')
            # Clears the text boxes after something is entered.
            
            self.tableWidget.setSortingEnabled(True)
            self.tableWidget.horizontalHeader().setSortIndicator(1, Qt.AscendingOrder)
            self.tableWidget.setSortingEnabled(False)
            # This quickly enables sorting, sorts by the second column, which is the player's last name,
            # then disables sorting. The order they are entered isn't important, it should just be easy to find
            # a player by their last name.

            self.playerFirstName.setFocus(True)
            # Returns the focus to the playerFirstName text box
            # Makes entering in names much faster!

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
