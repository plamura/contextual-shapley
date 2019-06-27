from numpy import * 

# 0, i, j, k, ij, ik, jk, ijk
#V = matrix('0 0 0 0 0 0 0 0; 0 100 0 0 0 0 0 0; 0 0 125 0 0 0 0 0; 0 0 0 50 0 0 0 0; 0 0 0 0 270 0 0 0; 0 0 0 0 0 375 0 0; 0 0 0 0 0 0 350 0; 0 0 0 0 0 0 0 500')
#V = matrix('0 0 0 0 0 0 0 0; 0 0 0 0 0 0 0 0; 0 0 125 0 0 0 0 0; 0 0 0 50 0 0 0 0; 0 0 0 0 125 0 0 0; 0 0 0 0 0 50 0 0; 0 0 0 0 0 0 350 0; 0 0 0 0 0 0 0 350')
#t = [0,1,2,3,4,5,6,7]
V = matrix('0 0 0 0 0 0 0 0; 0 100 -10 -10 0 0 -10 0; 0 -10 125 0 0 -10 0 0; 0 -10 0 50 -10 0 0 0; 0 0 0 -10 270 0 0 0; 0 0 -10 0 0 375 0 0; 0 -10 0 0 0 0 350 0; 0 0 0 0 0 0 0 500')
t = [6,1,2,0,5,4,3,7]
#V = matrix('0 0 0 0 0 0 0 0; 0 100 -10 -10 0 0 -10 0; 0 -10 50 0 0 -10 0 0; 0 -10 0 125 -10 0 0 0; 0 0 0 -10 375 0 0 0; 0 0 -10 0 0 270 0 0; 0 -10 0 0 0 0 350 0; 0 0 0 0 0 0 0 500')
#t = [6,1,0,2,4,5,3,7]
#V = matrix('0 0 0 0 0 0 0 0; 0 100 0 -10 0 0 -10 0; 0 0 0 0 0 0 0 0; 0 -10 0 50 -10 0 0 0; 0 0 0 -10 100 0 -10 0; 0 0 0 0 0 375 0 0; 0 -10 0 0 -10 0 50 0; 0 0 0 0 0 0 0 375')
#t = [5,1,4,3,2,6,0,7]

print(V)

TT = identity(8)
TT[:,:] = TT[t,:]

a, H = linalg.eig(V)
J = diag(a)
D = TT.dot(J).dot(TT.T)
G = H.dot(TT.T)

T1 = matrix('0 1 0 0 0 0 0 0; 1 0 0 0 0 0 0 0; 0 0 0 0 1 0 0 0; 0 0 0 0 0 1 0 0; 0 0 1 0 0 0 0 0; 0 0 0 1 0 0 0 0; 0 0 0 0 0 0 0 1; 0 0 0 0 0 0 1 0')
T2 = matrix('0 0 1 0 0 0 0 0; 0 0 0 0 1 0 0 0; 1 0 0 0 0 0 0 0; 0 0 0 0 0 0 1 0; 0 1 0 0 0 0 0 0; 0 0 0 0 0 0 0 1; 0 0 0 1 0 0 0 0; 0 0 0 0 0 1 0 0')
T3 = matrix('0 0 0 1 0 0 0 0; 0 0 0 0 0 1 0 0; 0 0 0 0 0 0 1 0; 1 0 0 0 0 0 0 0; 0 0 0 0 0 0 0 1; 0 1 0 0 0 0 0 0; 0 0 1 0 0 0 0 0; 0 0 0 0 1 0 0 0')

D1 = T1.dot(D).dot(T1.T)
D2 = T2.dot(D).dot(T2.T)
D3 = T3.dot(D).dot(T3.T)

I1 = diag(array([1,0,1,1,0,0,1,0]))
I2 = diag(array([1,1,0,1,0,1,0,0]))
I3 = diag(array([1,1,1,0,1,0,0,0]))

d1 = matrix(diagonal(I1.dot(D1 - D).dot(I1)))
d2 = matrix(diagonal(I2.dot(D2 - D).dot(I2)))
d3 = matrix(diagonal(I3.dot(D3 - D).dot(I3)))

q1 = sqrt((1/6)*matrix('2 0 1 1 0 0 2 0'))
q2 = sqrt((1/6)*matrix('2 1 0 1 0 2 0 0'))
q3 = sqrt((1/6)*matrix('2 1 1 0 2 0 0 0'))

g1 = matrix(square(q1.dot(G)))
g2 = matrix(square(q2.dot(G)))
g3 = matrix(square(q3.dot(G)))

print(d1.dot(g1.T))
print(d2.dot(g2.T))
print(d3.dot(g3.T))


W1 = G.dot(I1).dot(G.T)
W2 = G.dot(I2).dot(G.T)
W3 = G.dot(I3).dot(G.T)

Q1 = G.dot(T1).dot(G.T)
Q2 = G.dot(T2).dot(G.T)
Q3 = G.dot(T3).dot(G.T)

print(q1.dot(W1).dot(Q1.dot(V).dot(Q1) - V).dot(W1).dot(q1.T))
print(q2.dot(W2).dot(Q2.dot(V).dot(Q2) - V).dot(W2).dot(q2.T))
print(q3.dot(W3).dot(Q3.dot(V).dot(Q3) - V).dot(W3).dot(q3.T))


#print(q1.dot(W1).dot(Q1).dot(V).dot(Q1).dot(W1).dot(q1.T) - q1.dot(W1).dot(V).dot(W1).dot(q1.T))
#print(q2.dot(W2).dot(Q2).dot(V).dot(Q2).dot(W2).dot(q2.T) - q2.dot(W2).dot(V).dot(W2).dot(q2.T))
#print(q3.dot(W3).dot(Q3).dot(V).dot(Q3).dot(W3).dot(q3.T) - q3.dot(W3).dot(V).dot(W3).dot(q3.T))
