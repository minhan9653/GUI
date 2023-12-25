import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from dlgAddressBook import *
from mySql import *
myDB = mySqlDB

form_mainWin = uic.loadUiType("./res/mainWindow.ui")[0]
class mainWindow(QMainWindow,form_mainWin):
    def __init__(self):
        super().__init__()        
        self.setupUi(self)               
        
        # 메뉴 연결 
        self.actionAddressBook.triggered.connect(self.onActionAddressBook)
    # 메뉴 주소록이 눌렸을대 
    def onActionAddressBook(self):
        retf = dlgAddressBook.launch(None)
        print(retf)      
        if retf : 
            print ("OK")
        else:
            print ("NO")

app = QApplication(sys.argv)
window = mainWindow()
window.show()
sys.exit(app.exec_())