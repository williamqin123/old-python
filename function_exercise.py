from time import sleep, time
from sys import stdout

class Timer:
	def __init__(self, time, unit):
		self.time = int(time)
		self.unit = unit

	def count_down(self):
		for x in range(self.time, 0, -1):
			stdout.write("%s, " % x)
			stdout.flush()
			if self.unit == "minutes":
				sleep(60)
			else:
				sleep(1)
		stdout.write("Time's up!")

	def show_time_left(self):
		sec_left = self.time
		min_left = 0
		if self.unit == "seconds" and self.time >= 60:
			while sec_left >= 60:
				sec_left -= 60
				min_left += 1
		elif self.unit == "minutes":
			min_left = self.time
			sec_left = 0
		for i in range(self.time, 0, -1):
			time_left = "%s : %s" % (min_left, sec_left)
			if sec_left == 0:
				sec_left = 59
				min_left -= 1
			sec_left -= 1
			stdout.write("\010" * len(time_left))
			stdout.write(time_left)
			stdout.flush()
			sleep(1)

def timer_run():
	start = time()
	print(start)
	time_unit = raw_input("Time Unit: ")
	number_of_units = raw_input("Number of %s: " % time_unit)
	timer = Timer(number_of_units, time_unit)
	timer.show_time_left()
	print()
	print("%s seconds have passed since this program started." % str(int(time()) - int(start)))

timer_run()
