# -*- coding: utf-8 -*-

import numpy as np
from bruges.reflection import reflection as avomodel


class AVONumerical:
    ''' A class to isolate the AVO calls from the main gui'''
    # Extents and step of sliders
    # min, max, step
    vpextents = (100, 10000, 50)    # m/s
    vsextents = (100, 10000, 50)    # m/s
    rhoextents = (1000, 3500, 50)   # kg/cc

    # Initial values for sliders, text and AVO model
    # upper medium value, lower medium value
    vpinitial = (3110, 1980)    # m/s
    vsinitial = (2360, 2720)    # m/s
    rhoinitial = (1920, 3050)   # kg/cc

    theta = (0, 50, 1)
    thetarange = np.arange(theta[0], theta[1], theta[2])

    def __init__(self, maingui):
         self.maingui = maingui

    def getavo(self, method='zoe'):
        if method == 'zoe':
                return avomodel.zoeppritz_rpp(self.maingui.horizontalSlider_vp1.value(), self.maingui.horizontalSlider_vs1.value(),
                                        self.maingui.horizontalSlider_rho1.value() / 1000,
                                        self.maingui.horizontalSlider_vp2.value(), self.maingui.horizontalSlider_vs2.value(),
                                        self.maingui.horizontalSlider_rho2.value() / 1000, AVONumerical.thetarange)

        elif method == 'shuey':
                return avomodel.shuey(self.maingui.horizontalSlider_vp1.value(), self.maingui.horizontalSlider_vs1.value(),
                                        self.maingui.horizontalSlider_rho1.value() / 1000,
                                        self.maingui.horizontalSlider_vp2.value(), self.maingui.horizontalSlider_vs2.value(),
                                        self.maingui.horizontalSlider_rho2.value() / 1000, AVONumerical.thetarange)

        elif method == 'ar':
                return avomodel.akirichards(self.maingui.horizontalSlider_vp1.value(), self.maingui.horizontalSlider_vs1.value(),
                                        self.maingui.horizontalSlider_rho1.value() / 1000,
                                        self.maingui.horizontalSlider_vp2.value(), self.maingui.horizontalSlider_vs2.value(),
                                        self.maingui.horizontalSlider_rho2.value() / 1000, AVONumerical.thetarange)


    def getig(self):
        g, i = -0.1, 0.1
        return i, g

    def getthetarange(self):
        return AVONumerical.thetarange

    def getthetamin(self):
        pass

    def getthetamax(self):
        pass

    def getinitialproperties(self):
        pass

