from turtle import *
from time import sleep
print("2013 Pen Drawer 0.01.0")
print(">>>")
print("The main program should open in another window.")
print("This is the error message and notification window.")
color("blue")
fillcolor("blue")

pensize(2)
setup(width = 800, height = 600, startx = 0, starty = 0)
def turn(x, y):
	forward(20)
	right(90)

speed("fastest")
tracer(True)
ondrag(turn)
done()



