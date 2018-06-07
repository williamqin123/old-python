from os import system
from sys import stdout
import random
from time import sleep
print("2013 Dice 0.1.01")
print(">>>")
system("color 0c")
def run():
	input("Press enter to throw the dice.")
	count = 0
	while count < 6:
		stdout.flush()
		number = stdout.write(str(random.randint(1, 6)))
		sleep(0.18)
		stdout.write("\010")
		count += 1

	print()
	input("Press enter to throw again.")
	system("cls")
	run()
run()
