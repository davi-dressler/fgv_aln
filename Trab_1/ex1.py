import numpy as np
import time
import timeit
import random

#-------------------------------------------------- QUESTÃO 1 - LETRA A --------------------------------------------------
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

#-------------------------------------------------- QUESTÃO 1 - LETRA C --------------------------------------------------
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



# APÊNDICE

# Função usada para calcular os tempos
def benchmark(func, *args, num_times = 2):
    for i in range(2):
        func(*args)
    
    arr = np.zeros(num_times)
    
    for i in range(num_times):
        initial_time = time.perf_counter()
        func(*args)
        final_time = time.perf_counter()
        
        arr[i] = final_time - initial_time
        
    min = arr.min()
    
    return min

sizes = [(5,5), (10,10), (15,15), (450,450), (500,500)]
sizes_long = [(100,400), (50, 500)]
sizes_wide = [(400, 100), (500, 50)]


for size in sizes:

    tempo_estavel = benchmark(mat_prod, np.random.randint(1, 100, size), np.random.randint(1, 100, size))
    print(tempo_estavel)
    


