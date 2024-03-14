import numpy as np
import unittest


def swap_rows(M, row_index_1, row_index_2):
    """
    Swap rows in the given matrix.

    Parameters:
    - matrix (numpy.array): The input matrix to perform row swaps on.
    - row_index_1 (int): Index of the first row to be swapped.
    - row_index_2 (int): Index of the second row to be swapped.
    """

    # Copy matrix A so the changes do not affect the original matrix.
    M = M.copy()
    # Swap indexes
    M[[row_index_1, row_index_2]] = M[[row_index_2, row_index_1]]
    return M

def get_index_first_non_zero_value_from_column(M, column, starting_row):
    """
    Retrieve the index of the first non-zero value in a specified column of the given matrix.

    Parameters:
    - matrix (numpy.array): The input matrix to search for non-zero values.
    - column (int): The index of the column to search.
    - starting_row (int): The starting row index for the search.

    Returns:
    int or None: The index of the first non-zero value in the specified column, starting from the given row.
                Returns None if no non-zero value is found.
    """
    # Get the column array starting from the specified row
    column_array = M[starting_row:,column]
    print('column array: ', column_array)
    for i, val in enumerate(column_array):
        # Iterate over every value in the column array.
        # To check for non-zero values, you must always use np.isclose instead of doing "val == 0".
        if not np.isclose(val, 0, atol = 1e-5):
            # If one non zero value is found, then adjust the index to match the correct index in the matrix and return it.
            index = i + starting_row
            return index
    # If no non-zero value is found below it, return None.
    return None

# If a row is full of 0. Move row to the bottom
def move_row_to_bottom(M, row_index):
    """
        Move the specified row to the bottom of the given matrix.

        Parameters:
        - A (numpy.array): Input matrix.
        - row_index (int): Index of the row to be moved to the bottom.

        Returns:
            numpy.array: Matrix with the specified row moved to the bottom.
    """

    # Make a copy of A to avoid modifying the original matrix
    M = M.copy()

    # Extract the specified row
    row_to_move = M[row_index]

    # Delete the specified row from the matrix
    M = np.delete(M, row_index, axis=0)

    # Append the row at the bottom of the matrix
    M = np.vstack([M, row_to_move])

    return M

# Concatinate 2 Matrixes (Like concat 3x3 matrix with 1x1 matrix to get 4x4 matrix)
def augmented_matrix(A, B):
    """
    Create an augmented matrix by horizontally stacking two matrices A and B.

    Parameters:
    - A (numpy.array): First matrix.
    - B (numpy.array): Second matrix.

    Returns:
    - numpy.array: Augmented matrix obtained by horizontally stacking A and B.
    """
    augmented_M = np.hstack((A,B))
    return augmented_M

def multiply_matrix(matrix, row_num, row_num_multiple):
    # .copy() function is required here to keep the original matrix without any changes
    mul_matrix = matrix.copy()
    mul_matrix[row_num] = mul_matrix[row_num] * row_num_multiple
    return mul_matrix

def AddRow(M, row1, row2, row_multiplier):
    newM = M.copy()
    newM[row1] = newM[row1] + row_multiplier * newM[row2]
    return newM

# Indexing starts at 0
A = np.array([[1,2,3],[0,0,0], [0,0,5]])
B = np.array([[1], [2], [4]])

M = np.hstack((A, B.reshape(3, 1)))
print(M)
# x = np.linalg.solve(M)

for i in M:
    for k in range(len(M)):
        print(k)
    print(i)



