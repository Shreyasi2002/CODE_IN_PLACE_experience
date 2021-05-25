from simpleimage import SimpleImage

DEFAULT_FILE = 'images/quad.jpg'
NUM_REPEATS = 2

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Create new SimpleImage of correct dimensions
    # TODO: FILL IN THE WIDTH AND HEIGHT BELOW
    final_image = SimpleImage.blank(image.width*2, image.height)

    for x in range(image.width):
        for y in range(image.height):
            pixel = image.get_pixel(x,y)
            final_image.set_pixel(x,y,pixel)
            final_image.set_pixel(x+image.width,y,pixel)

    # Show the repeated image
    final_image.show()


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()
