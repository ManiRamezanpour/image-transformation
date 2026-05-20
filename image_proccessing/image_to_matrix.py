from PIL import Image
import os

def load_image_as_rgb_matrices(image_path):
    """Load image and convert to separate R, G, B matrices.
    
    Args:
        image_path (str): Path to the image file
        
    Returns:
        tuple: (red_matrix, green_matrix, blue_matrix, height, width)
            Each matrix is a 2D list of integers (0-255)
        
    Raises:
        FileNotFoundError: If image file doesn't exist
        Exception: If image cannot be loaded
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")
    
    try:
        img = Image.open(image_path)
        width, height = img.size
        
        # Initialize matrices for R, G, B channels
        red_matrix = [[0 for _ in range(width)] for _ in range(height)]
        green_matrix = [[0 for _ in range(width)] for _ in range(height)]
        blue_matrix = [[0 for _ in range(width)] for _ in range(height)]
        
        # Extract pixel data (handle different image modes)
        pixels = img.load()
        for y in range(height):
            for x in range(width):
                pixel = pixels[x, y]
                
                # Handle different image modes manually
                if img.mode == 'RGB':
                    r, g, b = pixel
                elif img.mode == 'RGBA':
                    # For RGBA: if alpha is 0 (transparent), use white; otherwise use RGB
                    r, g, b, a = pixel
                    if a == 0:  # Transparent - use white background
                        r, g, b = 255, 255, 255
                elif img.mode == 'L':  # Grayscale
                    gray = pixel
                    r = g = b = gray
                elif img.mode == 'LA':  # Grayscale with alpha
                    gray, a = pixel
                    if a == 0:
                        r = g = b = 255
                    else:
                        r = g = b = gray
                else:  # Other modes - convert pixel to RGB manually
                    r = g = b = 0
                    if isinstance(pixel, tuple):
                        if len(pixel) >= 3:
                            r, g, b = pixel[0], pixel[1], pixel[2]
                        elif len(pixel) == 1:
                            r = g = b = pixel[0]
                    else:
                        r = g = b = pixel if isinstance(pixel, int) else 0
                
                red_matrix[y][x] = max(0, min(255, r))
                green_matrix[y][x] = max(0, min(255, g))
                blue_matrix[y][x] = max(0, min(255, b))
        
        return red_matrix, green_matrix, blue_matrix, height, width
    
    except Exception as e:
        raise Exception(f"Error loading image: {str(e)}")


def image_to_grayscale_matrix(image_path):
    """Convert image to grayscale matrix using luminosity method.
    
    Args:
        image_path (str): Path to the image file
        
    Returns:
        list of list of int: Grayscale matrix (2D list)
    """
    red_m, green_m, blue_m, height, width = load_image_as_rgb_matrices(image_path)
    
    grayscale = [[0 for _ in range(width)] for _ in range(height)]
    
    # Luminosity method: 0.299*R + 0.587*G + 0.114*B
    for y in range(height):
        for x in range(width):
            gray_value = int(0.299 * red_m[y][x] + 0.587 * green_m[y][x] + 0.114 * blue_m[y][x])
            grayscale[y][x] = min(255, max(0, gray_value))
    
    return grayscale


def normalize_matrix(matrix):
    """Normalize matrix values to 0-255 range.
    
    Args:
        matrix (list of list): Input matrix
        
    Returns:
        list of list: Normalized matrix with values in 0-255 range
    """
    if not matrix:
        return matrix
    
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0
    
    # Find min and max values
    min_val = float('inf')
    max_val = float('-inf')
    
    for row in matrix:
        for val in row:
            min_val = min(min_val, val)
            max_val = max(max_val, val)
    
    # If all values are the same, return matrix with 128
    if max_val == min_val:
        return [[128 for _ in range(width)] for _ in range(height)]
    
    # Normalize to 0-255 range
    normalized = [[0 for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            normalized_val = int(((matrix[y][x] - min_val) / (max_val - min_val)) * 255)
            normalized[y][x] = min(255, max(0, normalized_val))
    
    return normalized


def get_image_dimensions(image_path):
    """Get image dimensions without loading full pixel data.
    
    Args:
        image_path (str): Path to the image file
        
    Returns:
        tuple: (width, height)
    """
    img = Image.open(image_path)
    return img.size
