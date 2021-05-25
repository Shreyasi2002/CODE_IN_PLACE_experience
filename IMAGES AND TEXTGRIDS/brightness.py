from simpleimage import SimpleImage

DEFAULT_FILE = 'images/quad.jpg'
BRIGHTNESS_TOGGLE = 100

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show the image before the transform
    image.show()

    for pixel in image:
        pixel.red=truncate(pixel.red+BRIGHTNESS_TOGGLE)
        pixel.green=truncate(pixel.green+BRIGHTNESS_TOGGLE)
        pixel.blue=truncate(pixel.blue+BRIGHTNESS_TOGGLE)

    # Show the image after the transform
    image.show()

def truncate(num):
    if num<0:
        num = 0
    if num>255:
        num = 255
    return num


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()
