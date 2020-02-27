import numpy as np
import sortedcontainers as st
from classparticle import *
	

box = st.SortedSet()
box.add(1)
box.add(2)

print(box)

for particles in box:

	if (particles != 1):
		print(particles)

box = np.empty(9, dtype=object)

for i in range(9):
	box[i] = elemento()

box.reshape(3,3)

box = np.empty(shape=(2,2), dtype=object)

box2 = box[0:2,0:2]

iden =np.eye(3)

iden2 = iden[0:2,0:2]

print(iden2)

for i in range(3):
	print(i)