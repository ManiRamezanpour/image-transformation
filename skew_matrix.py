# Skew/shear transformations for matrices

import math


def skew_horizontal(matrix, angle_degrees, fill_value=0):
    """
    Skew the matrix by given factos in x and y directions. Do not use any build-in transformations. Output is a new matrix after skewing
    """
    # Shift rows horizontally based on their position
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0
    
    if not matrix or not matrix[0]:
        return matrix
    
    angle_rad = math.radians(angle_degrees)
    tan_angle = math.tan(angle_rad)
    
    max_offset = abs(tan_angle * height)
    new_width = int(width + max_offset) + 1
    
    skewed = [[fill_value] * new_width for _ in range(height)]
    
    for y in range(height):
        for x in range(width):
            offset = int(tan_angle * y)
            new_x = x + offset
            
            if 0 <= new_x < new_width:
                skewed[y][new_x] = matrix[y][x]
    
    return skewed


def skew_vertical(matrix, angle_degrees, fill_value=0):
    # Shift columns vertically based on their position
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0
    
    if not matrix or not matrix[0]:
        return matrix
    
    angle_rad = math.radians(angle_degrees)
    tan_angle = math.tan(angle_rad)
    
    max_offset = abs(tan_angle * width)
    new_height = int(height + max_offset) + 1
    
    skewed = [[fill_value] * width for _ in range(new_height)]
    
    for y in range(height):
        for x in range(width):
            offset = int(tan_angle * x)
            new_y = y + offset
            
            if 0 <= new_y < new_height:
                skewed[new_y][x] = matrix[y][x]
    
    return skewed


def skew_matrix(matrix, angle_x_degrees=0, angle_y_degrees=0, fill_value=0):
    # Apply both horizontal and vertical skew
    if angle_x_degrees != 0:
        matrix = skew_horizontal(matrix, angle_x_degrees, fill_value)
    
    if angle_y_degrees != 0:
        matrix = skew_vertical(matrix, angle_y_degrees, fill_value)
    
    return matrix


def skew_interpolated(matrix, angle_degrees, direction='horizontal', fill_value=0):
    # Skew with interpolation for smoother blending
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0
    
    if not matrix or not matrix[0]:
        return matrix
    
    angle_rad = math.radians(angle_degrees)
    tan_angle = math.tan(angle_rad)
    
    if direction == 'horizontal':
        max_offset = abs(tan_angle * height)
        new_width = int(width + max_offset) + 1
        skewed = [[fill_value] * new_width for _ in range(height)]
        
        for y in range(height):
            for x in range(width):
                offset_float = tan_angle * y
                offset_int = int(offset_float)
                offset_frac = offset_float - offset_int
                
                new_x = x + offset_int
                
                if 0 <= new_x < new_width:
                    skewed[y][new_x] = matrix[y][x]
                
                if offset_frac > 0 and 0 <= new_x + 1 < new_width:
                    blended_value = int(matrix[y][x] * (1 - offset_frac))
                    if skewed[y][new_x + 1] == fill_value:
                        skewed[y][new_x + 1] = blended_value
    
    elif direction == 'vertical':
        max_offset = abs(tan_angle * width)
        new_height = int(height + max_offset) + 1
        skewed = [[fill_value] * width for _ in range(new_height)]
        
        for y in range(height):
            for x in range(width):
                offset_float = tan_angle * x
                offset_int = int(offset_float)
                offset_frac = offset_float - offset_int
                
                new_y = y + offset_int
                
                if 0 <= new_y < new_height:
                    skewed[new_y][x] = matrix[y][x]
                
                if offset_frac > 0 and 0 <= new_y + 1 < new_height:
                    blended_value = int(matrix[y][x] * (1 - offset_frac))
                    if skewed[new_y + 1][x] == fill_value:
                        skewed[new_y + 1][x] = blended_value
    
    return skewed
