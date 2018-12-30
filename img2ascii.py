import PIL
import sys
from PIL import Image

"""
Convert images to ascii art.
"""

# What we need:
# - image folder imgs
# - launch command from cmd
# - conversion of image to greyscale
# - resizing of the image to standard width
# - collection of ascii codes
# - bucketing of pixels into ascii codes


# 70 levels of gray
ascii_codes = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "


def resize_img(img, new_width=100):
    """
    Resizes the image to a given width 
    while keeping the aspect ratio.
    """
    width, height = img.size
    asp_ratio = width / float(height)
    new_height = int(asp_ratio * new_width)
    img = img.resize((new_width, new_height))
    return img


def convert_to_greyscale(img):
    return img.convert("L")


def pixels_to_ascii(img):
    """
    Converts pixels to ascii characters.
    """
    img_pixels = list(img.getdata())
    img_ascii = [ascii_codes[pixel // len(ascii_codes)] for pixel in img_pixels]
    return img_ascii


def print_ascii_art(img, width=100):
    """
    Returns an image converted to ascii characters.
    """
    img = resize_img(img, width)
    img = convert_to_greyscale(img)
    ascii_letters = pixels_to_ascii(img)

    # Convert list of ascii letters into list of strings, 
    # each string representing a row of the final picture.
    ascii_rows = ["".join(ascii_letters[i:i+width]) for i in range(0, len(ascii_letters), width)]

    # Print final picture
    print("\n".join(ascii_rows))


if __name__ == "__main__":

    try:
        img = sys.argv[1]
    except Exception as e:
        print(f"Usage: python img2ascii.py <image_name>")
        print(e)
        sys.exit()

    try:
        img = Image.open(f"imgs/{img}")
    except Exception as e:
        print("Image could not be loaded.")
        print(e)
        sys.exit()

    print_ascii_art(img)
