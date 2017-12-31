# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QSlider, \
                            QVBoxLayout, QHBoxLayout, QGridLayout, \
                            QLineEdit, QApplication
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon

class mainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        self.vpUpperLabel = QLabel("Vp Upper")
        self.vsUpperLabel = QLabel("Vs Upper")
        self.rhoUpperLabel = QLabel("Rho Upper")

        self.vpLowerLabel = QLabel("Vp Lower")
        self.vsLowerLabel = QLabel("Vs Lower")
        self.rhoLowerLabel = QLabel("Rho Lower")

        """
        Sliders
        """
        self.vpUpperSlider = QSlider(Qt.Horizontal)
        self.vpUpperSlider.setMinimum(0)
        self.vpUpperSlider.setMaximum(8000)
        self.vpUpperSlider.setValue(4000)
        self.vpUpperSlider.setTickPosition(QSlider.TicksBelow)
        self.vpUpperSlider.setTickInterval(10)

        self.vsUpperSlider = QSlider(Qt.Horizontal)
        self.vsUpperSlider.setMinimum(10)
        self.vsUpperSlider.setMaximum(30)
        self.vsUpperSlider.setValue(20)
        self.vsUpperSlider.setTickPosition(QSlider.TicksBelow)
        self.vsUpperSlider.setTickInterval(5)

        self.rhoUpperSlider = QSlider(Qt.Horizontal)
        self.rhoUpperSlider.setMinimum(10)
        self.rhoUpperSlider.setMaximum(30)
        self.rhoUpperSlider.setValue(20)
        self.rhoUpperSlider.setTickPosition(QSlider.TicksBelow)
        self.rhoUpperSlider.setTickInterval(5)

        """
        Text boxes
        """
        self.vpValue = QLineEdit(self)

        grid.addWidget(self.vpUpperLabel, 0, 1)
        grid.addWidget(self.vpUpperSlider, 0, 2)
        grid.addWidget(self.vpValue, 0, 3)

        grid.addWidget(self.vsUpperLabel, 1, 1)
        grid.addWidget(self.vsUpperSlider, 1, 2)

        grid.addWidget(self.rhoUpperLabel, 2, 1)
        grid.addWidget(self.rhoUpperSlider, 2, 2)

        self.vpUpperSlider.valueChanged.connect(self.on_vpUpperSliderChange)
        self.setLayout(grid)

        """
        Size and display
        """
        self.resize(600, 600)
        self.setGeometry(500, 300, 600, 300)
        self.setWindowTitle('AVO plotter')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def on_vpUpperSliderChange(self):
        value = str( self.vpUpperSlider.value() )
        self.vpValue.setText(value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainWindow()
    sys.exit(app.exec_())