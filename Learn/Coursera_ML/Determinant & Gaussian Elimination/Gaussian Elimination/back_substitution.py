from core_function import get_index_first_non_zero_value_from_row

def back_substitution(M):
    """
    Perform back substitution on an augmented matrix (with unique solution) in reduced row echelon form to find the solution to the linear system.

    Parameters:
    - M (numpy.array): The augmented matrix in row echelon form with unitary pivots (n x n+1).

    Returns:
    numpy.array: The solution vector of the linear system.
    """

    # Make a copy of the input matrix to avoid modifying the original
    M = M.copy()
    #     M[0] = [1, -1, 1/2, 1/2]
    #     M[1] = [0, 1, 1, -1]
    #     M[2] = [0, 0, 1, -1]

    print(M)

    # Get the number of rows (and columns) in the matrix of coefficients
    num_rows = M.shape[0]

    # Iterate from bottom to top
    for row in reversed(range(num_rows)):  # start with 3
        print("row: ", row)
        substitution_row = M[row]
        print("substitution_row: ", substitution_row)

        # Get the index of the first non-zero element in the substitution row. Remember to pass the correct value to the argument augmented.
        index = get_index_first_non_zero_value_from_row(M, row, augmented=False)
        print("index: ", index)

        # Iterate over the rows above the substitution_row
        for j in reversed(range(row)):
            # Get the row to be reduced. The indexing here is similar as above, with the row variable replaced by the j variable.
            row_to_reduce = M[j]
            print("row_to_reduce: ", row_to_reduce)
            # Get the value of the element at the found index in the row to reduce
            value = row_to_reduce[index]
            print("value to reduced: ", value)

            # Perform the back substitution step using the formula row_to_reduce -> row_to_reduce - value * substitution_row
            row_to_reduce = row_to_reduce - value * substitution_row

            # Replace the updated row in the matrix, be careful with indexing!
            M[j, :] = row_to_reduce
            print("M[j,:]: ", M[j, :])
            print("new matrix:\n", M)

    # Extract the solution from the last column`
    solution = M[:, -1]
    print("substitution_row: ", solution)
    return solution