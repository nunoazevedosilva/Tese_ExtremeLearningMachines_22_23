from scipy import *

def integrate(F,t,y,tstop,dt):

    def runk4(F,t,y,dt):
        K0=dt*F(t,y)
        K1=dt*F(t+dt/2.,y+K0/2.)
        K2=dt*F(t+dt/2.,y+K1/2.)
        K3=dt*F(t+dt,y+K2)
        return (K0 + 2.*K1 + 2.*K2 + K3)/6.0

    T=[]
    Y=[]
    T.append(t)
    Y.append(y)
    while t<tstop:
        #print(str(t) +'//'+str(tstop),end='\r')
        dt=min(dt,tstop-t)
        y=y+runk4(F,t,y,dt)
        t=t+dt
        T.append(t)
        Y.append(y)

    return array(T),array(Y) 

