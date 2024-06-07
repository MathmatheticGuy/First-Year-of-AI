import array
import numpy as np

'''
    Gaussian Elimination Module 1: Row Echelon
    Step-by-Step Guide:
    Step1: Find the first non-zero element in the first column
        If the first element is 0:
            swap the row with the row having non-zero element
    Step2: Make that element as 1 by dividing the row by that element
    Step3: Make all other elements in the first column as 0 by adding/subtracting the first row
    Step4: Repeat the above steps for all columns  
    
    M = M.copy() -> do this to avoid changing the original Matrix
'''


def augmented_matrix(A, B):
    B = B.reshape((len(A), 1))  # reshape b to column vector
    augMatrix = np.hstack((A, B))
    return augMatrix


def swap_rows(M: array, row_index1: int, row_index2: int) -> array:
    M = M.copy()
    '''
    This mean get row 1 to row 2 of M_new Matrix
    M[[row_index2, row_index1]]
    '''
    M[[row_index1, row_index2]] = M[[row_index2, row_index1]]
    print(f'Swap row {row_index1} with row {row_index2}')
    return M


def get_index_first_non_zero_value_from_column(M, column: int, starting_row: int):
    M = M.copy()

    # Get the first element from starting_row to the last row
    matrix_col = M[starting_row:, column]
    print(f"Col: {matrix_col}")

    if matrix_col[0] == 0:
        for value in matrix_col:
            # print(f'Tracked column value: {value}')
            first_non_zero_index = starting_row + 1
            if value != 0:
                print(f"first_non_zero_index: {first_non_zero_index}")
                return first_non_zero_index


def get_index_first_non_zero_value_from_row(M, row_index, augmented):
    # default for testing
    print('get_index_first_non_zero_value_from_row')
    M = M.copy()
    # If it is augmented matrix, Ignore the constant values
    if augmented:  # True by default
        M = M[:, :-1]  # take Matrix M from start to the last (:-1) array of the matrix
        print(M)

    row = M[row_index]
    for value in row:
        if value != 0:
            print(value)

def main():
    # Step 0: Making the matrix
    # Make sure data type is float for accurate calculation
    A = np.array([[1, 2, 3], [0, 1, 0], [2, 0, 5]], dtype=np.dtype(float))
    B = np.array([1, 2, 4])
    M = augmented_matrix(A, B)
    augmented = True;
    print(f'augmented_matrix:\n{M}')

    # new_matrix = swap_rows(M, 1, 0)
    # print(new_matrix)

    #? Step 1: Find the first non-zero element in the first column
    first_non_zero_below_pivot_index = get_index_first_non_zero_value_from_column(M, 0, 0)
    #? Step 2: Swap the row with the row having non-zero element
    swapped_matrix = swap_rows(M, 0, first_non_zero_below_pivot_index)
    print(swapped_matrix)

    get_index_first_non_zero_value_from_row(swapped_matrix, 0, augmented)
    
    #! Goal: Make all values below the pivot zeros
    #TODO 3s: For subtract each row with the 1/value below the pivot
    #TODO 3e: Write testcase for column 0 to 3


    #TODO 4: Move to next column and repeat the above steps


if __name__ == '__main__':
    main()
