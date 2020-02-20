#training set: particle moving through obstacles

import numpy as np

# System Parameters

N = 50
L = 70

# Particle parameter

active_vel= 0.1

radius = 1.
diameter = 2*radius
alpha_rot = 100.


beta = 1 
gamma_friction = 3.92*active_vel

dos_Pi = 2*np.pi

def distance(A=Particle,B=Particle):

	res = 0.
	for i in range(-1,2):
		for j in range(-1,2):
			x1 = A.x + i*L
			y1 = A.x + j*L 


			res = np.minimun( res,  )