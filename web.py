def html(string):

	newcode = '''\n<!doctype html>''';
	elements = {
		"heading" : "h1",
		"item" : "span",
		"box" : "div",
		"bold" : "strong",
		"italic" : "em",
		"picture" : "img",
		"link" : "a",
		"" : "p"
	}

	for line in string.split("\n"):

		element = elements[line[:line.index(" ")]]
		content = line[line.index(" ") + 1 :]

		if "///" in line:
			attrib = line[line.index(" ") + 1 : line.index("/")]
			content = line[line.index("///") + 3 :]

		if element == "img":
			newcode = newcode+"\n<%s %s='%s'>" % (element, attrib, content)

		else:
			newcode = newcode+"\n<%s>%s</%s>" % (element, content, element)

	print newcode + "\n"
	return newcode


code = '''heading text
box content
picture src /// image-url
 text
 text
bold information'''
html(code)