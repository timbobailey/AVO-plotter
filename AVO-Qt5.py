# -*- coding: utf-8 -*-

import sys
import pyqtgraph
from PyQt5.QtWidgets import QWidget, QLabel, QSlider, \
                            QVBoxLayout, QHBoxLayout, \
                            QLineEdit, QApplication, QSpacerItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import AVONumerical

class mainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.avoCalc = AVONumerical.avoNumerical(self)

        hBox1 = QHBoxLayout()
        hBox2 = QHBoxLayout()
        hBox3 = QHBoxLayout()

        hBox4 = QHBoxLayout()
        hBox5 = QHBoxLayout()
        hBox6 = QHBoxLayout()
        hSpacer = QHBoxLayout()
        vSpacer  = QHBoxLayout()
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
        self.avoplot = pyqtgraph.PlotWidget(title="AVO Curves")
        plotBox.addWidget(self.avoplot)
        self.avoplot.showGrid(x=True, y=True, alpha=0.5)

        # I / G Plot
        self.igplot = pyqtgraph.PlotWidget(title="I / G")
        self.igplot.showGrid(x=True, y=True, alpha=0.5)
        plotBox.addWidget(self.igplot)

        vBox1.addLayout(hBox1)
        vBox1.addLayout(hBox2)
        vBox1.addLayout(hBox3)
        hSpacer.addSpacerItem(QSpacerItem(10, 20))
        vBox1.addLayout(hSpacer)
        vBox1.addLayout(hBox4)
        vBox1.addLayout(hBox5)
        vBox1.addLayout(hBox6)
        vBox1.addLayout(plotBox)

        vSpacer.addSpacerItem(QSpacerItem(100, 20))
        vBox1.addLayout(vSpacer)

        self.setLayout(vBox1)
        self.avoCalc.calculateavo()
        #self.calculateAVO()

        """
        Size and display
        """
        self.setGeometry(100, 200, 1000, 800)
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
        self.vpUpperSlider.setMinimum(self.avoCalc.VP_MIN)
        self.vpUpperSlider.setMaximum(self.avoCalc.VP_MAX)
        self.vpUpperSlider.setValue(self.avoCalc.VP_UPPER_INITIAL)
        self.vpUpperSlider.setTickPosition(QSlider.TicksBelow)
        self.vpUpperSlider.setTickInterval(50)

        self.vpLowerSlider = QSlider(Qt.Horizontal)
        self.vpLowerSlider.setMinimum(self.avoCalc.VP_MIN)
        self.vpLowerSlider.setMaximum(self.avoCalc.VP_MAX)
        self.vpLowerSlider.setValue(self.avoCalc.VP_LOWER_INITIAL)
        self.vpLowerSlider.setTickPosition(QSlider.TicksBelow)
        self.vpLowerSlider.setTickInterval(50)
        """
        Text boxes
        """
        self.vpUpperValue = QLineEdit(self)
        self.vpLowerValue = QLineEdit(self)
        self.vpUpperValue.setText(str(self.avoCalc.VP_UPPER_INITIAL))
        self.vpLowerValue.setText(str(self.avoCalc.VP_LOWER_INITIAL))


    def initVsComponents(self):
        self.vsUpperLabel = QLabel("Vs Upper")
        self.vsLowerLabel = QLabel("Vs Lower")
        """
        Slidevs
        """
        self.vsUpperSlider = QSlider(Qt.Horizontal)
        self.vsUpperSlider.setMinimum(self.avoCalc.VS_MIN)
        self.vsUpperSlider.setMaximum(self.avoCalc.VS_MAX)
        self.vsUpperSlider.setValue(self.avoCalc.VS_UPPER_INITIAL)
        self.vsUpperSlider.setTickPosition(QSlider.TicksBelow)
        self.vsUpperSlider.setTickInterval(50)

        self.vsLowerSlider = QSlider(Qt.Horizontal)
        self.vsLowerSlider.setMinimum(self.avoCalc.VS_MIN)
        self.vsLowerSlider.setMaximum(self.avoCalc.VS_MAX)
        self.vsLowerSlider.setValue(self.avoCalc.VS_LOWER_INITIAL)
        self.vsLowerSlider.setTickPosition(QSlider.TicksBelow)
        self.vsLowerSlider.setTickInterval(50)
        """
        Text boxes
        """
        self.vsUpperValue = QLineEdit(self)
        self.vsLowerValue = QLineEdit(self)
        self.vsUpperValue.setText(str(self.avoCalc.VS_UPPER_INITIAL))
        self.vsLowerValue.setText(str(self.avoCalc.VS_LOWER_INITIAL))

    def initRhoComponents(self):
        self.rhoUpperLabel = QLabel("Rho Upper")
        self.rhoLowerLabel = QLabel("Rho Lower")
        """
        Sliders
        """
        self.rhoUpperSlider = QSlider(Qt.Horizontal)
        self.rhoUpperSlider.setMinimum(self.avoCalc.RHO_MIN)
        self.rhoUpperSlider.setMaximum(self.avoCalc.RHO_MAX)
        self.rhoUpperSlider.setValue(self.avoCalc.RHO_UPPER_INITIAL)
        self.rhoUpperSlider.setTickPosition(QSlider.TicksBelow)
        self.rhoUpperSlider.setTickInterval(self.avoCalc.RHO_STEP)

        self.rhoLowerSlider = QSlider(Qt.Horizontal)
        self.rhoLowerSlider.setMinimum(self.avoCalc.RHO_MIN)
        self.rhoLowerSlider.setMaximum(self.avoCalc.RHO_MAX)
        self.rhoLowerSlider.setValue(self.avoCalc.RHO_LOWER_INITIAL)
        self.rhoLowerSlider.setTickPosition(QSlider.TicksBelow)
        self.rhoLowerSlider.setTickInterval(self.avoCalc.RHO_STEP)
        """
        Text boxes
        """
        self.rhoUpperValue = QLineEdit(self)
        self.rhoLowerValue = QLineEdit(self)
        self.rhoUpperValue.setText(str(self.avoCalc.RHO_UPPER_INITIAL))
        self.rhoLowerValue.setText(str(self.avoCalc.RHO_LOWER_INITIAL))

    def on_vpUpperSliderChange(self):
        value = str( self.vpUpperSlider.value() )
        self.vpUpperValue.setText(value)
        self.avoCalc.calculateavo()

    def on_vsUpperSliderChange(self):
        value = str( self.vsUpperSlider.value() )
        self.vsUpperValue.setText(value)
        self.avoCalc.calculateavo()

    def on_rhoUpperSliderChange(self):
        value = str( self.rhoUpperSlider.value() / 1000 )
        self.rhoUpperValue.setText(value)
        self.avoCalc.calculateavo()

    def on_vpLowerSliderChange(self):
        value = str( self.vpLowerSlider.value() )
        self.vpLowerValue.setText(value)
        self.avoCalc.calculateavo()

    def on_vsLowerSliderChange(self):
        value = str( self.vsLowerSlider.value() )
        self.vsLowerValue.setText(value)
        self.avoCalc.calculateavo()

    def on_rhoLowerSliderChange(self):
        value = str( self.rhoLowerSlider.value() / 1000 )
        self.rhoLowerValue.setText(value)
        self.avoCalc.calculateavo()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainWindow()
    sys.exit(app.exec_())