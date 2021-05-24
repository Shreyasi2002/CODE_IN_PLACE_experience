from simpleimage import SimpleImage

def main():
    image = SimpleImage('images/simba-sq.jpg')
    bordered_img = add_border(image, 10)
    bordered_img.show()


def add_border(original_img, border_size):
    """
    This function returns a new SimpleImage which is the same as
    original image except with a black border added around it. The
    border should be border_size many pixels thick.

    Inputs:
        - original_img: The original image to process
        - border_size: The thickness of the border to add around the image

    Returns:
        A new SimpleImage with the border added around original image
    """
    width = original_img.width
    height = original_img.height
    border_image = SimpleImage.blank(width + 2*border_size, height + 2*border_size)
    for x in range(width):
        for y in range(height):
            pixel = original_img.get_pixel(x,y)
            border_image.set_pixel(x+border_size, y+border_size, pixel)
    
    add_borders(border_size, border_image)
    return border_image

def add_borders(border_size, border_image):
    width = border_image.width
    height = border_image.height
    for x in range(width):
        for y in range(height):
            pixel = border_image.get_pixel(x,y)
            if x<border_size or x>=width-border_size or y<border_size or y>=height-border_size:
                pixel.red = 0
                pixel.green = 0
                pixel.blue = 0      

if __name__ == '__main__':
    main()
