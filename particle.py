from classparticle import *
import sortedcontainers as st
import matplotlib.patches as patches


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

		accepted = True
		system[i]= create_particle()

		x = system[i].node[0]
		y = system[i].node[1]

		
		for x_rang in range(-2,3):
			for y_rang in range(-2,3):

				x_m = np.mod(x + x_rang, L)
				y_m = np.mod(y + y_rang, L)

				if (len(box[x_m, y_m].set)>0):

					for elem in box[x_m, y_m].set:
						if ( dx_distance(system[i],system[elem])[2] < diameter ): 
							accepted = False

		if (accepted): box[x,y].set.add(i)




#Exploracion

file  = open("array.txt","w")

save = np.empty(0)

for i in range(L):
	for j in range(L):

		if(len(box[i,j].set)>0):
			
			print(box[i,j].set, '[',i,',',j,']')

			for elem in box[i,j].set:
				save = np.append(save,system[elem].x)

save = save.reshape(N,2)
np.savetxt(file,save)

file.close()


#Gráfico

grafico = np.loadtxt('array.txt')

fig, ax =plt.subplots()

for i in range(N):
	circ = patches.Circle((grafico[i,0], grafico[i,1]), 1, alpha=0.7, fc='red')
	ax.add_patch(circ)

plt.title("Obstacles configuration") 
plt.xlabel("x axis") 
plt.ylabel("y axis")

plt.axis('square')

plt.xlim(-1,L+1)
plt.ylim(-1,L+1)


plt.grid(color='b', linestyle='-.', linewidth=0.5)

plt.plot(grafico[0:,0],grafico[0:,1], "o", color='b')

plt.show()



'''
#Evolución

file = open("array.txt","w")

for i in range(15):

	system[1] = evolution(system,1)
	save = np.append(system[1].x,np.array([i*delta_time]) )
	np.savetxt(file, save.reshape(1,3))
	
file.close()
'''


'''
#Gráfico

grafico = np.loadtxt('array.txt')

obstaculo = system[0].x.reshape(1,2)


plt.title("Trayectory") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption")
plt.xlim(-10,10)
plt.ylim(-10,10)

plt.plot(grafico[0:,0],grafico[0:,1],"o", color='r')
plt.plot(obstaculo[0:,0], obstaculo[0:,1],"o") 
plt.show()		
'''


'''
A = create_particle()
B = create_particle()

A.x = np.array([1.,2.])
B.x = np.array([1.,1.])

system = np.array([A,B])

'''