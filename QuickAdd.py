import Tkinter, random, sys, time

tk_ttk = Tkinter.Tk()

tk_ttk.wm_title("Multiplication Fact Quiz")

frame = Tkinter.Frame(tk_ttk)

frame.pack()

inti = Tkinter.Entry(frame)

seconds = time.time()

count = 1

total = 10

def run_game():

	global count, inti, tk_ttk, total

	rand_operand_1 = random.randint(1, 12)

	rand_operand_2 = random.randint(1, 12)
	
	def deehe():

		global frame

		if int(inti.get()) == rand_operand_1 * rand_operand_2:

			frame.destroy()

			frame = Tkinter.Frame(tk_ttk)

			frame.pack()

			run_game()
		
		else:

			print rand_operand_1 + rand_operand_2, inti.get()

	opr = Tkinter.Label(frame, text = "%s x %s" % (rand_operand_1, rand_operand_2))

	go_to_next = Tkinter.Button(frame, text = "Go", command = deehe)

	Tkinter.Label(frame, text = "Problem %s / %s" % (count, total)).pack()
	
	opr.pack()

	inti.pack()

	go_to_next.pack()

	if count > total:

		frame.destroy()

		Tkinter.Label(tk_ttk, text = "Great job! It took you %s seconds to do these problems." % time.time() - seconds)

	count = count + 1

	Tkinter.mainloop()

	run_game()

run_game()