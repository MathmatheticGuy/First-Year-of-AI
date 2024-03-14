import numpy as np
#
A = np.array([
    [2, 1, 5],
    [1, 3, 1],
    [4, 6, 6],
], dtype=np.dtype(float))

# b = np.array([5, 1, 6], dtype=np.dtype(float))


# A = np.array([
#     [1, 3],
#     [3, 12],
# ], dtype=np.dtype(float))
#
# b = np.array([15, 3], dtype=np.dtype(float))
# A_system = np.hstack((A, b.reshape((3, 1))))
# print(A_system)
# x = np.linalg.solve(A, b)
# print(f"Solution: {x}")  # print out solution of x,y,z

d = np.linalg.det(A)
print(f"Determinant of matrix A: {d:.2f}")

