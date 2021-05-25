"""
This program takes an image and generates a reflection.
The top half of the generated image is the same as the original.
The bottom half is the mirror reflection of the top half.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'images/mt-rainier.jpg'

def make_reflected(filename):
    image = SimpleImage(filename)
    height = image.height
    width = image.width

    # Create new blank image to contain the reflection
    reflection = SimpleImage.blank(width, height*2)
    for x in range(width):
        for y in range(height):
            pixel = image.get_pixel(x,y)
            reflection.set_pixel(x,y,pixel)
            reflection.set_pixel(x, (height*2)-(y+1), pixel)
    return reflection

def main():
    # Get file name from user input
    filename = get_file()

    # Show the original image
    original = SimpleImage(filename)
    original.show()

    # Show the reflected image
    reflected = make_reflected(filename)
    reflected.show()

def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename

if __name__ == '__main__':
    main()
