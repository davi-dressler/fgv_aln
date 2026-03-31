using LinearAlgebra 

function gs(A)
    m, n = size(A)
    rank = min(m,n) #Não é o posto real

    Q = zeros(m,rank)
    R = zeros(rank,n)
    u = zeros(m)

    for j in 1:rank
        u .=  A[:, j]

        for i in 1:(j-1)
            qi = @view Q[:,i]
            R[i,j] = qi' * u
            
        # end

        # for i in 1:(j-1)
        #     qi = @view Q[:,i]
            u .-= R[i,j] .* qi
        end

        r_jj =  norm(u)
        R[j,j] = r_jj
        Q[:, j] .= u ./ r_jj

    end

    for j in rank+1:n
        u .= A[:, j]
        for i in 1:rank
            qi = @view Q[:,i]
            R[i,j] = qi' * u
        end
    end

    return Q, R
end

function test(m, n)

    A = randn(m,n)
    @time Q, R = gs(A)
    @show norm(Q * R - A)
    @show norm(Q' * Q - I)

end


function main()
    A = [1 2 1 4; 3 4 5 7; 8 9 3 2; 1 4 7 6]
    @time Q, R = gs(A)
    @show Q * R

end