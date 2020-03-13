from turtle import *
setup(700, 700)
Screen()
title("Turtle Keys")
move = Turtle()
showturtle()

def k1():
    move.forward(45)

def k2():
    move.left(20)

def k3():
    move.right(20)

def k4():
    move.back(45)

onkeypress(k1, "w")
onkeypress(k2, "a")
onkeypress(k3, "d")
onkeypress(k4, "s")

listen()

mainloop()
