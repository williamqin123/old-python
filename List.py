list_of_games = ["Animal Jam", "Gamestar Mechanic", "Cool Math Games", "PBS Kids Go"]

dictionary_of_games = {"Animal Jam" : "No", "Gamestar Mechanic" : "Yes", "Cool Math Games" : "No", "PBS Kids Go" : "No"}

space = " "

no = "no"

yes = "yes"

error = '''I didn't understand what you said.
The only acceptable answers are yes and no.
Yes or no answers have to be typed in lowercase.'''

print "Play %s not %s" % (list_of_games[1], list_of_games[0])

loop = True

while loop == True:
    
    GSM_or_AJ = input("Do you play Gamestar Mechanic? %s" % space)
    
    GSM_or_AJ_string = str(GSM_or_AJ)
    
    if GSM_or_AJ_string == no:
        
        print "Gamestar Mechanic is way better than Animal Jam so play it!"
        
    elif GSM_or_AJ_string == yes:
        
        print "Great! But if you ever hear about Animal Jam don't play it."
        
        GSM_or_AJ = input("Do you play Animal Jam too? %s" % space)
        
        if GSM_or_AJ_string == yes:
            
            print "DELETE YOUR ACCOUNT NOW!"
            
        elif GSM_or_AJ_string == no:
            
            print "Great! But if you ever think Gamestar Mechanic is bad and decide to play Animal Jam instead, DON'T DO IT!"
            
        else:
            
            print error
    else:
        
        print error
