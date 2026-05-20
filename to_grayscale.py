import numpy as np
def to_grayscale(matrix_red, matrix_green, matrix_blue):

    # Ensure the input matrices are numpy arrays
    matrix_red = np.array(matrix_red)
    matrix_green = np.array(matrix_green)
    matrix_blue = np.array(matrix_blue)

    # Calculate the grayscale values using the luminosity method
    grayscale_matrix = 0.299 * matrix_red + 0.587 * matrix_green + 0.114 * matrix_blue

    return grayscale_matrix.astype('uint8')