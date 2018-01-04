# -*- coding: utf-8 -*-

import sys
import pyqtgraph
import numpy as np
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QSlider, \
                            QVBoxLayout, QHBoxLayout, QSizePolicy, \
                            QLineEdit, QApplication
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon
from bruges.reflection import reflection as avomodel

class mainWindow(QWidget):

    VP_MIN = 100
    VP_MAX = 10000
    VP_STEP = 50
    VP_UPPER_INITIAL = 12250
    VP_LOWER_INITIAL = 11600

    VS_MIN = 100
    VS_MAX = 10000
    VS_STEP = 50
    VS_UPPER_INITIAL = 6620
    VS_LOWER_INITIAL = 4050

    RHO_MIN = 1000
    RHO_MAX = 3500
    RHO_STEP = 50
    RHO_UPPER_INITIAL = 2660
    RHO_LOWER_INITIAL = 2340


    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hBox1 = QHBoxLayout()
        hBox2 = QHBoxLayout()
        hBox3 = QHBoxLayout()

        hBox4 = QHBoxLayout()
        hBox5 = QHBoxLayout()
        hBox6 = QHBoxLayout()

        vBox1 = QVBoxLayout()

        self.initVpComponents()
        self.initVsComponents()
        self.initRhoComponents()

        hBox1.addWidget(self.vpUpperLabel)
        hBox1.addWidget(self.vpUpperSlider)
        hBox1.addWidget(self.vpUpperValue)

        hBox2.addWidget(self.vsUpperLabel)
        hBox2.addWidget(self.vsUpperSlider)
        hBox2.addWidget(self.vsUpperValue)

        hBox3.addWidget(self.rhoUpperLabel)
        hBox3.addWidget(self.rhoUpperSlider)
        hBox3.addWidget(self.rhoUpperValue)

        hBox4.addWidget(self.vpLowerLabel)
        hBox4.addWidget(self.vpLowerSlider)
        hBox4.addWidget(self.vpLowerValue)

        hBox5.addWidget(self.vsLowerLabel)
        hBox5.addWidget(self.vsLowerSlider)
        hBox5.addWidget(self.vsLowerValue)

        hBox6.addWidget(self.rhoLowerLabel)
        hBox6.addWidget(self.rhoLowerSlider)
        hBox6.addWidget(self.rhoLowerValue)

        self.vpUpperSlider.valueChanged.connect(self.on_vpUpperSliderChange)
        self.vsUpperSlider.valueChanged.connect(self.on_vsUpperSliderChange)
        self.rhoUpperSlider.valueChanged.connect(self.on_rhoUpperSliderChange)

        self.vpLowerSlider.valueChanged.connect(self.on_vpLowerSliderChange)
        self.vsLowerSlider.valueChanged.connect(self.on_vsLowerSliderChange)
        self.rhoLowerSlider.valueChanged.connect(self.on_rhoLowerSliderChange)

        plotBox = QHBoxLayout()
        self.avoplot = pyqtgraph.PlotWidget()
        plotBox.addWidget(self.avoplot)

        vBox1.addLayout(hBox1)
        vBox1.addLayout(hBox2)
        vBox1.addLayout(hBox3)
        vBox1.addLayout(hBox4)
        vBox1.addLayout(hBox5)
        vBox1.addLayout(hBox6)
        vBox1.addLayout(plotBox)

        self.setLayout(vBox1)
        self.calculateAVO()

        """
        Size and display
        """
        self.setGeometry(500, 300, 600, 800)
        self.setWindowTitle('AVO plotter')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def calculateAVO(self):
        min_theta = 0
        max_theta = 60
        step_theta = 1
        theta = np.arange(min_theta, max_theta, step_theta)
        avo = avomodel.zoeppritz_rpp(self.vpUpperSlider.value(), self.vsUpperSlider.value(), self.rhoUpperSlider.value()/1000,
                                     self.vpLowerSlider.value(), self.vsLowerSlider.value(), self.rhoLowerSlider.value()/1000, theta)


        pltitem = self.avoplot.getPlotItem()
        pltitem.clear()

        self.avoplot.plot(avo, clickable=True)

        # curve.curve.setClickable(False)
        # curve.setPen('w')  ## white pen
        # curve.setShadowPen(pg.mkPen((70, 70, 30), width=6, cosmetic=True))
        # lr = pg.LinearRegionItem([1, 30], bounds=[0, 100], movable=True)
        # pw3.addItem(lr)
        # line = pg.InfiniteLine(angle=90, movable=True)
        # pw3.addItem(line)
        # line.setBounds([0, 200])

    def initVpComponents(self):
        self.vpUpperLabel = QLabel("Vp Upper")
        self.vpLowerLabel = QLabel("Vp Lower")
        """
        Sliders
        """
        self.vpUpperSlider = QSlider(Qt.Horizontal)
        self.vpUpperSlider.setMinimum(self.VP_MIN)
        self.vpUpperSlider.setMaximum(self.VP_MAX)
        self.vpUpperSlider.setValue(self.VP_UPPER_INITIAL)
        self.vpUpperSlider.setTickPosition(QSlider.TicksBelow)
        self.vpUpperSlider.setTickInterval(50)

        self.vpLowerSlider = QSlider(Qt.Horizontal)
        self.vpLowerSlider.setMinimum(self.VP_MIN)
        self.vpLowerSlider.setMaximum(self.VP_MAX)
        self.vpLowerSlider.setValue(self.VP_LOWER_INITIAL)
        self.vpLowerSlider.setTickPosition(QSlider.TicksBelow)
        self.vpLowerSlider.setTickInterval(50)
        """
        Text boxes
        """
        self.vpUpperValue = QLineEdit(self)
        self.vpLowerValue = QLineEdit(self)
        self.vpUpperValue.setText(str(self.VP_UPPER_INITIAL))


    def initVsComponents(self):
        self.vsUpperLabel = QLabel("Vs Upper")
        self.vsLowerLabel = QLabel("Vs Lower")
        """
        Slidevs
        """
        self.vsUpperSlider = QSlider(Qt.Horizontal)
        self.vsUpperSlider.setMinimum(self.VS_MIN)
        self.vsUpperSlider.setMaximum(self.VS_MAX)
        self.vsUpperSlider.setValue(self.VS_UPPER_INITIAL)
        self.vsUpperSlider.setTickPosition(QSlider.TicksBelow)
        self.vsUpperSlider.setTickInterval(50)

        self.vsLowerSlider = QSlider(Qt.Horizontal)
        self.vsLowerSlider.setMinimum(self.VS_MIN)
        self.vsLowerSlider.setMaximum(self.VS_MAX)
        self.vsLowerSlider.setValue(self.VS_LOWER_INITIAL)
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
        self.rhoUpperSlider.setValue(self.RHO_UPPER_INITIAL)
        self.rhoUpperSlider.setTickPosition(QSlider.TicksBelow)
        self.rhoUpperSlider.setTickInterval(self.RHO_STEP)

        self.rhoLowerSlider = QSlider(Qt.Horizontal)
        self.rhoLowerSlider.setMinimum(self.RHO_MIN)
        self.rhoLowerSlider.setMaximum(self.RHO_MAX)
        self.rhoLowerSlider.setValue(self.RHO_LOWER_INITIAL)
        self.rhoLowerSlider.setTickPosition(QSlider.TicksBelow)
        self.rhoLowerSlider.setTickInterval(self.RHO_STEP)
        """
        Text boxes
        """
        self.rhoUpperValue = QLineEdit(self)
        self.rhoLowerValue = QLineEdit(self)


    def on_vpUpperSliderChange(self):
        value = str( self.vpUpperSlider.value() )
        self.vpUpperValue.setText(value)
        self.calculateAVO()

    def on_vsUpperSliderChange(self):
        value = str( self.vsUpperSlider.value() )
        self.vsUpperValue.setText(value)
        self.calculateAVO()

    def on_rhoUpperSliderChange(self):
        value = str( self.rhoUpperSlider.value() / 1000 )
        self.rhoUpperValue.setText(value)
        self.calculateAVO()

    def on_vpLowerSliderChange(self):
        value = str( self.vpLowerSlider.value() )
        self.vpLowerValue.setText(value)
        self.calculateAVO()

    def on_vsLowerSliderChange(self):
        value = str( self.vsLowerSlider.value() )
        self.vsLowerValue.setText(value)
        self.calculateAVO()

    def on_rhoLowerSliderChange(self):
        value = str( self.rhoLowerSlider.value() / 1000 )
        self.rhoLowerValue.setText(value)
        self.calculateAVO()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainWindow()
    sys.exit(app.exec_())