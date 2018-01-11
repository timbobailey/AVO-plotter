# -*- coding: utf-8 -*-

import numpy as np
import pyqtgraph
from bruges.reflection import reflection as avomodel


class AVONumerical:
    ''' A class to isolate the AVO calls from the main gui'''
    # Extents and step of sliders
    # min, max, step
    vpextents = (100, 10000, 50)
    vsextents = (100, 10000, 50)
    rhoextents = (1000, 3500, 50)   #kg/cc

    # Initial values for sliders, text and AVO model
    # upper medium value, lower medium value
    vpinitial = (2730, 2050)
    vsinitial = (2470, 4000)
    rhoinitial = (1705, 1450)   #kg/cc

    theta = (0, 50, 1)
    thetarange = np.arange(theta[0], theta[1], theta[2])

    def __init__(self, maingui):
         self.maingui = maingui

    def getavo(self, method='zoe'):
            if method == 'zoe':
                return avomodel.zoeppritz_rpp(self.maingui.vpUpperSlider.value(), self.maingui.vsUpperSlider.value(),
                                        self.maingui.rhoUpperSlider.value() / 1000,
                                        self.maingui.vpLowerSlider.value(), self.maingui.vsLowerSlider.value(),
                                        self.maingui.rhoLowerSlider.value() / 1000, AVONumerical.thetarange)

            elif method == 'shuey':
                return avomodel.shuey(self.maingui.vpUpperSlider.value(), self.maingui.vsUpperSlider.value(),
                                   self.maingui.rhoUpperSlider.value() / 1000,
                                   self.maingui.vpLowerSlider.value(), self.maingui.vsLowerSlider.value(),
                                   self.maingui.rhoLowerSlider.value() / 1000, AVONumerical.thetarange)

            elif method == 'ar':
                return avomodel.akirichards(self.maingui.vpUpperSlider.value(), self.maingui.vsUpperSlider.value(),
                                      self.maingui.rhoUpperSlider.value() / 1000,
                                      self.maingui.vpLowerSlider.value(), self.maingui.vsLowerSlider.value(),
                                      self.maingui.rhoLowerSlider.value() / 1000, AVONumerical.thetarange)


    def getig(self):
        g, i = -0.1, 0.1
        return g, i

    def getthetarange(self):
        return AVONumerical.thetarange

    def getinitialproperties(self):

        pass

