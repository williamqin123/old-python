from os import system
from time import sleep
from sys import stdout
print("2013 Rainbow Colors 0.2.01")
print(">>>")
print('''Welcome to rainbow colors!
Press enter to switch background colors.''')
count = 1
while count == 100 or count < 100:
	system("color 0F")
	a = ("Loading..." + str(count) + "%")
	stdout.write(a)
	sleep(0.05)
	stdout.flush()
	count += 1
	stdout.write("\010" * len(a))
system("cls")
while count > 0:
	system("color 10")
	input("")
	system("color 20")
	input("")
	system("color 30")
	input("")
	system("color 40")
	input("")
	system("color 50")
	input("")
	system("color 60")
	input("")
	system("color 80")
	input("")
	