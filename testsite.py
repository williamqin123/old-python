file = open("../Gamestar Mechanic/Website/index.html", "r")
html = str(file.readlines())
print(html)
file.close()