
# created by William Qin
# remote control program

import tkinter, sys, os, webbrowser, time, tkinter.ttk

print("Remote Control 0.1.0")
print(">>>")

ttbar = tkinter.Tk()
ttbar.wm_title("Remote Control")

ttbar.geometry("160x400")

def google():
	webbrowser.open("http://www.google.com")
	
def bing():
	webbrowser.open("http://www.bing.com")

def hotmail():
	webbrowser.open("http://www.hotmail.com")
	
def gmail():
	webbrowser.open("http://www.gmail.com")

def ask():
	webbrowser.open("http://www.ask.com")
	
def textbox():
	ttbar_2 = tkinter.Tk()
	type_txt = tkinter.Text(ttbar_2, bd = 3, width = 30, height = 10).pack()
	ttbar_2.wm_title("Type Text")
	
def settings():
	ttbar_3 = tkinter.Tk()
	ttbar_3.wm_title("Remote Info")
	ttbar_3.geometry("192x156")
	# tkinter.OptionMenu(ttbar_3, variable = None, value = "Classic").pack()
	tkinter.Label(ttbar_3, text = "Remote Control 0.1.0").pack()
	
tkinter.Label(ttbar, text = "Remote Control", font = "arial 14 bold", fg = "red").pack()
tkinter.Label(ttbar, text = "Program Controls", width = 16, height = 1, fg = "blue", font = "arial 10 bold").pack()
tkinter.Button(ttbar, text = "Exit Remote", relief = "groove", activebackground = "red", bd = 4, width = 16, command = sys.exit).pack()
tkinter.Button(ttbar, text = "Do Nothing", relief = "groove", activebackground = "gray",  bd = 4, width = 16, command = None).pack()
tkinter.Label(ttbar, text = "Search Tools", width = 16, height = 1, fg = "blue", font = "arial 10 bold").pack()
tkinter.Button(ttbar, text = "Search Google", relief = "groove", activebackground = "gray", bd = 4, width = 16, command = google).pack()
tkinter.Button(ttbar, text = "Search Bing", relief = "groove", activebackground = "gray", bd = 4, width = 16, command = bing).pack()
tkinter.Button(ttbar, text = "Search Ask.com", relief = "groove", activebackground = "gray", bd = 4, width = 16, command = ask).pack()
tkinter.Label(ttbar, text = "E-Mail", width = 16, height = 1, fg = "blue", font = "arial 10 bold").pack()
tkinter.Button(ttbar, text = "Hotmail", relief = "groove", activebackground = "gray", bd = 4, width = 16, command = hotmail).pack()
tkinter.Button(ttbar, text = "Gmail", relief = "groove", activebackground = "gray", bd = 4, width = 16, command = gmail).pack()
tkinter.Label(ttbar, text = "Text Tools", width = 16, height = 1, fg = "blue", font = "arial 10 bold").pack()
tkinter.Button(ttbar, text = "Type Text", relief = "groove", activebackground = "gray", bd = 4, width = 16, command = textbox).pack()

menu_bar = tkinter.Menu(ttbar)
file_menu = tkinter.Menu(menu_bar)
file_menu.add_command(label = "Exit Remote", command = sys.exit)
file_menu.add_command(label = "Remote Info", command = settings)
menu_bar.add_cascade(label = "File", menu = file_menu)
ttbar.config(menu = menu_bar)
tkinter.mainloop()

