from os import listdir
from os.path import isfile

try:
    from PIL import Image
except ModuleNotFoundError:
    print('Please install Pillow using the following command: python -m pip install Pillow')
    exit()

img_list = list()

# Iterate through all .png images on the current directory
file_list = [f for f in listdir() if isfile(f) and (f.endswith('.png') or f.endswith('.jpg'))]
file_list.sort()

if not file_list:
    print('No images found! Please use only ".jpg" and ".png" images.')
    exit()

print('Insert your cropping area coordinates (or insert zeros if you don\'t want to crop):')

left = float(input('Insert left pixel coordinate: '))
upper = float(input('Insert upper pixel coordinate: '))
right = float(input('Insert right pixel coordinate: '))
lower = float(input('Insert lower pixel coordinate: '))

cropping_area = (left, upper, right, lower)

for file_name in file_list:
    img = Image.open(file_name)

    # If image has an alpha channel
    if len(img.split()) == 4:
        # Open RGBA image
        img_rgba = img
        # Create a new RGB image with same size and a white background
        img = Image.new('RGB', img_rgba.size, (255, 255, 255))
        # Paste RGBA image on RGB using alpha channel as mask
        img.paste(img_rgba, mask=img_rgba.split()[3])

    if cropping_area == (0, 0, 0, 0):
        img_list.append(img)
    # Crop the new converted image
    else:
        cropped_img = img.crop(cropping_area)
        # Append it to image list
        img_list.append(cropped_img)

# Save the image list as a PDF named 'slides.pdf'
img_list[0].save('slides.pdf', 'PDF', resolution=100.0, save_all=True, append_images=img_list[1:])
