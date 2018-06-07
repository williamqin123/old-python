import turtle
pencil = turtle.Pen()
pencil.speed(5)
count = 0
while count == 0:
	pencil.pensize(2)
	command = raw_input("Draw: ")
	if command == "turn":
		turn = raw_input("Turn direction: ")
		degrees = input("Turn degrees: ")
		if turn == "left":
			pencil.left(degrees)
		elif turn == "right":
			pencil.right(degrees)
	elif command == "line" or command == "move":
		if command == "move":
			pencil.penup()
		distance = input("How far: ")
		pencil.forward(distance)
		pencil.pendown()
	elif command == "reset":
		pencil.reset()
	elif command == "circle":
		radius = input("Radius: ")
		angle = input("Angle: ")
		pencil.circle(radius, angle)
	elif command == "begin fill shape":
		pencil.fill(True)
		print "If you behin a fill shape, you have to end the fill shape after the shape is drawn."
	elif command == "end fill shape":
		pencil.fill(False)
	elif command == "color":
		color = raw_input("Color: ")
		pencil.color(color)
		background = raw_input()
		if background == "bgcolor":
			bg = raw_input("Background color: ")
			turtle.bgcolor(bg)
		elif background == "bgpic":
			bgpic = raw_input("Background image: ")
			turtle.bgpic(bgpic)
	elif command == "text":
		text = raw_input("Text: ")
		change_font_yes_or_no = raw_input()
		if change_font_yes_or_no == "font":
			change_font = raw_input("Font: ")
			size = input("Font size: ")
			style = raw_input("Font style: ")
		elif change_font_yes_or_no == "":
			change_font = "Arial"
			size = 12
			style = "normal"
		pencil.write(text, font = (change_font, size, style))
	elif command == "dot":
		pencil.dot(5)
	else:
		None
	print