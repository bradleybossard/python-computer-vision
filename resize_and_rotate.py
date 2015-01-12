"""
Resize and rotate an image.
"""

from PIL import Image
pil_im = Image.open('empire.jpg')

#box = (100,0,150,50)
#region = pil_im.crop(box)
#region = region.transpose(Image.ROTATE_180)
resized = pil_im.resize((100, 100));
rotated = resized.rotate(45)

#pil_im.paste(region,box)

out = './empire_resize_and_rotate.jpg'
rotated.save(out)
