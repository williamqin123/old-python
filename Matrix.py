import random, os
from sys import stdout
from time import sleep
os.system("color 0A")
num = 0
while num < 10:
	code = 0
	while code < 25:
		stdout.flush()
		stdout.write(str(random.choice(list(["0 ", "1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 "]))))
		stdout.write(str("\010" * 2))
		sleep(0.025)
		code += 1
	
	num += 1
	if num == 1:
		stdout.write(str("T"))
	elif num == 2:
		stdout.write(str("h"))
	elif num == 3:
		stdout.write(str("e"))
	elif num == 4:
		stdout.write(str(" "))
	elif num == 5:
		stdout.write(str("M"))
	elif num == 6:
		stdout.write(str("a"))
	elif num == 7:
		stdout.write(str("t"))
	elif num == 8:
		stdout.write(str("r"))
	elif num == 9:
		stdout.write(str("i"))
	elif num == 10:
		stdout.write(str("x"))
	stdout.flush()
input()
