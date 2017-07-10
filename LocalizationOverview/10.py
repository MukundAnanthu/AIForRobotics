p=[0.2,0.2,0.2,0.2,0.2]
pHit = 0.6
pMiss = 0.2

#Enter code here
for i in range(5):
    if i == 1 or i == 2:
        p[i] = p[i] * pHit
    else:
        p[i] = p[i] * pMiss


print p
