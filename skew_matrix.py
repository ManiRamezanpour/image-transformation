"""
Image skewing transformations - shearing operations.
"""

import math


def skew_matrix_horizontal(matrix, angle_degrees, fill_value=0):
    """Apply horizontal skew (shear) transformation to matrix.
    
    Args:
        matrix (list of list): Input matrix
        angle_degrees (float): Skew angle in degrees
        fill_value (int): Value to fill displaced areas
        
    Returns:
        list of list: Skewed matrix
    """
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0
    
    if height == 0 or width == 0:
        return matrix
    
    angle_rad = math.radians(angle_degrees)
    tan_angle = math.tan(angle_rad)
    
    # Calculate new width needed for the skew
    max_offset = abs(tan_angle * height)
    new_width = int(width + max_offset) + 1
    
    skewed = [[fill_value for _ in range(new_width)] for _ in range(height)]
    
    for y in range(height):
        for x in range(width):
            # Calculate horizontal offset based on vertical position
            offset = int(tan_angle * y)
            new_x = x + offset
            
            if 0 <= new_x < new_width:
                skewed[y][new_x] = matrix[y][x]
    
    return skewed


def skew_matrix_vertical(matrix, angle_degrees, fill_value=0):
    """Apply vertical skew (shear) transformation to matrix.
    
    Args:
        matrix (list of list): Input matrix
        angle_degrees (float): Skew angle in degrees
        fill_value (int): Value to fill displaced areas
        
    Returns:
        list of list: Skewed matrix
    """
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0
    
    if height == 0 or width == 0:
        return matrix
    
    angle_rad = math.radians(angle_degrees)
    tan_angle = math.tan(angle_rad)
    
    # Calculate new height needed for the skew
    max_offset = abs(tan_angle * width)
    new_height = int(height + max_offset) + 1
    
    skewed = [[fill_value for _ in range(width)] for _ in range(new_height)]
    
    for y in range(height):
        for x in range(width):
            # Calculate vertical offset based on horizontal position
            offset = int(tan_angle * x)
            new_y = y + offset
            
            if 0 <= new_y < new_height:
                skewed[new_y][x] = matrix[y][x]
    
    return skewed


def skew_matrix(matrix, angle_x_degrees=0, angle_y_degrees=0, fill_value=0):
    """Apply both horizontal and vertical skew to matrix.
    
    Args:
        matrix (list of list): Input matrix
        angle_x_degrees (float): Horizontal skew angle in degrees
        angle_y_degrees (float): Vertical skew angle in degrees
        fill_value (int): Value to fill displaced areas
        
    Returns:
        list of list: Skewed matrix
    """
    # Apply horizontal skew first
    if angle_x_degrees != 0:
        matrix = skew_matrix_horizontal(matrix, angle_x_degrees, fill_value)
    
    # Then apply vertical skew
    if angle_y_degrees != 0:
        matrix = skew_matrix_vertical(matrix, angle_y_degrees, fill_value)
    
    return matrix


def skew_matrix_interpolated(matrix, angle_degrees, direction='horizontal', fill_value=0):
    """Apply skew transformation with interpolation for smoother results.
    
    Args:
        matrix (list of list): Input matrix
        angle_degrees (float): Skew angle in degrees
        direction (str): 'horizontal' or 'vertical'
        fill_value (int): Value to fill displaced areas
        
    Returns:
        list of list: Skewed matrix
    """
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0
    
    if height == 0 or width == 0:
        return matrix
    
    angle_rad = math.radians(angle_degrees)
    tan_angle = math.tan(angle_rad)
    
    if direction == 'horizontal':
        max_offset = abs(tan_angle * height)
        new_width = int(width + max_offset) + 1
        skewed = [[fill_value for _ in range(new_width)] for _ in range(height)]
        
        for y in range(height):
            for x in range(width):
                # Precise offset calculation
                offset_float = tan_angle * y
                offset_int = int(offset_float)
                offset_frac = offset_float - offset_int
                
                new_x = x + offset_int
                
                # Place pixel at new position
                if 0 <= new_x < new_width:
                    skewed[y][new_x] = matrix[y][x]
                
                # Blend with adjacent pixel for smoother transition
                if offset_frac > 0 and 0 <= new_x + 1 < new_width:
                    # Simple blend (can be improved)
                    blended_value = int(matrix[y][x] * (1 - offset_frac))
                    if skewed[y][new_x + 1] == fill_value:
                        skewed[y][new_x + 1] = blended_value
    
    elif direction == 'vertical':
        max_offset = abs(tan_angle * width)
        new_height = int(height + max_offset) + 1
        skewed = [[fill_value for _ in range(width)] for _ in range(new_height)]
        
        for y in range(height):
            for x in range(width):
                # Precise offset calculation
                offset_float = tan_angle * x
                offset_int = int(offset_float)
                offset_frac = offset_float - offset_int
                
                new_y = y + offset_int
                
                # Place pixel at new position
                if 0 <= new_y < new_height:
                    skewed[new_y][x] = matrix[y][x]
                
                # Blend with adjacent pixel
                if offset_frac > 0 and 0 <= new_y + 1 < new_height:
                    blended_value = int(matrix[y][x] * (1 - offset_frac))
                    if skewed[new_y + 1][x] == fill_value:
                        skewed[new_y + 1][x] = blended_value
    
    return skewed
