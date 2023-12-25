import sys
import pymysql.cursors

class mySqlDB():
    def __init__(self):
        pymysql.version_info = (1,0,2,'final',0)
        pymysql.install_as_MySQLdb()
        super().__init__()

        self.connection = pymysql.connect(
            host='218.237.147.91',
            user='iyrc', 
            passwd='Dodan1004!',              
            db='ROBOT_CLASS_2023',
            charset='utf8',    
            port = 3307,
            cursorclass=pymysql.cursors.DictCursor)

    def search(self, key):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM ADDRESSBOOK WHERE name LIKE %s"
            key = '%' + key + '%'
            cursor.execute(sql, (key,))
            result = cursor.fetchall()
            return result
        
    def insert(self, name, phone, address, university, class_name):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO ADDRESSBOOK (name, phone, address, university, class) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (name, phone, address, university, class_name))
            self.connection.commit()
            return True
        
    def delete(self, name):
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM ADDRESSBOOK WHERE name LIKE %s;"
            cursor.execute(sql, name)
            self.connection.commit()
            return True

    def update(self, new_name, phone, address, university, class_name, name):
        with self.connection.cursor() as cursor:
            sql = "UPDATE ADDRESSBOOK SET name = %s, phone = %s, address = %s, university = %s, class = %s WHERE name LIKE %s;"
            cursor.execute(sql, (new_name, phone, address, university, class_name, name))
            self.connection.commit()
            return True
        
    def view(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM ADDRESSBOOK"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def selectAll(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM ADDRESSBOOK"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result