import random

import numpy as np
def normal_distribution(x, mu, sigma):
	f = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * np.power((x - mu) / sigma, 2))
	return f

def erf(x):
	from scipy import integrate
	def f(u):
		return np.exp(-u**2)

	v, err = integrate.quad(f, 0, x.all())
	return (2/np.sqrt(np.pi))*v
def cdf(x, mu, sigma):
	#return ((1/sigma*np.sqrt(2*np.pi))*(1+erf((x-mu)/(sigma*np.sqrt(2)))))
	#return np.cos(1/(1/np.exp(-x**2)*(-1)))

	#return erf(x)*normal_distribution(x, mu, sigma)
	return np.cumsum(normal_distribution(x,mu,sigma))
