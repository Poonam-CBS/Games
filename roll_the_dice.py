import random
def rolling_a_dice():
    #Do the loop while it is true
    while True:
         dice_roll = random.randint(1,6) # the computer will chose a number between 1-6 randomly
         print(f"you rolled {dice_roll}")
         replay=input("do you want to play again? (y/n): ") 
         if replay == "y":
            continue
         elif replay == "n":
            print("Thanks for playing! See you next time!")
            return
         else:
            print("Invalid response!, please select either 'y' for yes or 'n' for no")
    return
    


begin=input("start the play? (y/n): ")
if begin=="n":
    print("See you next time!, have a good day!")
elif begin=="y":
    rolling_a_dice()
else: print("Invalid response!, please select either 'y' for yes or 'n' for no")
