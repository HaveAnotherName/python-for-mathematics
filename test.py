import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return x+1/x
x=np.linspace(-1,1,100)
plt.scatter(x,f(x),c='r',s=10)
plt.show()