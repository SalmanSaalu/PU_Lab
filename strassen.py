import numpy as np

def strassen(A, B):
    n = A.shape[0]
    if n == 1:
        return A * B
    else:
        # Divide the matrices into 4 sub-matrices
        a11 = A[:n//2, :n//2]
        a12 = A[:n//2, n//2:]
        a21 = A[n//2:, :n//2]
        a22 = A[n//2:, n//2:]
        b11 = B[:n//2, :n//2]
        b12 = B[:n//2, n//2:]
        b21 = B[n//2:, :n//2]
        b22 = B[n//2:, n//2:]

        # Compute the 7 products required by Strassen's algorithm
        p1 = strassen(a11, b12 - b22)
        p2 = strassen(a11 + a12, b22)
        p3 = strassen(a21 + a22, b11)
        p4 = strassen(a22, b21 - b11)
        p5 = strassen(a11 + a22, b11 + b22)
        p6 = strassen(a12 - a22, b21 + b22)
        p7 = strassen(a11 - a21, b11 + b12)

        # Compute the 4 sub-matrices of the product
        c11 = p5 + p4 - p2 + p6
        c12 = p1 + p2
        c21 = p3 + p4
        c22 = p5 + p1 - p3 - p7

        # Combine the sub-matrices to obtain the product
        C = np.zeros((n, n))
        C[:n//2, :n//2] = c11
        C[:n//2, n//2:] = c12
        C[n//2:, :n//2] = c21
        C[n//2:, n//2:] = c22

        return C

A = np.random.randint(0, 10,size=(4, 4))
B = np.random.randint(0, 10,size=(4, 4))
C = strassen(np.array(A), np.array(B))
print(A)
print(B)
print(C)