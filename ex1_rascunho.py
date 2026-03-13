import time
import numpy as np
import random


def calculate_process_time(f):
    def wrapper(*args, **kwargs):
        t_0 = time.process_time()
        result = f(*args, **kwargs)
        t_1 = time.process_time()
        print(f"A operação demorou {t_1-t_0:.8f} segundos.")
        
        return result
    
    return wrapper
    
    
class Matrix:
    
    def __init__(self, row_vectors: list[list]):
        self.row_vectors = row_vectors
        self.num_rows = len(row_vectors)
        self.num_col = len(row_vectors[0])
                
    @property
    def row_vectors(self):
        return self._row_vectors
    
    @row_vectors.setter
    def row_vectors(self, row_vectors: list[list]):
        num_col = len(row_vectors[0])
        for row in row_vectors[1:]:
            if len(row) != num_col:
                raise ValueError("Não é possível montar uma matriz com esses vetores linha.")
        
        self._row_vectors = row_vectors
                
    def get_shape(self):
        return self.num_rows, self.num_col
    
    def matrix_view(self):
        for row in self.row_vectors:
            print(f"{row}\n")
            
    def __str__(self):
        return (f"{self.row_vectors}")
    
    def __repr__(self):
        return (f"{self.row_vectors}")
            
            

#-------------------------------------------------- QUESTÃO 1 --------------------------------------------------

# --> A)
@calculate_process_time
def mat_prod(A: Matrix, B: Matrix):
    
    num_rows_A, num_cols_A = A.get_shape()
    num_rows_B, num_cols_B = B.get_shape()
    
    if num_cols_A != num_rows_B:
        print(f"Não é possível multiplicar uma matriz A: {A.get_shape()} por uma B: {B.get_shape()}")
        
    else:
        C = [[0 for j in range(num_cols_B)] for i in range(num_rows_A)]
        
        # Sabemos que cada entrada i,j em uma matriz que é resultado de um produto de duas matrizes é igual ao produto interno entre o 
        # vetor coluna i de A e o vetor linha j de B, os quais tem a mesma dimensão
        
        for i in range(num_rows_A): #Escolhe a linha de A
            row_A = A.row_vectors[i]
            
            for j in range(num_cols_B): # Escolhe a coluna de B
                soma = sum(row_A[_]*B.row_vectors[_][j] for _ in range(num_cols_A))
                C[i][j] = soma
                
        C_matrix = Matrix(C)
      
        return C_matrix

def create_matrix():
    pass

A = Matrix([[1,2,3,4], [1,2,3,4], [1,2,3,4]])
B = Matrix([[1,2,3], [1,2,3], [1,2,3], [1,2,3]])           

C = Matrix([[1,2,3],
            [1,2,3],
            [1,2,3]])

ID_3X3 = Matrix([[1,0,0],
                 [0,1,0],
                 [0,0,1]])

mat_prod(C, ID_3X3)