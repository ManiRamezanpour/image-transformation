def matrix_multiplication(A, B):
    
    # Check inputs
    if not isinstance(A, list) or not isinstance(B, list):
        print("Error: both A and B must be lists")
        return None
    
    if len(A) == 0 or len(B) == 0:
        print("Error: matrices cannot be empty")
        return None
    
    # Dimensions
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    
    # Check structure
    for row in A:
        if not isinstance(row, list) or len(row) != cols_A:
            print("Error: invalid structure in matrix A")
            return None
    
    for row in B:
        if not isinstance(row, list) or len(row) != cols_B:
            print("Error: invalid structure in matrix B")
            return None
    
    # Check if multiplication is possible
    if cols_A != rows_B:
        print("Error: number of columns in A must equal rows in B")
        return None
    
    # Result matrix
    result = []
    
    for i in range(rows_A):
        result_row = []
        for j in range(cols_B):
            value = 0
            for k in range(cols_A):
                value += A[i][k] * B[k][j]
            result_row.append(value)
        result.append(result_row)
    
    return result