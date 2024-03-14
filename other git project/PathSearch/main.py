def allocate_value(row, column, value):
    # Open the file in read mode
    with open('input.txt', 'r') as file:
        # Read the contents of the file
        contents = file.readlines()

    # Update the value at the specified position

    # print(contents[row][column+1:])
    # print(contents[row][:column])
    # Adding value before and after X.
    contents[row] = contents[row][:column] + value + contents[row][column+1:]

    # Open the file in write mode
    with open('output.txt', 'w') as file:
        # Write the updated contents back to the file
        file.writelines(contents)
    
    with open('output.txt', 'r') as file:
        # Read the contents of the file
        contents = file.readlines()
        
        def print_matrix(contents):
            for row in contents:
                print(row.strip())

        # Call the function to print the contents in matrix form
        print_matrix(contents)
    
# Allocate 'X' at position (m, n)
row = 4
column = 1
# total row: 6
# total column: 8
allocate_value(4, 3, 'X')

# Define a function to calculate the total value in a row

# Define a function to calculate the total value to the right of a specified position
def calculate_total_right_value(contents, row, column):
    total_commas = 0
    # Iterate over each character to the right of the specified position in the specified row
    for char in contents[row][column+1:]:
        # Check if the character is a comma
        if char == ',':
            # Increment the total comma count
            total_commas += 1
    # Return the total comma count
    return total_commas


# Open the file in read mode
with open('input.txt', 'r') as file:
    # Read the contents of the file
    contents = file.readlines()



calc_right = calculate_total_right_value(contents, row, column)
print(calc_right)

# Move closer to G algorithm
#   If any move available. 
#       Push the available move to a list
#       For each move in the list
#           Calculate the distant to G of each move (horiozontally)
#       

# While X coordinate != X > 1 
#   move closer to G
#   if it 1 move from G, then return after move position   
