from classparticle import *
import sortedcontainers as st
import matplotlib.patches as patches

########################################################################################################
#Cuadricula de sets
########################################################################################################

box = np.empty(L*L,dtype = object)

for i in range(L*L):
	box[i] = elemento()

box = box.reshape(L,L)



########################################################################################################
#Inicialización del sistema
########################################################################################################

file   = open("array.txt","w")

system     = np.empty(N, dtype=object)
system_new = np.empty(N, dtype=object)

save       = np.empty(0)

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

		if (accepted): 
			box[x,y].set.add(i)
			save = np.append(save,system[i].x)

save = save.reshape(N,2)
np.savetxt(file,save)

file.close()

########################################################################################################
#Exploracion
########################################################################################################

file  = open("array.txt","r")

for i in range(L):
	for j in range(L):

		if(len(box[i,j].set)>0):
			
			print(box[i,j].set, '[',i,',',j,']')


file.close()

print()


########################################################################################################
#Evolución
########################################################################################################

file = open("evolution.txt","w")

for i in range(time_f):

	for p in range(N):

		x_old = system[p].node[0]
		y_old = system[p].node[1]

		#5x5 sets donde se guardan las partículas que interactúan:
		interact_set = np.empty(shape=(5,5),dtype=object)

		#Busqueda de vecinos:
		for x_rang in range(-2,3):
			for y_rang in range(-2,3):

				x_m = np.mod(x_old + x_rang, L)
				y_m = np.mod(y_old + y_rang, L)
				interact_set[x_rang+2,y_rang+2] = box[x_m,y_m]

		#Evolución del sistema:
		system_new[p] = evolution(system, p, interact_set)

		#Grabamos x,y,t. Reshape para que los grabe como filas:
		save = np.append(system[p].x,np.array([(i+1)*delta_time]) )
		np.savetxt(file, save.reshape(1,3))

		#¿Acutaliza el nodo?¿Hace falta?  
		system[p].nodo()

		x_new = system[p].node[0]
		y_new = system[p].node[1]


		#Acutalizamos los set:
		flag = False
		if ( not (p in box[x_new,y_new].set)):
			box[x_old,y_old].set.discard(p)
			box[x_new,y_new].set.add(p)
			flag = True
		
		if flag:
			print(system[p].x, system[p].node, p)	
	
	#Seteamos system para el próximo loop en t:
	system = system_new			


file.close()



########################################################################################################
#Gráfico
########################################################################################################

grafico  = np.loadtxt('evolution.txt') #evolución 
grafico1 = np.loadtxt('array.txt')     #Cargamos distribución de obstáculos 

fig, ax =plt.subplots()
plt.title("Obstacles configuration") 
plt.xlabel("x axis") 
plt.ylabel("y axis")


########################################################################################################
#Ahora seguimos la evolución de alguna partícula:

for i in range(0,time_f,2):
	
	circ = patches.Circle((grafico[i,0], grafico[i,1]), 1, alpha=0.7, fc='red')
	ax.add_patch(circ)
	circ = patches.Circle((grafico[i+1,0], grafico[i+1,1]), 1, alpha=0.7, fc='blue')
	ax.add_patch(circ)
	

plt.axis('square')

plt.xlim(-1,L+1)
plt.ylim(-1,L+1)

plt.grid(color='b', linestyle='-.', linewidth=0.5)

#plt.plot(grafico[0:,0],grafico[0:,1], "o", color='b')

plt.show()

