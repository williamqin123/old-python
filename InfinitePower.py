import time
oldTime = None
elapsedList = []
def calcTime(cycles):
	for x in range(0, cycles):
		x = x * x
		actualEdit = str(x)
		editLength = len(actualEdit)
		print actualEdit + ("\b" * editLength) + (" " * editLength)
	elapsed = str(time.time() - oldTime)
	elapsedList.append(float(elapsed))
userInput = raw_input("Cycle Count: >>> _")
def reset():
	global oldTime
	oldTime = time.time()
	calcTime(int(userInput))
for y in range(0, 3):
	reset()
elapsedAverage = elapsedList[0] + elapsedList[1] + elapsedList[2]
calcAverage = str(elapsedAverage / 3)
print "Your computer can loop %s times in an average of %s seconds." % (userInput, calcAverage[:calcAverage.index(".") + 4])