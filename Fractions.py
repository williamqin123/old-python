import Tkinter
main = Tkinter.Tk()
main.geometry("240x180")
main.title("iFraction Bars")
main.attributes("-alpha", 0.85)
canvas = Tkinter.Canvas(main, width = 200, height = 99999999)
frame = Tkinter.Frame(main)
frame.pack()
coords = 0
whole = Tkinter.Entry(frame, width = 2)
numerator = Tkinter.Entry(frame, width = 2)
denominator = Tkinter.Entry(frame, width = 2)
whole.pack(side = "left")
numerator.pack(side = "left")
Tkinter.Label(frame, text = "/").pack(side = "left")
denominator.pack(side = "left")
def fraction():
	global coords
	coords = 0
	count_up = 0
	change_color = 0
	color = "gray"
	count = int(numerator.get())
	canvas.delete("all")
	if whole.get():
		count = int(whole.get()) * int(denominator.get()) + int(numerator.get())
		change_color = int(whole.get())
	if count > int(denominator.get()):
		while count > int(denominator.get()):
			color = "blue"
			if change_color > 0:
				color = "green"
				change_color = change_color - 1
			count_up = count_up + 0
			coords = (count_up * 20) + (count_up * 4)
			canvas.create_rectangle(0, coords, 200, coords + 20, fill = color)
			count = count - int(denominator.get())
			count_up = count_up + 1
			coords = (count_up * 20) + (count_up * 4)
		canvas.create_rectangle(0, coords, 200 / int(denominator.get()) * count, coords + 20, fill = "red")
	else:
		canvas.create_rectangle(0, coords, (200 / int(denominator.get())) * int(numerator.get()), coords + 20, fill = "red")
	canvas.create_rectangle(0, coords, 200, coords + 20)
	canvas.pack()
Tkinter.Button(frame, text = "iFraction", command = fraction).pack(side = "left")
Tkinter.mainloop()