using LinearAlgebra

function mat_prod(A, B)
    A_nrow, A_ncol = size(A)
    B_nrow, B_ncol = size(B)

    if A_ncol != B_nrow
        println("A multiplicação não pode ser feita entre as matrizes.")

    else
        C = zeros(A_nrow, B_ncol)
        for i in 1:A_nrow
            for j in 1:B_ncol
                C[i,j] = sum(A[i,k]*B[k,j] for k in 1:A_ncol)
            end
        end
        return C
    end
end

function mat_dot_prod(A, B)
    A_nrow, A_ncol = size(A)
    B_nrow, B_ncol = size(B)

    if A_ncol != B_nrow
        println("A multiplicação não pode ser feita entre as matrizes.")

    else
        C = zeros(A_nrow, B_ncol)
        for i in 1:A_nrow
            for j in 1:B_ncol
                C[i,j] = dot(A[i,:],B[:,j])
            end
        end
        return C
    end
end

A = [1 0 0; 0 1 0; 0 0 1]
B = [1 2 3; 1 2 3; 1 2 3]

display(mat_prod(A,B))
display(mat_dot_prod(A,B))
