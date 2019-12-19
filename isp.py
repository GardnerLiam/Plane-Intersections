import numpy as np
from fractions import Fraction
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D

def printPlane(p, name='plane', alt=False):
    if (not alt):
        print('{}: {}x + {}y + {}z = {}'.format(name, p[0], p[1], p[2], p[3]))
    else:
        print('{}x + {}y + {}z = {}'.format(p[0], p[1], p[2], p[3]))


def plot(P, ax):
    X = np.outer(np.linspace(-100,100,200), np.ones(200))
    Y = np.copy(X).T
    Z = (P[3] -X*P[0] -Y*P[1])/P[2]
    ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

def T(v):
    r0 = np.random.randint(1,6)
    r1 = np.random.randint(1,6)
    return [-v[1]*r0 - v[2]*r1, v[0]*r0, v[0]*r1]

def Point(V, P, R):
    den = (V[1]-P[1])*(V[2]*P[0] - V[0]*P[2])
    x = Fraction((2*V[1]*V[2] - 3*P[1]*V[2] + P[1]*P[2]),den)
    y = Fraction(1, V[1]-P[1])
    z = Fraction(-2*V[0]*V[1] + 3*V[0]*P[1] - P[0]*P[1], den)
    return (x,y,z)

def Line(R):
    return [Fraction(2*R[1] - R[2], R[0]), -2, 1]

def testLine(line, P):
    points = np.array(line)
    points2 = np.array(line)*3
    print(np.dot(P[:-1], points), np.dot(P[:-1], points2))

def getPrimes(n):
    primes = []
    for j in range(2,n+1):
        add = True
        for i in range(2,int(n**0.5)+1):
            if j%i == 0 and i != j:
                add = False
        if add:
            primes.append(j)
    return primes


fig = plt.figure()
ax = Axes3D(fig)


primes = getPrimes(10)



starting_index = np.random.randint(0, len(primes)-3)

V = [primes[starting_index], primes[starting_index+1], primes[starting_index+2]]
P = T(V)
R = [V[0], P[1], V[2]]
Q = [R[0], R[1]+1, R[2]+2]
K = T(np.cross(R,Q))
L = K[:]

V.append(1)
P.append(2)
R.append(0)
Q.append(0)
K.append(0)
L.append(1)

printPlane(V, 'V', alt=True)
printPlane(P, 'P', alt=True)
printPlane(R, 'R', alt=True)
printPlane(Q, 'Q', alt=True)
printPlane(K, 'K', alt=True)
printPlane(L, 'L', alt=True)

pt = Point(V,P,R)
ln = Line(R)
sln = [str(i) for i in ln]

print(tuple([str(i).replace("'", "") for i in pt]))
print("t{}".format(sln).replace("'", ""))

#plot(V, ax)
#plot(P, ax)
#plot(R, ax)
#plot(Q, ax)
#plot(K, ax)
#plot(L, ax)

#plt.show()
