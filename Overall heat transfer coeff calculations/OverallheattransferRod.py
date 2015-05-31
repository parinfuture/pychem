def overallht_coeff(T, A, h):
    Q = h[1]*A[1]*(T[2]- T[1])
    U = 0
    for i in range(0, len(A)):
        U = U + Q/float(h[i]*A[i])
        return U
    return U


#test case
overallht_coeff([100,102,103], [100,102,103], [1,2,3])
    
