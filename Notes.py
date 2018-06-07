recent = "Recent notes: "
print ("2013 Research Notes 0.1.01")
print (">>>")
fUser = open ("Data/userdata.css", "r+")
username = str(fUser.readline())
notepad = ">>>"
fSaveTxt = open("Data/savetxt.css", "r+")
txt = str(fSaveTxt.readline())

def loop():
	count = 1
	while count > 0:
		data = ""
		data = input(notepad + data)
		fSaveTxt.seek(0)
		fSaveTxt.write(str(data))
		count += 1
		
if username == "":
	print("Register to research notes: ")
	username = input("Create username: ")
	fUser.seek(0)
	fUser.write(str(username))
	print (recent)
	print(txt)
	loop()
else:
	print ("Login to research notes: ")
	userinput = input("Username: ")
	if userinput == username:
		print (recent)
		print(txt)
		loop()
	else:
		input("The username could was not recognized. Press enter to use research notes as a guest.")
		print ("You are a guest. Research notes does not remember history for guests.")
		loop()
