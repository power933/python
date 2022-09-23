from sqlite3 import *
from MySQLdb import *
#mysql 연결에 필요한 pip들
#pip install dbconnect
#pip install pysqlite3
#pip install mysqlclient
#pip install pysqlite

connect = connect(
    user = "power933",
    passwd = "so9332650!@",
    host = "umj7-009.cafe24.com",
    db = "power933",
    charset="utf8"
)