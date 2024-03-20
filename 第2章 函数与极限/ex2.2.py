#绘制函数y=sgn x的图像 散点图 多图
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    if x>0:
        return 1
    elif x<0:
        return -1
    else:
        return 0
def part1():
    x = np.linspace(-2, 2, 51)
    y = []
    for i in range(len(x)):
        y.append(f(x[i]))
    plt.plot(x, y, 'g', linewidth=3)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('y=sgn(x)')
    plt.show()

#使用散点函数scatter()函数替代plot()函数
#plot函数实质是把点连成线
#scatter函数生成的是散点图，当点很多时，看起来就是线
def part2():
    x = np.linspace(-2, 2, 201)
    plt.scatter(x, np.sign(x), c='g', s=10)  # s为点的大小
    plt.xlabel('x')  #设置x轴标签
    plt.ylabel('f(x)')  #设置y轴标签
    plt.title('y=sgn(x)')  #设置标题
    plt.show()

#多图 subplots()返回一个包含figure和axes对象的元组，因此，使用fig,ax=将元组分解为fig和ax两个变量
def part3():
    x=np.linspace(0,3,100)
    fig,ax=plt.subplots()   #
    ax.plot(x,x,label='y=x')
    ax.plot(x,x**2,label='y=x^2')
    ax.plot(x,x**3,label='y=x^3')
    ax.legend()  # 显示.plot方法里设置的label值
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('y=f(x)')
    plt.show()

#更多sbuplots()函数的用法
def part4():
    x=np.linspace(-1.9,1.9,100)
    fig,(ax1,ax2,ax3)=plt.subplots(1,3,figsize=(10,6))
    ax1.scatter(x,np.floor(x),s=5)
    ax2.scatter(x,np.round(x),s=5,c='r')
    ax3.scatter(x,np.ceil(x),s=5,c='g')
    plt.show()

part4()