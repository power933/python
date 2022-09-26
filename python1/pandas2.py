import pandas as pd
data = {
    'area' : ['서울','경기도','제주도'],
    'gas' : [1150,1200,980],
    'diesel' : [1860,1845,1998],
    'gasoline' : [1750,1700,1810],
    "ev" : [173.8,170,158.4]
}
pr = pd.DataFrame(data)
pr.index.name = '각 지역별 유가'
#pr.to_csv('opinet.csv',encoding='euc-kr')
pr.to_csv('data.txt',encoding='euc-kr')

#data2 = pd.read_csv('ori.csv', encoding='euc-kr')
#print(data2)

#pr.to_excel("data.xlsx",index=False)