
"""
IMAGE PROCESSING PIPELINE
Starter code for image transformation project
"""

from PIL import Image
from image_proccessing.image_to_matrix import load_image_as_rgb_matrices
from image_proccessing.image_transformation import save_rgb_matrices_as_image

# Import transformation functions
from rotate_matrix import rotate_matrix
from scale_matrix import scale_matrix
from skew_matrix import skew_matrix
from matrix.Matrix_transpose import (
    transpose_matrix, flip_matrix_horizontal, flip_matrix_vertical
)
from to_grayscale import rgb_to_grayscale
from edge_detection import sobel_edge_detection
from transform_matrix import apply_brightness, apply_contrast


def main():
    import os
    
    # Create output directory
    os.makedirs("output", exist_ok=True)
    
    # TODO: Load the image using Image.open.
    image_path = input("\nEnter image path: ").strip()
    if not image_path:
        print("✗ No image provided")
        return
    
    # TODO: Convert the image to a matrix.
    print("Loading image...")
    try:
        red, green, blue, height, width = load_image_as_rgb_matrices(image_path)
        print(f"✓ Loaded: {width}x{height} pixels")
    except Exception as e:
        print(f"✗ Error: {e}")
        return
    
    # TODO: Ask the user for the type of transformation and corresponding parameters.
    print("\nTransformations:")
    print("  1. Rotation (45°)")
    print("  2. Scaling (0.75x)")
    print("  3. Skewing (20°)")
    print("  4. Transpose")
    print("  5. Flip Horizontal")
    print("  6. Flip Vertical")
    print("  7. Grayscale")
    print("  8. Edge Detection")
    print("  9. Brightness (+50)")
    print(" 10. Contrast (1.5x)")
    
    choice = input("\nSelect (1-10): ").strip()
    
    # TODO: Call the appropriate transformation function.
    if choice == "1":
        red = rotate_matrix(red, 45)
        green = rotate_matrix(green, 45)
        blue = rotate_matrix(blue, 45)
        print("✓ Rotated 45°")
    
    elif choice == "2":
        red = scale_matrix(red, 0.75, 0.75)
        green = scale_matrix(green, 0.75, 0.75)
        blue = scale_matrix(blue, 0.75, 0.75)
        print("✓ Scaled 0.75x")
    
    elif choice == "3":
        red = skew_matrix(red, 20, 0)
        green = skew_matrix(green, 20, 0)
        blue = skew_matrix(blue, 20, 0)
        print("✓ Skewed 20°")
    
    elif choice == "4":
        red = transpose_matrix(red)
        green = transpose_matrix(green)
        blue = transpose_matrix(blue)
        print("✓ Transposed")
    
    elif choice == "5":
        red = flip_matrix_horizontal(red)
        green = flip_matrix_horizontal(green)
        blue = flip_matrix_horizontal(blue)
        print("✓ Flipped horizontal")
    
    elif choice == "6":
        red = flip_matrix_vertical(red)
        green = flip_matrix_vertical(green)
        blue = flip_matrix_vertical(blue)
        print("✓ Flipped vertical")
    
    elif choice == "7":
        gray = rgb_to_grayscale(red, green, blue)
        red = gray
        green = gray
        blue = gray
        print("✓ Converted to grayscale")
    
    elif choice == "8":
        gray = rgb_to_grayscale(red, green, blue)
        edges = sobel_edge_detection(gray)
        red = edges
        green = edges
        blue = edges
        print("✓ Edge detection applied")
    
    elif choice == "9":
        red = apply_brightness(red, 50)
        green = apply_brightness(green, 50)
        blue = apply_brightness(blue, 50)
        print("✓ Brightness +50")
    
    elif choice == "10":
        red = apply_contrast(red, 1.5)
        green = apply_contrast(green, 1.5)
        blue = apply_contrast(blue, 1.5)
        print("✓ Contrast 1.5x")
    
    else:
        print("✗ Invalid choice")
        return
    
    # TODO: Convert the matrix back to an image.
    # (Image.new is used inside save_rgb_matrices_as_image)
    
    # TODO: Save the output image.
    output_name = input("\nOutput filename [output.png]: ").strip()
    if not output_name:
        output_name = "output.png"
    
    try:
        save_rgb_matrices_as_image(red, green, blue, f"output/{output_name}")
        print(f"✓ Saved: output/{output_name}")
    except Exception as e:
        print(f"✗ Error saving: {e}")


if __name__ == "__main__":
    main()