import tkinter, tkinter.ttk, random, sys, time

tk_ttk = tkinter.Tk()

tk_ttk.wm_title("Multiplication Math Star! (1-12)")

tk_ttk.geometry("360x120")

frame_tk = tkinter.Frame(tk_ttk)

sty = tkinter.ttk.Style()

inti = tkinter.ttk.Entry(tk_ttk, font = "Arial 16 bold")
def run_game():
	global sty
	rand_operand_1 = random.randint(1, 12)
	rand_operand_2 = random.randint(1, 12)
	
	def deehe():
		if int(inti.get()) == int(rand_operand_1) * int(rand_operand_2):
			opr.pack_forget()
			inti.pack_forget()
			go_to_next.pack_forget()
			run_game()
		
		else:
			None

	opr = tkinter.ttk.Label(tk_ttk, text = str(rand_operand_1) + "x" + str(rand_operand_2), font = "Arial 28 bold")

	go_to_next = tkinter.ttk.Button(text = "Next", command = deehe)
	
	sty.configure("TButton", font = "Arial 16 bold", width = 12, background = "#091")
	
	opr.pack()

	inti.pack()

	go_to_next.pack()

	tkinter.mainloop()
	
run_game()