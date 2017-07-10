p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
	q = []
	for i in range(len(p)):
	    if world[i] == 'green':
	        q.append(p[i]*pMiss)
	    else:
	        q.append(p[i]*pHit)
	return q
