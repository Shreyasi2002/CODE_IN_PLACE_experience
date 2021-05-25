"""
This program implements a rad image filter.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'images/quad.jpg'

def Code_In_Place_filter(image):
    for pixel in image:
        pixel.red *= 1.5
        pixel.green *= 0.7
        pixel.blue *= 1.5

def main():
    # Get file name from user input
    filename = get_file()
    
    # Load image and show image before the transform
    image = SimpleImage(filename)
    image.show()

    # Apply the filter
    Code_In_Place_filter(image)

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
