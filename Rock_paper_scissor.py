#May the Force be with you!
"""This is a code to play the game rock paper scisor"""
import random  #import random for random number generation
def rock_paper_scisor():#the function beigins for the game
    while True:  #start an infinite loop
            

        #Block to determine user selection of rock, paper or scisor
        #We ask the user for an input either r, p or s
        user_inp = input("Select r for rock, p for paper, s for scissor: ")
        #if user selects anything other than r, p or s it is invalid response
        if user_inp != "r" and user_inp != "p" and user_inp != "s":
            print("invalid choice!, please select one of these: r,p,s")
            choice1=input("Do you want to continue? (y/n): ").lower()
            if choice1 == "y":
                continue
            elif choice1 == "n":
                return
            else: #anything other than y or n
                print("invalid response! exiting the game! See you next time")
                return
            

        #block to determine computer's response
        game_ran_num = random.randint(1, 3) #a number is selected randomly between 1 and 3
        if game_ran_num == 1:
            game_inp = "r"
        elif game_ran_num == 2:
            game_inp = "p"
        else: # game_ran_num == 3
            game_inp = "s"

        print(f"The computer selected {game_inp}")
         
        if user_inp == game_inp: #if user and computer selected the same thing
            choice2=input("we have reached an impass! do you want to go again? (y/n): ").lower()
            if choice2 == "y":
                continue
            elif choice2 == "n":
                print("Thanks for playing, see you next time")
                return
            else: #anything else
                print("invalid response! exiting the game! Thanks for playing, See you next time")
                return
        
        
        if user_inp == "p": #if user selects p
            if game_inp == "s": 
                print("Scisor cuts Paper! you lose!")
            else: # game_inp = r
                print("Paper covers rock! you win!")            
        
        elif user_inp == "r": #if user selects r
            if game_inp == "p":
                print("Paper covers rock! you lose!")
            else: # game_inp = s
                print("Rock beats scisor! you win!")
                                
        else:  # user_inp = s
            if game_inp == "r":
                print("Rock beats Scisor! you lose!")
            else: #game_inp = p
                print("Scisor cuts Paper! you win!")

        #play again option
        play_again=input("Do you want to play again? (y/n): ").lower()
        if play_again == "n":
            print("Thanks for playing! See you next time!")
            return
        elif play_again != "y":
            print("Invalid response! Exiting the game! See you next time!")
            return
            
            
                       
begin=input("start the play? (y/n): ")
if begin=="n":
    print("See you next time! have a good day!")
elif begin=="y":
   choice=rock_paper_scisor()
else:
    print("Invalid response!, please select either 'y' for yes or 'n' for no") 

        
    
