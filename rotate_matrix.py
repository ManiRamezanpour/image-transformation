import math
def rotate_matrix(matrix,point,angle_degreess):
    angle_radians = math.radians(angle_degreess)
    cos_angle = math.cos(angle_radians)
    sin_angle = math.sin(angle_radians)

    # Translate the point to the origin
    translated_x = point[0] - matrix.shape[1] / 2
    translated_y = point[1] - matrix.shape[0] / 2

    # Rotate the point
    rotated_x = translated_x * cos_angle - translated_y * sin_angle
    rotated_y = translated_x * sin_angle + translated_y * cos_angle

    # Translate back to the original position
    final_x = int(rotated_x + matrix.shape[1] / 2)
    final_y = int(rotated_y + matrix.shape[0] / 2)

    return (final_x, final_y)