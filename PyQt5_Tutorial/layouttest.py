#!/bin/usr/python3

'''
layouttest.py - Testing a layout in PyQt5. This widget has 5 buttons labeled
            Up, Down, Left, and Right, with an Exit button in the center.
'''

import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication

class Window(QWidget):

    def __init__(self):

        super().__init__()
        # Makes the window a child of the QWidget class

        self.initUI()
        # Loads the UI

    def initUI(self):

        grid = QGridLayout()
        # Creates an instance of the QGridLayout() class
        
        self.setLayout(grid)
        # Sets the layout to the grid layout.

        up_button = QPushButton('Up', self)
        grid.addWidget(up_button, 0, 1)
        # Creates a button that says 'Up' at position 0,1
        # AKA top center of the widget.

        left_button = QPushButton('Left', self)
        grid.addWidget(left_button, 1, 0)
        # Location: Center left

        close_button = QPushButton('Exit', self)
        close_button.clicked.connect(self.close)
        # When exit button is clicked, the window will close.
        grid.addWidget(close_button, 1, 1)
        # Location: Center

        right_button = QPushButton('Right', self)
        grid.addWidget(right_button, 1, 2)
        # Location: Center Right

        down_button = QPushButton('Down', self)
        grid.addWidget(down_button, 2, 1)
        # Location: Bottom center

        #Looks like:

        #        'Up'
        # 'Left' 'Exit' 'Right'
        #        'Down'


        self.move(300, 300)
        # Moves the window to positon 300, 300 when it is launched
        self.setWindowTitle('Layout Test')
        
        self.show()
        #Displays the window.

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
