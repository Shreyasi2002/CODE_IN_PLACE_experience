"""
This program loads an image and applies the narok filter
to it by setting "bright" pixels to grayscale values.
"""

from simpleimage import SimpleImage

def get_average_pixel(red, green, blue):
    average = (red + green + blue)//3
    return average

def apply_narok_filter(image):
    for pixel in image:
        average = get_average_pixel(pixel.red, pixel.green, pixel.blue)
        if average > 153:
            pixel.red = average
            pixel.green = average
            pixel.blue = average

def main():
    image = SimpleImage('images/simba-sq.jpg')
    apply_narok_filter(image)
    image.show()

if __name__ == '__main__':
    main()
