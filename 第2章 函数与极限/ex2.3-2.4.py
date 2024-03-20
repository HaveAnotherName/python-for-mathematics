#x^3与x^(1/3)的图像 双曲函数图像
import numpy as np
import matplotlib.pyplot as plt

def part1():
    def f(x):
        return np.power(x,3)
    x=np.linspace(-1,1)
    fig,ax=plt.subplots()
    plt.axis('equal')  #设置等比例缩放
    ax.plot(x,f(x),label='y=x^3')
    ax.plot(f(x),x,label='y=x^(1/3')
    ax.plot(x,x,label='y=x')
    ax.legend()
    plt.show()

def part2():
    x=np.linspace(-2,2)
    fig,ax=plt.subplots()
    ax.plot(x,np.sinh(x),label='y=sinh(x)')
    ax.plot(x,np.cosh(x),label='y=cosh(x)')
    ax.plot(x,np.tanh(x),label='y=tanh(x)')
    ax.legend()
    plt.show()

part2()