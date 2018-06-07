import Tkinter, time
sketchpad = Tkinter.Tk()
sketchpad.title("SketchPad BasicDraw")
sketchpad.geometry("640x480")
colorframe = Tkinter.Frame(sketchpad, padx = 5, pady = 5, highlightbackground = "black", highlightthickness = 2)
colorframe.pack()
lasttime = time.time()
class SliderScale:
	def __init__(self, background):
		self.id = Tkinter.Scale(colorframe, orient = "horizontal", bg = background, width = 10, from_ = 0, to = 255)
		self.id.pack(side = "left")
pencillinesize = Tkinter.Spinbox(colorframe, from_ = 1, to = 50, width = 3)
Tkinter.Label(colorframe, text = " R ").pack(side = "left")
redslider = SliderScale("red")
Tkinter.Label(colorframe, text = " G ").pack(side = "left")
greenslider = SliderScale("green")
Tkinter.Label(colorframe, text = " B ").pack(side = "left")
blueslider = SliderScale("blue")
Tkinter.Label(colorframe, text = " Line Size ").pack(side = "left")
pencillinesize.pack(side = "left")
fgcolor = "#%s%s%s" % (str(format(redslider.id.get(), "02x")), str(format(greenslider.id.get(), "02x")), str(format(blueslider.id.get(), "02x")))
eraser = True
def erase():
	global fgcolor, eraser, bgvar, colorvar, hexcode
	if eraser == True:
		fgcolor = "white"
		eraseractivate.config(text = "Drawing Mode")
		eraser = False
	elif eraser == False:
		fgcolor = "#%s%s%s" % (str(format(redslider.id.get(), "02x")), str(format(greenslider.id.get(), "02x")), str(format(blueslider.id.get(), "02x")))
		eraseractivate.config(text = "Eraser Mode")
		eraser = True
eraseractivate = Tkinter.Button(colorframe, text = "Eraser Mode", width = 12, command = erase)
eraseractivate.pack(side = "left")
canvas = Tkinter.Canvas(sketchpad, width = 9999, height = 9999)
laststroke = "Undefined"
def drawline(event):
	global laststroke, fgcolor, bgvar, colorvar, lasttime, hexcode
	autocorrect = True
	line = int(pencillinesize.get()) / 2
	if not laststroke == "Undefined":
		laststrokecoords = canvas.coords(laststroke)
		if not fgcolor == "white":
			fgcolor = "#%s%s%s" % (str(format(redslider.id.get(), "02x")), str(format(greenslider.id.get(), "02x")), str(format(blueslider.id.get(), "02x")))
			print fgcolor
		if time.time() - lasttime > 0.1:
			autocorrect = False
		if event.x - laststrokecoords[0] + line > int(pencillinesize.get()) or event.y - laststrokecoords[1] + line > int(pencillinesize.get()):
			if autocorrect == True:
				canvas.create_line(laststrokecoords[0], laststrokecoords[1], event.x, event.y, width = int(pencillinesize.get()), fill = fgcolor)
	laststroke = canvas.create_oval(event.x - line, event.y - line, event.x + line, event.y + line, width = 0, fill = fgcolor)
	lasttime = time.time()
canvas.bind_all("<B1-Motion>", drawline)
canvas.pack()
while True:
	sketchpad.update_idletasks()
	sketchpad.update()