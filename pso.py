from random import *
import math
def particles():
    
    a=[]
    for i in range(0,10):
        a.append(uniform(-5,5))
    print('particles:',a)
    return a
def fitness(a):
    b=[]
    for i in a:
        x=(3*i)-2
        if x>=0:
            b.append(x)
        else:
            b.append(-x)
    print('fitness:',b)
    return(b)
def one_fitness(a):
    x=(3*a)-2
    if x>=0:
        x=x
    else:
        x=-x
    return x
    
v=[0,0,0,0,0,0,0,0,0,0]
iteration=0
particle=particles()
fitnes=fitness(particle)
pbest=particle
fitbest=fitnes
fit_gbest=min(fitnes)
index_gbest=fitnes.index(fit_gbest)
gbest=particle[index_gbest]
print('1.',gbest)
print(fit_gbest,' , ',index_gbest)
while(fit_gbest>0.05 and iteration<900):
    for t in range(0,10):
        v[t]=v[t]+(2*random()*(pbest[t]-particle[t]))+(2*random()*(gbest-particle[t]))
        particle[t]=particle[t]+v[t]
        fitnes[t]=one_fitness(particle[t])
        if fitnes[t]<fit_gbest:
            fitbest[t]=fitnes[t]
            pbest[t]=particle[t]
    x=min(fitbest)
    x_index=fitbest.index(x)
    if x<fit_gbest:
        fit_gbest=x
        gbest=particle[x_index]
    iteration+=1
print('fitnes gbest',fit_gbest)
print('gbest',gbest)
print('iteration:',iteration)        
    
