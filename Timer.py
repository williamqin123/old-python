print("2013 Timer 1.0.01")
print(">>>")
from time import sleep
from sys import stdout
print("Time elapsed:")

def count():
	stop = 0
	k = 1
	while k > 0:
		s = str(k) + " seconds"
		stdout.write(s)
		b = len(s)
		stdout.flush()
		k += 1
		sleep(1)
		stdout.write("\010" * b)
		
count()
