
import numpy as np

#matriks
A = [[1,-2,1,0], 
     [0,2,-8,8], 
     [5,0,-5,10]]
print("A12:", A[0][1], "A32 :", A[2][1])

#persamaan linier
def findSol(a,b):
    sol = np.linalg.solve(a,b)
    return sol
X = [[1,-2,1], 
     [0,2,-8], 
     [5,0,-5]]
res = [0,8,10]
print("The Solutions: ", findSol(X,res))

#diagonal matriks


#soal latihan 1
A = np.array([[0,1,-4],[2,-3,2],[4,-8,12]])
B = np.array([8,1,1])
print("The Solutions:", findSol(A,B)) 