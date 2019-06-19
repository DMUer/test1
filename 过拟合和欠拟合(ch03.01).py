import matplotlib.pyplot as plt
import numpy as np

n_dots = 20

x = np.linspace(0, 1, n_dots)                   # [0, 1] 之间创建 20 个点
y = np.sqrt(x) + 0.2*np.random.rand(n_dots) - 0.1;   #(根号2)+r,r=[-0.1,0.1]
def plot_polynomial_fit(x, y, order):
    p = np.poly1d(np.polyfit(x, y, order))  #poly1d是用来构造多项式的函数，polyfit是用来拟合的函数

    # 画出拟合出来的多项式所表达的曲线以及原始的点
    t = np.linspace(0, 1, 200)  #生产等差数列
    plt.plot(x, y, 'ro', t, p(t), '-', t, np.sqrt(t), 'r--')  
	#ro代表红实心点，-为蓝色线,r--为红色线段,p(t)代表x=t时的函数值
    return p
	
plt.figure(figsize=(18, 4))  #plt.figure()设置画布
titles = ['Under Fitting', 'Fitting', 'Over Fitting']
models = [None, None, None]
for index, order in enumerate([1, 3, 10]):
    plt.subplot(1, 3, index + 1)          #subplot(‘行’，‘列’，‘编号’)
    models[index] = plot_polynomial_fit(x, y, order)    #构造了三个函数，放在models列表里
    plt.title(titles[index], fontsize=20)  #


for m in models:
    print('model coeffs: {0}'.format(m.coeffs))
# 针对一阶多项式的模型，不同的参数拟合出来的直线和训练样本对应的位置关系
coeffs_1d = [0.2, 0.6]

plt.figure(figsize=(9, 6))
t = np.linspace(0, 1, 200)
plt.plot(x, y, 'ro', t, models[0](t), '-', t, np.poly1d(coeffs_1d)(t), 'r-')
plt.annotate(r'L1: $y = {1} + {0}x$'.format(coeffs_1d[0], coeffs_1d[1]),
             xy=(0.8, np.poly1d(coeffs_1d)(0.8)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate(r'L2: $y = {1} + {0}x$'.format(models[0].coeffs[0], models[0].coeffs[1]),
             xy=(0.3, models[0](0.3)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))


plt.figure()函数操作			 
	figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True)

	num:图像编号或名称，数字为编号 ，字符串为名称
	figsize:指定figure的宽和高，单位为英寸；
	dpi参数指定绘图对象的分辨率，即每英寸多少个像素，缺省值为80      1英寸等于2.5cm,A4纸是 21*30cm的纸张 
	facecolor:背景颜色
	edgecolor:边框颜色
	frameon:是否显示边框
