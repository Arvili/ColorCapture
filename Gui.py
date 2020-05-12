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
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton, QLabel
from color import ColorItem
from player import Player
import math
import random



class GUI(QWidget):
    
    def __init__(self):
        self.colors = []
        self.colorCodes = [Qt.green, Qt.red, Qt.blue, Qt.yellow, Qt.magenta]
        self.sceneWidth = 600
        self.sceneHeight = 300
        super().__init__()
        
        self.player1 = Player(1, self.sceneWidth, self.sceneHeight)
        self.player2 = Player(2, self.sceneWidth, self.sceneHeight)
        self.init_window()
        self.current_player = self.player1
        self.winning_size = 0.5*(self.get_width()/20)*(self.get_height()/20)

    def init_window(self):
        #Set up the window
        self.setFixedSize(self.get_width()+400, self.get_height()+100)
        self.setWindowTitle('Colour capture')
        self.setStyleSheet("QWidget { background: #aeddf9 }") 
        
        #set up scenes
        self.mainScene = QtWidgets.QGraphicsScene()
        self.mainScene.setSceneRect(0, 0, self.get_width()+400, self.get_height()+100)

        #self.controlScene = QtWidgets.QGraphicsScene()
        #self.controlScene.setSceneRect(self.get_width(), 0, 1000-self.get_width(), self.get_height())
        
        self.view = QtWidgets.QGraphicsView(self.mainScene, self)
        #self.view.setFocusPolicy(QtCore.Qt.NoFocus)
        #self.view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        #self.view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.view.ensureVisible(self.mainScene.sceneRect())

        self.brush = QtGui.QBrush(Qt.SolidPattern)
        self.pen = QtGui.QPen(Qt.SolidLine)
         
        
        self.init_color_items()
        self.init_colors()
        self.paint_colors()
        self.init_buttons()
        
        self.turn_label = QLabel()
        self.turn_label.setText("Player 1's turn!")
        self.turn_label.move(self.get_width()+100, 100)
        self.mainScene.addWidget(self.turn_label)
        
        self.show()
        self.view.show() 

    def change_turn(self):
        if(self.check_winner() == False):
            self.change_colors()
            if(self.current_player == self.player1):
                self.current_player = self.player2
                self.turn_label.setText("Player 2's turn!")
            else:
                self.current_player = self.player1
                self.turn_label.setText("Player 1's turn!")
            self.hide_color_buttons()
            self.paint_colors()
    
    def get_width(self):
        return self.sceneWidth

    def get_height(self):
        return self.sceneHeight
        # grid 40 x 25
    
    def get_winning_size(self):
        return self.winning_size
               
    def check_winner(self):
        if(self.current_player.get_area_size() > self.get_winning_size()):
            return True
        return False
        
        
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
                m.set_color(random.randint(0,4))
        self.init_corners()

    def init_corners(self):
        self.colors[len(self.colors)-1][0].set_color(0)
        self.colors[0][len(self.colors[0])-1].set_color(1)

    def paint_colors(self):
        for n in self.colors:
            for m in n:
                self.brush.setColor(m.get_color())
                self.pen.setColor(m.get_color())
                self.mainScene.addRect(m.get_rect_item(), self.pen, self.brush)


    
                
    def init_buttons(self):
    
        self.blueBtn = QPushButton()
        self.blueBtn.setStyleSheet('QPushButton {background-color: blue}')
        self.greenBtn = QPushButton()
        self.greenBtn.setStyleSheet('QPushButton {background-color: green}')
        self.redBtn = QPushButton()
        self.redBtn.setStyleSheet('QPushButton {background-color: red}')  
        self.yellowBtn = QPushButton()
        self.yellowBtn.setStyleSheet('QPushButton {background-color: yellow}')
        self.purpleBtn = QPushButton()
        self.purpleBtn.setStyleSheet('QPushButton {background-color: purple}')

        self.colorBtns = [self.greenBtn, self.redBtn, self.blueBtn, self.yellowBtn, self.purpleBtn]

        for idx, i in enumerate(self.colorBtns):
            i.resize(40, 40)
            i.move(self.get_width() + 20 + 50*idx, 150)
            i.clicked.connect(self.click_color(idx))
            self.mainScene.addWidget(i)

        self.hide_color_buttons()    
                
    
    def click_color(self, idx):
        def choose_color():
            self.current_player.set_color(idx)
            self.change_turn()
        return choose_color


    def hide_color_buttons(self):
        player1_color = self.player1.get_color()
        player2_color = self.player2.get_color()

        for i in self.colorBtns:
            i.show()

        for idx, j in enumerate(self.colorCodes):
            if player1_color == j:
                self.colorBtns[idx].hide()

        for idx2, k in enumerate(self.colorCodes):
            if player2_color == k:
                self.colorBtns[idx2].hide()


    def change_colors(self):
        new_color = self.current_player.get_color_index()
        players_area = self.current_player.get_area()
        

        for idx, i in enumerate(self.colors):
            for jdx, j in enumerate(i):
                if(players_area[idx][jdx] == 1):
                    j.set_color(new_color)
                    self.check_neighbour_colors(idx, jdx, new_color)
                    

    def check_neighbour_colors(self, x, y, c):
        if(x > 0):
            if (self.colors[x-1][y].get_color() == self.current_player.get_color()):
                self.colors[x-1][y].set_color(c)
                self.current_player.update_area(x-1, y)
        if(x < (self.get_height() / 20 - 1)):
            if (self.colors[x+1][y].get_color() == self.current_player.get_color()):
                self.colors[x+1][y].set_color(c)
                self.current_player.update_area(x+1, y)
        if(y > 0):
            if self.colors[x][y-1].get_color() == self.current_player.get_color():
                self.colors[x][y-1].set_color(c)
                self.current_player.update_area(x, y-1)
        if(y < (self.get_width() / 20 - 1)):
            if self.colors[x][y+1].get_color() == self.current_player.get_color():
                self.colors[x][y+1].set_color(c)
                self.current_player.update_area(x, y+1)