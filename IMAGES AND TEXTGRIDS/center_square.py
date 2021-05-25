from simpleimage import SimpleImage

DEFAULT_FILE = 'images/quad.jpg'
SQUARE_WIDTH = 200

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    center_square = SimpleImage.blank(SQUARE_WIDTH, SQUARE_WIDTH)

    width = image.width
    height = image.height
    i=0
    for x in range((width-SQUARE_WIDTH)//2 ,(width+SQUARE_WIDTH)//2):
        j=0
        for y in range((height-SQUARE_WIDTH)//2, (height+SQUARE_WIDTH)//2):
            pixel = image.get_pixel(x,y)
            center_square.set_pixel(i,j,pixel)
            j += 1
        i += 1

    # Show the image after the transform
    center_square.show()


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()
