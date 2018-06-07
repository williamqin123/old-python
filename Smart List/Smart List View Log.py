import pickle, Tkinter
tk_view_scores = Tkinter.Tk()
tk_view_scores.wm_title("Smart List Log Information")
frame = Tkinter.Frame(tk_view_scores)
frame2 = Tkinter.Frame(tk_view_scores)
Tkinter.Label(tk_view_scores, text = "Information from the Last Time Smart List was Run").pack()
frame.pack(side = "left")
frame2.pack(side = "right")
scores = open("Smart List Log.txt", "rb")
scores_list = pickle.load(scores)
print scores_list
for score in scores_list:
	Tkinter.Label(frame, text = score).pack()
	Tkinter.Label(frame2, text = scores_list[score]).pack()
Tkinter.mainloop()