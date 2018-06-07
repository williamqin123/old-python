from Tkinter import *
import random
from time import sleep
def run():
	rand = random.choice("abcdefghijklmnopqrstuvwxyz")
	lab = Label(text = str(rand))
	lab.pack(side = "top")
	enter = Entry(width = 50)
	enter.pack()
	def new():
		if str(enter.get) == str(rand):
			run()
		else:
			None
	Button(text = "Test my memory skills!", command = new).pack()
	mainloop()
	sleep(3)
	lab.pack_forget()
	mainloop()
run()
