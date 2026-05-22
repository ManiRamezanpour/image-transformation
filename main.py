
from PIL import Image
from image_proccessing.image_to_matrix import load_image_as_rgb_matrices
from image_proccessing.image_transformation import save_rgb_matrices_as_image
from rotate_matrix import rotate_matrix
from scale_matrix import scale_matrix
from skew_matrix import skew_matrix
from matrix.Matrix_transpose import transpose_matrix
from to_grayscale import rgb_to_grayscale, grayscale_image
from edge_detection import sobel_edge_detection


def main():
    import os
    os.makedirs("output", exist_ok=True)
    
    image_path = input("\nEnter image path: ").strip()
    if not image_path:
        print("✗ No image provided")
        return
    
    print("Loading image...")
    try:
        red, green, blue, height, width = load_image_as_rgb_matrices(image_path)
        print(f"✓ Loaded: {width}x{height} pixels")
    except Exception as e:
        print(f"✗ Error: {e}")
        return
    
    print("\nTransformations:")
    print("  1. Rotation (45°)")
    print("  2. Scaling (0.75x)")
    print("  3. Skewing (20°)")
    print("  4. Transpose")
    print("  5. Grayscale")
    print("  6. Edge Detection")
    
    choice = input("\nSelect (1-6): ").strip()
    
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
        gray_img = grayscale_image(red, green, blue)
        output_name = input("\nOutput filename [grayscale.png]: ").strip()
        if not output_name:
            output_name = "grayscale.png"
        output_path = f"output/{output_name}"
        gray_img.save(output_path)
        print(f"✓ Saved grayscale to: {output_path}")
        gray_img.show()
        return
    
    elif choice == "6":
        gray = rgb_to_grayscale(red, green, blue)
        edges = sobel_edge_detection(gray)
        red = edges
        green = edges
        blue = edges
        print("✓ Edge detection applied")
    
    else:
        print("✗ Invalid choice")
        return
    
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