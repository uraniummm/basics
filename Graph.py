#Submitted by= Nikita Rana

import numpy as np
import matplotlib.pyplot as plt

#Q.1)Plot the function f(x)=sin(x)/x in range [-10,10].
plt.figure(1)
def f(x):
    if x!=0:
        return(np.sin(x))/x
    else:
        return 1

x=np.linspace(-10,10,200)
y=np.linspace(-10,10,200)
i=0
for item in x:
    y[i]=f(x[i])
    i=i+1

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title('Graph of sin x/x')
plt.plot(x,y)

#Q.2)Plot both the functions f1(x)=sin(x)/x and f2(x)=cos(x)/x in the range [-10,10] in the same plot.

plt.figure(2)
x=np.linspace(-10,10,200)
y1=(np.sin(x))/x
y2=(np.cos(x))/x
plt.axis((-10,10,-10,10))
plt.plot(x,y1,'r')
plt.plot(x,y2,'g')
plt.legend(['sin(x)/x and cos(x)/x'])
plt.title('Graph of sin(x)/x and cos(x)/x')

#Q.3)Plot z = f(x,y)= sin(x*y) in the range x=[-5,5] and y=[-5,5]

def zf(x,y):
    return np.sin(x*y)
x1=np.linspace(-5,5,50)
y1=np.linspace(-5,5,50)

plt.figure(3)
X1,Y1= np.meshgrid(x1,y1)
Z1= zf(X1,Y1)
ax= plt.axes(projection='3d')
ax.plot_surface(X1,Y1,Z1,color='red')
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
ax.set_zlim(-5,5)
plt.title('Graph of z=sin(x*y)')
plt.show()
