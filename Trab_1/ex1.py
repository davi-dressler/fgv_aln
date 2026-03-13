import numpy as np
import timeit
import random

def mat_prod(A: np.ndarray, B: np.ndarray):
    A_nrow, A_ncol = A.shape
    B_nrow, B_ncol = B.shape
    
    if A_ncol != B_nrow:
        print("Não é possível multiplicar essas matrizes.")
        return
    
    C = np.zeros((A_nrow, B_ncol))
    for i in range(A_nrow):
        for j in range(B_ncol):
            C[i,j] = sum(A[i,k]*B[k,j] for k in range(A_ncol))
    
    return C

def mat_dot_prod(A: np.ndarray, B: np.ndarray):
    A_nrow, A_ncol = A.shape
    B_nrow, B_ncol = B.shape
    
    if A_ncol != B_nrow:
        print("Não é possível multiplicar essas matrizes.")
        return
    
    C = np.zeros((A_nrow, B_ncol))
    for i in range(A_nrow):
        for j in range(B_ncol):
            C[i,j] = np.dot(A[i,:],B[:,j])
    
    return C



tempo = timeit.timeit("mat_prod(np.random.randint(1, 100,(5,5)), np.random.randint(1, 100,(5,5))),", globals= globals(), number = 100)
print(tempo)

tempo = timeit.timeit("mat_dot_prod(np.random.randint(1, 100,(5,5)), np.random.randint(1, 100,(5,5))),", globals= globals(), number = 100)
print(tempo)

tempo = timeit.timeit("np.random.randint(1, 100,(5,5))@np.random.randint(1, 100,(5,5))", globals= globals(), number = 100)
print(tempo)



