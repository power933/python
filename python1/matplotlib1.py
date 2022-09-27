import matplotlib.pyplot as mpt # 그래프 모듈
from matplotlib import font_manager, rc

font = "C:\Windows\Fonts\H2GTRM.TTF"
font = font_manager.FontProperties(fname=font).get_name()
rc('font_text',family=font)

x = [1,3,5]
y = [2,4,6]
#mpt.plot(x,y)
#mpt.show()

data = [1,5,9,10,2]
mpt.plot(data)
mpt.show()

