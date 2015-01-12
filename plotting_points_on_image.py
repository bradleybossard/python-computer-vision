"""
Using pylab to plot lines over top of an image.
"""

from PIL import Image
from pylab import *
# read image to array
im = array(Image.open('empire.jpg'))
# plot the image
imshow(im)
# some points
x = [10,100,150,150]
y = [140,30,100,100]
# plot the points with red star-markers
plot(x,y,'r*')

x = [20,120,160,160]
y = [100,90,70,100]
# plot the points with green circle-markers
plot(x,y,'go-')

x = [120,150,190,20]
y = [130,5,15,20]
# black dotted line with square-markers
plot(x,y,'ks:')

# line plot connecting the first two points
plot(x[:2],y[:2])
# add title and show the plot
title('Plotting: "empire.jpg"')
#show()
savefig('empire_plot.jpg')
