"""
Edge detection algorithms - using convolution kernels.
"""


def sobel_edge_detection(matrix):
    """Detect edges using Sobel operator.
    
    Uses Sobel kernels to compute gradients in X and Y directions.
    
    Args:
        matrix (list of list): Input grayscale matrix
        
    Returns:
        list of list: Edge-detected matrix with gradient magnitudes
    """
    if not matrix or len(matrix) < 3 or len(matrix[0]) < 3:
        return matrix
    
    height = len(matrix)
    width = len(matrix[0])
    
    # Sobel kernels
    sobel_x = [[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]]
    
    sobel_y = [[-1, -2, -1],
               [0, 0, 0],
               [1, 2, 1]]
    
    edges = [[0 for _ in range(width)] for _ in range(height)]
    
    # Apply Sobel operator (skip borders)
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            gx = 0
            gy = 0
            
            # Convolve with kernels
            for ky in range(-1, 2):
                for kx in range(-1, 2):
                    pixel = matrix[y + ky][x + kx]
                    gx += pixel * sobel_x[ky + 1][kx + 1]
                    gy += pixel * sobel_y[ky + 1][kx + 1]
            
            # Calculate magnitude
            magnitude = int((gx ** 2 + gy ** 2) ** 0.5)
            edges[y][x] = min(255, magnitude)
    
    return edges


def laplacian_edge_detection(matrix):
    """Detect edges using Laplacian operator.
    
    Laplacian detects edges by finding zero crossings.
    
    Args:
        matrix (list of list): Input grayscale matrix
        
    Returns:
        list of list: Edge-detected matrix
    """
    if not matrix or len(matrix) < 3 or len(matrix[0]) < 3:
        return matrix
    
    height = len(matrix)
    width = len(matrix[0])
    
    # Laplacian kernel (8-neighbor)
    laplacian_kernel = [[0, -1, 0],
                        [-1, 4, -1],
                        [0, -1, 0]]
    
    edges = [[0 for _ in range(width)] for _ in range(height)]
    
    # Apply Laplacian (skip borders)
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            result = 0
            
            # Convolve with kernel
            for ky in range(-1, 2):
                for kx in range(-1, 2):
                    pixel = matrix[y + ky][x + kx]
                    result += pixel * laplacian_kernel[ky + 1][kx + 1]
            
            # Normalize
            edges[y][x] = min(255, max(0, abs(result)))
    
    return edges


def prewitt_edge_detection(matrix):
    """Detect edges using Prewitt operator.
    
    Similar to Sobel but with simpler kernels.
    
    Args:
        matrix (list of list): Input grayscale matrix
        
    Returns:
        list of list: Edge-detected matrix
    """
    if not matrix or len(matrix) < 3 or len(matrix[0]) < 3:
        return matrix
    
    height = len(matrix)
    width = len(matrix[0])
    
    # Prewitt kernels
    prewitt_x = [[-1, 0, 1],
                 [-1, 0, 1],
                 [-1, 0, 1]]
    
    prewitt_y = [[-1, -1, -1],
                 [0, 0, 0],
                 [1, 1, 1]]
    
    edges = [[0 for _ in range(width)] for _ in range(height)]
    
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            gx = 0
            gy = 0
            
            for ky in range(-1, 2):
                for kx in range(-1, 2):
                    pixel = matrix[y + ky][x + kx]
                    gx += pixel * prewitt_x[ky + 1][kx + 1]
                    gy += pixel * prewitt_y[ky + 1][kx + 1]
            
            magnitude = int((gx ** 2 + gy ** 2) ** 0.5)
            edges[y][x] = min(255, magnitude)
    
    return edges


def canny_edge_detection(matrix, low_threshold=50, high_threshold=150):
    """Detect edges using Canny edge detection algorithm.
    
    Simplified Canny without non-maximum suppression.
    
    Args:
        matrix (list of list): Input grayscale matrix
        low_threshold (int): Low threshold for edge detection
        high_threshold (int): High threshold for edge detection
        
    Returns:
        list of list: Binary edge map (0 or 255)
    """
    if not matrix or len(matrix) < 3 or len(matrix[0]) < 3:
        return matrix
    
    height = len(matrix)
    width = len(matrix[0])
    
    # Step 1: Apply Gaussian blur (simple 3x3 averaging)
    blur_kernel = [[1, 2, 1],
                   [2, 4, 2],
                   [1, 2, 1]]
    
    blurred = [[0 for _ in range(width)] for _ in range(height)]
    
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            sum_val = 0
            for ky in range(-1, 2):
                for kx in range(-1, 2):
                    sum_val += matrix[y + ky][x + kx] * blur_kernel[ky + 1][kx + 1]
            blurred[y][x] = sum_val // 16
    
    # Step 2: Calculate gradients using Sobel
    sobel_x = [[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]]
    
    sobel_y = [[-1, -2, -1],
               [0, 0, 0],
               [1, 2, 1]]
    
    edges = [[0 for _ in range(width)] for _ in range(height)]
    
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            gx = 0
            gy = 0
            
            for ky in range(-1, 2):
                for kx in range(-1, 2):
                    pixel = blurred[y + ky][x + kx]
                    gx += pixel * sobel_x[ky + 1][kx + 1]
                    gy += pixel * sobel_y[ky + 1][kx + 1]
            
            magnitude = int((gx ** 2 + gy ** 2) ** 0.5)
            
            # Step 3: Apply double threshold
            if magnitude >= high_threshold:
                edges[y][x] = 255
            elif magnitude >= low_threshold:
                edges[y][x] = 128  # Weak edge
            else:
                edges[y][x] = 0
    
    return edges


def edge_detection(matrix):
    """Default edge detection using Sobel operator.
    
    Args:
        matrix (list of list): Input matrix (can be RGB or grayscale)
        
    Returns:
        list of list: Edge-detected matrix
    """
    return sobel_edge_detection(matrix)


def threshold_edges(edge_matrix, threshold=100):
    """Apply threshold to edge detection results to create binary edge map.
    
    Args:
        edge_matrix (list of list): Edge detection result
        threshold (int): Threshold value
        
    Returns:
        list of list: Binary edge map
    """
    height = len(edge_matrix)
    width = len(edge_matrix[0]) if height > 0 else 0
    
    if height == 0 or width == 0:
        return edge_matrix
    
    thresholded = [[0 for _ in range(width)] for _ in range(height)]
    
    for y in range(height):
        for x in range(width):
            thresholded[y][x] = 255 if edge_matrix[y][x] >= threshold else 0
    
    return thresholded