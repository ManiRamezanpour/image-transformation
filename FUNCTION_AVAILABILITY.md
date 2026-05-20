# Function Availability Check

## ✅ All Required Functions Are Available

### Matrix Operations

1. **✅ matrix_addition(A, B)**
   - **Status**: Available
   - **Location**: `matrix/Matrix_addition.py`
   - **Function Name**: `add_matrices(A, B)`
   - **Purpose**: Add two matrices element-wise

2. **✅ matrix_subtraction(A, B)**
   - **Status**: Available
   - **Location**: `matrix/Matrix_subtraction.py`
   - **Function Name**: `subtract_matrices(A, B)`
   - **Purpose**: Subtract matrix B from matrix A

3. **✅ matrix_multiplication(A, B)**
   - **Status**: Available
   - **Location**: `matrix/Matrix_multilipication.py`
   - **Function Name**: `matrix_multiplication(A, B)`
   - **Purpose**: Multiply two matrices (A cols must equal B rows)

4. **✅ matrix_transpose(A)**
   - **Status**: Available
   - **Location**: `matrix/Matrix_transpose.py`
   - **Function Name**: `transpose_matrix(matrix)`
   - **Purpose**: Transpose matrix (swap rows and columns)
   - **Note**: Takes only 1 parameter (B not needed)

5. **✅ scalar_multiplication(K, A)**
   - **Status**: Available
   - **Location**: `matrix/Matrix_scalar_multiplication.py`
   - **Function Name**: `scalar_multiplication(scalar, matrix)`
   - **Purpose**: Multiply matrix by a scalar value

### Image Processing - Loading/Saving

6. **✅ image_to_matrix(image_path)**
   - **Status**: Available
   - **Location**: `image_proccessing/image_to_matrix.py`
   - **Function Name**: `load_image_as_rgb_matrices(image_path)`
   - **Returns**: `(red_matrix, green_matrix, blue_matrix, height, width)`
   - **Purpose**: Load image and convert to RGB matrices

7. **✅ matrix_to_image(matrix_red, matrix_green, matrix_blue)**
   - **Status**: Available
   - **Location**: `image_proccessing/image_transformation.py`
   - **Function Names**: 
     - `matrices_to_image(red_matrix, green_matrix, blue_matrix, output_path=None)`
     - `save_rgb_matrices_as_image(red_matrix, green_matrix, blue_matrix, output_path, format='PNG')`
   - **Purpose**: Convert RGB matrices back to image and save

### Image Transformations

8. **✅ rotate_matrix(matrix, angle_degrees, center=None)**
   - **Status**: Available
   - **Location**: `rotate_matrix.py`
   - **Function Name**: `rotate_matrix(matrix, angle_degrees, center_x=None, center_y=None, fill_value=0)`
   - **Purpose**: Rotate matrix by specified angle around center point
   - **Parameters**: 
     - angle_degrees: rotation angle
     - center_x, center_y: rotation center (defaults to matrix center)
     - fill_value: value for empty areas

9. **✅ scale_matrix(matrix, scale_factor)**
   - **Status**: Available
   - **Location**: `scale_matrix.py`
   - **Function Name**: `scale_matrix(matrix, scale_x, scale_y=None, fill_value=0)`
   - **Purpose**: Scale/resize matrix by factors
   - **Parameters**:
     - scale_x: horizontal scale factor
     - scale_y: vertical scale factor (defaults to scale_x)
     - fill_value: value for expanded areas

10. **✅ skew_matrix(matrix, skew_x, skew_y)**
    - **Status**: Available
    - **Location**: `skew_matrix.py`
    - **Function Name**: `skew_matrix(matrix, angle_x_degrees=0, angle_y_degrees=0, fill_value=0)`
    - **Purpose**: Apply skewing (shear) transformation
    - **Parameters**:
      - angle_x_degrees: horizontal shear angle
      - angle_y_degrees: vertical shear angle
      - fill_value: value for displaced areas

11. **✅ transpose_matrix(matrix)**
    - **Status**: Available
    - **Location**: `matrix/Matrix_transpose.py`
    - **Function Name**: `transpose_matrix(matrix)`
    - **Purpose**: Transpose matrix (swap rows and columns)

### Color/Image Effects

12. **✅ to_grayscale(matrix_red, matrix_green, matrix_blue)**
    - **Status**: Available
    - **Location**: `to_grayscale.py`
    - **Function Names**: 
      - `to_grayscale(matrix_red, matrix_green, matrix_blue)`
      - `rgb_to_grayscale(red_matrix, green_matrix, blue_matrix, method='luminosity')`
    - **Purpose**: Convert RGB matrices to grayscale
    - **Methods**: 
      - 'luminosity': 0.299R + 0.587G + 0.114B (default)
      - 'average': (R+G+B)/3
      - 'lightness': (max+min)/2

13. **✅ edge_detection(matrix)**
    - **Status**: Available
    - **Location**: `edge_detection.py`
    - **Function Names**:
      - `edge_detection(matrix)` - Default Sobel
      - `sobel_edge_detection(matrix)` - Sobel operator
      - `laplacian_edge_detection(matrix)` - Laplacian operator
      - `prewitt_edge_detection(matrix)` - Prewitt operator
    - **Purpose**: Detect edges in matrix using kernel convolution

---

## Usage Example

```python
# Load image
red, green, blue, height, width = load_image_as_rgb_matrices("logo.png")

# Matrix operations
red_rotated = rotate_matrix(red, 45)
green_scaled = scale_matrix(green, 0.75)
blue_gray = rgb_to_grayscale(red, green, blue)

# Save result
save_rgb_matrices_as_image(red_rotated, green_scaled, blue_gray, "output.png")
```

---

## Summary

| Function | Status | File | Alternative Name |
|----------|--------|------|-----------------|
| matrix_addition | ✅ | matrix/Matrix_addition.py | add_matrices |
| matrix_subtraction | ✅ | matrix/Matrix_subtraction.py | subtract_matrices |
| matrix_multiplication | ✅ | matrix/Matrix_multilipication.py | - |
| matrix_transpose | ✅ | matrix/Matrix_transpose.py | transpose_matrix |
| scalar_multiplication | ✅ | matrix/Matrix_scalar_multiplication.py | - |
| image_to_matrix | ✅ | image_proccessing/image_to_matrix.py | load_image_as_rgb_matrices |
| matrix_to_image | ✅ | image_proccessing/image_transformation.py | matrices_to_image |
| rotate_matrix | ✅ | rotate_matrix.py | - |
| scale_matrix | ✅ | scale_matrix.py | - |
| skew_matrix | ✅ | skew_matrix.py | - |
| transpose_matrix | ✅ | matrix/Matrix_transpose.py | - |
| to_grayscale | ✅ | to_grayscale.py | rgb_to_grayscale |
| edge_detection | ✅ | edge_detection.py | sobel_edge_detection |

**Status: ✅ ALL 13 FUNCTIONS AVAILABLE**
