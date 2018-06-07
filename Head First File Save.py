import Tkinter

MainWindow = Tkinter.Tk()
MainWindow.title("Python Dictionary")
MainWindow.attributes("-transparent", 1)
MainWindow.attributes("-titlepath", 1)
MainWindow.attributes("-notify", 1)

class DictionaryProgram:
	def __init__(self, DictFileName):
		self.DictionaryFile = open(DictFileName, "rw")
		self.WordEntry = Tkinter.Entry(MainWindow)
		self.WordEntry.pack()
		self.DefinitionLabel = Tkinter.Label(MainWindow, text = "[ Definition ]")
		self.DefinitionLabel.pack()
		exec(self.DictionaryFile)

	def LookItUp(self):
		for word in self.DictionaryLine:
			if word == self.WordEntry.get():
				self.DefinitionLabel.destroy()
				self.DefinitionLabel = Tkinter.Label(MainWindow, text = self.DictionaryLine[word])
				self.DefinitionLabel.pack()

dictionaryProgram = DictionaryProgram("Dictionary.txt")
LookUpButton = Tkinter.Button(MainWindow, text = "Look it Up", command = dictionaryProgram.LookItUp)
LookUpButton.pack()
Tkinter.mainloop()