import numpy as np

L=100
infinity = 10000000000000000
N=100

active_vel= 0.1
gamma_friction = 3.92*active_vel

class Particle(object):

#Métodos
	
	def __init__(self,x=np.zeros(2),angle=0,velocity=0, node=np.zeros(2)):

		self.x = x		
		self.angle = angle
		self.velocity = velocity
		self.node = x.astype(int)

#Funciones

def print_particle(A=Particle, optional=False):
	print(A.x)
	if optional:
		print(x.node,A.angle,A.velocity)

def create_particle():
	A = Particle(np.random.uniform(size=2)*L,np.random.uniform())
	return A

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

def dx_distance(A=Particle,B=Particle):
	
	res = infinity
	dy = np.zeros(2)
	res_x = infinity
	res_y = infinity
	dx=np.zeros(shape=(3,2))

	for i in range(-1,2):
		x  = A.x + i*L		
		dx[i+1] = x - B.x

		if ( np.abs(dx[i+1][0]) < res_x ):
			dy[0]=dx[i+1][0]
			res_x=abs(dy[0])

		if ( np.abs(dx[i+1][1]) < res_y ):
			dy[1]=dx[i+1][1]
			res_y=abs(dy[1])	

	return dy


def field(system=np.array, part_index=int, dtype=np.object):
	print(system[0].x,system[1].x)

	potencial = np.zeros(2)
	campo = np.zeros(2)

	for i in range(system.size-1):
		dx = dx_distance(system[part_index],system[i])

		distance = np.square(dx).sum()
		distance = np.sqrt(distance)
		print(distance)
		potencial += np.power(distance,-3)*dx

	potencial = gamma_friction*potencial

	field = np.array([np.cos(system[part_index].angle), np.sin(system[part_index].angle)])
	field *=active_vel
	field +=potencial 

	print(field)
	return field


#########################################################################


A = create_particle()
B = create_particle()

A.x = np.array([1.,1.])
B.x = np.array([1.,1.1])

system = np.array([A,B])

field(system,1)


