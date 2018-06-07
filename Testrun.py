#First lines and importing:
import os
os.system("cls")
print ("2013 Testrun Viewers 0.1.02")
print (">>>")
input ("Press enter to view a test file. Press CTRL-SHIFT-C or ALT-F4 to quit Testrun Viewer.")
message = ("Press enter to view the next test file.")

#Choose random name:
def randname():
	os.system("cls")
	print ("Random name chooser")
	import random
	print(random.choice(["William", "Daddy", "Mommy", "Aaron"]))
	input (message)
	
#Display numbers that are less than 5:
def loop1():
	os.system("cls")
	print ("loop test 1")
	count = 0
	while count < 5:
		print (count)
		count += 1 
	input (message)
	
#Display all even numbers before 501:
def loop2():
	os.system("cls")
	print ("Loop test 2")
	numbers = [951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
		615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
		386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
		399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
		815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
		958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
		743, 527]

	for number in numbers:
		if number % 2 == 1:
			print (number)
		if number == 501:
			break   
	input (message)
	
#Asks you how much a car is worth:
def carworth():
	os.system("cls")
	print ("Worth of a vehicle")
	period = "."
	class MyCar1:
		name = "Fer"
		kind = "convertible"
		color = "red"
		worth = "$60000.00"
		description = "%s is a %s %s worth %s%s" % (name, color, kind, worth, period)
	class MyCar2:
		name = "Jump"
		kind = "van"
		color = "blue"
		worth = "$10000.00"
		description = "%s is a %s %s worth %s%s" % (name, color, kind, worth, period)
	print (MyCar1.description)
	print (MyCar2.description)
	print ("Don't forget the $ symbol and .00 when you answer this question:")
	print ("How much is Fer worth?")
	moneyinput = input ("")
	if moneyinput == "$60000.00":
		print ("Correct! Fer is worth $60000.00.")
	else:
		print ("Sorry, but that is incorrect. Fer is worth $60000.00.")
	input (message)

#Tells who is in the phonebook:
def phonebook():
	os.system("cls")
	print ("Phonebook contacts")
	print ("Phonebook: John - 938477566, Jack - 938377264, Jill - 947662781")
	contacts = {"John" : 938477566, "Jack" : 938377264, "Jill" : 947662781}
	if "Jake" in contacts:
		print ("Jake is listed in the phonebook.")
	else:
		print ("Jake is not listed in the phonebook.")
	if "Jill" not in contacts:
		print ("Jill is not listed in the phonebook.")
	else:
		print ("Jill is listed in the phonebook.")
	input (message)

#Displays text about someone's balance:
def myvariables():
	os.system("cls")
	print ("Variable and print data test")
	myString = ("John Doe. ")
	mySegment = ("Your current balance is $54.44.")
	def printdata():
		print ("Hello %s %s" % (myString, mySegment))
	printdata()
	input (message)

#Types super characters:
def specialchar():
	os.system("cls")
	password = input("Type your name for approval to crash the program: ")
	if password == "william" or password == "William":
		os.system("cls")
		input("")
		hfgfvhfbehgmweaajfkehsgfg(hfehf)
	else:
		testrun()
	input(message)

#Calls all functions:
def testrun():
	randname()
	loop1()
	loop2()
	carworth()
	phonebook()
	myvariables()
	specialchar()
	testrun()

#Repeats all functions:	
testrun()
