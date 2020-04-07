

from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)


class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.originalPalette = QApplication.palette()

        #styleComboBox = QComboBox()
        #styleComboBox.addItems(QStyleFactory.keys())

        #styleLabel = QLabel("&Style:")
        #styleLabel.setBuddy(styleComboBox)


        #disableWidgetsCheckBox = QCheckBox("&Disable widgets") #asigna para deshabilitar los widgets

        self.createTopLeftGroupBox() #grupo1 
        self.createTopRightGroupBox() #grupo2

        satComboBox = QComboBox()
     
        satLabel = QLabel("&Satelite:")
        satLabel.setBuddy(satComboBox)

      #  styleComboBox.activated[str].connect(self.changeStyle)        # widget de barra
        
        #deshabilita los widgets
        #disableWidgetsCheckBox.toggled.connect(self.topLeftGroupBox.setDisabled)
        #disableWidgetsCheckBox.toggled.connect(self.topRightGroupBox.setDisabled)
      

        topLayout = QHBoxLayout()
        #topLayout.addWidget(styleLabel)
        topLayout.addWidget(satLabel)
        topLayout.addWidget(satComboBox)
        #topLayout.addWidget(styleComboBox)   # widget de barra
        topLayout.addStretch(1)
        #topLayout.addWidget(self.useStylePaletteCheckBox)     # widget de barra
        #topLayout.addWidget(disableWidgetsCheckBox)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2) 
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        mainLayout.addWidget(self.topRightGroupBox, 1, 1) 
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 2)
        mainLayout.setColumnStretch(1, 2)
        self.setLayout(mainLayout)

        self.setWindowTitle("GUI") # nombre de la ventana
        self.changeStyle('Fusion') # estilo de la interfaz

    def changeStyle(self, styleName):#cambia de estilo con la barra de opciones
       QApplication.setStyle(QStyleFactory.create(styleName))



    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("Group 1")

        radioButton1 = QRadioButton("Radio button 1")
        radioButton2 = QRadioButton("Radio button 2")
        radioButton3 = QRadioButton("Radio button 3")
        radioButton1.setChecked(True)

        checkBox = QCheckBox("Tri-state check box")
        checkBox.setTristate(True)
        checkBox.setCheckState(Qt.PartiallyChecked)

        layout = QVBoxLayout()
        layout.addWidget(radioButton1)
        layout.addWidget(radioButton2)
        layout.addWidget(radioButton3)
        layout.addWidget(checkBox)
        layout.addStretch(1)
        self.topLeftGroupBox.setLayout(layout)    

    def createTopRightGroupBox(self):
        self.topRightGroupBox = QGroupBox("Group 2")

        spinBox1 = QSpinBox(self.topRightGroupBox)
        spinBox1.setValue(50)
        spinBox2 = QSpinBox(self.topRightGroupBox)
        spinBox2.setValue(60)
        disableButton1 = QRadioButton("&Manual") #asigna para deshabilitar los widget
        disableButton2 = QRadioButton("&Automático") #asigna para deshabilitar los widget
        disableButton1.setChecked(True)
        #if disableButton2.isChecked == True:
        disableButton2.toggled.connect(spinBox1.setDisabled)
        disableButton2.toggled.connect(spinBox2.setDisabled)

        togglePushButton = QPushButton("Toggle Push Button")
        togglePushButton.setCheckable(True)
        togglePushButton.setChecked(True)

        flatPushButton = QPushButton("Flat Push Button")
        flatPushButton.setFlat(True)

        layout = QGridLayout()
        #layout.addWidget(defaultPushButton)
        layout.addWidget(spinBox1,0,0,1,1)
        layout.addWidget(spinBox2,0,1,1,1)
        layout.addWidget(disableButton1,0,2,1,1)
        layout.addWidget(disableButton2,1,2,1,1)
        layout.addWidget(togglePushButton,2,0)
        layout.addWidget(flatPushButton,3,0)
        layout.setRowStretch(3,1)
        layout.setColumnStretch(0,2)
        self.topRightGroupBox.setLayout(layout)

        
  


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec_()) 
