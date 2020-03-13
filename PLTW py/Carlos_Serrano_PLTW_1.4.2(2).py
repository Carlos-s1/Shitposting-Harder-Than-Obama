# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import os.path
import numpy as np # “as” lets us use standard abbreviations
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)
  
# Create figure with 2 subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img)
ax[1].imshow(img, interpolation='none') # Override default
ax[0].set_xlim(135, 165)
ax[0].set_ylim(470, 420)
ax[1].set_xlim(135, 165)
ax[1].set_ylim(470, 420)
# Show the figure on the screen
###
# Make a rectangle of pixels yellow
###
img.setflags(write=1)  
height = len(img)
width = len(img[0])
for row in range(200, 220):
    for column in range(50, 100):
        img[row][column] = [255, 255, 0] # red + green = yellow
fig.show()