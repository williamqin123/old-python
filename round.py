digit_ones = input("Digit in the ones place: ")
digit_tens = input("Digit in the tens place: ")
digits = input ("Digits in the rest of the places: ")
if digit_ones >= 5:
	digit_tens = digit_tens + 1
digit_ones = 0
print "Rounded number is %s%s%s" % (digits, digit_tens, digit_ones)
raw_input()