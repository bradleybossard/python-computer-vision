"""
Resize and rotate an image.
"""

from PIL import Image
pil_im = Image.open('empire.jpg')

resized = pil_im.resize((100, 100));
rotated = resized.rotate(45)

out = './empire_resize_and_rotate.jpg'
rotated.save(out)
