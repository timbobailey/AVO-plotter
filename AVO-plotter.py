
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QSlider, \
                            QVBoxLayout, QHBoxLayout, \
                            QLineEdit, QApplication, QSpacerItem

import pyqtgraph
import AVOui
import avonumericals as avon

def initUI(ui):
    ui.horizontalSlider_vp1.setMinimum(avon.AVONumerical.vpextents[0])
    ui.horizontalSlider_vp1.setMaximum(avon.AVONumerical.vpextents[1])
    ui.horizontalSlider_vp1.setTickInterval(avon.AVONumerical.vpextents[2])
    ui.horizontalSlider_vp1.setValue(avon.AVONumerical.vpinitial[0])
    ui.horizontalSlider_vp1.setTickPosition(QSlider.TicksBelow)
    ui.horizontalSlider_vp1.valueChanged.connect(onsliderchange)

    ui.horizontalSlider_vs1.setMinimum(avon.AVONumerical.vsextents[0])
    ui.horizontalSlider_vs1.setMaximum(avon.AVONumerical.vsextents[1])
    ui.horizontalSlider_vs1.setTickInterval(avon.AVONumerical.vsextents[2])
    ui.horizontalSlider_vs1.setValue(avon.AVONumerical.vsinitial[0])
    ui.horizontalSlider_vs1.setTickPosition(QSlider.TicksBelow)
    ui.horizontalSlider_vs1.valueChanged.connect(onsliderchange)

    ui.horizontalSlider_rho1.setMinimum(avon.AVONumerical.rhoextents[0])
    ui.horizontalSlider_rho1.setMaximum(avon.AVONumerical.rhoextents[1])
    ui.horizontalSlider_rho1.setTickInterval(avon.AVONumerical.rhoextents[2])
    ui.horizontalSlider_rho1.setValue(avon.AVONumerical.rhoinitial[0])
    ui.horizontalSlider_rho1.setTickPosition(QSlider.TicksBelow)
    ui.horizontalSlider_rho1.valueChanged.connect(onsliderchange)

    ui.horizontalSlider_vp2.setMinimum(avon.AVONumerical.vpextents[0])
    ui.horizontalSlider_vp2.setMaximum(avon.AVONumerical.vpextents[1])
    ui.horizontalSlider_vp2.setTickInterval(avon.AVONumerical.vpextents[2])
    ui.horizontalSlider_vp2.setValue(avon.AVONumerical.vpinitial[1])
    ui.horizontalSlider_vp2.setTickPosition(QSlider.TicksBelow)
    ui.horizontalSlider_vp2.valueChanged.connect(onsliderchange)

    ui.horizontalSlider_vs2.setMinimum(avon.AVONumerical.vsextents[0])
    ui.horizontalSlider_vs2.setMaximum(avon.AVONumerical.vsextents[1])
    ui.horizontalSlider_vs2.setTickInterval(avon.AVONumerical.vsextents[2])
    ui.horizontalSlider_vs2.setValue(avon.AVONumerical.vsinitial[1])
    ui.horizontalSlider_vs2.setTickPosition(QSlider.TicksBelow)
    ui.horizontalSlider_vs2.valueChanged.connect(onsliderchange)

    ui.horizontalSlider_rho2.setMinimum(avon.AVONumerical.rhoextents[0])
    ui.horizontalSlider_rho2.setMaximum(avon.AVONumerical.rhoextents[1])
    ui.horizontalSlider_rho2.setTickInterval(avon.AVONumerical.rhoextents[2])
    ui.horizontalSlider_rho2.setValue(avon.AVONumerical.rhoinitial[1])
    ui.horizontalSlider_rho2.setTickPosition(QSlider.TicksBelow)
    ui.horizontalSlider_rho2.valueChanged.connect(onsliderchange)

    ui.pushButton_quit.clicked.connect(QtCore.QCoreApplication.instance().quit)

    avoplot.showGrid(x=True, y=True, alpha=0.5)
    igplot.showGrid(x=True, y=True, alpha=0.5)
    avoplot.setXRange(0, 50)
    avoplot.setYRange(-1, 1)
    igplot.setXRange(-1, 1)
    igplot.setYRange(-1, 1)
    ui.plotLayout.addWidget(avoplot)
    ui.plotLayout.addWidget(igplot)
    onsliderchange()

def updateplots():
    zoe = avoCalculator.getavo('zoe')
    shuey = avoCalculator.getavo('shuey')
    ar = avoCalculator.getavo('ar')
    theta = avoCalculator.getthetarange()

    g, i = avoCalculator.getig()
    # one of: r, g, b, c, m, y, k, w
    avoplot.getPlotItem().clear()
    igplot.getPlotItem().clear()

    igplot.plot([i], [g], pen=pyqtgraph.mkPen(None), symbol='o', brush='r')
    avoplot.plot(theta, zoe).curve.setPen('r')
    avoplot.plot(theta, zoe).curve.setShadowPen(pyqtgraph.mkPen((70, 70, 30), width=6, cosmetic=True))
    avoplot.plot(theta, shuey).curve.setPen('g')
    avoplot.plot(theta, ar).curve.setPen('y')


def onsliderchange():
    ui.lineEdit_vp1.setText(str(ui.horizontalSlider_vp1.value()))
    ui.lineEdit_vs1.setText(str(ui.horizontalSlider_vs1.value()))
    ui.lineEdit_rho1.setText(str(ui.horizontalSlider_rho1.value() / 1000))

    ui.lineEdit_vp2.setText(str(ui.horizontalSlider_vp2.value()))
    ui.lineEdit_vs2.setText(str(ui.horizontalSlider_vs2.value()))
    ui.lineEdit_rho2.setText(str(ui.horizontalSlider_rho2.value() / 1000))
    updateplots()

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = AVOui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    avoCalculator = avon.AVONumerical(ui)
    avoplot = pyqtgraph.PlotWidget(title="AVO Curves")
    igplot = pyqtgraph.PlotWidget(title="I / G")
    initUI(ui)

    MainWindow.show()
    sys.exit(app.exec_())
