import Tkinter, time, copy, random

game_window = Tkinter.Tk()
game_window.title("PaddleBall")
game_window.resizable(0, 0)
canvas = Tkinter.Canvas(game_window, width = 768, height = 480, bd = 0, highlightthickness = 0)

wallpaper = Tkinter.PhotoImage(file = "../Mr. Stick Man Races for the Exit/Wallpaper.gif")
canvas.create_image(0, 0, anchor = "nw", image = wallpaper)

class Paddle:
	def __init__(self, canvas, color, top):
		self.canvas = canvas
		self.id = canvas.create_rectangle(10, 10, 160, 22, fill = color)
		self.canvas.move(self.id, 10, top)
	def setBall(self, ball):
		self.ball = ball
	def draw(self):
		pos = self.canvas.coords(self.id)
		if pos[0] < 0:
			canvas.move(self.id, 20, 0)
		elif pos[2] > self.canvas.winfo_width():
			canvas.move(self.id, -20, 0)

class Computerpaddle(Paddle):
	def __init__(self, canvas, color, top):
		self.canvas = canvas
		self.id = canvas.create_rectangle(10, 10, 160, 22, fill = color)
		self.canvas.move(self.id, 10, top)
		self.x = 0
		self.y = 0

	def draw(self):
		poss = self.canvas.coords(self.ball.id)
		cpupaddlepos = self.canvas.coords(self.id)
		canvas.move(self.id, self.x, self.y)
		if poss[2] > cpupaddlepos[2]:
			self.x = 5
		elif poss[0] < cpupaddlepos[0]:
			self.x = -5

class Ball:
	def __init__(self, canvas, color):
		self.canvas = canvas
		self.id = canvas.create_oval(10, 10, 32, 32, fill = color)
		self.canvas.move(self.id, 300, 200)
		starts = [-3, 3]
		random.shuffle(starts)
		self.x = starts[0]
		self.y = starts[1]
	def setpaddle(self, paddle1, paddle2):
		self.paddle1 = paddle1
		self.paddle2 = paddle2		
	def hitpaddle(self, pos):
		print 'position: ' + str(pos)
		paddle_pos = self.canvas.coords(self.paddle1.id)
		paddle_pos2 = self.canvas.coords(self.paddle2.id)

		if pos[2] > paddle_pos[0] and pos[0] < paddle_pos[2]:
			if pos[3] > paddle_pos[3] and pos[1] < paddle_pos[3]:
				print("Ball hits the bottom of the top paddle.")
				return "Down"
			if pos[1] < paddle_pos[1] and pos[3] > paddle_pos[1]:
				print("Ball hits the top of the top paddle.")
				return "Up"
		if pos[2] > paddle_pos2[0] and pos[0] < paddle_pos2[2]:
			if pos[3] > paddle_pos2[3] and pos[1] < paddle_pos2[3]:
				print("Ball hits the bottom of the bottom paddle.")
				return "Down"
			if pos[1] < paddle_pos2[1] and pos[3] > paddle_pos2[1]:
				print("Ball hits the top of the bottom paddle.")
				return "Up"
		return False

	def draw(self):
		self.canvas.move(self.id, self.x, self.y)
		pos = self.canvas.coords(self.id)
		if self.hitpaddle(pos) == "Up":
			self.y = -3
		elif self.hitpaddle(pos) == "Down":
			self.y = 3
		if pos[0] < 0:
			self.x = 3
		elif pos[2] > self.canvas.winfo_width():
			self.x = -3
		elif pos[1] < 0:
			self.y = 3
		elif pos[3] > self.canvas.winfo_height():
			self.y = -3
		else:
			None
		print(self.hitpaddle(pos))

def movepaddle(event):
	global item
	if event.keysym == "Right":
		canvas.move(paddle2.id, 20, 0)
	elif event.keysym == "Left":
		canvas.move(paddle2.id, -20, 0)

class Game:
	def __init__(self, paddle1, paddle2, ball):
		ball.setpaddle(paddle1, paddle2)
		paddle1.setBall(ball)
		paddle2.setBall(ball)

paddle1 = Computerpaddle(canvas, "blue", 38)
paddle2 = Paddle(canvas, "blue", 418)
ball = Ball(canvas, "red")
game = Game(paddle1, paddle2, ball)

canvas.bind_all("<KeyPress-Right>", movepaddle)
canvas.bind_all("<KeyPress-Left>", movepaddle)
canvas.pack()

while True:
	ball.draw()
	paddle1.draw()
	paddle2.draw()
	game_window.update_idletasks()
	game_window.update()
	time.sleep(0.01)

Tkinter.mainloop()
