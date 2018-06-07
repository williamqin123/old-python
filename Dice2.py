import tkinter.ttk, tkinter
import random
from time import sleep
title = "Roll Dice"
count = 0

def roll_dice():
	global count
	while count < 6:
		button.pack_forget()
		title = random.choice(list(["1", "2", "3", "4", "5", "6"]))
		sleep(0.17)
		button.pack()
	if count == 6:
		count = 0
		title = "Roll Dice"

button = tkinter.ttk.Button(text = title, command = roll_dice)
button.pack()
tkinter.mainloop()