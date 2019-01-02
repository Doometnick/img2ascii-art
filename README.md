# Image to ASCII art creator

## Description
img2ascii-art is a command-line program that converts an image into text. After execution, the text-picture will be printed to the console and also saved in a text file in the root folder.

![](http://funkyimg.com/i/2PJpz.jpg)

## Usage
The program can be run by `python img2ascii.py <image file name> <text image width>` on windows or the equivalent on iOS/Linux, for example `python img2ascii.py img1.jpg 100`. Images that are taken as input have to be stored in the folder _imgs_.

## Output
Executing the code will do two things:

1. Print the text-picture to the console
2. Save the text-picture in a text file named _last_ascii_mapping.txt_. 

## Randomization
When executed several times, the resulting text-picture will always look different. The string of potential ASCII characters that are used for the final pictures is shuffled in both length and order. Every randomized sequence of ASCII characters is saved together with the resulting picture for reproducibility, but only for the last code execution. 
