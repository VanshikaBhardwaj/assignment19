#Question 1

import numpy as np
a=np.random.random((10,1))
x=a.sum()
print(a)
avg=x/len(a)
print(avg)

#Question 2

print "Standard deviation:",np.std(a)
print "Variance",np.std(a)**2

#Question 3

A=np.random.random((10,20))
B=np.random.random((20,25))
C=A.dot(B)
print("C: ",C)
print("Sum of elements of C Matrix:",C.sum())

#Qustion 4
exp = 2.718
def f(x):
    return 1/(1 + exp**(-x)) 
A=np.random.random((10,1))
B=np.random.random((10,1))
for i in range(0,10):
    x=f(A[i,0])
    B[i,0]=x
print "B:",B