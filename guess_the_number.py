import random
import re
def guess_the_number():
    selected_num = random.randint(1,100) 
    #return selected_num: This was a check in the beginning 
    while True:
        user_guess = input("Guess the number; it must be an integer: ")
        if '.' in user_guess or re.search("[a-z]",user_guess): #This is to avoid real number and alphabets
            print("Invalid guess, please guess an integer")
            continue
        if int(user_guess) > int(selected_num): #If the guessed number is higher than the selected number
            print("Too high")
        elif int(user_guess) < int(selected_num): #If the guesses number is lower than the selected number
            print("Too low!!") 
        else: #user_guess = selected_num #If the guessed number is equal to the seceted number
            print("Congratulations! you guessed it right!!")
            return
    return

begin=input("start the play? (y/n): ")
if begin=="n":
    print("See you next time!, have a good day!")
elif begin=="y":
    guess_the_number()
else: print("Invalid response!, please select either 'y' for yes or 'n' for no")
