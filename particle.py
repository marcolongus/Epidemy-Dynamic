#training set: particle moving through obstacles

import numpy as np

def f(x,a):
	f = 3*a
	return f

print (f(np.ones(3)))

a = 3


''' No sé si irá a  servir: 
def particle_distance(A=Particle,B=Particle):

	res = infinity
	x1 = np.zeros(2)
	for i in range(-1,2):
		for j in range(-1,2):

			x1[0] = A.x[0] + i*L
			x1[1] = A.x[1] + j*L

			x_dif = x1-B.x 

			res = min(res, np.square(x_dif).sum())

	return np.sqrt(res)
'''
