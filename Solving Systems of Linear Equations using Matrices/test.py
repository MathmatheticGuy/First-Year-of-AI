# GRADED FUNCTION: reduced_row_echelon_form
import numpy as np;
def AddRows(M, row1, row2, M_multiply):
    M_new = M.copy()
    # adding (row1 * 1/2) to row2
    M_new[row2] = M_new[row1] * M_multiply + M_new[row2]
    return M_new


# exchange row_num_1 and row_num_2 of the matrix A
def SwapRows(M, row_num_1, row_num_2):
    M_new = M.copy()
    M_new[[row_num_1, row_num_2]] = M_new[[row_num_2, row_num_1]]
    return M_new

def multiply_matrix(matrix, row_num, row_num_multiple):
    # .copy() function is required here to keep the original matrix without any changes
    mul_matrix = matrix.copy()
    mul_matrix[row_num] = mul_matrix[row_num] * row_num_multiple
    return mul_matrix



def reduced_row_echelon_form(A, B):
    """
    Utilizes elementary row operations to transform a given set of matrices,
    which represent the coefficients and constant terms of a linear system,
    into reduced row echelon form.

    Parameters:
    - A (numpy.array): The input square matrix of coefficients.
    - B (numpy.array): The input column matrix of constant terms

    Returns:
    numpy.array: A new augmented matrix in reduced row echelon form.
    """
    # Make copies of the input matrices to avoid modifying the originals
    A = A.copy()
    B = B.copy()

    # Convert matrices to float to prevent integer division
    A = A.astype('float64')
    B = B.astype('float64')

    # Number of rows in the coefficient matrix
    num_rows = len(A)

    # List to store rows that should be moved to the bottom (rows of zeroes)
    rows_to_move = []

    ### START CODE HERE ###

    # Transform matrices A and B into the augmented matrix M
    M = np.hstack((A, B.reshape(3, 1)))

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
        column_array = M[starting_row:, column]
        print('column array: ', column_array)
        for i, val in enumerate(column_array):
            # Iterate over every value in the column array.
            # To check for non-zero values, you must always use np.isclose instead of doing "val == 0".
            if not np.isclose(val, 0, atol=1e-5):
                # If one non zero value is found, then adjust the index to match the correct index in the matrix and return it.
                index = i + starting_row
                return index
        # If no non-zero value is found below it, return None.
        return None

    # Iterate over the rows.
    for i in M:

        # Find the first non-zero entry in the current row (pivot)
        # Check if Row 1st value == 0
        pivot = get_index_first_non_zero_value_from_column(i, 0, 0)
        # This variable stores the pivot's column index, it starts at i, but it may change if the pivot is not in the main diagonal.
        column_index = pivot

        # CASE PIVOT IS ZERO
        if np.isclose(pivot, 0):
            # PART 1: Look for rows below current row to swap, you may use the function get_index_first_non_zero_value_from_column to find a row with non zero value
            index = get_index_first_non_zero_value_from_column(M, 0, 0)

            # If there is a non-zero pivot
            if index is not None:
                # Swap rows if a non-zero entry is found below the current row
                M = swap_rows(M, None, None)

                # Update the pivot after swapping rows
                pivot = None

            # PART 2 - NOT GRADED. This part deals with the case where the pivot isn't in the main diagonal.
            # If no non-zero entry is found below it to swap rows, then look for a non-zero pivot outside from diagonal.
            if index is None:
                index_new_pivot = get_index_first_non_zero_value_from_row(M, i)
                # If there is no non-zero pivot, it is a row with zeroes, save it into the list rows_to_move so you can move it to the bottom further.
                # The reason in not moving right away is that it would mess up the indexing in the for loop.
                # The second condition i >= num_rows is to avoid taking the augmented part into consideration.
                if index_new_pivot is None or index_new_pivot >= num_rows:
                    rows_to_move.append(i)
                    continue
                # If there is another non-zero value outside from diagonal, it will be the pivot.
                else:
                    pivot = None
                    # Update the column index to agree with the new pivot position
                    column_index = None

        # END HANDLING FOR PIVOT 0

        # Divide the current row by the pivot, so the new pivot will be 1. (reduced row echelon form)
        M[i] = (1 / column_index) * M[i]

        # Perform row reduction for rows below the current row
        for j in None:
            # Get the value in the row that is below the pivot value. Remember that the value in the column position is given by the variable called column_index
            value_below_pivot = None

            # Perform row reduction using the formula:
            # row_to_reduce -> row_to_reduce - value_below_pivot * pivot_row
            M[j] = None

    ### END CODE HERE ###

    # Move every rows of zeroes to the bottom
    for row_index in rows_to_move:
        M = move_row_to_bottom(M, row_index)
    return M

A = np.array([[1,2,3],[0,0,0], [0,0,5]])
B = np.array([[1], [2], [4]])
reduced_row_echelon_form(A,B)