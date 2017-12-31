# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QSlider, \
                            QVBoxLayout, QHBoxLayout, QGridLayout, \
                            QApplication
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon

class mainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        """
        Sliders
        """
        grid = QGridLayout()
        grid.setSpacing(10)

        vpUpperLabel = QLabel("Vp Upper")


        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(10)
        slider.setMaximum(30)
        slider.setValue(20)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setTickInterval(5)

        grid.addWidget(vpUpperLabel, 0, 1)
        grid.addWidget(slider, 1, 1)


        #slider.valueChanged.connect(self.valuechange)
        self.setLayout(grid)

        """
        quitButton = QPushButton('Quit', self)
        quitButton.clicked.connect(QCoreApplication.instance().quit)
        quitButton.resize(quitButton.sizeHint())

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(quitButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        """

        """
        Size and display
        """
        self.resize(600, 600)
        self.setGeometry(500, 300, 250, 150)
        self.setWindowTitle('AVO plotter')
        self.setWindowIcon(QIcon('web.png'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainWindow()
    sys.exit(app.exec_())