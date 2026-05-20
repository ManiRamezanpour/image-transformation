from PIL import Image
import os


def matrices_to_image(red_matrix, green_matrix, blue_matrix, output_path=None):
    """Convert RGB matrices back to image.
    
    Args:
        red_matrix (list of list): Red channel matrix
        green_matrix (list of list): Green channel matrix
        blue_matrix (list of list): Blue channel matrix
        output_path (str, optional): Path to save the image
        
    Returns:
        Image.Image: PIL Image object
    """
    height = len(red_matrix)
    width = len(red_matrix[0]) if height > 0 else 0
    
    # Create new image
    img = Image.new('RGB', (width, height))
    pixels = img.load()
    
    # Set pixel values from matrices
    for y in range(height):
        for x in range(width):
            r = int(min(255, max(0, red_matrix[y][x])))
            g = int(min(255, max(0, green_matrix[y][x])))
            b = int(min(255, max(0, blue_matrix[y][x])))
            pixels[x, y] = (r, g, b)
    
    # Save if output path provided
    if output_path:
        os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
        img.save(output_path)
        print(f"Image saved to: {output_path}")
    
    return img


def grayscale_matrix_to_image(matrix, output_path=None):
    """Convert grayscale matrix back to image.
    
    Args:
        matrix (list of list): Grayscale matrix
        output_path (str, optional): Path to save the image
        
    Returns:
        Image.Image: PIL Image object
    """
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0
    
    # Create new image
    img = Image.new('L', (width, height))
    pixels = img.load()
    
    # Set pixel values from matrix
    for y in range(height):
        for x in range(width):
            gray_value = int(min(255, max(0, matrix[y][x])))
            pixels[x, y] = gray_value
    
    # Save if output path provided
    if output_path:
        os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
        img.save(output_path)
        print(f"Image saved to: {output_path}")
    
    return img


def save_rgb_matrices_as_image(red_matrix, green_matrix, blue_matrix, output_path, format='PNG'):
    """Save RGB matrices as an image file.
    
    Args:
        red_matrix (list of list): Red channel matrix
        green_matrix (list of list): Green channel matrix
        blue_matrix (list of list): Blue channel matrix
        output_path (str): Path where to save the image
        format (str): Image format (PNG, JPEG, etc.)
    """
    height = len(red_matrix)
    width = len(red_matrix[0]) if height > 0 else 0
    
    img = Image.new('RGB', (width, height))
    pixels = img.load()
    
    for y in range(height):
        for x in range(width):
            r = int(min(255, max(0, red_matrix[y][x])))
            g = int(min(255, max(0, green_matrix[y][x])))
            b = int(min(255, max(0, blue_matrix[y][x])))
            pixels[x, y] = (r, g, b)
    
    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
    img.save(output_path, format=format)
    print(f"Image saved to: {output_path}")


def save_grayscale_matrix_as_image(matrix, output_path, format='PNG'):
    """Save grayscale matrix as an image file.
    
    Args:
        matrix (list of list): Grayscale matrix
        output_path (str): Path where to save the image
        format (str): Image format (PNG, JPEG, etc.)
    """
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0
    
    img = Image.new('L', (width, height))
    pixels = img.load()
    
    for y in range(height):
        for x in range(width):
            gray_value = int(min(255, max(0, matrix[y][x])))
            pixels[x, y] = gray_value
    
    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
    img.save(output_path, format=format)
    print(f"Image saved to: {output_path}")


def display_matrix_stats(matrix):
    """Display statistics about the matrix.
    
    Args:
        matrix (list of list): Input matrix
    """
    if not matrix:
        print("Empty matrix")
        return
    
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0
    
    # Calculate statistics
    all_values = []
    min_val = float('inf')
    max_val = float('-inf')
    
    for row in matrix:
        for val in row:
            all_values.append(val)
            min_val = min(min_val, val)
            max_val = max(max_val, val)
    
    mean_val = sum(all_values) / len(all_values) if all_values else 0
    variance = sum((x - mean_val) ** 2 for x in all_values) / len(all_values) if all_values else 0
    std_dev = variance ** 0.5
    
    print(f"\nMatrix Statistics:")
    print(f"  Dimensions: {height} x {width}")
    print(f"  Min value: {min_val:.2f}")
    print(f"  Max value: {max_val:.2f}")
    print(f"  Mean value: {mean_val:.2f}")
    print(f"  Std deviation: {std_dev:.2f}")
