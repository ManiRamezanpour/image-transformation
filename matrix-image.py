def matrix_to_image(matrix_red, matrix_green, matrix_blue, ):
    from PIL import Image
    import numpy as np

    # Ensure the input matrices are numpy arrays
    matrix_red = np.array(matrix_red)
    matrix_green = np.array(matrix_green)
    matrix_blue = np.array(matrix_blue)

    # Stack the color channels to create an RGB image
    rgb_array = np.stack((matrix_red, matrix_green, matrix_blue), axis=-1)

    # Create an image from the RGB array
    image = Image.fromarray(rgb_array.astype('uint8'), 'RGB')

    # Save the image to the specified output file
    image.save(output_file)
    