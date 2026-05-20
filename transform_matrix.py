def transform_matrix(matrix):
    """Transforms the given matrix by applying a specific operation.

    Args:
        matrix (list of list of int): The input matrix to be transformed.

    Returns:
        list of list of int: The transformed matrix.
    """
    # Example
    transformed_matrix = []
    for row in matrix:
        transformed_row = [element * 2 for element in row]  # Example transformation: doubling each element
        transformed_matrix.append(transformed_row)
    return transformed_matrix