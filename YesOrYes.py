import random
import sys


# AUTHOR: Michelle Moise
# DATE CREATED: April 28th 2026 to keep my brain sane and running during finals. ha

# --------------------CODE DOCUMENTATION-------------------------
# yes or no determinator, can be used for choosing things when youre in a pickle or making decisions.
# random choice allows the user to let the program pick between some defined word choices
# (whether it be a yes or no answer or changing the yes' and nos to some item you want to buy impulsively!

# ================================================================

# Do I go to the beach today?
# Should I have ice cream for dessert?
# Wash my hair today?
# Go to the park immediately after school/work?
#
#
# Any of the above questions work for this wheel of decisions!

# =================== code starts here ! ==========================

# list of yes' and no string values
x = ['yes', 'no', 'yes', 'no', 'yes', 'no']

# value to determine whether we exit the program
more = 'yup'

# keeping track of how many yes' and nos we have
i = 0
j = 0

#forever loop without the more value. do not delete
#keeps the program running and choosing y or n (yes or no!)
#      for fun a user could change the x values to just yes. yes or yes!
#      cause why not haha
turns = 0

randomq = ['chiikawa has blessed you!', 'megan thee stallion just followed you! YAAAY!', 'you will be blessed!', 'you will pass this finals season #trust',
           'today is just a filler episode dont even worry', 'rock, paper... scissors....... . what comes next again?']

print("Welcome to your own personified spinning wheel------")
print("\n\nLICENSE AGREEMENT DISCLOSURE: This company is not accredited enough to provide...")
print("...users with a visual wheel.")
print("Please donate to the following link if you want to see a wheel.\n")
print("---------------------------link unavailable. LOL.----------------")

print("ANYYYWAYS. This is a program that just chooses yes or no for you.")
print("To quit, just simply type 'no' without the quotations in ALL LOWERCASE LETTERS upon this program's inquiry to 'go again'.")
print("Otherwise the game'll just keep on making choices for you! You have been warned. (OOOOOooooo ooooo im a ghost)\n")

print("Have Fun! \n\n")
print("Okay honestly I'm a Genie. Ask away.... I only answe yes or no.")

while turns >= 0:
    
    y = random.choice(x) # picks randomly
    choice = random.choice(randomq)
    if y == 'yes': # if yes you'll tell the user they rolled a yes
        i+=1
        turns += 1
        print("you rolled a " + y, '!')
        print("")
        print(choice)
        print("")
        # tbh these two following lines could be after the if else statement but oh well
        print("current status: ", + i, 'for yes, and', + j, 'for no.')
        
        more = input("\ngo again?")

    else : # otherwise tell the user they rolled a no
        j+=1
        turns += 1
        print("you rolled a " + y, '.')
        print("current status: ", + i, 'for yes, and', + j, 'for no.')
        more = input("go again?")
        
    if(more == 'no'):
        print("Bye for now!\n")
        sys.exit()

