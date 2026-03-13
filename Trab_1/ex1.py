import numpy as np
import timeit

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
            C[i,j] = np.dot(A[i],B[j])
    
    return C

def solve_tridiag(A):
    A_orig = A.copy()
    A_nrow, A_ncol = A.shape
    ident = np.identity(A_nrow)
    
    for i in range(A_nrow-1):
        t = A[i,i]/A[i+1,i]
        A[i+1] = A[i] - t*A[i+1]
        ident[i+1] = ident[i] - t*ident[i+1]
    
    print(A)
    
    for i in range(1,A_nrow):
        t = A[i-1,i]/A[i,i]
        A[i-1,i] = A[i-1,i] - t*A[i,i]
        ident[i-1] = ident[i-1] - t*ident[i,i]
    
    for i in range(A_nrow):
        t = 1/A[i,i]
        A[i,i] = t*A[i,i]
        ident[i,i] = t*ident[i,i]
    
    print("A inversa * A:")
    print(A_orig)
    print(ident)
    print(ident@A_orig)
    print("\n")
    return A

tempo = timeit.timeit("mat_prod(np.random.randint(1, 100,(5,5)), np.random.randint(1, 100,(5,5))),", globals= globals(), number = 100)
print(tempo)

tempo = timeit.timeit("mat_dot_prod(np.random.randint(1, 100,(5,5)), np.random.randint(1, 100,(5,5))),", globals= globals(), number = 100)
print(tempo)

tempo = timeit.timeit("np.random.randint(1, 100,(5,5))@np.random.randint(1, 100,(5,5))", globals= globals(), number = 100)
print(tempo)

def criar_tridiagonal(n, sub, main, super):
    # Cria matriz n x n de zeros
    matrix = np.zeros((n, n))
    
    # Preenche a diagonal principal
    np.fill_diagonal(matrix, main)
    
    # Preenche a diagonal superior (k=1)
    # Seleciona a submatriz a partir da primeira linha, segunda coluna
    np.fill_diagonal(matrix[:, 1:], super)
    
    # Preenche a diagonal inferior (k=-1)
    # Seleciona a submatriz a partir da segunda linha, primeira coluna
    np.fill_diagonal(matrix[1:, :], sub)
    
    return matrix

# Exemplo: n=4, sub=-1, main=2, super=-1
print(criar_tridiagonal(4, -1, 2, -1))
A= np.array([[30,5,3],[1,19,40],[1,17,8]])
B = criar_tridiagonal(4, -1, 2, -1)

print(solve_tridiag(B))