import Tkinter, time, pickle
list_window = Tkinter.Tk()
list_window.wm_title("My List")
frame = Tkinter.Frame(list_window)
frame.pack()
list = ["(Blank List)"]
item_name = None
blank_list = True
num = 1
add_item = None
add_frame = None
add_frame_2 = None
seconds = time.time()
startup = None
list_check = Tkinter.StringVar(add_item)
list_check.set("Numbered List")
def main(code):
	if code == 56473228465732645637172846362128782948390587283682521:
		global startup
		def print_info():
			global seconds
			elapsed_time = time.time() - seconds
			item_count = len(list)
			list_type = list_check.get()
			list_end_info = {"Elapsed Time in Seconds" : elapsed_time, "Items in List on Exit" : item_count, "Current List Type": list_type, "Startup Time in Seconds" : startup}
			print list_end_info
			log = open("Smart List Log.txt", "wb")
			pickle.dump(list_end_info, log)
			log.close()
		def delete_item(name):
			index = list.index(name)
			del list[index]
		def refresh():
			global frame
			global num
			global period
			frame.destroy()
			frame = Tkinter.Frame(list_window)
			frame.pack()
			if list_check.get() == "Numbered List":
				num = 1
				period = "."
				whitespace = " "
			elif list_check.get() == "Bulleted List":
				num = "*"
				period = ""
				whitespace = " "
			elif list_check.get() == "List":
				num = ""
				period = ""
				whitespace = ""
			for item in list:
				Tkinter.Label(frame, text = "%s%s" % (str(num) + period + whitespace, item)).pack()
				if type(num) is int:
					num += 1
		def remove_from_list():
			delete_item(item_name.get())
			refresh()
		def reset_list():
			for item in list:
				del item
			refresh()
		def add_to_list():
			global blank_list
			list.append(item_name.get())
			if blank_list == True:
				delete_item("(Blank List)")
				blank_list = False
			refresh()
		def add_list_item():
			global item_name
			global list_check
			global add_item
			global add_frame
			global add_frame_2
			add_item = Tkinter.Tk()
			add_item.wm_title("Add Item")
			add_frame_2 = Tkinter.Frame(add_item)
			add_frame_2.pack()
			Tkinter.OptionMenu(add_frame_2, list_check, "List", "Numbered List", "Bulleted List").pack(side = "left")
			Tkinter.Button(add_frame_2, text = "X", command = reset_list).pack(side = "right")
			item_name = Tkinter.Entry(add_item)
			item_name.pack()
			add_frame = Tkinter.Frame(add_item)
			add_frame.pack()
			Tkinter.Button(add_frame, text = "Add", command = add_to_list).pack(side = "left")
			Tkinter.Button(add_frame, text = "Remove", command = remove_from_list).pack(side = "right")
			Tkinter.Button(add_item, text = "Apply Changes", command = refresh).pack()
		Tkinter.Button(list_window, text = "Edit List", command = add_list_item).pack()
		refresh()
		print "%s seconds application startup" % (time.time() - seconds)
		startup = time.time() - seconds
		Tkinter.mainloop()
		print_info()
main(56473228465732645637172846362128782948390587283682521)