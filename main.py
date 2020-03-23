'''
Created on 23.3.2020

@author: arvil
'''

'''
Created on 26.2.2019

@author: arvil
'''

import sys
from PyQt5.QtWidgets import QApplication
from Gui import GUI



def main():
    
    
    global app # Use global to dprevent crashing dosn exit
    app = QApplication(sys.argv)
    gui = GUI() 

    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()
