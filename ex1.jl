function mat_prod(A, B)
    A_nrow, A_ncol = size(A)
    B_nrow, B_ncol = size(B)

    if A_ncol != B_nrow
        println("A multiplicação não pode ser feita entre as matrizes.")

    else
        C = zeros(A_ncol, B_nrow)
        for i in 1::A_nrow
            for j in 1::B_ncol
            end
        end
    end        
end

A = [1 2; 1 2]
print(A[1,2])