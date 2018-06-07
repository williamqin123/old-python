from sys import stdout
import winsound, random
print("2013 Microsoft Windows Beeper 1.0.01")
print(">>>")

def beep():
	count = 0
	while count > 0 or count == 0:
		dur = random.randint(100, 700)
		freq1 = random.randint(300, 1000)
		winsound.Beep(freq1, dur)
beep()
	