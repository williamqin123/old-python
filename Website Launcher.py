import webbrowser
from sys import stdout
print("2013 Website Launcher 1.0.01")
print(">>>")
print("Go to website:")
count = 1
while count > 0:
	stdout.flush()
	open = input("http://")
	webbrowser.open("" + open)
	stdout.write("\010" * len(open))