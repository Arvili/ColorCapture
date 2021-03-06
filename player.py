


import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton

colors = [Qt.green, Qt.red, Qt.blue, Qt.yellow, Qt.magenta]

class Player():

    def __init__(self, number, width, height):
        self.color = colors[number-1]
        self.number = number
        self.area = []
        self.init_own_area(width, height)
        self.area_size = 1

    def get_number(self):
        return self.number

    def get_color(self):
        return self.color

    def get_color_index(self):
        return colors.index(self.color)

    def get_area(self):
        return self.area

    def set_color(self, idx):
        self.color = colors[idx]

    def update_area(self, x, y):
        self.area[x][y] = 1
        self.area_size += 1

    def get_area_size(self):
        return self.area_size

    def init_own_area(self, w, h):
        tmp = []
        for i in range(0, h, 20):
            for j in range(0,w, 20):
                tmp.append(0)
            self.area.append(tmp)
            tmp = []

        if (self.number == 1):
            self.area[len(self.area)-1][0] = 1
        else:
            self.area[0][len(self.area[0])-1] = 1