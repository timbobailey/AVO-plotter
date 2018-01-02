# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QSlider, \
                            QVBoxLayout, QHBoxLayout, QGridLayout, \
                            QLineEdit, QApplication
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon

class mainWindow(QWidget):

    VP_MIN = 100
    VP_MAX = 10000
    VP_STEP = 50

    VS_MIN = 100
    VS_MAX = 10000
    VS_STEP = 50

    RHO_MIN = 1.0
    RHO_MAX = 3.5
    RHO_STEP = 0.1

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        self.initVpComponents()
        self.initVsComponents()
        self.initRhoComponents()

        grid.addWidget(self.vpUpperLabel, 0, 1)
        grid.addWidget(self.vpUpperSlider, 0, 2)
        grid.addWidget(self.vpUpperValue, 0, 3)

        grid.addWidget(self.vsUpperLabel, 1, 1)
        grid.addWidget(self.vsUpperSlider, 1, 2)
        grid.addWidget(self.vsUpperValue, 1, 3)

        grid.addWidget(self.rhoUpperLabel, 2, 1)
        grid.addWidget(self.rhoUpperSlider, 2, 2)
        grid.addWidget(self.rhoUpperValue, 2, 3)

        grid.addWidget(self.vpLowerLabel, 3, 1)
        grid.addWidget(self.vpLowerSlider, 3, 2)
        grid.addWidget(self.vpLowerValue, 3, 3)

        grid.addWidget(self.vsLowerLabel, 4, 1)
        grid.addWidget(self.vsLowerSlider, 4, 2)
        grid.addWidget(self.vsLowerValue, 4, 3)

        grid.addWidget(self.rhoLowerLabel, 5, 1)
        grid.addWidget(self.rhoLowerSlider, 5, 2)
        grid.addWidget(self.rhoLowerValue, 5, 3)

        self.vpUpperSlider.valueChanged.connect(self.on_vpUpperSliderChange)
        self.vsUpperSlider.valueChanged.connect(self.on_vsUpperSliderChange)
        self.rhoUpperSlider.valueChanged.connect(self.on_rhoUpperSliderChange)

        self.setLayout(grid)

        """
        Size and display
        """
        self.resize(600, 600)
        self.setGeometry(500, 300, 600, 300)
        self.setWindowTitle('AVO plotter')
        self.setWindowIcon(QIcon('web.png'))
        self.show()


    def initVpComponents(self):
        self.vpUpperLabel = QLabel("Vp Upper")
        self.vpLowerLabel = QLabel("Vp Lower")
        """
        Sliders
        """
        self.vpUpperSlider = QSlider(Qt.Horizontal)
        self.vpUpperSlider.setMinimum(self.VP_MIN)
        self.vpUpperSlider.setMaximum(self.VP_MAX)
        self.vpUpperSlider.setValue(3500)
        self.vpUpperSlider.setTickPosition(QSlider.TicksBelow)
        self.vpUpperSlider.setTickInterval(50)

        self.vpLowerSlider = QSlider(Qt.Horizontal)
        self.vpLowerSlider.setMinimum(self.VP_MIN)
        self.vpLowerSlider.setMaximum(self.VP_MAX)
        self.vpLowerSlider.setValue(3500)
        self.vpLowerSlider.setTickPosition(QSlider.TicksBelow)
        self.vpLowerSlider.setTickInterval(50)
        """
        Text boxes
        """
        self.vpUpperValue = QLineEdit(self)
        self.vpLowerValue = QLineEdit(self)

    def initVsComponents(self):
        self.vsUpperLabel = QLabel("Vs Upper")
        self.vsLowerLabel = QLabel("Vs Lower")
        """
        Slidevs
        """
        self.vsUpperSlider = QSlider(Qt.Horizontal)
        self.vsUpperSlider.setMinimum(self.VS_MIN)
        self.vsUpperSlider.setMaximum(self.VS_MAX)
        self.vsUpperSlider.setValue(3500)
        self.vsUpperSlider.setTickPosition(QSlider.TicksBelow)
        self.vsUpperSlider.setTickInterval(50)

        self.vsLowerSlider = QSlider(Qt.Horizontal)
        self.vsLowerSlider.setMinimum(self.VS_MIN)
        self.vsLowerSlider.setMaximum(self.VS_MAX)
        self.vsLowerSlider.setValue(3500)
        self.vsLowerSlider.setTickPosition(QSlider.TicksBelow)
        self.vsLowerSlider.setTickInterval(50)
        """
        Text boxes
        """
        self.vsUpperValue = QLineEdit(self)
        self.vsLowerValue = QLineEdit(self)

    def initRhoComponents(self):
        self.rhoUpperLabel = QLabel("Rho Upper")
        self.rhoLowerLabel = QLabel("Rho Lower")
        """
        Sliders
        """
        self.rhoUpperSlider = QSlider(Qt.Horizontal)
        self.rhoUpperSlider.setMinimum(self.RHO_MIN)
        self.rhoUpperSlider.setMaximum(self.RHO_MAX)
        self.rhoUpperSlider.setValue(3500)
        self.rhoUpperSlider.setTickPosition(QSlider.TicksBelow)
        self.rhoUpperSlider.setTickInterval(50)

        self.rhoLowerSlider = QSlider(Qt.Horizontal)
        self.rhoLowerSlider.setMinimum(self.RHO_MIN)
        self.rhoLowerSlider.setMaximum(self.RHO_MAX)
        self.rhoLowerSlider.setValue(3500)
        self.rhoLowerSlider.setTickPosition(QSlider.TicksBelow)
        self.rhoLowerSlider.setTickInterval(50)
        """
        Text boxes
        """
        self.rhoUpperValue = QLineEdit(self)
        self.rhoLowerValue = QLineEdit(self)


    def on_vpUpperSliderChange(self):
        value = str( self.vpUpperSlider.value() )
        self.vpUpperValue.setText(value)

    def on_vsUpperSliderChange(self):
        value = str( self.vsUpperSlider.value() )
        self.vsUpperValue.setText(value)

    def on_rhoUpperSliderChange(self):
        value = str( self.rhoUpperSlider.value() )
        self.rhoUpperValue.setText(value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainWindow()
    sys.exit(app.exec_())