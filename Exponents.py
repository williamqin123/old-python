import Tkinter
window = Tkinter.Tk()
window.title("BMI Calculator")
window.attributes("-alpha", 0.85)
window.attributes("-transparent", 1)
frame = Tkinter.Frame(window)
frame.pack()
frame2 = Tkinter.Frame(window)
frame2.pack()
canvas = Tkinter.Canvas(window, height = 38, width = 200, border = 0, highlightthickness = 0)
var = Tkinter.StringVar()
var2 = Tkinter.StringVar()
Tkinter.Label(frame, text = "Height").pack(side = "left")
feet = Tkinter.OptionMenu(frame, var, "1", "2", "3", "4", "5", "6", "7")
feet.pack(side = "left")
inches = Tkinter.OptionMenu(frame, var2, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11")
inches.pack(side = "left")
Tkinter.Label(frame2, text = "Weight").pack(side = "left")
pounds = Tkinter.Entry(frame2, width = 4)
pounds.pack(side = "left")
Tkinter.Label(frame2, text = "Pounds").pack(side = "left")
def calculate():
	kg = float(pounds.get()) * 0.45
	m = ((int(var.get()) * 12) + (int(var2.get()))) * 0.025
	squ = m * m
	answ = kg / squ
	hth = "Undefined"
	hth3c = "gray"
	if answ < 18.5:
		hth = "Underweight"
		hth3c = "cyan"
	elif answ >= 18.5 and answ <= 25:
		hth = "Healthy"
		hth3c = "green"
	elif answ > 25 and answ <= 30:
		hth = "Overweight"
		hth3c = "orange"
	else:
		hth = "Obese"
		hth3c = "red"
	canvas.delete("all")
	canvas.create_rectangle(4, 4, int(answ) * 3, 34, fill = hth3c)
	canvas.create_text(5, 5, anchor = "nw", text = "%s (%s)" % (answ, hth))
	canvas.pack()
Tkinter.Button(window, text = "Calculate Your BMI", command = calculate).pack()
Tkinter.mainloop()