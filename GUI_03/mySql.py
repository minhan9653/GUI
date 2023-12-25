import sys
import pymysql.cursors
class mySqlDB():
    def __init__(self):
        global DBconnection

        pymysql.version_info = (1,4,2,'final',0)
        pymysql.install_as_MySQLdb()
        super().__init__()

        DBconnection = pymysql.connect(
            host='218.237.147.91',
            user='iyrc', 
            passwd='Dodan1004!',              
            db='ROBOT_CLASS_2023',
            charset='utf8',    
            port = 3307,
            cursorclass=pymysql.cursors.DictCursor)
        
    def search(self,key):
        with DBconnection.cursor() as cursor:
            sql = "SELECT * FROM ADDRESSBOOK WHERE name Like %s"
            key = '%'+key+'%'
            cursor.execute(sql,key)
            result = cursor.fetchone()
            return result



