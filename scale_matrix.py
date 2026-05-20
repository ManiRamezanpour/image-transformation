"""
Image scaling transformations - implementing bilinear interpolation for smooth scaling.
"""


def scale_matrix(matrix, scale_x, scale_y=None, fill_value=0):
    """Scale a 2D matrix by specified factors.
    
    Args:
        matrix (list of list): Input matrix
        scale_x (float): Horizontal scaling factor (< 1 shrinks, > 1 enlarges)
        scale_y (float, optional): Vertical scaling factor. If None, uses scale_x
        fill_value (int): Value to fill when upscaling
        
    Returns:
        list of list: Scaled matrix
    """
    if scale_y is None:
        scale_y = scale_x
    
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0
    
    if height == 0 or width == 0:
        return matrix
    
    # Calculate new dimensions
    new_width = max(1, int(width * scale_x))
    new_height = max(1, int(height * scale_y))
    
    # Create output matrix
    scaled = [[fill_value for _ in range(new_width)] for _ in range(new_height)]
    
    # Use inverse mapping with bilinear interpolation
    for y_new in range(new_height):
        for x_new in range(new_width):
            # Map back to original coordinates
            x_orig = x_new / scale_x
            y_orig = y_new / scale_y
            
            # Bilinear interpolation
            x_floor = int(x_orig)
            y_floor = int(y_orig)
            x_ceil = min(x_floor + 1, width - 1)
            y_ceil = min(y_floor + 1, height - 1)
            
            dx = x_orig - x_floor
            dy = y_orig - y_floor
            
            # Get corner values
            v00 = matrix[y_floor][x_floor]
            v10 = matrix[y_floor][x_ceil]
            v01 = matrix[y_ceil][x_floor]
            v11 = matrix[y_ceil][x_ceil]
            
            # Bilinear interpolation formula
            value = (1 - dx) * (1 - dy) * v00 + \
                    dx * (1 - dy) * v10 + \
                    (1 - dx) * dy * v01 + \
                    dx * dy * v11
            
            scaled[y_new][x_new] = int(round(value))
    
    return scaled


def scale_matrix_nearest(matrix, scale_x, scale_y=None):
    """Scale matrix using nearest neighbor interpolation (faster but blockier).
    
    Args:
        matrix (list of list): Input matrix
        scale_x (float): Horizontal scaling factor
        scale_y (float, optional): Vertical scaling factor
        
    Returns:
        list of list: Scaled matrix
    """
    if scale_y is None:
        scale_y = scale_x
    
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0
    
    if height == 0 or width == 0:
        return matrix
    
    new_width = max(1, int(width * scale_x))
    new_height = max(1, int(height * scale_y))
    
    scaled = [[0 for _ in range(new_width)] for _ in range(new_height)]
    
    for y_new in range(new_height):
        for x_new in range(new_width):
            x_orig = int(x_new / scale_x)
            y_orig = int(y_new / scale_y)
            
            # Clamp to valid range
            x_orig = min(x_orig, width - 1)
            y_orig = min(y_orig, height - 1)
            
            scaled[y_new][x_new] = matrix[y_orig][x_orig]
    
    return scaled


def shrink_matrix(matrix, factor):
    """Shrink matrix by averaging pixel blocks.
    
    Args:
        matrix (list of list): Input matrix
        factor (int): Shrinking factor (2 = half size, 3 = third size, etc)
        
    Returns:
        list of list: Shrunk matrix
    """
    if factor <= 1:
        return matrix
    
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0
    
    if height == 0 or width == 0:
        return matrix
    
    new_height = height // factor
    new_width = width // factor
    
    if new_height == 0 or new_width == 0:
        return [[0]]
    
    shrunk = [[0 for _ in range(new_width)] for _ in range(new_height)]
    
    # Average pixels in each block
    for y_new in range(new_height):
        for x_new in range(new_width):
            total = 0
            count = 0
            
            for dy in range(factor):
                for dx in range(factor):
                    y_src = y_new * factor + dy
                    x_src = x_new * factor + dx
                    
                    if y_src < height and x_src < width:
                        total += matrix[y_src][x_src]
                        count += 1
            
            shrunk[y_new][x_new] = int(total / count) if count > 0 else 0
    
    return shrunk


def expand_matrix(matrix, factor, fill_value=0):
    """Expand matrix by repeating pixels.
    
    Args:
        matrix (list of list): Input matrix
        factor (int): Expansion factor
        fill_value (int): Fill value for expanded areas
        
    Returns:
        list of list: Expanded matrix
    """
    if factor <= 1:
        return matrix
    
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0
    
    if height == 0 or width == 0:
        return matrix
    
    new_height = height * factor
    new_width = width * factor
    
    expanded = [[fill_value for _ in range(new_width)] for _ in range(new_height)]
    
    for y_orig in range(height):
        for x_orig in range(width):
            for dy in range(factor):
                for dx in range(factor):
                    y_new = y_orig * factor + dy
                    x_new = x_orig * factor + dx
                    expanded[y_new][x_new] = matrix[y_orig][x_orig]
    
    return expanded
