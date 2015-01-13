"""
Create an image contour
"""
from PIL import Image
from pylab import *
# read image to array
im = array(Image.open('empire.jpg').convert('L'))
# create a new figure
figure()
# don't use colors
gray()
# show contours with origin upper left corner
contour(im, origin='image')
axis('equal')
axis('off')
#show()
savefig('empire_contour.jpg')