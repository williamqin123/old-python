import os
print ("2013 Calculators 0.1.01")
print (">>>")

count = 1
while count > 0:
	d = input ("Operation: ")

	print ()
	a = int(input ("Enter first operand: "))
	print ("+ - # * % ^ > < /")
	b = int(input ("Enter second operand: "))

	c = a + b
	e = a - b
	f = a * b
	g = a / b

	if d == "+":
		print ("The answer is: " + str(c))
	elif d == "-":
		print ("The answer is: " + str(e))
	elif d == "x" or d == "*":
		print ("The answer is: " + str(f))
	elif d == "/" or d == "%":
		print ("The answer is: " + str(g))

	else:
		count = 1
		while count > 0:
			os.system("cls")
			print ("Note: application encountered an error.")
	input ("The command completed successfully.")
	os.system("cls")


