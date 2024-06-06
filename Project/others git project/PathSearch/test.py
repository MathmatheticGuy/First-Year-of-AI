def load_matrix(filename):
    """Loads the matrix from the specified file."""
    with open(filename, 'r') as file:
        return [line.strip().split(',') for line in file.readlines()]

def save_matrix(matrix, filename):
    """Saves the matrix to the specified file."""
    with open(filename, 'w') as file:
        for row in matrix:
            file.write(','.join(row) + '\n')

def calculate_total_above_value(matrix, row, column):
    """Calculates the total value of digits above 'X'."""
    total = 0
    for r in range(row):  # Iterate rows above 'X'
        if matrix[r][column].isdigit():
            total += int(matrix[r][column])
    return total

def calculate_total_right_value(matrix, row, column):
    """Calculates the total value of digits to the right of 'X'."""
    total = 0
    for c in range(column + 1, len(matrix[row])):  # Iterate to the right
        if matrix[row][c].isdigit():
            total += int(matrix[row][c])
    return total

def main():
    matrix = load_matrix('input.txt')  # Load matrix

    row = 4
    column = 1
    matrix[row][column] = 'X'  # Place 'X'

    # Calculate and display results
    total_above = calculate_total_above_value(matrix, row, column)
    total_right = calculate_total_right_value(matrix, row, column)

    print("Total value above X:", total_above)
    print("Total value to the right of X:", total_right)

    save_matrix(matrix, 'output.txt')  # Optionally save the modified matrix

if __name__ == "__main__":
    main()