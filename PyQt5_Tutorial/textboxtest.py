#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QTextEdit,
                             QGridLayout, QApplication, QLineEdit,
                             QPushButton)

class Window(QWidget):

    def __init__(self):

        super().__init__()
        # Initializes the Window class as a child of the QWidget class and runs
        # the __init__ from QWidget

        self.initUI()
        # Displays the UI

    def initUI(self):

        self.textBox = QTextEdit()       
        self.textBox.setReadOnly(True)
        # Creates a text box and sets it to Read Only. This is read only
        # because I want the user to use the button below to add text to this
        
        self.textLine = QLineEdit()
        self.textLine.returnPressed.connect(self.addText)
        # Creates a single-line text box. If enter is pressed it will work
        # the same as clicking the 'Add Text' button below.
        
        self.add_text = QPushButton('Add Text', self)
        self.add_text.clicked.connect(self.addText)
        self.add_text.setAutoDefault(True)
        # Creates a button that will add the text from textLine to textBox
        # setAutoDefault makes the button run self.addText if the user presses
        # enter while it is highlighted

        grid = QGridLayout()
        grid.setVerticalSpacing(5)
        # Creates the grid layout 

        grid.addWidget(self.textBox, 0, 0)
        grid.addWidget(self.textLine, 1, 0)
        grid.addWidget(self.add_text, 1, 1)
        # Adds the text boxes and the button to the grid

        self.setLayout(grid)
        # sets the layout to the grid layout

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Testing text boxes')

        self.show()

    def addText(self):

        if self.textLine.text() != '':

            self.textBox.append(self.textLine.text())
            self.textLine.setText('')
            # When Add Text is clicked, if it isn't blank, the text is added
            # to textBox and a new line is automatically added.
        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
