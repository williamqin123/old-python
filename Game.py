import random
import os
def game():
    count = 1
    you_points = 0
    cpu_points = 0
    you = False
    cpu = False
    while True:
        if count == 1:
            you_num = random.randint(1, 26)
            print "You got %s" % you_num
            count = 2
            you = True
        elif count == 2:
            cpu_num = random.randint(1, 26)
            print "Computer got %s" % cpu_num
            count = 1
            cpu = True
        if you == True and cpu == True:
            raw_input("Press enter to see the current point scores.")
            if cpu_num > you_num:
                cpu_points = cpu_points + 1
            elif cpu_num < you_num:
                you_points = you_points + 1
            print "Computer: %s %s" % (cpu_points, "points")
            print "You: %s %s" % (you_points, "points")
            you = False
            cpu = False
        if you_points == 5 or cpu_points == 5:
            if you_points == 5:
                print "You win!"
            elif cpu_points == 5:
                print "Computer wins!"
            elif cpu_points == 5 and you_points == 5:
                print "Tie!"
            you_points = 0
            cpu_points = 0
            raw_input("Press enter to play this game again.")
            os.system("cls")
        raw_input()
game()
