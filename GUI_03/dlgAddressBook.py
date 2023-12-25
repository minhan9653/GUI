import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox,QDialog
from mySql import *
myDB = mySqlDB()
form_dlgAddress = uic.loadUiType("./res/dlgAddressBook.ui")[0]
mTitle = '주소록 연습01'
class dlgAddressBook(QDialog,form_dlgAddress):    
    def __init__(self,parent):
        super().__init__()        
        self.setupUi(self)
        # 윈도우 타이틀 입력
        self.setWindowTitle(mTitle)
        # 맴버 label_2의 Test를 바꿈
        self.label_2.setText('핸폰')

        #이유 없이 추가 했음
        print ('진자 이유 없이 뭐가 다른지 보기 위해서')
        
        # 입력 버튼을 눌렀을때 컨트롤할 함수를 지정함.
        self.pushButton_1.clicked.connect(self.onpushButtonclicked)
        self.pushButton_4.clicked.connect(self.onpushButton4clicked)

    def onpushButton4clicked(self):
        global myDB
        if self.lineEdit.text() < 'a' :
            QMessageBox.warning(self,'주소록 찾기','이름을 최소 1글자 이상 입력하세요')       
        else:
            result = myDB.search(self.lineEdit.text())
            print (result)
        print ('전체보기')

    # 입력 버튼이 눌렸을 때 
    def onpushButtonclicked(self):
        retf = QMessageBox.question(self,'주소록 입력','저장하시겠습니까?') 
        print(retf)      
        if retf == QMessageBox.Yes : 
            QMessageBox.information(self,'주소록 입력','저장되었습니다.')                   
            self.accept()
        else:
            QMessageBox.warning(self,'주소록 입력','취소되었습니다.')       
            self.reject()
    @staticmethod
    def launch(parent):
        dlg = dlgAddressBook(parent)
        r = dlg.exec()
        if r : 
            return True
        return False
    def showModal(self):
            return False 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = dlgAddressBook(None)
    window.show()
    sys.exit(app.exec_())