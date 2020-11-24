from PyQt5.QtWidgets import QDialog, QWidget, QMainWindow, QApplication, QPushButton, QGroupBox, QHBoxLayout, QGridLayout, QVBoxLayout
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect
import sys

class Window(QDialog):
    def __init__(self):
        
        super().__init__()
        
        self.title = "Grid Layout"
        self.top = 500
        self.left = 200
        self.width = 300
        self.height = 250
        self.iconName = "setec.png"
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
        self.show()
        
    def createLayout(self):
        self.groupBox = QGroupBox("")
        gridLayout = QGridLayout()

        button = QPushButton("FM", self)
        button.setMinimumHeight(40)
        gridLayout.addWidget(button,0,0)

        button1 = QPushButton("AM", self)
        button1.setMinimumHeight(40)
        gridLayout.addWidget(button1,1,0)

        button2 = QPushButton("FSK", self)
        button2.setMinimumHeight(40)
        gridLayout.addWidget(button2,2,0)

        button3 = QPushButton("CW Morse", self)
        button3.setIconSize(QtCore.QSize(40,40))
        button3.setMinimumHeight(40)
        gridLayout.addWidget(button3,3,0)
        gridLayout.setColumnStretch(0,0)
        
        self.groupBox.setLayout(gridLayout)
    

if __name__=="__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
