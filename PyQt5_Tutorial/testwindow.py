#!/usr/bin/python3

'''
testwindow.py - a window that has multiple ways to close it. This is mostly a
               testing what I've learned so far about PyQt5 GUIs

'''

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QAction

class MainWindow(QMainWindow):

    # Inherits from QMainWIndow

    def __init__(self):

        super().__init__()
        # Makes MainWindow object also a QMainWindow Object

        self.initUI()
        #Loads the GUI window

    def initUI(self):

        self.setGeometry(600, 300, 400, 400)
        # First two numbers set the x and y coordinates of the window
        # Second two set the height and width
        
        self.setWindowTitle('Close This Window')

        exiting = QAction('&Exit', self)
        # Creates a QAction object that lets us create an exit action
        exiting.setShortcut('Ctrl+Q')
        # Allows the user to exit by pressing ctrl + q
        # Won't work if there is no menu bar actions that call it.
        exiting.setStatusTip('Exit')
        #Displays 'Exit' on the status bar
        exiting.triggered.connect(self.close)
        # Closes the window when the user presses ctrl + q

        menubar = self.menuBar()
        # Creates the menu bar where File, edit, ect usually sit
        fileMenu = menubar.addMenu('&File')
        # Creates a File menu
        fileMenu.addAction(exiting)
        # Adds the exiting action to the File menu

        quitbutton = QPushButton('Quit', self)
        # Creates a button to quit
        quitbutton.clicked.connect(self.close)
        # CLoses the window when the button is clicked.
        quitbutton.resize(quitbutton.sizeHint())
        # Sets a suggested size for the button

        quitbutton.move(150, 175)
        # Moves the button based on the window's x and y coordinates.

        self.statusBar()
        # Adds a status bar to the bottom of the window.

        self.show()
        # Displays the window

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
    
