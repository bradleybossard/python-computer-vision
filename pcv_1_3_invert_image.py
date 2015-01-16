"""
  Example for inverting an image. PCV 1.3, Graylevel transforms.
"""

from PIL import Image
from numpy import *
# Read image into numpy array
im = array(Image.open('empire.jpg').convert('L'))
im2 = 255 - im #invert image
pil_im = Image.fromarray(im2)
pil_im.save('empire_inverted.jpg')
