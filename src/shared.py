from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtProperty, pyqtSignal, qInstallMessageHandler
qInstallMessageHandler(lambda x,y,z: None)

class Myshared(QWidget):
    finish = pyqtSignal(str)

    def __init__(self):
        super().__init__()
    
    def PyQt52WebValue(self):
        return "666"
    
    def Web2PyQt5Value(self, strs):
        print(strs)        
        self.finish.emit(strs)

    value = pyqtProperty(str, fget=PyQt52WebValue, fset=Web2PyQt5Value)

class EWRankShared(QWidget):
    finish = pyqtSignal(str)

    def __init__(self):
        super().__init__()
    
    def PyQt52WebValue(self):
        return "666"
    
    def Web2PyQt5Value(self, strs):
        print(strs)        
        self.finish.emit(strs)

    value = pyqtProperty(str, fget=PyQt52WebValue, fset=Web2PyQt5Value)
