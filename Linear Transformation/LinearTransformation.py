import numpy as np
import cv2

def swap_rows(M, row_index_1, row_index_2):
    """
    Swap rows in the given matrix.

    Parameters:
    - matrix (numpy.array): The input matrix to perform row swaps on.
    - row_index_1 (int): Index of the first row to be swapped.
    - row_index_2 (int): Index of the second row to be swapped.
    """

    # Copy matrix M so the changes do not affect the original matrix.
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
    int or False: The index of the first non-zero value in the specified column, starting from the given row.
                Returns False if no non-zero value is found.
    """
    # Get the column array starting from the specified row
    column_array = M[starting_row:,column]
    for i, val in enumerate(column_array):
        # Iterate over every value in the column array.
        # To check for non-zero values, you must always use np.isclose instead of doing "val == 0".
        if not np.isclose(val, 0, atol = 1e-5):
            # If one non zero value is found, then adjust the index to match the correct index in the matrix and return it.
            index = i + starting_row
            return index
    # If no non-zero value is found below it, return None.
    return False

# Define a 3x3 matrix
M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
M_swapped = swap_rows(M, 0, 2)
print(M_swapped)

N = np.array([
    [0, 5, -3 ,6 ,8],
    [0, 6, 3, 8, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0 ,0 ,7],
    [0, 2, 1, 0, 4]])
print(N)
print(get_index_first_non_zero_value_from_column(N, column = 1, starting_row = 3))


