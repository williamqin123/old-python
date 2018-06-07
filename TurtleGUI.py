import turtle
from Tkinter import *
controls = Tk()
controls.wm_title("Drawing Options")
pencil = turtle.Pen()
dotsize = None
change_font = None
size = None
style = None
radius = None
angle = None
howfar = None
textbox = None
turndeg = None
turntxt = None
width = None
def movepen():
	pencil.penup()
	pencil.forward(int(howfar.get()))
	pencil.pendown()
def moveit():
	movetk = Tk()
	movetk.wm_title("Move Pen")
	global howfar
	Label(movetk, text = "Distance").pack()
	howfar = Entry(movetk)
	howfar.pack()
	Button(movetk, text = "Move Pen", command = movepen).pack()
def update():
	pencil.color(fgcolor.get())
	turtle.bgcolor(bgcolor.get())
	pencil.speed(int(speed.get()))
	pencil.pensize(int(lsize.get()))
	global dotsize
	dotsize = int(dotwidth.get())
	global change_font, size, style
	change_font = font.get()
	size = int(fsize.get())
	style = fsty.get()
def maketxt():
	pencil.write(textbox.get(), font = (change_font, size, style))
def turnit():
	if turntxt.get() == "left":
		pencil.left(int(turndeg.get()))
	elif turntxt.get() == "right":
		pencil.right(int(turndeg.get()))
def turn():
	turntk = Tk()
	global turndeg
	global turntxt
	turntk.wm_title("Turn Pen Around")
	Label(turntk, text = "Turn Direction").pack()
	turntxt = Entry(turntk)
	turntxt.pack()
	Label(turntk, text = "Turn Degrees").pack()
	turndeg = Entry(turntk)
	turndeg.pack()
	Button(turntk, text = "Turn", command = turnit).pack()
def text():
	txttk = Tk()
	global textbox
	txttk.wm_title("Text")
	Label(txttk, text = "Text to Display").pack()
	textbox = Entry(txttk)
	textbox.pack()
	Button(txttk, text = "Display Text", command = maketxt).pack()
def createcircle():
	pencil.circle(int(radius.get()), int(angle.get()))
def dot():
	pencil.dot(dotsize)
def resett():
	pencil.reset()
def startfill():
	pencil.fill(True)
def endfill():
	pencil.fill(False)
def drawline():
	pencil.forward(int(width.get()))
def line():
	global width
	linetk = Tk()
	linetk.wm_title("Draw Line")
	Label(linetk, text = "Length").pack()
	width = Entry(linetk)
	width.pack()
	Button(linetk, text = "Draw Line", command = drawline).pack()
def circle():
	circletk = Tk()
	circletk.wm_title("Create Circle")
	global radius, angle
	Label(circletk, text = "Radius").pack()
	radius = Entry(circletk)
	radius.pack()
	Label(circletk, text = "Angle").pack()
	angle = Entry(circletk)
	angle.pack()
	Button(circletk, text = "Create Circle", command = createcircle).pack()
fgcolor = Entry(controls)
bgcolor = Entry(controls)
lsize = Entry(controls)
dotwidth = Entry(controls)
speed = Entry(controls)
font = Entry(controls)
fsize = Entry(controls)
fsty = Entry(controls)
Label(controls, text = "Foreground Color").pack()
fgcolor.pack()
Label(controls, text = "Background Color").pack()
bgcolor.pack()
Label(controls, text = "Drawing Speed").pack()
speed.pack()
Label(controls, text = "Line Size").pack()
lsize.pack()
Label(controls, text = "Dot Size").pack()
dotwidth.pack()
Label(controls, text = "Font Family").pack()
font.pack()
Label(controls, text = "Font size").pack()
fsize.pack()
Label(controls, text = "Font Style").pack()
fsty.pack()
Label(controls, text = "Actions")
Button(controls, text = "Dot", command = dot).pack()
Button(controls, text = "Circle", command = circle).pack()
Button(controls, text = "Begin Fill", command = startfill).pack()
Button(controls, text = "End Fill", command = endfill).pack()
Button(controls, text = "Reset", command = resett).pack()
Button(controls, text = "Move", command = moveit).pack()
Button(controls, text = "Text", command = text).pack()
Button(controls, text = "Turn", command = turn).pack()
Button(controls, text = "Line", command = line).pack()
Button(controls, text = "Apply", command = update).pack()
raw_input()