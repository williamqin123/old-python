import tkinter, tkinter.ttk
window = tkinter.Tk()
frame = tkinter.Frame(window)
window.wm_title("Writer")
textbox = tkinter.Text(window, width = 99999999, height = 99999999, font = "Arial 12", border = 0)
window.geometry("800x600")
grip = tkinter.ttk.Sizegrip(window).pack(side = "bottom", anchor = "se")
scrollbar = tkinter.ttk.Scrollbar(window)
scrollbar.pack(side = "right", fill = "y")
scrollbar.config(orient = "vertical", command = textbox.yview)
'''openbox = tkinter.Tkopenbox = tkinter.Tk
location = tkinter.ttk.Entry(openbox, width = 50)

def openfile():
	finalloc = str(location.get)
	finalloc = []
	openthetxtfile = open(finalloc)
	
def open():
	global location
	openbox = tkinter.Tk()
	openbox.wm_title("Open text file...")
	tkinter.ttk.Label(openbox, text = "Enter location of file").pack()
	location.pack()
	tkinter.ttk.Button(openbox, text = "Open text file", command = openfile).pack()
def save():
	savebox = tkinter.Tk()
	savebox.wm_title("Save as file...")
	tkinter.ttk.Label(savebox, text = "Enter file name").pack()
	tkinter.ttk.Entry(savebox, width = 50).pack()
	tkinter.ttk.Label(savebox, text = "Enter saving location").pack()
	tkinter.ttk.Entry(savebox, width = 50).pack()
	tkinter.ttk.Button(savebox, text = "Save as file", command = None).pack()


#tkinter.ttk.Button(text = "Save", command = save).pack(side = "left")'''
textbox.pack(side = "left")
'''menubar = tkinter.Menu(window)
bar = tkinter.Menu(menubar)
bar.add_command(label = "Save as file...", command = save)
bar.add_command(label = "Open text file...", command = open)
menubar.add_cascade(label = "File", menu = bar)
window.config(menu = menubar)'''
tkinter.mainloop()