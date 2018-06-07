from Tkinter import *
import random
tkkk = Tk()
tkkk.wm_title("Crazy Art Studio Deluxe")
cvs = Canvas(height = 600, width = 800)
def nerase():
	cvs.delete("all")
def rec():
	cvs.create_rectangle(random.randint(1, 800), random.randint(1, 600), random.randint(1, 800), random.randint(1, 600), fill = random.choice(list(["#f20", "#fd0", "#091", "#03f", "#f90", "#0fa", "#f07", "#70a"])))
def circ():
	cvs.create_oval(random.randint(1, 800), random.randint(1, 600), random.randint(1, 800), random.randint(1, 600), fill = random.choice(list(["#f20", "#fd0", "#091", "#03f", "#f90", "#0fa", "#f07", "#70a"])))
def crazyart():
	cvs.create_line(random.randint(1, 800), random.randint(1, 600), random.randint(1, 800), random.randint(1, 600), fill = random.choice(list(["#f20", "#fd0", "#091", "#03f", "#f90", "#0fa", "#f07", "#70a"])))
def gocrazy():
	count = 0
	while count < 50:
		cvs.create_line(random.randint(1, 800), random.randint(1, 600), random.randint(1, 800), random.randint(1, 600), fill = random.choice(list(["#f20", "#fd0", "#091", "#03f"])))
		cvs.create_rectangle(random.randint(1, 800), random.randint(1, 600), random.randint(1, 800), random.randint(1, 600), fill = random.choice(list(["#f90", "#0fa", "#f07", "#70a"])))
		cvs.create_oval(random.randint(1, 800), random.randint(1, 600), random.randint(1, 800), random.randint(1, 600), fill = random.choice(list(["#f20", "#fd0", "#091", "#03f"])))
		count += 1
Button(text = "Draw a line", width = 16, command = crazyart).pack(side = "bottom")
Button(text = "Go crazy", width = 16, command = gocrazy).pack(side = "bottom")
Button(text = "Draw a rectangle", width = 16, command = rec).pack(side = "bottom")
Button(text = "Draw an oval", width = 16, command = circ).pack(side = "bottom")
Button(text = "Clear canvas", width = 16, command = nerase).pack(side = "bottom")
Label(text = "Crazy Art Studio", font = "Arial 36 bold", fg = "red").pack(side = "top")
cvs.pack()
mainloop()
