import Tkinter
list_window = Tkinter.Tk()
list_window.wm_title("My List")
frame = Tkinter.Frame(list_window)
frame.pack()
list = []
item_name = None
def refresh():
	global frame
	frame.destroy()
	frame = Tkinter.Frame(list_window)
	frame.pack()
	for items in list:
		Tkinter.Label(frame, text = items).pack()
def add_to_list():
	list.append(item_name.get())
	refresh()
def add_list_item():
	global item_name
	add_item = Tkinter.Tk()
	item_name = Tkinter.Entry(add_item)
	item_name.pack()
	Tkinter.Button(add_item, text = "Add", command = add_to_list).pack()
	Tkinter.Button(add_item, text = "Remove", command = remove_from_list).pack()
Tkinter.Button(list_window, text = "Add List Item", command = add_list_item).pack()
Tkinter.mainloop()