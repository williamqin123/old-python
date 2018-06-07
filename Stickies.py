import Tkinter, sys
maze = Tkinter.Tk()
maze.title("Maze")
mazeframe = Tkinter.Frame(maze, highlightbackground = "red", highlightthickness = 10)
canvas = Tkinter.Canvas(mazeframe, height = 300, width = 400, border = 0, highlightthickness = 0)
sprites = []
class Wall1:
	def __init__(self, x, y):
		self.id = canvas.create_rectangle(x, y, x + 100, y + 10, fill = "red")
class Wall2:
	def __init__(self, x, y):
		self.id = canvas.create_rectangle(x, y, x + 10, y + 100, fill = "red")
class Wall2T:
	def __init__(self, x, y):
		self.id = canvas.create_rectangle(x, y, x + 10, y + 100, fill = "yellow")
class Avatar:
	def __init__(self, sprites):
		self.sprites = sprites
		self.id = canvas.create_oval(385, 285, 395, 295, fill = "blue")
	def detectwall(self, event):
		for sprite in self.sprites:
			pos = canvas.coords(self.id)
			wallpos = canvas.coords(sprite.id)
			if pos[2] > wallpos[0] and pos[0] < wallpos[2]:
				if pos[1] < wallpos[1] and pos[3] > wallpos[1] and event.keysym == "Down":
					return wallpos
				elif pos[3] > wallpos[3] and pos[1] < wallpos[3] and event.keysym == "Up":
					return wallpos
			if pos[3] > wallpos[1] and pos[1] < wallpos[3]:
				if pos[0] < wallpos[0] and pos[2] > wallpos[0] and event.keysym == "Right":
					return wallpos
				elif pos[2] > wallpos[2] and pos[0] < wallpos[2] and event.keysym == "Left":
					return wallpos
		if event.keysym == "Up":
			y = -5
			x = 0
		elif event.keysym == "Down":
			y = 5
			x = 0
		elif event.keysym == "Left":
			y = 0
			x = -5
		elif event.keysym == "Right":
			y = 0
			x = 5
		canvas.move(self.id, x, y)
	def detectwallbegin(self, event):
		self.detectwall(event)
		if not self.detectwall(event) == None:
			if self.detectwall(event)[0] == 0 and self.detectwall(event)[1] == 0:
				sys.exit()
wall1 = Wall2T(0, 0)
wall2 = Wall1(0, 100)
wall3 = Wall2(100, 100)
wall4 = Wall1(100, 200)
wall5 = Wall1(200, 200)
wall6 = Wall2(300, 0)
wall8 = Wall1(200, 200)
wall9 = Wall1(200, 100)
sprites.append(wall1)
sprites.append(wall2)
sprites.append(wall3)
sprites.append(wall4)
sprites.append(wall5)
sprites.append(wall6)
sprites.append(wall8)
sprites.append(wall9)
avatar = Avatar(sprites)
canvas.bind_all("<KeyPress-Up>", avatar.detectwallbegin)
canvas.bind_all("<KeyPress-Down>", avatar.detectwallbegin)
canvas.bind_all("<KeyPress-Left>", avatar.detectwallbegin)
canvas.bind_all("<KeyPress-Right>", avatar.detectwallbegin)
canvas.pack()
mazeframe.pack()
Tkinter.mainloop()