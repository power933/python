import pandas as pd
from sqlite3 import *
from dbconnect import *

sqlin = connect.cursor()
sqlin.execute("select * from test3")
#for data in sqlin.fetchall():
    #print(data)
sql = "select * from test3"
data = pd.read_sql_query(sql,connect)
#print(data.drop(columns="mpw"))
data = data[["mid","mnm","mage"]]
#print(data)
#r:기존 데이터를 삭제사고 새롭게 저정하게 하는 속성값
data.to_csv(r"test3.csv",encoding="euc-kr")