# -*- coding: utf-8 -*-

import sys
import pyqtgraph
from PyQt5.QtWidgets import QWidget, QLabel, QSlider, \
                            QVBoxLayout, QHBoxLayout, \
                            QLineEdit, QApplication, QSpacerItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import avonumericals as avon

class mainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.avoCalc = avon.AVONumerical(self)

        hBox1 = QHBoxLayout()       # Horizontal boxes
        hBox2 = QHBoxLayout()
        hBox3 = QHBoxLayout()
        hBox4 = QHBoxLayout()
        hBox5 = QHBoxLayout()
        hBox6 = QHBoxLayout()
        vBox1 = QVBoxLayout()
        hSpacer = QHBoxLayout()
        vSpacer = QHBoxLayout()

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
        self.vpUpperSlider.valueChanged.connect(self.onsliderchange)
        self.vsUpperSlider.valueChanged.connect(self.onsliderchange)
        self.rhoUpperSlider.valueChanged.connect(self.onsliderchange)
        self.vpLowerSlider.valueChanged.connect(self.onsliderchange)
        self.vsLowerSlider.valueChanged.connect(self.onsliderchange)
        self.rhoLowerSlider.valueChanged.connect(self.onsliderchange)
        plotBox = QHBoxLayout()
        self.avoplot = pyqtgraph.PlotWidget(title="AVO Curves")
        self.igplot = pyqtgraph.PlotWidget(title="I / G")
        self.avoplot.showGrid(x=True, y=True, alpha=0.5)
        self.igplot.showGrid(x=True, y=True, alpha=0.5)

        tr = self.avoCalc.getthetarange()
        self.avoplot.setXRange(0, 50)
        self.avoplot.setYRange(-1, 1)
        self.igplot.setXRange(-1, 1)
        self.igplot.setYRange(-1, 1)

        plotBox.addWidget(self.avoplot)
        plotBox.addWidget(self.igplot)

        vBox1.addLayout(hBox1)
        vBox1.addLayout(hBox2)
        vBox1.addLayout(hBox3)
        hSpacer.addSpacerItem(QSpacerItem(10, 20))
        vBox1.addLayout(hSpacer)
        vBox1.addLayout(hBox4)
        vBox1.addLayout(hBox5)
        vBox1.addLayout(hBox6)
        vBox1.addStretch()
        vBox1.addLayout(plotBox)
        vSpacer.addSpacerItem(QSpacerItem(10, 10))
        vBox1.addLayout(vSpacer)

        vbox2 = QVBoxLayout()
        vbox2.addStretch()
        self.setLayout(vBox1)
        self.setLayout(vbox2)
        self.updateplots()
        """
        Size and display
        """
        self.setGeometry(100, 200, 1000, 800)
        self.setWindowTitle('AVO plotter')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def updateplots(self):
        zoe = self.avoCalc.getavo('zoe')
        shuey = self.avoCalc.getavo('shuey')
        ar = self.avoCalc.getavo('ar')
        theta = self.avoCalc.getthetarange()

        g, i = self.avoCalc.getig()
        # one of: r, g, b, c, m, y, k, w
        self.avoplot.getPlotItem().clear()
        self.igplot.getPlotItem().clear()

        self.igplot.plot([i], [g], pen=pyqtgraph.mkPen(None), symbol='o', brush='r')
        self.avoplot.plot(theta, zoe).curve.setPen('r')
        self.avoplot.plot(theta, zoe).curve.setShadowPen(pyqtgraph.mkPen((70, 70, 30), width=6, cosmetic=True))
        self.avoplot.plot(theta, shuey).curve.setPen('g')
        self.avoplot.plot(theta, ar).curve.setPen('y')

    def initVpComponents(self):
        self.vpUpperLabel = QLabel("Vp Upper")


        self.vpLowerLabel = QLabel("Vp Lower")
        """
        Sliders
        """
        self.vpUpperSlider = QSlider(Qt.Horizontal)
        self.vpUpperSlider.setMaximumWidth(100)
        self.vpUpperSlider.setMinimum(avon.AVONumerical.vpextents[0])
        self.vpUpperSlider.setMaximum(avon.AVONumerical.vpextents[1])
        self.vpUpperSlider.setValue(avon.AVONumerical.vpinitial[0])
        self.vpUpperSlider.setTickPosition(QSlider.TicksBelow)
        self.vpUpperSlider.setTickInterval(avon.AVONumerical.vpextents[2])

        self.vpLowerSlider = QSlider(Qt.Horizontal)
        self.vpLowerSlider.setMinimum(avon.AVONumerical.vpextents[0])
        self.vpLowerSlider.setMaximum(avon.AVONumerical.vpextents[1])
        self.vpLowerSlider.setValue(avon.AVONumerical.vpinitial[1])
        self.vpLowerSlider.setTickPosition(QSlider.TicksBelow)
        self.vpLowerSlider.setTickInterval(avon.AVONumerical.vpextents[2])
        """
        Text boxes
        """
        self.vpUpperValue = QLineEdit(self)
        self.vpUpperValue.setMaximumWidth(100)
        self.vpLowerValue = QLineEdit(self)
        self.vpUpperValue.setText(str(avon.AVONumerical.vpinitial[0]))
        self.vpLowerValue.setText(str(avon.AVONumerical.vpinitial[1]))

    def initVsComponents(self):
        self.vsUpperLabel = QLabel("Vs Upper")
        self.vsLowerLabel = QLabel("Vs Lower")
        """
        Slidevs
        """
        self.vsUpperSlider = QSlider(Qt.Horizontal)
        self.vsUpperSlider.setMinimum(avon.AVONumerical.vsextents[0])
        self.vsUpperSlider.setMaximum(avon.AVONumerical.vsextents[1])
        self.vsUpperSlider.setValue(avon.AVONumerical.vsinitial[0])
        self.vsUpperSlider.setTickPosition(QSlider.TicksBelow)
        self.vsUpperSlider.setTickInterval(avon.AVONumerical.vsextents[2])

        self.vsLowerSlider = QSlider(Qt.Horizontal)
        self.vsLowerSlider.setMinimum(avon.AVONumerical.vsextents[0])
        self.vsLowerSlider.setMaximum(avon.AVONumerical.vsextents[1])
        self.vsLowerSlider.setValue(avon.AVONumerical.vsinitial[1])
        self.vsLowerSlider.setTickPosition(QSlider.TicksBelow)
        self.vsLowerSlider.setTickInterval(avon.AVONumerical.vsextents[2])
        """
        Text boxes
        """
        self.vsUpperValue = QLineEdit(self)
        self.vsLowerValue = QLineEdit(self)
        self.vsUpperValue.setText(str(avon.AVONumerical.vsinitial[0]))
        self.vsLowerValue.setText(str(avon.AVONumerical.vsinitial[1]))

    def initRhoComponents(self):
        self.rhoUpperLabel = QLabel("Rho Upper")
        self.rhoLowerLabel = QLabel("Rho Lower")
        """
        Sliders
        """
        self.rhoUpperSlider = QSlider(Qt.Horizontal)
        self.rhoUpperSlider.setMinimum(avon.AVONumerical.rhoextents[0])
        self.rhoUpperSlider.setMaximum(avon.AVONumerical.rhoextents[1])
        self.rhoUpperSlider.setValue(avon.AVONumerical.rhoinitial[0])
        self.rhoUpperSlider.setTickPosition(QSlider.TicksBelow)
        self.rhoUpperSlider.setTickInterval(avon.AVONumerical.rhoextents[2])

        self.rhoLowerSlider = QSlider(Qt.Horizontal)
        self.rhoLowerSlider.setMinimum(avon.AVONumerical.rhoextents[0])
        self.rhoLowerSlider.setMaximum(avon.AVONumerical.rhoextents[1])
        self.rhoLowerSlider.setValue(avon.AVONumerical.rhoinitial[1])
        self.rhoLowerSlider.setTickPosition(QSlider.TicksBelow)
        self.rhoLowerSlider.setTickInterval(avon.AVONumerical.rhoextents[2])
        """
        Text boxes
        """
        self.rhoUpperValue = QLineEdit(self)
        self.rhoLowerValue = QLineEdit(self)
        self.rhoUpperValue.setText(str(avon.AVONumerical.rhoinitial[0] / 1000))
        self.rhoLowerValue.setText(str(avon.AVONumerical.rhoinitial[1] / 1000))

    def onsliderchange(self):
        self.vpUpperValue.setText(str(self.vpUpperSlider.value()))
        self.vsUpperValue.setText(str(self.vsUpperSlider.value()))
        self.rhoUpperValue.setText(str(self.rhoUpperSlider.value()/1000))

        self.vpLowerValue.setText(str(self.vpLowerSlider.value()))
        self.vsLowerValue.setText(str(self.vsLowerSlider.value()))
        self.rhoLowerValue.setText(str(self.rhoLowerSlider.value()/1000))
        self.updateplots()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainWindow()
    sys.exit(app.exec_())