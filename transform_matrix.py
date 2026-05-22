# Basic pixel value transformations

def transform_matrix(matrix, operation='double', factor=2):
    # Apply transformations to pixel values
    if not matrix or not matrix[0]:
        return matrix
    
    height = len(matrix)
    width = len(matrix[0])
    result = [[0] * width for _ in range(height)]
    
    if operation == 'double':
        for y in range(height):
            for x in range(width):
                result[y][x] = min(255, matrix[y][x] * 2)
    
    elif operation == 'halve':
        for y in range(height):
            for x in range(width):
                result[y][x] = matrix[y][x] // 2
    
    elif operation == 'scale':
        # Multiply by factor (useful for brightness)
        for y in range(height):
            for x in range(width):
                val = int(matrix[y][x] * factor)
                result[y][x] = min(255, max(0, val))
    
    elif operation == 'invert':
        for y in range(height):
            for x in range(width):
                result[y][x] = 255 - matrix[y][x]
    
    elif operation == 'threshold':
        threshold = int(factor)
        for y in range(height):
            for x in range(width):
                result[y][x] = 255 if matrix[y][x] >= threshold else 0
    
    else:
        # Copy as-is
        for y in range(height):
            for x in range(width):
                result[y][x] = matrix[y][x]
    
    return result


def posterize(matrix, levels):
    # Reduce colors to given number of levels
    if levels < 2 or levels > 256:
        return matrix
    
    if not matrix or not matrix[0]:
        return matrix
    
    height = len(matrix)
    width = len(matrix[0])
    result = [[0] * width for _ in range(height)]
    levels_factor = 256 // levels
    
    for y in range(height):
        for x in range(width):
            level = matrix[y][x] // levels_factor
            result[y][x] = min(255, level * levels_factor)
    
    return result


def gamma_correct(matrix, gamma):
    # Adjust brightness with gamma
    if not matrix or not matrix[0] or gamma <= 0:
        return matrix
    
    height = len(matrix)
    width = len(matrix[0])
    result = [[0] * width for _ in range(height)]
    
    for y in range(height):
        for x in range(width):
            # Convert to 0-1, apply gamma, back to 0-255
            norm = matrix[y][x] / 255.0
            corrected = (norm ** (1.0 / gamma)) * 255
            result[y][x] = int(corrected)
    
    return result