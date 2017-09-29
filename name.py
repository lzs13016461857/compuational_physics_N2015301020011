import numpy as np
import pylab as pl
inital_v=0
g=9.8
time=10
step=0.05
nsteps=int(time//step+1)
dt=step
def plot():
    v=[inital_v]
    t=[0]
    for i in range(nsteps):
        tmp=v[i]+g*dt
        v.append(tmp)
        t.append(t[i]+dt)   
    pl.plot(t,v)
    pl.title('plot of v vs t')
    pl.xlabel('t(s) axis')
    pl.ylabel('v(m/s) axis')
    pl.xlim(0.0,10)
    pl.ylim(0.00,100.00)
    pl.show()
plot()
