import numpy as np
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



# tempo = timeit.timeit("mat_prod(np.random.randint(1, 100,(5,5)), np.random.randint(1, 100,(5,5))),", globals= globals(), number = 100)
# print(tempo)

# tempo = timeit.timeit("mat_dot_prod(np.random.randint(1, 100,(5,5)), np.random.randint(1, 100,(5,5))),", globals= globals(), number = 100)
# print(tempo)

# tempo = timeit.timeit("np.random.randint(1, 100,(5,5))@np.random.randint(1, 100,(5,5))", globals= globals(), number = 100)
# print(tempo)

# data_solve_tridiag = []

sizes = [(5,5), (10,10), (15,15), (450,450), (500,500)]
sizes_long = [(100,400), (50, 500)]
sizes_wide = [(400, 100), (500, 50)]

lim_inf = 25
lim_max = 100
for n in range(lim_inf, lim_max, 25):

    A_rand = np.diag(np.random.rand(n)) + np.diag(np.random.rand(n-1), -1) + np.diag(np.random.rand(n-1), 1)
    b_rand = np.random.rand(n)

    tempos = [timeit.timeit("solve_tridiag(A_rand, b_rand)", globals= globals(), number= 20) for i in range(20)]
    tempo_estavel = min(tempos)

    data_solve_tridiag.append({"size": n, "process_time": tempo_estavel})

df_solve_tridiag = pd.DataFrame(data_solve_tridiag)
df_solve_tridiag.plot(x="size", y="process_time", title="Desempenho")


