# Convert RGB to grayscale

def rgb_to_grayscale_luminosity(red, green, blue):
    # Weights based on human eye sensitivity
    height = len(red)
    width = len(red[0])
    result = [[0] * width for _ in range(height)]
    
    for y in range(height):
        for x in range(width):
            gray = int(0.299 * red[y][x] + 0.587 * green[y][x] + 0.114 * blue[y][x])
            result[y][x] = min(255, max(0, gray))
    
    return result


def rgb_to_grayscale_average(red, green, blue):
    # Simple average of RGB
    height = len(red)
    width = len(red[0])
    result = [[0] * width for _ in range(height)]
    
    for y in range(height):
        for x in range(width):
            gray = (red[y][x] + green[y][x] + blue[y][x]) // 3
            result[y][x] = min(255, max(0, gray))
    
    return result


def rgb_to_grayscale_lightness(red, green, blue):
    # Average of max and min values
    height = len(red)
    width = len(red[0])
    result = [[0] * width for _ in range(height)]
    
    for y in range(height):
        for x in range(width):
            r, g, b = red[y][x], green[y][x], blue[y][x]
            gray = (max(r, g, b) + min(r, g, b)) // 2
            result[y][x] = min(255, max(0, gray))
    
    return result


def rgb_to_grayscale_desaturation(red, green, blue):
    # Same as lightness
    return rgb_to_grayscale_lightness(red, green, blue)


def extract_channel(channel_matrix):
    # Just copy the channel as grayscale
    return [[val for val in row] for row in channel_matrix]


def rgb_to_grayscale(red, green, blue, method='luminosity'):
    methods = {
        'luminosity': rgb_to_grayscale_luminosity,
        'average': rgb_to_grayscale_average,
        'lightness': rgb_to_grayscale_lightness,
        'desaturation': rgb_to_grayscale_desaturation,
    }
    
    if method in ('red', 'green', 'blue'):
        # Extract single channel
        channel_map = {'red': red, 'green': green, 'blue': blue}
        return extract_channel(channel_map[method])
    
    converter = methods.get(method, rgb_to_grayscale_luminosity)
    return converter(red, green, blue)


# Shorthand for common use
def to_grayscale(r, g, b):
    return rgb_to_grayscale_luminosity(r, g, b)