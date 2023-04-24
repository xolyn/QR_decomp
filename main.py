from QR_decomp import *

def main():
    """
    Prompts for n and generates a random matrix.
    """
    cols = input('give number of columns : ')
    rows = input('give number of rows : ')
    A = np.random.rand(int(rows), int(cols))
    print('Given matrix of columns to be orthonormalized: \n A = \n ', A)
    Q, R = QR_Decomposition(A)
    print('ONB: \n Q = \n', Q)
    print('Representation of A on Q (should be upper-triangular): \n  R = \n' , R)
    print('Check orthonormality of Q (the following should be close to I): \n  Q.T @ Q  \n= \n', Q.T @ Q)
    print('approximation error (should be close to zero): \n ||A-Q@R||_F = \n', np.linalg.norm(A-Q@R))

# Personal test only, don't grade based on this:
# mat=np.array([[12,-51,4],[6,167,-68],[-4,24,-41]])
# QR_Decomposition(mat) 