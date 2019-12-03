def rps():
    import random

    print('''   \t\n\tHi, you have chosen 'Rock, Paper, Scissor'.
    
        I, the computer, will be your opponent.
            
        Let's Begin!!!!\n''')
    
    computerPoints = 0
    playerPoints = 0
    
    while(True):
        choice = ["r", "p", "s"]
        computerChoice = random.choice(choice)
        
        playerInput = input("Choose 'r' for rock, 'p' for paper, and 's' for scissor\n")
        if ( computerPoints == 2 or playerPoints == 2):
            if (computerPoints > playerPoints):
                print("**** YOU LOST!! COMPUTER HAS WON!! ****\n")
                print("Game is over!\n")
                print(f"Computer Points: {computerPoints + 1}")
                print(f"Player Points: {playerPoints + 1}")
                break
            else:
                print("**** Congratulations **** YOU ARE THE WINNER ****!!!!\n")
                print(f"Computer Points: {computerPoints + 1}")
                print(f"Player Points: {playerPoints + 1}")
                break
        elif (playerInput == computerChoice):
            print("It is a draw/n please try again")
            print(f"Computer Points: {computerPoints}")
            print(f"Player Points: {playerPoints}")
            print(f"Computer has chosen {computerChoice}")
        elif (playerInput == 'r' and computerChoice == 's'):
            print("player won this round")
            playerPoints += 1
            print(f"Computer Points: {computerPoints}")
            print(f"Player Points: {playerPoints}")
            print(f"Computer has chosen {computerChoice}")
        elif (playerInput == 'r' and computerChoice == 'p'):
            print("computer won this round")
            computerPoints += 1
            print(f"Computer Points: {computerPoints}")
            print(f"Player Points: {playerPoints}")
            print(f"Computer has chosen {computerChoice}")
        elif (playerInput == 'p' and computerChoice == 'r'):
            print("player won this round")
            playerPoints += 1
            print(f"Computer Points: {computerPoints}")
            print(f"Player Points: {playerPoints}")
            print(f"Computer has chosen {computerChoice}")
        elif (playerInput == 'p' and computerChoice == 's'):
            print("computer won this round")
            computerPoints += 1
            print(f"Computer Points: {computerPoints}")
            print(f"Player Points: {playerPoints}")
            print(f"Computer has chosen {computerChoice}")
        elif (playerInput == 's' and computerChoice == 'r'):
            print("computer won this round")
            computerPoints += 1
            print(f"Computer Points: {computerPoints}")
            print(f"Player Points: {playerPoints}")
            print(f"Computer has chosen {computerChoice}")
        elif (playerInput == 's' and computerChoice == 'p'):
            print("player won this round")
            playerPoints += 1
            print(f"Computer Points: {computerPoints}")
            print(f"Player Points: {playerPoints}")
            print(f"Computer has chosen {computerChoice}")
        else: 
            print("You have entered an invadlid option. Try again")

# **** Work on this function *****
def dice_function():
    import random
    
    playing = True
    num = [1,2,3,4,5,6]
  
    
    
    while (playing):
        die1 = random.choice(num);
        die2 = random.choice(num);
        userInt = input("Press 'r' to roll the dices\nEnter 'e' to exit\n")
        if (userInt == 'r'):
            print(f"Die 1: {die1}")
            print(f"Die 2: {die2}")
            print(f"Total number: {die1 + die2}")
    
        elif (userInt == 'e'):
            break
        else:
            print("Invalid option. Try again.")

    
def guessing_game():
    import random
    choice = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    computerChoice = random.choice(choice)
    chances = 3

    print('''\nYou have chosen The Guessing Game. 
            \nYou have 3 chances to guess the letter \n''')

    while(True):
        playerInput = input("Enter a lowercase letter from a-z.\n")
        if (playerInput != computerChoice):
            print(''' You've guessed the wrong letter.
            Please try again ''')
            chances -= 1
            print(chances)
            print(f"Computer choice: {computerChoice}")
            if (chances == 0):
                print (''' \n\tOH NO!! 
                \n\tYou have ran out of chances!\n''')
                restart = input(''' Do you want to play again? 
                 Enter 'y' for yes or 'n' for no. ''')
                if (restart == "y"):
                    guessing_game()
                elif (restart == "n"):
                    break
                else:
                    print("You have entered an invalid option. Enter 'n' to exit.")
                break
                print(chances)
        else:
            print(''' CONGRATULATIONS!!! 
            
                    You've guessed the RIGHT letter!''')
            print(f"Computer choice: {computerChoice}")
            break


   




        

