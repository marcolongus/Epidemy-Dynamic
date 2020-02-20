import numpy as np
import matplotlib.pyplot as plt

L=100
infinity = 10000000000000000
N=100

delta_time = 0.1

active_vel= 0.1
gamma_friction = 3.92*active_vel
radius =1.
diamater = 2*radius

class Particle(object):

#Métodos
	
	def __init__(self,x=np.zeros(2),angle=0,velocity=active_vel, node=np.zeros(2)):

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

	#dis = np.sqrt((np.squre(dy).sum()))

	#if (dis <= diameter):
		#inter = True
	#else:
		#inter = False
			
	return dy


def field(system=np.array, part_index=int, dtype=np.object):
	
	potencial = np.zeros(2)
	campo = np.zeros(2)

	#Loop sobre todas las partículas que interactúa:
	for i in range(system.size-1):
		dx = dx_distance(system[part_index],system[i])

		distance = np.square(dx).sum()
		distance = np.sqrt(distance)

		potencial += np.power(distance,-3)*dx

	potencial = gamma_friction*potencial

	#Calculo del campo resultante
	field = np.array([np.cos(system[part_index].angle), np.sin(system[part_index].angle)])
	field *=active_vel
	field +=potencial 

	return field

def evolution(system=np.array, index=int, inter=bool):

	A = system[index]

	if inter:
		A.x += delta_time*field(system, index)
	
	else:
		vel = active_vel*np.array([np.cos(system[index].angle), np.sin(system[index].angle)])		
		A.x += delta_time*vel


	return A


#########################################################################


A = create_particle()
B = create_particle()

A.x = np.array([1.,1.])
B.x = np.array([1.,1.1])

system = np.array([A,B])

print(system[1].x)

file = open("array.txt","r+")
for i in range(3):

	system[1]=evolution(system,1)
	print(system[1].x)

	np.savetxt(file,system[1].x)

file.close()
	



