import numpy as np

def QR_Decomposition(A):
    """
    Applies the Gram-Schmidt method to A
    and returns orthonormal Q and upper triangular R, so Q @ R = A.
    """
    
    n, m = A.shape # get the shape of A

    Q = np.empty((n, n)) # initialize matrix Q (orthonormal)
    u = np.empty((n, n)) # initialize matrix u

    u[:, 0] = A[:, 0]
    Q[:, 0] = u[:, 0]/(np.linalg.norm(u[:,0]))#Fill this line: normalize u[:, 0]

    for i in range(1, m):

        u[:, i] = A[:, i]
        for j in range(i):
            u[:, i] = u[:,i]-(np.inner(u[:,i],u[:,j])/np.inner(u[:,j],u[:,j]))*u[:,j]#Fill this line: from u[:, i] subtract off orthogonal projection of A[:,i] on Q[:,j]

        Q[:, i] = u[:,i]/(np.linalg.norm(u[:,i]))#Fill this line : normalize u[:, i]

    R = np.zeros((n, m))
    for i in range(n):
        for j in range(i,m):
            R[i, j] = np.inner(Q[:, i],A[:, j])# Fill this line # Coefficient of orthogonal projection of A[:,j] onto Q[:,i]

    return Q, R