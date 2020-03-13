from turtle import *
color('blue', 'white')
begin_fill()
while True:
    speed(100)
    forward(500)
    left(-190)
    n=180
    if abs(pos())<1:
        break
end_fill()
bye()