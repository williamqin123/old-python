import random, os
print("[-Sith name generator-]")
first = input("What are the first letter(s) of your real first name? [-")
second = input("What letter(s) do you want your sith name to end with? [-")
print("Your new sith name:")
print(str("Darth " + first + random.choice("aeiou") + second))
os.system("color 0f")
input("Exit ->")