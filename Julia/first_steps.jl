
# Aprendendo a criar matrizes em Julia

# Funções Nativas:

#Matriz de zeros: zeros(m, n) , gera uma matriz m x n preenchida com zeros
zero_matrix = zeros(3,3)
println(zero_matrix)
println(" ")
println("-----------------------------------------------------------------------------------------")

# Matriz de uns: ones(m, n)
ones_matrix = ones(3,3)
println(ones_matrix)
println(" ")
println("-----------------------------------------------------------------------------------------")

# Matriz de valores aleatórios entre 0 e 1 
random_matrix = rand(3, 3)
println(random_matrix)
println(" ")
println("-----------------------------------------------------------------------------------------")

# Função reshape: recebe um vetor, e as dimensões que nós queremos, reshape(vector, m, n)
vector = [1,2,3,4,5,6,7,8,9]
vector_reshape = reshape(vector, 3, 3)
println(vector_reshape)
println(" ")
println("-----------------------------------------------------------------------------------------")

# Matriz identidade:
id3 = [1 0 0; 0 1 0; 0 0 1]
print(id3 * id3)

# @process_time_function
# def mat_prod(A, B):
#     A_nrow, A_ncol = A.shape
#     B_nrow, B_ncol = B.shape
    
#     if A_ncol != B_nrow:
#         print("Não é possível multiplicar essas matrizes.")
#         return
    
#     C = np.zeros((A_nrow, B_ncol))
#     for i in range(A_nrow):
#         for j in range(B_ncol):
#             C[i,j] = sum(A[i,k]*B[k,j] for k in range(A_ncol))
    
#     return C


