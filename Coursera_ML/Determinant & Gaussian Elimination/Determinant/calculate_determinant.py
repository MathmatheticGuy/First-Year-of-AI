import numpy as np

A_2 = np.array([
        [-3, 8, 1],
        [2, 2, -1],
        [-5, 6, 2]
    ], dtype=np.dtype(float))

b_2 = np.array([7, 1], dtype=np.dtype(float))
d_2 = np.linalg.det(A_2)

print(f"Determinant of matrix A_2: {d_2:.2f}")


A = np.array([
        [4, -3, 1],
        [2, 1, 3],
        [-1, 2, -5]
    ], dtype=np.dtype(float))
b = np.array([-10, 0, 17], dtype=np.dtype(float))

print("Matrix A:")
print(A)
print("\nArray b:")
print(b)

print(f"Shape of A: {np.shape(A)}")
print(f"Shape of b: {np.shape(b)}")

x = np.linalg.solve(A, b) # Solve using Gaussian Elimination

print(f"Solution: {x}")
