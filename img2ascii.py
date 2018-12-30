import PIL
import sys
import string
import random
from PIL import Image

"""
Convert images to ascii art.
"""

# ascii_chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
ascii_chars = "#?%.S+.*:,@"  # lesser chars create a more beautiful picture
ascii_chars = "".join(random.sample(ascii_chars, random.randint(3, len(ascii_chars))))


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
    # Pixel values go from 0-255 and get fitted into the range from
    # 0 to length of possible ascii characters in variable ascii_chars.
    img_ascii = [ascii_chars[int(pixel_val / 255 * (len(ascii_chars) - 1))] for pixel_val in img_pixels]
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

    # Print final pictures
    ascii_picture = "\n".join(ascii_rows)
    export_ascii_picture(ascii_picture)
    print(ascii_picture)


def export_ascii_picture(text):
    open("last_ascii_mapping.txt", "w").writelines("ASCII order used: " + ascii_chars + "\n")
    open("last_ascii_mapping.txt", "a").writelines(text)



if __name__ == "__main__":

    try:
        img, width = sys.argv[1], int(sys.argv[2])
    except Exception as e:
        print(f"Usage: python img2ascii.py <image_name> <width>")
        print(e)
        sys.exit()

    try:
        img = Image.open(f"imgs/{img}")
    except Exception as e:
        print("Image could not be loaded.")
        print(e)
        sys.exit()

    print_ascii_art(img, width)
