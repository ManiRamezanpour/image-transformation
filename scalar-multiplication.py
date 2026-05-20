def scalar_multiplication(scalar, matrix):
    
    # Check scalar
    if not isinstance(scalar, (int, float)):
        print(f"Error: scalar must be a number, got {type(scalar)}")
        return None
    
    # Check matrix type
    if not isinstance(matrix, list):
        print("Error: matrix must be a list")
        return None
    
    # Check empty matrix
    if len(matrix) == 0:
        print("Error: matrix is empty")
        return None
    
    cols = len(matrix[0])
    
    # Validate matrix structure
    for row in matrix:
        if not isinstance(row, list) or len(row) != cols:
            print("Error: invalid matrix structure")
            return None
    
    result = []
    
    for row in matrix:
        new_row = []
        for value in row:
            new_row.append(value * scalar)
        result.append(new_row)
    
    return result