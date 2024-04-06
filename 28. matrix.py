def matrix_addition(mat1, mat2):
    # Initialize an empty matrix to store the result
    result = []
    
    # Iterate over each row of the matrices
    for i in range(len(mat1)):
        # Initialize an empty list to store the current row of the result matrix
        row = []
        # Iterate over each element of the current row
        for j in range(len(mat1[0])):
            # Add corresponding elements from mat1 and mat2 and append to the current row
            row.append(mat1[i][j] + mat2[i][j])
        # Append the current row to the result matrix
        result.append(row)
    
    # Return the result matrix
    return result

# Sample Input
mat1 = [[1, 2],
        [5, 3]]

mat2 = [[2, 3],
        [4, 1]]

# Calculate the sum of matrices
mat_sum = matrix_addition(mat1, mat2)

# Output
print("Mat Sum =", mat_sum)
