import math

import numpy as np
import random as rnd
import matplotlib.pyplot as plt
from scipy.stats import norm
import normal
import random as rnd
import my_random as rndndn
from printer import print_function



n = 1000
a = 0
b = 100
x = rndndn.normalvariatee(a,b,n)
x = np.sort(x)
#print("Массив случайных значений длинной {} в диапазоне [{}, {}): ".format(n, a, b))
#print(x)
#x = np.sort(x)
#print("Отсортированный массив: ")
#print(x)

# Подсчет среднего арифметического
mu = np.mean(x)
# Подсчет среднего квадратичного отклонения:
# s = sqrt(1/n * sum(ai - avg(a)))
sigma = np.std(x)

#print("mu = {}".format(mu))
#print("sigma = {}".format(sigma))

distribution = normal.normal_distribution(x, mu, sigma)
print_function(x, distribution, x_name="Х", y_name="Плотность", title="Нормальное распределение")

distribution2 = normal.cdf(x,mu,sigma)
#print ((np.abs(normal.cdf(x,mu,sigma)))
#print(norm.cdf(x))
#print (x)
print_function(x, normal.cdf(x,mu,sigma), x_name="Х", y_name="Функция", title="Нормальное распределение")
#cdf с помощью функции
#print_function(x, norm.cdf(x), x_name="Х", y_name="Функция библ", title="Нормальное распределение")
mu, std = norm.fit(x)
# Plot the histogram.
plt.hist(x, bins=100, density=True, alpha=0.6, color='g')
# Plot the PDF.
xmin, xmax = plt.xlim()


plt.plot(x, np.abs(normal.normal_distribution(x, mu, sigma)), 'k', linewidth=1)
title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
plt.title(title)
plt.show()