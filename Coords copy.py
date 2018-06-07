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
		self.label = None
		self.mouse_y = 0
		self.mouse_x = 0
		#self.id = self.canvas.create_oval(10, 10, 15, 15, fill = self.color)
		self.y = 0
		self.x = 0
	def draw_dot(self):
		coords_x = self.mouse_x
		coords_y = self.mouse_y
		if self.yes_dot == True:
			if self.dot == False:
				last_dot = self.canvas.create_oval(coords_x, coords_y, coords_x + 5, coords_y + 5, fill = self.color_dot)
				self.last_dot_coords = self.canvas.coords(last_dot)
				self.dot = True
			elif self.dot == True:
				self.canvas.create_line(coords_x + 2, coords_y + 2, self.last_dot_coords[0] + 2, self.last_dot_coords[1] + 2, fill = self.line_color)
				self.canvas.create_oval(coords_x, coords_y, coords_x + 5, coords_y + 5, fill = self.color_dot)
				self.dot = False
		else:
			point = self.canvas.create_oval(coords_x, coords_y, coords_x + 5, coords_y + 5, fill = self.color_dot)
			point_coords = self.canvas.coords(point)
			self.canvas.create_text(point_coords[0], point_coords[1] - 10, text = self.label)
		self.yes_dot = False
pen = Pen(canvas, "black", "red", "blue")
def draw_direction(event):
	if event.x and event.y:
		pen.mouse_x = event.x
		pen.mouse_y = event.y
		if pen.label == None:
			pen.yes_dot = True
		else:
			pen.yes_dot = "LabelPoint"
			print("You have made a point labeled the letter %s." % pen.label)
		pen.draw_dot()
		pen.label = None
	if event.keysym:
		pen.label = event.keysym
		print("You have pressed the letter %s." % event.keysym)
canvas.bind_all("<Button-1>", draw_direction)
canvas.bind_all("<Key>", draw_direction)
canvas.pack()
Tkinter.mainloop()