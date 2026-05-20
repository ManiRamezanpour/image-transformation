"""
Example usage of the Image Processing Pipeline

This script demonstrates different ways to use the image processing system.
All transformations are implemented manually without Pillow's built-in methods.
"""

import sys
import os
from main import ImageProcessor


def example_1_rotation():
    """Example 1: Rotate image by 30 degrees."""
    print("\n" + "="*70)
    print("EXAMPLE 1: Image Rotation (30 degrees)")
    print("="*70)
    
    image_path = "test_image.jpg"
    
    if not os.path.exists(image_path):
        print(f"⚠️  Note: Test image '{image_path}' not found.")
        print("   Please provide your own image file.")
        return
    
    processor = ImageProcessor(image_path, output_dir="output/example1")
    
    if processor.load_image():
        processor.apply_transformation("rotate", angle=30)
        processor.save_result("rotated_30.png")


def example_2_scaling():
    """Example 2: Scale image to 75% size."""
    print("\n" + "="*70)
    print("EXAMPLE 2: Image Scaling (75%)")
    print("="*70)
    
    image_path = "test_image.jpg"
    
    if not os.path.exists(image_path):
        print(f"⚠️  Note: Test image '{image_path}' not found.")
        return
    
    processor = ImageProcessor(image_path, output_dir="output/example2")
    
    if processor.load_image():
        processor.apply_transformation("scale", scale_x=0.75, scale_y=0.75)
        processor.save_result("scaled_75.png")


def example_3_skewing():
    """Example 3: Apply horizontal skew of 30 degrees."""
    print("\n" + "="*70)
    print("EXAMPLE 3: Image Skewing (30 degrees)")
    print("="*70)
    
    image_path = "test_image.jpg"
    
    if not os.path.exists(image_path):
        print(f"⚠️  Note: Test image '{image_path}' not found.")
        return
    
    processor = ImageProcessor(image_path, output_dir="output/example3")
    
    if processor.load_image():
        processor.apply_transformation("skew", angle_x=30, angle_y=0)
        processor.save_result("skewed_30.png")


def example_4_transpose():
    """Example 4: Transpose image (swap rows and columns)."""
    print("\n" + "="*70)
    print("EXAMPLE 4: Matrix Transpose (Manual Implementation)")
    print("="*70)
    
    image_path = "test_image.jpg"
    
    if not os.path.exists(image_path):
        print(f"⚠️  Note: Test image '{image_path}' not found.")
        return
    
    processor = ImageProcessor(image_path, output_dir="output/example4")
    
    if processor.load_image():
        print(f"\nOriginal dimensions: {processor.width} x {processor.height}")
        processor.apply_transformation("transpose")
        print(f"New dimensions: {processor.width} x {processor.height}")
        processor.save_result("transposed.png")


def example_5_flipping():
    """Example 5: Flip image horizontally and vertically."""
    print("\n" + "="*70)
    print("EXAMPLE 5: Image Flipping")
    print("="*70)
    
    image_path = "test_image.jpg"
    
    if not os.path.exists(image_path):
        print(f"⚠️  Note: Test image '{image_path}' not found.")
        return
    
    processor = ImageProcessor(image_path, output_dir="output/example5")
    
    if processor.load_image():
        processor.apply_transformation("flip_h")
        processor.save_result("flipped_horizontal.png")
        
        processor.reset_to_original()
        processor.apply_transformation("flip_v")
        processor.save_result("flipped_vertical.png")


def example_6_grayscale():
    """Example 6: Convert to grayscale using different methods."""
    print("\n" + "="*70)
    print("EXAMPLE 6: Grayscale Conversion (Multiple Methods)")
    print("="*70)
    
    image_path = "test_image.jpg"
    
    if not os.path.exists(image_path):
        print(f"⚠️  Note: Test image '{image_path}' not found.")
        return
    
    processor = ImageProcessor(image_path, output_dir="output/example6")
    
    if processor.load_image():
        # Luminosity method
        processor.apply_transformation("grayscale", method='luminosity')
        processor.save_result("grayscale_luminosity.png")
        
        processor.reset_to_original()
        # Average method
        processor.apply_transformation("grayscale", method='average')
        processor.save_result("grayscale_average.png")


def example_7_edge_detection():
    """Example 7: Edge detection using different methods."""
    print("\n" + "="*70)
    print("EXAMPLE 7: Edge Detection (Manual Implementation)")
    print("="*70)
    
    image_path = "test_image.jpg"
    
    if not os.path.exists(image_path):
        print(f"⚠️  Note: Test image '{image_path}' not found.")
        return
    
    processor = ImageProcessor(image_path, output_dir="output/example7")
    
    if processor.load_image():
        # Sobel edge detection
        processor.apply_transformation("edge", method='sobel')
        processor.save_result("edges_sobel.png")
        
        processor.reset_to_original()
        # Laplacian edge detection
        processor.apply_transformation("edge", method='laplacian')
        processor.save_result("edges_laplacian.png")


