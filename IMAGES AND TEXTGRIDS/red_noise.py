import random
from simpleimage import SimpleImage

DEFAULT_FILE = 'images/simba-sq.jpg'

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show the image before the transform
    image.show()

    for pixel in image:
        pixel.green = random.randint(0,255)

    # Show the image after the transform
    image.show()


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()
