
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton

colors = [Qt.red, Qt.green, Qt.blue, Qt.magenta, Qt.yellow]

class ColorItem(QtWidgets.QGraphicsRectItem):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.color = colors[0]
        self.width = width
        self.height = height
        self.x = x
        self.y = y



    def get_color(self):
        return self.color

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_rect_item(self):
        return self.rect()

    def set_color(self, color_index):
        self.color = colors[color_index]