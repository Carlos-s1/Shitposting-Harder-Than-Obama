'''
JDoe_JSmith_1_4_3: Change pixels in an image.
'''
import matplotlib.pyplot as plt
import os.path
import numpy as np  # "as" lets us use standard abbreviations
   
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)
 
  
###
# Change a region if condition is True
###
  
height = len(img)
width = len(img[0])
for r in range(160,800):
    for c in range(width):
        if sum(img[r][c])>200: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[230,230,250] # R + B = magenta
  
###
###
# Make a rectangle of pixels yellow
###
height = len(img)
width = len(img[0])
for row in range(0, 220):
    for column in range(0, 400):
        img[row][column] = [255, 0, 0] # red + green = yellow

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')


fig.show()  