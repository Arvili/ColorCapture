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
from player import Player
import random



class GUI(QWidget):
    
    def __init__(self):
        self.colors = []
        self.sceneWidth = 800
        self.sceneHeight = 500
        super().__init__()
        self.init_window()
        self.player1 = Player(1)
        
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
        self.setFixedSize(1000, 600)
        self.setWindowTitle('Colour capture')
        self.setStyleSheet("QWidget { background: #aeddf9 }") 
        
        #set up scenes
        self.mainScene = QtWidgets.QGraphicsScene()
        self.mainScene.setSceneRect(0, 0, 1000, 600)

        self.controlScene = QtWidgets.QGraphicsScene()
        self.controlScene.setSceneRect(self.get_width(), 0, 1000-self.get_width(), self.get_height())
        
        self.view = QtWidgets.QGraphicsView(self.mainScene, self)
        self.view.setFocusPolicy(QtCore.Qt.NoFocus)
        self.view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.view.adjustSize()

        self.brush = QtGui.QBrush(Qt.SolidPattern)
        self.pen = QtGui.QPen(Qt.SolidLine)
         
        
        self.init_color_items()
        self.init_colors()
        self.paint_colors()
        self.init_buttons()
        
            
        self.show()
        self.view.show()        

        
    def init_color_items(self):
        tmp = []
        for i in range(0,self.get_height(), 20):
            for j in range(0,self.get_width(), 20):
                tmp.append(ColorItem(j, i, 20, 20))
            self.colors.append(tmp)
            tmp = []

    def init_colors(self):
        for n in self.colors:
            for m in n:
                m.set_color(random.randint(0,3))

    def paint_colors(self):
        for n in self.colors:
            for m in n:
                self.brush.setColor(m.get_color())
                self.mainScene.addRect(m.get_rect_item(), self.pen, self.brush)


    def change_colors(self):
        self.init_colors()
        self.paint_colors()
                
    def init_buttons(self):
        self.button = QPushButton("Change colors")
        self.button.resize(200,100)
        self.button.move(self.get_width(), 0)
        self.button.clicked.connect(self.change_colors) 
        self.mainScene.addWidget(self.button)


    
