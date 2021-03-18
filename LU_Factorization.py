import scipy as sp
import numpy as np
from scipy import linalg

#Decomposition of A into A = P L U
print("In solving Ax = b, A can be decomposed into LU where;")
A = sp.array([ [9, 3, 2, 0, 7], [7, 6, 9, 6, 4], [2, 7, 7, 8, 2], [0, 9, 7, 2, 2], [7, 3, 6, 4, 3] ])
b = sp.array([35, 58, 53, 37, 39])

print("A is: ")
print(A)

print("b is: ")
print(b)

print("Decomposing A gives: ")
LU, P = sp.linalg.lu_factor(A)

print("LU: ")
print(LU)

print("P: ")
print(P)

print("Solving Ax = b for x we will get: ")
x = sp.linalg.lu_solve((LU, P), b)

print("x: ")

x[0] = 0

print(x)

p, l, u = sp.linalg.lu(A)

print("L is: ")
print(l)

print("U is: ")
print(u)




































