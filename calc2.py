import turtle
pencil = turtle.Pen()
def draw_polygon(side_length, points, line_size, fg_color, bg_color):
	degrees_1 = 360 / points
	degrees_2 = 720 / points
	pencil.pensize(line_size)
	pencil.color(fg_color)
	pencil.fill(True)
	for loop in range(0, points):
		pencil.forward(side_length)
		pencil.left(degrees_1)
		pencil.forward(side_length)
		pencil.right(degrees_2)
	pencil.color(bg_color)
	pencil.fill(False)
draw_polygon(side_length = 100, points = 5, line_size = 2, fg_color = "black", bg_color = "red")
raw_input()