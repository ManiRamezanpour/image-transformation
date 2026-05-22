import math

# Rotate matrix by angle around a center point
# Not using PIL Image.rotate - doing it manually

def rotate_matrix(matrix, angle_degrees, center_x=None, center_y=None, fill_value=0):
    """
    Rotate the matrix by given angle (in degrees) around
    the specified point. The point is a vector with the
    x and y value. DO no use Image-rotate or similar methods.
    output is a new matrix after rotation, this matrix can
    have different sizes
    """
    # Default to center of matrix if no center specified
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0
    
    if not matrix or not matrix[0]:
        return matrix
    
    if center_x is None:
        center_x = (width - 1) / 2.0
    if center_y is None:
        center_y = (height - 1) / 2.0
    
    angle_rad = math.radians(angle_degrees)
    cos_a = math.cos(angle_rad)
    sin_a = math.sin(angle_rad)
    
    rotated = [[fill_value] * width for _ in range(height)]
    
    # For each output pixel, ap it back to input using inverse rotation
    for y_out in range(height):
        for x_out in range(width):
            # Shift to center, rotate, shift back
            x_centered = x_out - center_x
            y_centered = y_out - center_y
            
            x_rotated = x_centered * cos_a + y_centered * sin_a
            y_rotated = -x_centered * sin_a + y_centered * cos_a
            
            x_in = x_rotated + center_x
            y_in = y_rotated + center_y
            
            # Bilinear interpolation for smoothness
            x_floor = int(math.floor(x_in))
            y_floor = int(math.floor(y_in))
            x_ceil = x_floor + 1
            y_ceil = y_floor + 1
            
            if 0 <= x_floor < width and 0 <= y_floor < height:
                dx = x_in - x_floor
                dy = y_in - y_floor
                
                v00 = matrix[y_floor][x_floor]
                v10 = matrix[y_floor][x_ceil] if x_ceil < width else v00
                v01 = matrix[y_ceil][x_floor] if y_ceil < height else v00
                v11 = matrix[y_ceil][x_ceil] if x_ceil < width and y_ceil < height else v00
                
                value = (1 - dx) * (1 - dy) * v00 + dx * (1 - dy) * v10 + \
                        (1 - dx) * dy * v01 + dx * dy * v11
                
                rotated[y_out][x_out] = int(round(value))
            elif x_floor == width - 1 and 0 <= y_floor < height:
                rotated[y_out][x_out] = matrix[y_floor][x_floor]
            elif y_floor == height - 1 and 0 <= x_floor < width:
                rotated[y_out][x_out] = matrix[y_floor][x_floor]
    
    return rotated


def rotate_matrix_nearest(matrix, angle_degrees, center_x=None, center_y=None, fill_value=0):
    """Rotate a 2D matrix using nearest neighbor interpolation (faster but lower quality).
    
    Args:
        matrix (list of list): Input matrix
        angle_degrees (float): Rotation angle in degrees
        center_x (int, optional): X coordinate of rotation center
        center_y (int, optional): Y coordinate of rotation center
        fill_value (int): Value to fill empty areas
        
    Returns:
        list of list: Rotated matrix
    """
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0
    
    if height == 0 or width == 0:
        return matrix
    
    if center_x is None:
        center_x = (width - 1) / 2.0
    if center_y is None:
        center_y = (height - 1) / 2.0
    
    angle_rad = math.radians(angle_degrees)
    cos_a = math.cos(angle_rad)
    sin_a = math.sin(angle_rad)
    
    rotated = [[fill_value for _ in range(width)] for _ in range(height)]
    
    for y_out in range(height):
        for x_out in range(width):
            x_centered = x_out - center_x
            y_centered = y_out - center_y
            
            x_rotated = x_centered * cos_a + y_centered * sin_a
            y_rotated = -x_centered * sin_a + y_centered * cos_a
            
            x_in = int(round(x_rotated + center_x))
            y_in = int(round(y_rotated + center_y))
            
            if 0 <= x_in < width and 0 <= y_in < height:
                rotated[y_out][x_out] = matrix[y_in][x_in]
    
    return rotated