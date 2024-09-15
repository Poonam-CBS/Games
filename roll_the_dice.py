import random
def roll_the_dice():
    #Do the loop while it is true
    while True:
         dice_roll = random.randint(1,6) # chose a number between 1-6 randomly
         print(f"you got {dice_roll}")
         replay=input("Do you want to play again? (y/n): ") # Asking user if they want to play again
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
    roll_the_dice()
else: print("Invalid response!, please select either 'y' for yes or 'n' for no")
