# Slide formatter

This is a Python script for cropping and formatting multiple images into a single PDF file. It supports `.png` and `.jpg` images.

## Requirements

* Python 3.8
* Pip 20.0.2
* Pillow 7.1.2

## How to use it

1. Put all images you want in a folder ordered alphabetically as they will be displayed in the PDF file and copy the script into the folder.

2. Run the script:

```sh
python slide_formatter.py
```

3. If you want to crop all the images, insert left, upper, right and lower pixel positions of your cropping area (use an image manipulation software such as GIMP or Photoshop to help you find those). Otherwise, just insert zeros and the images won't be cropped.

4. Done! The PDF file will be generated as `slides.pdf`.
