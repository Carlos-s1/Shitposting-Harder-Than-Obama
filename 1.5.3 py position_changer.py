#####
# position_changer.py
# 
# Creates a Scale and a Canvas. Updates a circle based on the Scale.
# (c) 2013 PLTW
# version 11/1/2013
####

import tkinter #often people import tkinter as *

#####
# Create root window 
####
root = tkinter.Tk()

#####
# Create Model
######
r=100

x_intvar= tkinter.IntVar()
x_intvar.set(550)
y_intvar= tkinter.IntVar()
y_intvar.set(450)
######
# Create Controller
#######
# Event handler for slider
def position_changed(new_intval):
    # Get data from model
    # Could do this: r = int(new_intval)
    y1= y_intvar.get()
    y2= y_intvar.get()
    # Controller updating the view
    canvas.coords(circle_item, x1-r, y1-r, x2+r, y2+r)
    return (y1,y2)
# Instantiate and place slider
y_slider = tkinter.Scale(root, from_=-100, to=1000, variable=y_intvar,    
                              label='Vertical', command=position_changed)
y_slider.grid(row=1, column=0, sticky=tkinter.W)
# Create and place directions for the user
text = tkinter.Label(root, text='Drag slider \nto adjust\ncircle.')
text.grid(row=0, column=0)

def positionx_changed(new_intval):
    # Get data from model
    # Could do this: r = int(new_intval)
    x1= x_intvar.get()
    x2= x_intvar.get()
    # Controller updating the view
    canvas.coords(circle_item, x1-r, y1-r, x2+r, y2+r)
    return (x1,x2)
# Instantiate and place slider
x_slider = tkinter.Scale(root, from_=-100, to=1000, variable=x_intvar,    
                              label='Horizontal', command=positionx_changed)
x_slider.grid(row=2, column=0, sticky=tkinter.W)
# Create and place directions for the user
text = tkinter.Label(root, text='Drag slider \nto adjust\ncircle.')
text.grid(row=0, column=1)
 
######
# Create View
#######
# Create and place a canvas
canvas = tkinter.Canvas(root, width=1000, height=800, background='#FFFFFF')
canvas.grid(row=0, rowspan=2, column=1)

# Create a circle on the canvas to match the initial model
circle_item = canvas.create_oval()
x1, y1, x2, y2 = canvas.coords(circle_item)

#######
# Event Loop
#######
root.mainloop()