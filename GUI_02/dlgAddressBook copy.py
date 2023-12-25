import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox,QDialog


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
        
        # 입력 버튼을 눌렀을때 컨트롤할 함수를 지정함.
        self.pushButton_1.clicked.connect(self.onpushButtonclicked)
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
    window = dlgAddressBook()
    window.show()
    sys.exit(app.exec_())