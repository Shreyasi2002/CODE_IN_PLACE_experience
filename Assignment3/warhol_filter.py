"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage
import random

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter.
    It loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixel's red component by
    :param green_scale: A number to multiply each pixel's green component by
    :param blue_scale: A number to multiply each pixel's blue component by
    Returns the newly generated patch.
    '''
    patch = SimpleImage(PATCH_NAME)
    for pixel in patch:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale
    return patch

def get_scales_randomly():
    scales = random.uniform(0,2)
    return scales

def put_patch(final_image, start_row, start_col):
    red_scale = get_scales_randomly()
    green_scale = get_scales_randomly()
    blue_scale = get_scales_randomly()
    patch = make_recolored_patch(red_scale, green_scale, blue_scale)
    for x in range(PATCH_SIZE):
        for y in range(PATCH_SIZE):
            pixel = patch.get_pixel(x,y)
            final_image.set_pixel((PATCH_SIZE*start_col)+x, (PATCH_SIZE*start_row)+y, pixel)

def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)
    for row in range(N_ROWS):
        for col in range(N_COLS):
            put_patch(final_image, row, col)
    
    final_image.show()

if __name__ == '__main__':
    main()
