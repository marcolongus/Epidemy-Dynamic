from classparticle import *
import sortedcontainers as st


#Cuadricula de sets

box = np.empty(L*L,dtype = object)

for i in range(L*L):
	box[i] = elemento()

box = box.reshape(L,L)


#Inicialización del sistema

system = np.empty(N, dtype=object)

for i in range(N):
	
	accepted=False

	while (not accepted):

		print(i)
		accepted = True
		system[i]= create_particle()
		box[system[i].node[0],system[i].node[1]].set.add(i)

		inter_set = st.SortedSet()

		for x_rang in range(-2,3):
			for y_rang in range(-2,3):

				if (len(box[ np.mod(system[i].node[0] + x_rang,L) , np.mod(system[i].node[1] + y_rang,L) ].set)>0):
					accepted = False


#Exploracion

for i in range(L):
	for j in range(L):
		if(len(box[i,j].set)>0):
			print(box[i,j].set, '[',i,',',j,']')





'''
A = create_particle()
B = create_particle()

A.x = np.array([1.,2.])
B.x = np.array([1.,1.])

system = np.array([A,B])

#Evolución

file = open("array.txt","w")

for i in range(15):

	system[1] = evolution(system,1)
	save = np.append(system[1].x,np.array([i*delta_time]) )
	np.savetxt(file, save.reshape(1,3))
	
file.close()
'''