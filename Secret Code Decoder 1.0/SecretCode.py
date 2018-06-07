charlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "@", " ", "\n"]
codelist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "&", "%", "*", "@", "!", "#", "$", "(", ")", "^", ">", "<", "?", "/", "|", "~", " ", " ", "\n"]
entry = raw_input("Enter the directory/location of the file you want to encode or decode: ")
codefile = open(entry, "w+")
codefile.seek(0, 0)
header = "@\n"
content = ""
lines = codefile.readlines()
encode = False
decode = False
for line in lines:
	line.split()
	if line == header or decode == True:
		for i in line:
			content = content + charlist[codelist.index(i)]
		decode = True
	else:
		for x in line:
			content = content + codelist[charlist.index(x)]
		encode = True
if encode == True:
	content = "@\n" + content
print("Your final processed secret message is:\n" + content)
codefile.truncate()
codefile.write(content)
codefile.close()