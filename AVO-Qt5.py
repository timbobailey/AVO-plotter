# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QSlider, \
                            QVBoxLayout, QHBoxLayout, QGridLayout, \
                            QLineEdit, \
                            QApplication
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon

class mainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):


        grid = QGridLayout()
        grid.setSpacing(10)

        vpUpperLabel = QLabel("Vp Upper")
        vsUpperLabel = QLabel("Vs Upper")
        rhoUpperLabel = QLabel("Rho Upper")

        vpLowerLabel = QLabel("Vp Lower")
        vsLowerLabel = QLabel("Vs Lower")
        rhoLowerLabel = QLabel("Rho Lower")

        """
        Sliders
        """
        vpUpperSlider = QSlider(Qt.Horizontal)
        vpUpperSlider.setMinimum(0)
        vpUpperSlider.setMaximum(8000)
        vpUpperSlider.setValue(4000)
        vpUpperSlider.setTickPosition(QSlider.TicksBelow)
        vpUpperSlider.setTickInterval(10)

        vsUpperSlider = QSlider(Qt.Horizontal)
        vsUpperSlider.setMinimum(10)
        vsUpperSlider.setMaximum(30)
        vsUpperSlider.setValue(20)
        vsUpperSlider.setTickPosition(QSlider.TicksBelow)
        vsUpperSlider.setTickInterval(5)

        rhoUpperSlider = QSlider(Qt.Horizontal)
        rhoUpperSlider.setMinimum(10)
        rhoUpperSlider.setMaximum(30)
        rhoUpperSlider.setValue(20)
        rhoUpperSlider.setTickPosition(QSlider.TicksBelow)
        rhoUpperSlider.setTickInterval(5)


        """
        Text boxes
        """
        vpValue = QLineEdit(self)

        grid.addWidget(vpUpperLabel, 0, 1)
        grid.addWidget(vpUpperSlider, 0, 2)
        grid.addWidget(vpValue, 0, 3)

        grid.addWidget(vsUpperLabel, 1, 1)
        grid.addWidget(vsUpperSlider, 1, 2)

        grid.addWidget(rhoUpperLabel, 2, 1)
        grid.addWidget(rhoUpperSlider, 2, 2)


        vpUpperSlider.valueChanged.connect(self.on_vpSliderChange)
        self.setLayout(grid)


        """
        Size and display
        """
        self.resize(600, 600)
        self.setGeometry(500, 300, 250, 150)
        self.setWindowTitle('AVO plotter')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def on_vpSliderChange(self):
        print('event')

        #print('value: ', self.vpUpperSlider.value())
        #self.vpValue.setValue(self.vpUpperSlider.value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainWindow()
    sys.exit(app.exec_())