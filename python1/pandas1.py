import pandas as pd
data = pd.Series([10,20,30,40])
#servies로 배열값을 로드(인덱스를 자동으로 설정)
print(data)

data2 = pd.Series([17,19,20,17,16,15,16], index=['토','일','월','화','수','목','금'])
print(data2['토'])
array = {
    "username" : ['홍길동','이순신','강감찬'],
    "userage" : ['20','36','44'],
    "usercp" : ['SKT','KT','LG']
}
pr = pd.DataFrame(array,index=['no1','no2','no3'])
print(pr)
pr2 = pd.DataFrame(array,columns=['usercp','username','userage'])
print(pr2)