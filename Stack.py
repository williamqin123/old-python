mynumber = 1
print ("2013 Stack Engine 0.1.02")
print (">>>")

def stackit():
	file = open ("Data/stackdata.css", "r+")
	myint = int(file.readline())
	while myint > 0:
		print (myint)
		myint += 1
		file.seek(0)
		file.write(str(myint))

print ("Select your choice:")
print ("A)Start stacking from the beginning")
print ("B)Continue stacking from where you left off")
select_choice = input ("Choice: ")

if select_choice == "a" or select_choice == "A":
	while mynumber > 0:
		print (mynumber)
		mynumber += 1
elif select_choice == "b" or select_choice == "B":
	stackit()
else:
	input ("Sorry, that is not a choice. Press enter to quit.")