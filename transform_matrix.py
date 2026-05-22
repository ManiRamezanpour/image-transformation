"""
Standard matrix transformations - pixel value operations.
"""


def transform_matrix(matrix, operation='double', factor=2):
    """Apply a standard transformation to matrix values.
    
    Args:
        matrix (list of list): Input matrix
        operation (str): Type of transformation
            - 'double': Double pixel values
            - 'halve': Halve pixel values
            - 'scale': Scale by factor
            - 'invert': Invert pixel values (255 - value)
            - 'threshold': Binary threshold
        factor (float): Factor for scaling operations
        
    Returns:
        list of list: Transformed matrix
    """
    if not matrix:
        return matrix
    
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0
    
    if height == 0 or width == 0:
        return matrix
    
    transformed = [[0 for _ in range(width)] for _ in range(height)]
    
    if operation == 'double':
        for y in range(height):
            for x in range(width):
                value = matrix[y][x] * 2
                transformed[y][x] = min(255, value)
    
    elif operation == 'halve':
        for y in range(height):
            for x in range(width):
                transformed[y][x] = matrix[y][x] // 2
    
    elif operation == 'scale':
        for y in range(height):
            for x in range(width):
                value = int(matrix[y][x] * factor)
                transformed[y][x] = min(255, max(0, value))
    
    elif operation == 'invert':
        for y in range(height):
            for x in range(width):
                transformed[y][x] = 255 - matrix[y][x]
    
    elif operation == 'threshold':
        threshold = int(factor)
        for y in range(height):
            for x in range(width):
                transformed[y][x] = 255 if matrix[y][x] >= threshold else 0
    
    else:
        # Default: return copy
        for y in range(height):
            for x in range(width):
                transformed[y][x] = matrix[y][x]
    
    return transformed

def posterize_matrix(matrix, levels):
    """Reduce number of tones in matrix (posterization effect).
    
    Args:
        matrix (list of list): Input matrix
        levels (int): Number of levels (2-256)
        
    Returns:
        list of list: Posterized matrix
    """
    if levels < 2 or levels > 256:
        return matrix
    
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0
    
    if height == 0 or width == 0:
        return matrix
    
    posterized = [[0 for _ in range(width)] for _ in range(height)]
    levels_factor = 256 // levels
    
    for y in range(height):
        for x in range(width):
            # Quantize to level
            level = matrix[y][x] // levels_factor
            posterized[y][x] = min(255, level * levels_factor)
    
    return posterized


def gamma_correction(matrix, gamma):
    """Apply gamma correction to matrix.
    
    Args:
        matrix (list of list): Input matrix
        gamma (float): Gamma value (< 1.0 brightens, > 1.0 darkens)
        
    Returns:
        list of list: Gamma corrected matrix
    """
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0
    
    if height == 0 or width == 0 or gamma <= 0:
        return matrix
    
    corrected = [[0 for _ in range(width)] for _ in range(height)]
    
    for y in range(height):
        for x in range(width):
            # Normalize to 0-1, apply gamma, scale back to 0-255
            normalized = matrix[y][x] / 255.0
            corrected_val = (normalized ** (1.0 / gamma)) * 255
            corrected[y][x] = int(corrected_val)
    
    return corrected