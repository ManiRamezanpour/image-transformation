"""
Grayscale conversion functions for color to grayscale transformation.
"""


def rgb_to_grayscale_luminosity(red_matrix, green_matrix, blue_matrix):
    """Convert RGB matrices to grayscale using luminosity method.
    
    Luminosity method weights colors based on human eye sensitivity.
    Formula: Gray = 0.299*R + 0.587*G + 0.114*B
    
    Args:
        red_matrix (list of list): Red channel matrix
        green_matrix (list of list): Green channel matrix
        blue_matrix (list of list): Blue channel matrix
        
    Returns:
        list of list: Grayscale matrix
    """
    height = len(red_matrix)
    width = len(red_matrix[0]) if height > 0 else 0
    
    if height == 0 or width == 0:
        return red_matrix
    
    grayscale = [[0 for _ in range(width)] for _ in range(height)]
    
    for y in range(height):
        for x in range(width):
            gray = int(0.299 * red_matrix[y][x] + 
                      0.587 * green_matrix[y][x] + 
                      0.114 * blue_matrix[y][x])
            grayscale[y][x] = min(255, max(0, gray))
    
    return grayscale


def rgb_to_grayscale_average(red_matrix, green_matrix, blue_matrix):
    """Convert RGB matrices to grayscale using average method.
    
    Simple average of RGB values.
    Formula: Gray = (R + G + B) / 3
    
    Args:
        red_matrix (list of list): Red channel matrix
        green_matrix (list of list): Green channel matrix
        blue_matrix (list of list): Blue channel matrix
        
    Returns:
        list of list: Grayscale matrix
    """
    height = len(red_matrix)
    width = len(red_matrix[0]) if height > 0 else 0
    
    if height == 0 or width == 0:
        return red_matrix
    
    grayscale = [[0 for _ in range(width)] for _ in range(height)]
    
    for y in range(height):
        for x in range(width):
            gray = (red_matrix[y][x] + green_matrix[y][x] + blue_matrix[y][x]) // 3
            grayscale[y][x] = min(255, max(0, gray))
    
    return grayscale


def rgb_to_grayscale_lightness(red_matrix, green_matrix, blue_matrix):
    """Convert RGB matrices to grayscale using lightness method.
    
    Lightness method uses average of max and min RGB values.
    Formula: Gray = (max(R,G,B) + min(R,G,B)) / 2
    
    Args:
        red_matrix (list of list): Red channel matrix
        green_matrix (list of list): Green channel matrix
        blue_matrix (list of list): Blue channel matrix
        
    Returns:
        list of list: Grayscale matrix
    """
    height = len(red_matrix)
    width = len(red_matrix[0]) if height > 0 else 0
    
    if height == 0 or width == 0:
        return red_matrix
    
    grayscale = [[0 for _ in range(width)] for _ in range(height)]
    
    for y in range(height):
        for x in range(width):
            max_val = max(red_matrix[y][x], green_matrix[y][x], blue_matrix[y][x])
            min_val = min(red_matrix[y][x], green_matrix[y][x], blue_matrix[y][x])
            gray = (max_val + min_val) // 2
            grayscale[y][x] = min(255, max(0, gray))
    
    return grayscale


def rgb_to_grayscale_desaturation(red_matrix, green_matrix, blue_matrix):
    """Convert RGB matrices to grayscale using desaturation method.
    
    Uses average of max and min RGB values (same as lightness).
    
    Args:
        red_matrix (list of list): Red channel matrix
        green_matrix (list of list): Green channel matrix
        blue_matrix (list of list): Blue channel matrix
        
    Returns:
        list of list: Grayscale matrix
    """
    return rgb_to_grayscale_lightness(red_matrix, green_matrix, blue_matrix)


def rgb_to_grayscale_decompose_red(red_matrix, green_matrix, blue_matrix):
    """Convert to grayscale using only red channel.
    
    Args:
        red_matrix (list of list): Red channel matrix
        green_matrix (list of list): Green channel matrix
        blue_matrix (list of list): Blue channel matrix
        
    Returns:
        list of list: Grayscale matrix (red channel values)
    """
    height = len(red_matrix)
    width = len(red_matrix[0]) if height > 0 else 0
    
    if height == 0 or width == 0:
        return red_matrix
    
    # Copy red channel
    grayscale = [[red_matrix[y][x] for x in range(width)] for y in range(height)]
    return grayscale


def rgb_to_grayscale_decompose_green(red_matrix, green_matrix, blue_matrix):
    """Convert to grayscale using only green channel.
    
    Args:
        red_matrix (list of list): Red channel matrix
        green_matrix (list of list): Green channel matrix
        blue_matrix (list of list): Blue channel matrix
        
    Returns:
        list of list: Grayscale matrix (green channel values)
    """
    height = len(green_matrix)
    width = len(green_matrix[0]) if height > 0 else 0
    
    if height == 0 or width == 0:
        return green_matrix
    
    # Copy green channel
    grayscale = [[green_matrix[y][x] for x in range(width)] for y in range(height)]
    return grayscale


def rgb_to_grayscale_decompose_blue(red_matrix, green_matrix, blue_matrix):
    """Convert to grayscale using only blue channel.
    
    Args:
        red_matrix (list of list): Red channel matrix
        green_matrix (list of list): Green channel matrix
        blue_matrix (list of list): Blue channel matrix
        
    Returns:
        list of list: Grayscale matrix (blue channel values)
    """
    height = len(blue_matrix)
    width = len(blue_matrix[0]) if height > 0 else 0
    
    if height == 0 or width == 0:
        return blue_matrix
    
    # Copy blue channel
    grayscale = [[blue_matrix[y][x] for x in range(width)] for y in range(height)]
    return grayscale


def rgb_to_grayscale(red_matrix, green_matrix, blue_matrix, method='luminosity'):
    """Convert RGB matrices to grayscale using specified method.
    
    Args:
        red_matrix (list of list): Red channel matrix
        green_matrix (list of list): Green channel matrix
        blue_matrix (list of list): Blue channel matrix
        method (str): Conversion method
            - 'luminosity': Luminosity method (default, most accurate)
            - 'average': Simple average
            - 'lightness': Lightness method
            - 'desaturation': Desaturation method
            - 'red', 'green', 'blue': Extract single channel
            
    Returns:
        list of list: Grayscale matrix
    """
    if method == 'luminosity':
        return rgb_to_grayscale_luminosity(red_matrix, green_matrix, blue_matrix)
    elif method == 'average':
        return rgb_to_grayscale_average(red_matrix, green_matrix, blue_matrix)
    elif method == 'lightness':
        return rgb_to_grayscale_lightness(red_matrix, green_matrix, blue_matrix)
    elif method == 'desaturation':
        return rgb_to_grayscale_desaturation(red_matrix, green_matrix, blue_matrix)
    elif method == 'red':
        return rgb_to_grayscale_decompose_red(red_matrix, green_matrix, blue_matrix)
    elif method == 'green':
        return rgb_to_grayscale_decompose_green(red_matrix, green_matrix, blue_matrix)
    elif method == 'blue':
        return rgb_to_grayscale_decompose_blue(red_matrix, green_matrix, blue_matrix)
    else:
        # Default to luminosity
        return rgb_to_grayscale_luminosity(red_matrix, green_matrix, blue_matrix)


# Alias for backward compatibility
def to_grayscale(matrix_red, matrix_green, matrix_blue):
    """Backward compatibility wrapper for rgb_to_grayscale."""
    return rgb_to_grayscale_luminosity(matrix_red, matrix_green, matrix_blue)