# Transpose and flip operations on matrices

def transpose_matrix(matrix):
    # Swap rows and columns - (height x width) becomes (width x height)
    if not matrix or not matrix[0]:
        return matrix
    
    height = len(matrix)
    width = len(matrix[0])
    
    # New matrix with swapped dimensions
    transposed = [[0] * height for _ in range(width)]
    
    # Element at [y][x] goes to [x][y]
    for y in range(height):
        for x in range(width):
            transposed[x][y] = matrix[y][x]
    
    return transposed


def flip_matrix_horizontal(matrix):
    # Mirror left-right
    if not matrix or not matrix[0]:
        return matrix
    
    height = len(matrix)
    width = len(matrix[0])
    
    flipped = [[0] * width for _ in range(height)]
    
    for y in range(height):
        for x in range(width):
            flipped[y][x] = matrix[y][width - 1 - x]
    
    return flipped


def flip_matrix_vertical(matrix):
    # Mirror top-bottom
    if not matrix or not matrix[0]:
        return matrix
    
    height = len(matrix)
    flipped = [row[:] for row in reversed(matrix)]
    
    return flipped


def rotate_90_clockwise(matrix):
    # Transpose then flip horizontally
    transposed = transpose_matrix(matrix)
    return flip_matrix_horizontal(transposed)


def rotate_90_counterclockwise(matrix):
    # Transpose then flip vertically
    transposed = transpose_matrix(matrix)
    return flip_matrix_vertical(transposed)


def rotate_180(matrix):
    # Flip both ways
    if not matrix or not matrix[0]:
        return matrix
    
    height = len(matrix)
    width = len(matrix[0])
    
    rotated = [[0] * width for _ in range(height)]
    
    for y in range(height):
        for x in range(width):
            rotated[y][x] = matrix[height - 1 - y][width - 1 - x]
    
    return rotated


# Aliases for shorthand
flip_horizontal = flip_matrix_horizontal
flip_vertical = flip_matrix_vertical


# RGB wrappers
def transpose_rgb(r, g, b):
    return transpose_matrix(r), transpose_matrix(g), transpose_matrix(b)


def flip_rgb_horizontal(r, g, b):
    return flip_matrix_horizontal(r), flip_matrix_horizontal(g), flip_matrix_horizontal(b)


def flip_rgb_vertical(r, g, b):
    return flip_matrix_vertical(r), flip_matrix_vertical(g), flip_matrix_vertical(b)

