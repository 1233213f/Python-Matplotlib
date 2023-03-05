# 拟合曲线
import math

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.optimize import leastsq

# 样本数据
# 身高数据
Yi = np.array([18.5, 24.4, 31.0, 2.8, -3])
# 体重数据
Xi = np.array([4.690895705, 5.829204678, 7.331880427, 4.698970004, 0.477121255])


# 需要拟合的函数func（）指定函数的形状
def func(p, x):
    a, b = p
    return a*x + b


# 定义偏差函数，x，y为数组中对应Xi,Yi的值
def error(p, x, y):
    return func(p, x) - y


# 设置k，b的初始值，可以任意设定，经过实验，发现p0的值会影响cost的值：Para[1]
p0 = [5, -8]

# 把error函数中除了p0以外的参数打包到args中,leastsq()为最小二乘法函数
Para = leastsq(error, p0, args=(Xi, Yi))
# 读取结果
a, b = Para[0]
print('a=', a, 'b=', b)

# 画样本点
plt.figure(figsize=(8, 6))
plt.scatter(Xi, Yi, color='red', label='Sample data', linewidth=2)

# 画拟合直线
x = np.linspace(0, 8, 80)
y = a * x + b

# 绘制拟合曲线
plt.plot(x, y, color='blue', label='Fitting Curve', linewidth=2)
plt.legend()  # 绘制图例

plt.xlabel('D(pc)', fontproperties='simHei', fontsize=12)
plt.ylabel('m-M', fontproperties='simHei', fontsize=12)

plt.show()

