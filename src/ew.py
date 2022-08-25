import sys 

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from shared import Myshared, EWRankShared
from ui.UI_Window import MainWindow

from PyQt5.QtWebChannel import QWebChannel

def run_app():
    app = QApplication(sys.argv)
    demo = MainWindow()  
    #demo.showMaximized()  
    demo.show()  

    channel = QWebChannel()
    shared = Myshared()
    channel.registerObject("connection", shared)
    demo.ew_grid.page().setWebChannel(channel) 
    shared.finish[str].connect(demo.update_display)

    rank_shared = EWRankShared()
    rank_channel = QWebChannel()
    rank_channel.registerObject("connection", rank_shared) 
    demo.ew_rank.page().setWebChannel(rank_channel) 
    rank_shared.finish[str].connect(demo.update_homepage_display)
    sys.exit(app.exec_())