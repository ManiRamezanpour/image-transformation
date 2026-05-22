# Scale matrices up or down - bilinear interpolation for smooth results

def scale_matrix(matrix, scale_x, scale_y=None, fill_value=0):
    """
   scale the matrix up or down by the given scale factor.
   Do not use Image.resize or similar build-in methods,
   output is a new matrix after scaling.
   """
    # Default to uniform scaling if only one factor given
    if scale_y is None:
        scale_y = scale_x
    
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0
    
    if not matrix or not matrix[0]:
        return matrix
    
    new_width = max(1, int(width * scale_x))
    new_height = max(1, int(height * scale_y))
    
    scaled = [[fill_value] * new_width for _ in range(new_height)]
    
    # Map back to original coordinates and interpolate
    for y_new in range(new_height):
        for x_new in range(new_width):
            x_orig = x_new / scale_x
            y_orig = y_new / scale_y
            
            x_floor = int(x_orig)
            y_floor = int(y_orig)
            x_ceil = min(x_floor + 1, width - 1)
            y_ceil = min(y_floor + 1, height - 1)
            
            dx = x_orig - x_floor
            dy = y_orig - y_floor
            
            v00 = matrix[y_floor][x_floor]
            v10 = matrix[y_floor][x_ceil]
            v01 = matrix[y_ceil][x_floor]
            v11 = matrix[y_ceil][x_ceil]
            
            value = (1 - dx) * (1 - dy) * v00 + \
                    dx * (1 - dy) * v10 + \
                    (1 - dx) * dy * v01 + \
                    dx * dy * v11
            
            scaled[y_new][x_new] = int(round(value))
    
    return scaled


def scale_nearest(matrix, scale_x, scale_y=None):
    # Fast version - just use nearest pixel, no interpolation
    if scale_y is None:
        scale_y = scale_x
    
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0
    
    if not matrix or not matrix[0]:
        return matrix
    
    new_width = max(1, int(width * scale_x))
    new_height = max(1, int(height * scale_y))
    
    scaled = [[0] * new_width for _ in range(new_height)]
    
    for y_new in range(new_height):
        for x_new in range(new_width):
            x_orig = min(int(x_new / scale_x), width - 1)
            y_orig = min(int(y_new / scale_y), height - 1)
            scaled[y_new][x_new] = matrix[y_orig][x_orig]
    
    return scaled


def shrink_matrix(matrix, factor):
    # Reduce size by averaging pixel blocks
    if factor <= 1:
        return matrix
    
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0
    
    if not matrix or not matrix[0]:
        return matrix
    
    new_height = height // factor
    new_width = width // factor
    
    if new_height == 0 or new_width == 0:
        return [[0]]
    
    shrunk = [[0] * new_width for _ in range(new_height)]
    
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
    # Make bigger by repeating each pixel
    if factor <= 1:
        return matrix
    
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0
    
    if not matrix or not matrix[0]:
        return matrix
    
    new_height = height * factor
    new_width = width * factor
    
    expanded = [[fill_value] * new_width for _ in range(new_height)]
    
    for y_orig in range(height):
        for x_orig in range(width):
            for dy in range(factor):
                for dx in range(factor):
                    y_new = y_orig * factor + dy
                    x_new = x_orig * factor + dx
                    expanded[y_new][x_new] = matrix[y_orig][x_orig]
    
    return expanded
