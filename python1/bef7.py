from sqlite3 import *
from MySQLdb import *
from dbconnect import *

cur = connect.cursor() #명령어를 입력시키기 위한 대기상태
cur.execute("select * from test3") #execute : 콘솔상태에 문자값을 입력
for a in cur.fetchall(): #fetchall select에 대한 데이터를 문자열형태
    print(a)
cur = connect.cursor()
# cur.execute("insert into test3 values('블라블라')")
sql = "insert into test3 values('0',%s,%s,%s,%s,%s)"
with connect:
    cur.execute(sql,('red','red1234','레드사용자','01045678987','22'))
connect.commit() #이거 안넣으면 안서트 안됨
'''
con = connect("./test.db")
create = con.cursor()
create.execute("create table test(idx int(4) not null, name char(200) not null, primary key(idx)); ")

insert.execute("insert into test values('0','hong');")
'''