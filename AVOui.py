# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\AVO-plotter.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(867, 731)
        MainWindow.setMinimumSize(QtCore.QSize(867, 731))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_quit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_quit.setGeometry(QtCore.QRect(760, 660, 101, 23))
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.slidersvLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.slidersvLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.slidersvLayout.setContentsMargins(0, 0, 0, 0)
        self.slidersvLayout.setObjectName("slidersvLayout")
        self.hLayout1 = QtWidgets.QHBoxLayout()
        self.hLayout1.setObjectName("hLayout1")
        self.label_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_1.setObjectName("label_1")
        self.hLayout1.addWidget(self.label_1)
        self.horizontalSlider_vp1 = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider_vp1.setEnabled(True)
        self.horizontalSlider_vp1.setMaximumSize(QtCore.QSize(200, 16777215))
        self.horizontalSlider_vp1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_vp1.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_vp1.setObjectName("horizontalSlider_vp1")
        self.hLayout1.addWidget(self.horizontalSlider_vp1)
        self.lineEdit_vp1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_vp1.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_vp1.setObjectName("lineEdit_vp1")
        self.hLayout1.addWidget(self.lineEdit_vp1)
        self.slidersvLayout.addLayout(self.hLayout1)
        self.hLayout2 = QtWidgets.QHBoxLayout()
        self.hLayout2.setObjectName("hLayout2")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.hLayout2.addWidget(self.label_4)
        self.horizontalSlider_vs1 = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider_vs1.setEnabled(True)
        self.horizontalSlider_vs1.setMaximumSize(QtCore.QSize(200, 16777215))
        self.horizontalSlider_vs1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_vs1.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_vs1.setObjectName("horizontalSlider_vs1")
        self.hLayout2.addWidget(self.horizontalSlider_vs1)
        self.lineEdit_vs1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_vs1.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_vs1.setObjectName("lineEdit_vs1")
        self.hLayout2.addWidget(self.lineEdit_vs1)
        self.slidersvLayout.addLayout(self.hLayout2)
        self.hLayout3 = QtWidgets.QHBoxLayout()
        self.hLayout3.setObjectName("hLayout3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.hLayout3.addWidget(self.label_3)
        self.horizontalSlider_rho1 = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider_rho1.setEnabled(True)
        self.horizontalSlider_rho1.setMaximumSize(QtCore.QSize(200, 16777215))
        self.horizontalSlider_rho1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_rho1.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_rho1.setObjectName("horizontalSlider_rho1")
        self.hLayout3.addWidget(self.horizontalSlider_rho1)
        self.lineEdit_rho1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_rho1.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_rho1.setObjectName("lineEdit_rho1")
        self.hLayout3.addWidget(self.lineEdit_rho1)
        self.slidersvLayout.addLayout(self.hLayout3)
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.slidersvLayout.addItem(spacerItem)
        self.hLayout4 = QtWidgets.QHBoxLayout()
        self.hLayout4.setObjectName("hLayout4")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.hLayout4.addWidget(self.label_5)
        self.horizontalSlider_vp2 = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider_vp2.setEnabled(True)
        self.horizontalSlider_vp2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.horizontalSlider_vp2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_vp2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_vp2.setObjectName("horizontalSlider_vp2")
        self.hLayout4.addWidget(self.horizontalSlider_vp2)
        self.lineEdit_vp2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_vp2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_vp2.setObjectName("lineEdit_vp2")
        self.hLayout4.addWidget(self.lineEdit_vp2)
        self.slidersvLayout.addLayout(self.hLayout4)
        self.hLayout5 = QtWidgets.QHBoxLayout()
        self.hLayout5.setObjectName("hLayout5")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.hLayout5.addWidget(self.label_6)
        self.horizontalSlider_vs2 = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider_vs2.setEnabled(True)
        self.horizontalSlider_vs2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.horizontalSlider_vs2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_vs2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_vs2.setObjectName("horizontalSlider_vs2")
        self.hLayout5.addWidget(self.horizontalSlider_vs2)
        self.lineEdit_vs2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_vs2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_vs2.setObjectName("lineEdit_vs2")
        self.hLayout5.addWidget(self.lineEdit_vs2)
        self.slidersvLayout.addLayout(self.hLayout5)
        self.hLayout6 = QtWidgets.QHBoxLayout()
        self.hLayout6.setObjectName("hLayout6")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.hLayout6.addWidget(self.label_7)
        self.horizontalSlider_rho2 = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider_rho2.setEnabled(True)
        self.horizontalSlider_rho2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.horizontalSlider_rho2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_rho2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_rho2.setObjectName("horizontalSlider_rho2")
        self.hLayout6.addWidget(self.horizontalSlider_rho2)
        self.lineEdit_rho2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_rho2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_rho2.setObjectName("lineEdit_rho2")
        self.hLayout6.addWidget(self.lineEdit_rho2)
        self.slidersvLayout.addLayout(self.hLayout6)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(10, 270, 851, 381))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.plotLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.plotLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.plotLayout.setContentsMargins(0, 0, 0, 0)
        self.plotLayout.setObjectName("plotLayout")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(360, 170, 105, 92))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_zoe = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_zoe.setChecked(True)
        self.checkBox_zoe.setObjectName("checkBox_zoe")
        self.verticalLayout.addWidget(self.checkBox_zoe)
        self.checkBox_aandr = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_aandr.setChecked(True)
        self.checkBox_aandr.setObjectName("checkBox_aandr")
        self.verticalLayout.addWidget(self.checkBox_aandr)
        self.checkBox_shuey = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_shuey.setChecked(True)
        self.checkBox_shuey.setObjectName("checkBox_shuey")
        self.verticalLayout.addWidget(self.checkBox_shuey)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 867, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AVO Plotter"))
        self.pushButton_quit.setText(_translate("MainWindow", "Quit"))
        self.label_1.setText(_translate("MainWindow", "Vp Upper"))
        self.label_4.setText(_translate("MainWindow", "Vs Upper"))
        self.label_3.setText(_translate("MainWindow", "Rho Upper"))
        self.label_5.setText(_translate("MainWindow", "Vp Lower"))
        self.label_6.setText(_translate("MainWindow", "Vs Lower"))
        self.label_7.setText(_translate("MainWindow", "Rho Upper"))
        self.checkBox_zoe.setText(_translate("MainWindow", "Zoeppritz"))
        self.checkBox_aandr.setText(_translate("MainWindow", "Aki and Richards"))
        self.checkBox_shuey.setText(_translate("MainWindow", "Shuey"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

