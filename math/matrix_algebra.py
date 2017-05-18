# Matrix Algebra

import numpy as np
A = np.array([[1, 2, 3],[2, 7, 4]])
B = np.array([[1, -1],[0,1]])
C = np.array([[5,-1], [9,1], [6,0]])
D = np.array([[3,-2,-1], [1,2,3]])
u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.transpose(np.array([[1,8,0,5]]))

# 1: dimensions of each matrix
# A: 2x3
# B: 2x2
# C: 3x2
# D: 2x3
# u: 1x4
# v: 1x4
# w: 4x1

print(A.shape)
print(B.shape)
print(C.shape)
print(D.shape)
print(u.shape)
print(v.shape)
print(w.shape)

# 2: vector operations
# u + v = [9,7,-4,9]
# u-v = [3, -3, -2, 1]
# au = [36, 12, -18, 30]
# u * v = 51
# norm(u) = 8.60 = sqrt(36+4+9+25) = sqrt(74)

alp = 6
print(u + v)
print(u-v)
print(alp*u)
print(np.dot(u,v))
print(np.linalg.norm(u))

# 3: matrix operations
# A+C is not defined; dimension mismatch
# A-C' = [-4, -7, -3; 3, 6, 4]
# C' + 3D = [14, 3, 3; 2 7 9]
# BA = [-1, -5, -1; 2, 7, 4]
# BA' = not defined; dimension mismatch

print(A-np.transpose(C))
print(np.transpose(C)+3*D)
print(np.matmul(B,A))
