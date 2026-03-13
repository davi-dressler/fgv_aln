from __future__ import annotations
import numpy as np
import time
import pandas as pd
import timeit

times = [] #Lista que armazena os tempos de processamento para calcular a mediana
data = [] 



def process_time_function(f: function):
        def wrapper(*args, **kwargs):
            global times
            
            #Processa a função e calcula o tempo de execução
            time_init = time.perf_counter()
            result = f(*args, **kwargs)
            time_fin = time.perf_counter()
            total_time = time_fin - time_init
            
            print(f"{total_time:.8f}")
            times.append(total_time)
            return result
        
        return wrapper



@process_time_function
def mat_prod(A, B):
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



def realize_test(n: int, size_1: tuple[int], size_2: tuple[int]):
    
    for i in range(n):
        mat_prod(np.random.randint(1, 100, size= size_1), np.random.randint(1, 100, size= size_2))
    
    arr = np.array(times)
    mediana = np.median(arr)
    
    registro = {"size_1": f"{size_1}", "size_2": f"{size_2}", "median_process_time": f"{mediana:.10f}"}
    data.append(registro)
    
    

# for m in range(5, 1005, 200):
#     for n in range(5, 1005, 200):
#         for p in range(5 ,1005, 200):
#             realize_test(1, (m,p) , (p,n))


# df = pd.DataFrame(data)
# df.to_csv('teste.csv', index=False, sep=';', encoding='utf-8')

tempo = timeit.timeit(stmt= "realize_test(1, (5,5), (5,5))", globals= globals(), number= 5)
print(tempo)