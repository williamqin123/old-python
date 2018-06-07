import tkinter.ttk, tkinter, webbrowser

window_1 = tkinter.Tk()
window_1.wm_title("Website Launcher")

txt_box = tkinter.ttk.Entry(width = 75)
def enter_web_address():
	address = txt_box.get()
	webbrowser.open(address)

sch_box = tkinter.Button(text = "Go", width = 4, fg = "white", command = enter_web_address)

sch_box.configure(bg = "#081")
txt_box.pack(side = "left")
sch_box.pack(side = "right")

tkinter.mainloop()