import pandas as pd
from idlelib.iomenu import encoding
data = pd.read_csv("area.csv",encoding="euc-kr")
#print(data)
#print(data.describe()) #.describe() 다양한 산술(평균,최대,최소,카운트 등등)을 뽑아냄
#print(data.loc[[0,1],"휘발유"])
#print(data.loc[[0,1],["휘발유","경유"]])
filter2 = data.loc[(data["휘발유"]<=1900 & (data["지역"]=="부산"))]
#print(filter2)
filter3 = data.loc[(data["휘발유"]<1700) & (data["지역"]=="서울")]
#print(filter3)

#print(data.sort_values("휘발유",ascending=False))
#print(data["경유"].sort_values(ascending=False))

#print(data.replace({"서울":"서울특별시","부산":"부산광역시"}))

def add_liter(z) :
    return str(z) +"L"

#data["휘발유"] = data["휘발유"].apply(add_liter)
#print(data)

def add_literck(k) :
    if k > 1100:
        return str(k)+"L"
    return str(k)

data["휘발유"] = data["휘발유"].apply(add_literck)
print(data["휘발유"])