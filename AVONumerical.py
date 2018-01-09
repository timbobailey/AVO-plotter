# -*- coding: utf-8 -*-

import numpy as np
import pyqtgraph
from bruges.reflection import reflection as avomodel


class avoNumerical():
    
    VP_MIN = 100
    VP_MAX = 10000
    VP_STEP = 50
    VP_UPPER_INITIAL = 2730
    VP_LOWER_INITIAL = 2050

    VS_MIN = 100
    VS_MAX = 10000
    VS_STEP = 50
    VS_UPPER_INITIAL = 2470
    VS_LOWER_INITIAL = 4000

    RHO_MIN = 1000
    RHO_MAX = 3500
    RHO_STEP = 50
    RHO_UPPER_INITIAL = 1705
    RHO_LOWER_INITIAL = 1450

    def __init__(self, maingui):
        self.maingui = maingui

    def calculateavo(self):
        min_theta = 0
        max_theta = 50
        step_theta = 1
        theta = np.arange(min_theta, max_theta, step_theta)
        self.maingui.avoplot.getPlotItem().clear()
        self.maingui.igplot.getPlotItem().clear()
        self.maingui.avoplot.setXRange(min_theta, max_theta)
        self.maingui.avoplot.setYRange(-1, 1)

        self.maingui.igplot.setXRange(-1, 1)
        self.maingui.igplot.setYRange(-1, 1)

        zoe_avo = avomodel.zoeppritz_rpp(self.maingui.vpUpperSlider.value(), self.maingui.vsUpperSlider.value(),
                                         self.maingui.rhoUpperSlider.value() / 1000,
                                         self.maingui.vpLowerSlider.value(), self.maingui.vsLowerSlider.value(),
                                         self.maingui.rhoLowerSlider.value() / 1000, theta)

        shuey_avo = avomodel.shuey(self.maingui.vpUpperSlider.value(), self.maingui.vsUpperSlider.value(),
                                   self.maingui.rhoUpperSlider.value() / 1000,
                                   self.maingui.vpLowerSlider.value(), self.maingui.vsLowerSlider.value(),
                                   self.maingui.rhoLowerSlider.value() / 1000, theta)

        ar_avo = avomodel.akirichards(self.maingui.vpUpperSlider.value(), self.maingui.vsUpperSlider.value(),
                                      self.maingui.rhoUpperSlider.value() / 1000,
                                      self.maingui.vpLowerSlider.value(), self.maingui.vsLowerSlider.value(),
                                      self.maingui.rhoLowerSlider.value() / 1000, theta)

        G, I = np.polyfit(theta, zoe_avo, 1)
        self.maingui.igplot.plot([I], [G], pen=pyqtgraph.mkPen(None), symbol='o', brush='r')
        # self.igplot.plot(I, G)
        print('I, G: ', I, G)

        # one of: r, g, b, c, m, y, k, w
        self.maingui.avoplot.plot(theta, zoe_avo).curve.setPen('r')
        self.maingui.avoplot.plot(theta, zoe_avo).curve.setShadowPen(pyqtgraph.mkPen((70, 70, 30), width=6, cosmetic=True))
        self.maingui.avoplot.plot(theta, shuey_avo).curve.setPen('g')
        self.maingui.avoplot.plot(theta, ar_avo).curve.setPen('y')
