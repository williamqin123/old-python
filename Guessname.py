import os
os.system("cls")
print ("2013 Guess My Name 0.1.00") 
print (">>>")
input ("Welcome to Guess My Name. In this game you will guess the name of the creator of this program.")
def guessname():
	correct = False
	print ("What is the name of the creator of this program? ")
	name = input ("")
	if name == "william" or name == "William":
		print ("Correct! 'William' is the creator of this program.")
		input ("Press enter to quit game.")
		correct = True
	elif name == "richard" or name == "Richard":
		print ("'Richard' is in the family of the creator of this program.")
		input ("Press enter to guess again.")
		guessname()
	elif name == "emma" or name == "Emma":
		print ("'Emma' is in the family of the creator of this program.")
		input ("Press enter to guess again.")
		guessname()
	else: 
		print ("The name you typed is not the creator of this program, and/or does not have any relationships with him/her.")
		input ("Press enter to guess again.")
		guessname()

	if correct == True:
			print ("Quit game? Type 'yes' to quit. Type 'no' to continue.")
			asktoquit = input ("")
			if asktoquit == "yes" or name == "Yes":
				print ("Bye-bye!")
			else:
				guessname()

guessname()