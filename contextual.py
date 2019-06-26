from numpy import * 

# 0, i, j, k, ij, ik, jk, ijk
#V = matrix('0 0 0 0 0 0 0 0; 0 100 0 0 0 0 0 0; 0 0 125 0 0 0 0 0; 0 0 0 50 0 0 0 0; 0 0 0 0 270 0 0 0; 0 0 0 0 0 375 0 0; 0 0 0 0 0 0 350 0; 0 0 0 0 0 0 0 500')
#V = matrix('0 0 0 0 0 0 0 0; 0 0 0 0 0 0 0 0; 0 0 125 0 0 0 0 0; 0 0 0 50 0 0 0 0; 0 0 0 0 125 0 0 0; 0 0 0 0 0 50 0 0; 0 0 0 0 0 0 350 0; 0 0 0 0 0 0 0 350')
#t = [0,1,2,3,4,5,6,7]
#V = matrix('0 0 0 0 0 0 0 0; 0 100 -10 -10 0 0 -10 0; 0 -10 125 0 0 -10 0 0; 0 -10 0 50 -10 0 0 0; 0 0 0 -10 270 0 0 0; 0 0 -10 0 0 375 0 0; 0 -10 0 0 0 0 350 0; 0 0 0 0 0 0 0 500')
#t = [6,1,2,0,5,4,3,7]
#z = [3,1,2,6,5,4,0,7]
#V = matrix('0 0 0 0 0 0 0 0; 0 100 -10 -10 0 0 -10 0; 0 -10 50 0 0 -10 0 0; 0 -10 0 125 -10 0 0 0; 0 0 0 -10 375 0 0 0; 0 0 -10 0 0 270 0 0; 0 -10 0 0 0 0 350 0; 0 0 0 0 0 0 0 500')
#t = [6,1,0,2,4,5,3,7]
V = matrix('0 0 0 0 0 0 0 0; 0 100 0 -10 0 0 -10 0; 0 0 0 0 0 0 0 0; 0 -10 0 50 -10 0 0 0; 0 0 0 -10 100 0 0 0; 0 0 0 0 0 375 0 0; 0 -10 0 0 0 0 50 0; 0 0 0 0 0 0 0 375')
t = [4,0,5,3,1,6,2,7]
#V = matrix('0 0 0 0 0 0 0 0; 0 0 1 0 0 0 0 0; 0 1 0 0 0 0 0 0; 0 0 0 0 0 0 0 0; 0 0 0 0 0 0 0 0; 0 0 0 0 0 0 0 0; 0 0 0 0 0 0 0 0; 0 0 0 0 0 0 0 0')

q1 = sqrt((1/6)*matrix('2 0 1 1 0 0 2 0'))
q2 = sqrt((1/6)*matrix('2 1 0 1 0 2 0 0'))
q3 = sqrt((1/6)*matrix('2 1 1 0 2 0 0 0'))

print(V)

a, H = linalg.eig(V)
J = diag(a)

t1 = [1,0,4,5,2,3,7,6]
t2 = [2,4,0,6,1,7,3,5]
t3 = [3,5,6,0,7,1,2,4]

I = identity(8)
I1= I.copy()
I1[:,:]=I1[t1,:]
I2= I.copy()
I2[:,:]=I2[t2,:]
I3= I.copy()
I3[:,:]=I3[t3,:]

D = J.copy()
G = H.copy()
D[:,:] = D[t,:]
D[:,:] = D[:,t]
G[:,:] = G[:,t]

D1 = D.copy()
tt1 = [1,0,4,5,0,0,7,0]
D1[:,:] = D1[tt1,:]
D1[:,:] = D1[:,tt1]

D2 = D.copy()
tt2 = [2,4,0,6,0,7,0,0]
D2[:,:] = D2[tt2,:]
D2[:,:] = D2[:,tt2]

D3 = D.copy()
tt3 = [3,5,6,0,7,0,0,0]
D3[:,:] = D3[tt3,:]
D3[:,:] = D3[:,tt3]

DD1 = maximum((D1-D),0)
d1 = matrix(diagonal(DD1))
g1 = matrix(square(q1.dot(G)))
print(d1.dot(g1.T))

DD2 = maximum((D2-D),0)
d2 = matrix(diagonal(DD2))
g2 = matrix(square(q2.dot(G)))
print(d2.dot(g2.T))

DD3= maximum((D3-D),0)
d3 = matrix(diagonal(DD3))
g3 = matrix(square(q3.dot(G)))
print(d3.dot(g3.T))

Q1VQ1 = G.dot(maximum(I1.dot(G.T).dot(V).dot(G).dot(I1),G.T.dot(V).dot(G))).dot(G.T)
Q2VQ2 = G.dot(maximum(D2,G.T.dot(V).dot(G))).dot(G.T)
Q3VQ3 = G.dot(maximum(D3,G.T.dot(V).dot(G))).dot(G.T)

print(q1.dot(Q1VQ1 - V).dot(q1.T))
print(q2.dot(Q2VQ2 - V).dot(q2.T))
print(q3.dot(Q3VQ3 - V).dot(q3.T))
