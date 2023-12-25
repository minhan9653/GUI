import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox,QDialog
from mySql import *
from PyQt5.QtWidgets import QTableWidgetItem
myDB = mySqlDB()



form_dlgAddress = uic.loadUiType("./picture/dlgAddressBook.ui")[0]
mTitle = '주소록 연습01'

#수정하는 창이 나오는 클래스
class EditDialog(QDialog):
    def __init__(self, name, phone, address, university, class_name):
        super().__init__()
        uic.loadUi("./picture/update.ui", self)  # update.ui 파일 로드

        self.name = name
        self.phone = phone
        self.address = address
        self.university = university
        self.class_name = class_name

        self.lineEdit.setText(self.name)
        self.lineEdit_4.setText(self.phone)
        self.lineEdit_3.setText(self.address)
        self.lineEdit_2.setText(self.university)
        self.lineEdit_5.setText(self.class_name)

        self.pushButton.clicked.connect(self.accept)
        self.pushButton_2.clicked.connect(self.reject)
        
    def accept(self):
        new_name = self.lineEdit.text() # 수정된 이름 가져오기
        self.phone = self.lineEdit_4.text()
        self.address = self.lineEdit_3.text()
        self.university = self.lineEdit_2.text()
        self.class_name = self.lineEdit_5.text()
        super().accept()
        self.name = new_name

    @staticmethod
    def launch(parent=None, name="", phone="", address="", university="", class_name=""):
        dlg = EditDialog(name, phone, address, university, class_name)
        r = dlg.exec_()
        if r == QDialog.Accepted:
            return dlg.name, dlg.phone, dlg.address, dlg.university, dlg.class_name
        else:
            return None

#전체보기 창이 나오는 클래스
class View(QDialog):
    def __init__(self, records):
        super().__init__()
        uic.loadUi("./picture/view.ui", self)  # view.ui 파일 로드
        
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["이름", "전화번호", "주소", "대학", "학과"])
        self.tableWidget.setRowCount(len(records))
        
        row = 0
        for record in records:
            self.tableWidget.setItem(row, 0, QTableWidgetItem(record["name"]))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(record["phone"]))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(record["address"]))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(record["university"]))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(record["class"]))
            row += 1


        
        self.pushButton_3.clicked.connect(self.onpushButton3clicked)
    
    

    #수정 버튼 활성화시키는 함수
    def onpushButton3clicked(self):
        global myDB
        row = self.tableWidget.currentRow()  # 선택한 행의 인덱스 가져오기
        if row == -1:  # 선택한 행이 없으면
            QMessageBox.warning(self, '주소록 수정', '수정할 항목을 선택해주세요.')
            return

        name = self.tableWidget.item(row, 0).text()
        phone = self.tableWidget.item(row, 1).text()
        address = self.tableWidget.item(row, 2).text()
        university = self.tableWidget.item(row, 3).text()
        class_name = self.tableWidget.item(row, 4).text()

        # 다이얼로그 띄우기
        values = EditDialog.launch(self, name, phone, address, university, class_name)
        if values is not None:  # 저장 버튼이 눌렸을 경우
            new_name, new_phone, new_address, new_university, new_class = values
            myDB.update(new_name, new_phone, new_address, new_university, new_class, name)
            self.refresh_table()  # 테이블 위젯 업데이트

    def refresh_table(self):
        global myDB
        records = myDB.selectAll()
        self.tableWidget.setRowCount(len(records))
        row = 0
        for record in records:
            self.tableWidget.setItem(row, 0, QTableWidgetItem(record["name"]))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(record["phone"]))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(record["address"]))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(record["university"]))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(record["class"]))
            row += 1



#입력등을 하는 맨 처음 창이 나오는 클래스
class dlgAddressBook(QDialog,form_dlgAddress):    
    def __init__(self,parent):
        super().__init__()        
        self.setupUi(self)
        # 윈도우 타이틀 입력
        self.setWindowTitle(mTitle)
        
        
        # 해당 버튼을 눌렀을때 컨트롤할 함수를 지정함.
        self.pushButton_1.clicked.connect(self.onpushButtonclicked)
        self.pushButton_4.clicked.connect(self.onpushButton4clicked)
        self.pushButton_5.clicked.connect(self.onpushButton5clicked)

    #입력 버튼 활성화시키는 함수
    def onpushButtonclicked(self):
        global myDB
        name = self.lineEdit.text()
        phone = self.lineEdit_4.text()
        address = self.lineEdit_3.text()
        university = self.lineEdit_2.text()
        class_name = self.lineEdit_5.text()
        result = myDB.insert(name, phone, address, university, class_name)
        print(result)
        retf = QMessageBox.question(self,'주소록 입력','저장하시겠습니까?') 
        print(retf)      
        if retf == QMessageBox.Yes : 
            QMessageBox.information(self,'주소록 입력','저장되었습니다.')                   
            self.accept()
        else:
            QMessageBox.warning(self,'주소록 입력','취소되었습니다.')       
            self.reject()


    #찾기 버튼 활성화시키는 함수
    def onpushButton4clicked(self):
        global myDB
        result = myDB.search(self.lineEdit.text())
        if len(self.lineEdit.text()) < 1:
            QMessageBox.warning(self, '주소록 찾기', '이름을 최소 1글자 이상 입력하세요')
        elif result:
            result_view = View(result)
            result_view.exec_()
        else:
            print("찾는 정보가 없습니다.")


    #전체보기 버튼 활성화시키는 함수
    def onpushButton5clicked(self):
        global myDB
        result = myDB.view()
        if result:
            print("주소록 전체 내용:")
            result_view = View(result)
            result_view.exec_()
        else:
            print("주소록이 비어 있습니다.")


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