def example_8_brightness_contrast():
    """Example 8: Adjust brightness and contrast."""
    print("\n" + "="*70)
    print("EXAMPLE 8: Brightness and Contrast Adjustment")
    print("="*70)
    
    image_path = "test_image.jpg"
    
    if not os.path.exists(image_path):
        print(f"⚠️  Note: Test image '{image_path}' not found.")
        return
    
    processor = ImageProcessor(image_path, output_dir="output/example8")
    
    if processor.load_image():
        # Increase brightness
        processor.apply_transformation("brightness", adjustment=50)
        processor.save_result("bright_50.png")
        
        processor.reset_to_original()
        # Increase contrast
        processor.apply_transformation("contrast", factor=2.0)
        processor.save_result("contrast_2x.png")


def example_9_sequential():
    """Example 9: Apply multiple transformations sequentially."""
    print("\n" + "="*70)
    print("EXAMPLE 9: Sequential Transformations")
    print("="*70)
    
    image_path = "test_image.jpg"
    
    if not os.path.exists(image_path):
        print(f"⚠️  Note: Test image '{image_path}' not found.")
        return
    
    processor = ImageProcessor(image_path, output_dir="output/example9")
    
    if processor.load_image():
        # Step 1: Convert to grayscale
        print("\nStep 1: Convert to grayscale")
        processor.apply_transformation("grayscale")
        
        # Step 2: Apply edge detection
        print("\nStep 2: Apply edge detection")
        processor.apply_transformation("edge", method='sobel')
        
        # Step 3: Adjust brightness
        print("\nStep 3: Adjust brightness")
        processor.apply_transformation("brightness", adjustment=50)
        
        processor.save_result("sequential_transformation.png")


def example_10_rotation_advanced():
    """Example 10: Various rotation angles."""
    print("\n" + "="*70)
    print("EXAMPLE 10: Various Rotation Angles")
    print("="*70)
    
    image_path = "test_image.jpg"
    
    if not os.path.exists(image_path):
        print(f"⚠️  Note: Test image '{image_path}' not found.")
        return
    
    processor = ImageProcessor(image_path, output_dir="output/example10")
    
    if processor.load_image():
        angles = [45, 90, 180]
        for angle in angles:
            processor.reset_to_original()
            processor.apply_transformation("rotate", angle=angle)
            processor.save_result(f"rotated_{angle}.png")


def main():
    """Run all examples."""
    print("\n" + "="*80)
    print(" "*20 + "IMAGE PROCESSING PIPELINE - EXAMPLES")
    print("="*80)
    print("\nThese examples demonstrate manual implementations of image transformations.")
    print("Note: Replace 'test_image.jpg' with your own image file.")
    print("\nNo Pillow built-in transformation methods are used (only Image.open/Image.new).")
    
    examples = {
        "1": ("Rotation (30°)", example_1_rotation),
        "2": ("Scaling (75%)", example_2_scaling),
        "3": ("Skewing (30°)", example_3_skewing),
        "4": ("Transpose", example_4_transpose),
        "5": ("Flipping", example_5_flipping),
        "6": ("Grayscale Conversion", example_6_grayscale),
        "7": ("Edge Detection", example_7_edge_detection),
        "8": ("Brightness/Contrast", example_8_brightness_contrast),
        "9": ("Sequential Transformations", example_9_sequential),
        "10": ("Multiple Rotation Angles", example_10_rotation_advanced),
    }
    
    print("\nAvailable examples:")
    for key, (name, _) in examples.items():
        print(f"  {key:2}. {name}")
    print("  11. Run all examples")
    print("   0. Exit")
    
    while True:
        choice = input("\nSelect example (0-11): ").strip()
        
        if choice == "0":
            print("Exiting...")
            break
        elif choice == "11":
            for key in sorted(examples.keys()):
                name, func = examples[key]
                try:
                    func()
                except Exception as e:
                    print(f"✗ Error in {name}: {e}")
                    import traceback
                    traceback.print_exc()
        elif choice in examples:
            name, func = examples[choice]
            try:
                func()
            except Exception as e:
                print(f"✗ Error in {name}: {e}")
                import traceback
                traceback.print_exc()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Run specific example if provided
        example_num = sys.argv[1]
        examples = {
            "1": example_1_rotation,
            "2": example_2_scaling,
            "3": example_3_skewing,
            "4": example_4_transpose,
            "5": example_5_flipping,
            "6": example_6_grayscale,
            "7": example_7_edge_detection,
            "8": example_8_brightness_contrast,
            "9": example_9_sequential,
            "10": example_10_rotation_advanced,
        }
        if example_num in examples:
            examples[example_num]()
        else:
            print(f"Unknown example: {example_num}")
    else:
        main()
