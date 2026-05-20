
"""
Matrix transpose operation - flip matrix rows and columns.
"""


def transpose_matrix(matrix):
    """Transpose a 2D matrix (swap rows and columns).
    
    A transpose operation transforms:
    - Input: (height x width) matrix
    - Output: (width x height) matrix
    - Element at position [y][x] moves to position [x][y]
    
    Args:
        matrix (list of list): Input matrix
        
    Returns:
        list of list: Transposed matrix
        
    Example:
        >>> matrix = [[1, 2, 3], [4, 5, 6]]
        >>> transpose_matrix(matrix)
        [[1, 4], [2, 5], [3, 6]]
    """
    if not matrix:
        return matrix
    
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0
    
    if height == 0 or width == 0:
        return matrix
    
    # Create transposed matrix with swapped dimensions
    transposed = [[0 for _ in range(height)] for _ in range(width)]
    
    # Transpose: element [y][x] becomes [x][y]
    for y in range(height):
        for x in range(width):
            transposed[x][y] = matrix[y][x]
    
    return transposed


def transpose_rgb_channels(red_matrix, green_matrix, blue_matrix):
    """Transpose all three RGB channels.
    
    Args:
        red_matrix (list of list): Red channel matrix
        green_matrix (list of list): Green channel matrix
        blue_matrix (list of list): Blue channel matrix
        
    Returns:
        tuple: (transposed_red, transposed_green, transposed_blue)
    """
    return (
        transpose_matrix(red_matrix),
        transpose_matrix(green_matrix),
        transpose_matrix(blue_matrix)
    )


def flip_matrix_horizontal(matrix):
    """Flip matrix horizontally (mirror left-right).
    
    Args:
        matrix (list of list): Input matrix
        
    Returns:
        list of list: Horizontally flipped matrix
    """
    if not matrix:
        return matrix
    
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0
    
    if height == 0 or width == 0:
        return matrix
    
    flipped = [[0 for _ in range(width)] for _ in range(height)]
    
    for y in range(height):
        for x in range(width):
            flipped[y][x] = matrix[y][width - 1 - x]
    
    return flipped


def flip_matrix_vertical(matrix):
    """Flip matrix vertically (mirror top-bottom).
    
    Args:
        matrix (list of list): Input matrix
        
    Returns:
        list of list: Vertically flipped matrix
    """
    if not matrix:
        return matrix
    
    height = len(matrix)
    
    if height == 0:
        return matrix
    
    flipped = [[0 for _ in range(len(matrix[0]))] for _ in range(height)]
    
    for y in range(height):
        flipped[y] = matrix[height - 1 - y][:]
    
    return flipped


def rotate_90_clockwise(matrix):
    """Rotate matrix 90 degrees clockwise.
    
    Combines transpose and horizontal flip.
    
    Args:
        matrix (list of list): Input matrix
        
    Returns:
        list of list: Rotated matrix
    """
    # First transpose
    transposed = transpose_matrix(matrix)
    # Then flip horizontally
    return flip_matrix_horizontal(transposed)


def rotate_90_counterclockwise(matrix):
    """Rotate matrix 90 degrees counter-clockwise.
    
    Combines transpose and vertical flip.
    
    Args:
        matrix (list of list): Input matrix
        
    Returns:
        list of list: Rotated matrix
    """
    # First transpose
    transposed = transpose_matrix(matrix)
    # Then flip vertically
    return flip_matrix_vertical(transposed)


def rotate_180(matrix):
    """Rotate matrix 180 degrees.
    
    Args:
        matrix (list of list): Input matrix
        
    Returns:
        list of list: Rotated matrix
    """
    if not matrix:
        return matrix
    
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0
    
    if height == 0 or width == 0:
        return matrix
    
    rotated = [[0 for _ in range(width)] for _ in range(height)]
    
    for y in range(height):
        for x in range(width):
            rotated[y][x] = matrix[height - 1 - y][width - 1 - x]
    
    return rotated


def transpose_rgb_image(red_matrix, green_matrix, blue_matrix):
    """Transpose all RGB channels of an image.
    
    Args:
        red_matrix (list of list): Red channel
        green_matrix (list of list): Green channel
        blue_matrix (list of list): Blue channel
        
    Returns:
        tuple: (transposed_red, transposed_green, transposed_blue)
    """
    return transpose_rgb_channels(red_matrix, green_matrix, blue_matrix)


def flip_rgb_image_horizontal(red_matrix, green_matrix, blue_matrix):
    """Flip RGB image horizontally.
    
    Args:
        red_matrix (list of list): Red channel
        green_matrix (list of list): Green channel
        blue_matrix (list of list): Blue channel
        
    Returns:
        tuple: (flipped_red, flipped_green, flipped_blue)
    """
    return (
        flip_matrix_horizontal(red_matrix),
        flip_matrix_horizontal(green_matrix),
        flip_matrix_horizontal(blue_matrix)
    )


def flip_rgb_image_vertical(red_matrix, green_matrix, blue_matrix):
    """Flip RGB image vertically.
    
    Args:
        red_matrix (list of list): Red channel
        green_matrix (list of list): Green channel
        blue_matrix (list of list): Blue channel
        
    Returns:
        tuple: (flipped_red, flipped_green, flipped_blue)
    """
    return (
        flip_matrix_vertical(red_matrix),
        flip_matrix_vertical(green_matrix),
        flip_matrix_vertical(blue_matrix)
    )

