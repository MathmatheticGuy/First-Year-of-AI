import numpy as np;

# solving linear systems 3 variables
A = np.array([
    [1, 2, 3],
    [0, 2, 2],
    [1, 4, 5]
], dtype=np.dtype(float))

b = np.array([10, 4, 8], dtype=np.dtype(float))

# calculate the value of A matrix
d = np.linalg.det(A)
print(f"Determinant of matrix A: {d:.2f}")

print("Matrix A:")
print(A)
print("\nArray b:")
print(b)

print(f"Shape of A: {np.shape(A)}")
print(f"Shape of b: {np.shape(b)}")

"""
    Solve 
        [ 4 -3  1 | -10]
        [ 2  1  3 |  0 ]
        [-1  2 -5 |  17]
    using Gaussian Elimination
"""
x = np.linalg.solve(A, b)

print(f"Solution: {x}")  # print out solution of x,y,z



# np.hstack() -> Unified Matrix A with B
# reshape
A_system = np.hstack((A, b.reshape((3, 1))))
print(A_system)


# write a function that multiply a number row n of A_system
def multiply_matrix(matrix, row_num, row_num_multiple):
    # .copy() function is required here to keep the original matrix without any changes
    mul_matrix = matrix.copy()
    mul_matrix[row_num] = mul_matrix[row_num] * row_num_multiple
    return mul_matrix


print("\nOriginal Matrix\n", A_system)
print("After multiple\n", multiply_matrix(A_system, 0, 2))


# multiply row_num_1 by row_num_1_multiple and add it to the row_num_2,
# This is the step where a Row eliminate it below Row's a value
def AddRows(M, row1, row2, M_multiply):
    M_new = M.copy()
    # adding (row1 * 1/2) to row2
    M_new[row2] = M_new[row1] * M_multiply + M_new[row2]
    return M_new


print("\nOriginal Matrix\n", A_system)
print("New Matrix:\n", AddRows(A_system, 0, 1, -1 / 2))


# exchange row_num_1 and row_num_2 of the matrix A
def SwapRows(M, row_num_1, row_num_2):
    M_new = M.copy()
    M_new[[row_num_1, row_num_2]] = M_new[[row_num_2, row_num_1]]
    return M_new


print("Original matrix:")
print(A_system)
print("\nMatrix after exchange its first (0) and third rows (2):")
# swap row 1 and 3
A_ref = SwapRows(A_system, 0, 2)
print(A_ref)
# Note: ref is an abbreviation of the row echelon form (row reduced form)

# Multiply row 0 of the new matrix A_ref by 2 and add it to the row 1
A_ref = AddRows(A_ref, 0, 1, 2)
print('Multiply row 0 of the new matrix A_ref by 2 and add it to the row 1\n', A_ref)

# Multiply row 0 of the new matrix A_ref by 4 and add it to the row 2
A_ref = AddRows(A_ref, 0, 2, 4)
print('Multiply row 0 of the new matrix A_ref by 4 and add it to the row 2\n', A_ref)

# Multiply row 1 of the new matrix A_ref by -1 and add it to the row 2
A_ref = AddRows(A_ref, 1, 2, -1)
print('Multiply row 1 of the new matrix A_ref by -1 and add it to the row 2\n', A_ref)

# multiply row 2 of the new matrix A_ref by -1/12 to get y
A_ref = multiply_matrix(A_ref, 2, -1 / 12)
print('Multiply row 2 of the new matrix A_ref by -1/12 to get y\n', A_ref)

# ! Notice: python start from 0
x3 = A_ref[2, 3]  # == A_ref[2][4] (row 3, value 4th)
print('Solution\nx3: ', x3)

# Row 2 (1): divide all to b coefficient and calculate like normal
x2 = (A_ref[1, 3] - A_ref[1, 2] * x3) / A_ref[1, 1]
print('x2: ', x2)

# Row 1 (0): divide all to b coefficient and calculate like normal
# If not understand visualize the system on paper
x1 = (A_ref[0, 3] - A_ref[0, 2] * x3 - A_ref[0, 1] * x2) / A_ref[0, 0]
print('x2: ', x1)