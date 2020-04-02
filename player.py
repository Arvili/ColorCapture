


import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton

colors = [Qt.green, Qt.red, Qt.blue, Qt.yellow, Qt.magenta]

class Player():

    def __init__(self, number):
        self.color = colors[number-1]
        self.number = number
        self.area = []
        self.init_own_area()

    def get_number(self):
        return self.number

    def get_color(self):
        return self.color

    def set_color(self, idx):
        self.color = colors[idx]

    def init_own_area(self):
        tmp = []
        for i in range(0,500, 20):
            for j in range(0,800, 20):
                tmp.append(0)
            self.area.append(tmp)
            tmp = []

        if (self.number == 1):
            self.area[len(self.area)-1][0] = 1
        else:
            self.area[0][len(self.area[0])-1] = 1