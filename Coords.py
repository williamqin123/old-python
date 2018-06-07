import Tkinter
coords_plane = Tkinter.Tk()
coords_plane.title("Line Segments Basic")
coords_plane.attributes("-alpha", 0.85)
canvas = Tkinter.Canvas(coords_plane, height = 320, width = 480)
'''grid = Tkinter.PhotoImage(file = "Grid.gif")
canvas.create_image(0, 0, anchor = "nw", image = grid)'''
class Pen:
	def __init__(self, canvas, color, color_dot, line_color):
		self.canvas = canvas
		self.color = color
		self.line_color = line_color
		self.color_dot = color_dot
		self.dot = False
		self.yes_dot = False
		self.last_dot_coords = None
		self.label = "Undefined"
		self.id = self.canvas.create_oval(10, 10, 15, 15, fill = self.color)
		self.y = 0
		self.x = 0
	def draw_dot(self):
		coords = self.canvas.coords(self.id)
		if self.yes_dot == True:
			if self.dot == False:
				last_dot = self.canvas.create_oval(coords[0], coords[1], coords[0] + 5, coords[1] + 5, fill = self.color_dot)
				self.last_dot_coords = self.canvas.coords(last_dot)
				self.dot = True
			elif self.dot == True:
				self.canvas.create_line(coords[0] + 2, coords[1] + 2, self.last_dot_coords[0] + 2, self.last_dot_coords[1] + 2, fill = self.line_color)
				self.canvas.create_oval(coords[0], coords[1], coords[0] + 5, coords[1] + 5, fill = self.color_dot)
				self.dot = False
		elif self.yes_dot == "LabelPoint":
			self.canvas.create_oval(coords[0], coords[1], coords[0] + 5, coords[1] + 5, fill = self.color_dot)
			self.canvas.create_text(coords[0], coords[1] - 10, text = self.label)
		else:
			self.canvas.move(self.id, self.x, self.y)
		self.yes_dot = False
pen = Pen(canvas, "black", "red", "blue")
def draw_direction(event):
	if not event.keysym == "space":
		if event.keysym == "Up":
			pen.x = 0
			pen.y = -10
		elif event.keysym == "Down":
			pen.x = 0
			pen.y = 10
		elif event.keysym == "Left":
			pen.y = 0
			pen.x = -10
		elif event.keysym == "Right":
			pen.y = 0
			pen.x = 10
		else:
			pen.label = event.keysym
			pen.yes_dot = "LabelPoint"
		pen.draw_dot()
	elif event.keysym == "space":
		pen.yes_dot = True
		pen.draw_dot()
canvas.bind_all("<KeyPress-Up>", draw_direction)
canvas.bind_all("<KeyPress-Down>", draw_direction)
canvas.bind_all("<KeyPress-Left>", draw_direction)
canvas.bind_all("<KeyPress-Right>", draw_direction)
canvas.bind_all("<Key>", draw_direction)
canvas.bind_all("<space>", draw_direction)
canvas.pack()
Tkinter.mainloop()