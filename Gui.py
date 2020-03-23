'''
Created on 23.3.2020

@author: arvil
'''

'''
Created on 9.3.2019

@author: arvil
'''
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton
from color import ColorItem
import random



class GUI(QWidget):
    
    def __init__(self):
        self.colors = []
        self.sceneWidth = 800
        self.sceneHeight = 500
        super().__init__()
        self.init_window()
        
        #self.timer = QtCore.QTimer()
        #self.timer.setInterval(10)
        #self.timer.timeout.connect() #update player position in every 10ms
    
    
    def get_width(self):
        return self.sceneWidth

    def get_height(self):
        return self.sceneHeight
        # grid 40 x 25
     
                
    def init_window(self):
        #Set up the window
        self.setFixedSize(1000, 500)
        self.setWindowTitle('Colour capture')
        self.setStyleSheet("QWidget { background: #aeddf9 }") 
        
        #set up scenes
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, self.get_width(), self.get_height())
        
        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.setFocusPolicy(QtCore.Qt.NoFocus)
        self.view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.view.adjustSize()

        self.brush = QtGui.QBrush(Qt.SolidPattern)
        self.pen = QtGui.QPen(Qt.SolidLine)
        
        
        tmp = []
        
        for i in range(0,self.get_width(), 20):
            for j in range(0,self.get_height(), 20):
                tmp.append(ColorItem(i, j, 20, 20))
            self.colors.append(tmp)
            tmp = []

        self.init_colors()

        
        for n in self.colors:
            for m in n:
                self.brush.setColor(m.get_color())
                self.scene.addRect(m.get_rect_item(), self.pen, self.brush)
            
        self.show()
        self.view.show()        

        

    def init_colors(self):
        for n in self.colors:
            for m in n:
                m.set_color(random.randint(0,3))
                
        
