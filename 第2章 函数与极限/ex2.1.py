#绘制函数y=|x|的图像
import matplotlib.pyplot as plt

x=[]
y=[]
for i in range(100):
    element=-1+0.02*i
    x.append(element)
    y.append(element if element>0 else -element)
#plt.plot(x,y)
#plt.show()

#另一种方法
import numpy as np
def f(x):
    return np.abs(x)
x=np.linspace(-1,1,100)
plt.plot(x,f(x),'r',linewidth=2) #颜色为红色，线宽为2
plt.show()