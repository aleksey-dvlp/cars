# N cars, v = 1 km/s  , L = 1 km
#how much time to go away from the road
from random import *
import numpy as np
import matplotlib.pyplot as plt

N = 20
L = 1.0
x = []
#get initial positions
for i in range(N):
    x.append(random())
x.sort()

print (x)
#get initial velocities and its directions
v = []
for i in range(N):
    v.append(1.0)

#get random directions
for i in range(N):
    r = random()
    if r>0.5:
        v[i] = -v[i]

T = 1.
dt = 1.0/60.0/60.0
xnew = []
xnew1 = []
for i in range(N):
    xnew.append(0.0)  #just to initialize xnew
    xnew1.append(0.0)

xcar = []
for i in range(N):
    xcar.append([])

left = [] #to draw boundaries
right = []
    
time = []
    
print('   start time loop   ')
for t in np.arange(dt,T,dt):

    time.append(t)
    left.append(0.0)
    right.append(1.0)

    for i in range(N):
        xnew[i] = x[i] + v[i]*dt


    j = []
    for i in range(N):
        if i == 0:
            if xnew[0] > xnew[1]:
                xnew1[0] = x[0]
                v[0] = -v[0]
                j.append(i)
        elif i==N-1:
            if xnew[N-1]<xnew[N-2]:
                xnew1[N-1] = x[N-1]
                v[N-1] = -v[N-1]
                j.append(i)
        else:
            if xnew[i] > xnew[i+1] or xnew[i] < xnew[i-1]:
                xnew1[i] = x[i]
                v[i] = -v[i]
                j.append(i)

    for i in range(len(j)):
        xnew[j[i]] = xnew1[j[i]]
            
        

    
                
    for i in range(N):
        x[i] = xnew[i]
        xcar[i].append(x[i])

    
        
    print('--------', t)
    print(x)

for i in range(N):
    plt.plot(xcar[i], time)


plt.xlabel('position on the road (a coordinate), km')
plt.ylabel('time, min')
plt.plot(left, time, color='black')
plt.plot(right, time, color = 'black')



plt.show()
