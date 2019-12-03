import games

print(''' \nPlease enter 'a', 'b', or 'c'.
    \n a) Rock, Paper, Scissor Game
    \n b) Dice Function Game
    \n c) Guessing Game \n''')
userChoice = input("Enter you game letter:\n")

if (userChoice == "a"):
    games.rps()
elif (userChoice == "b"):
    # print("\n\nGame is not yet availible. Coming soon!\n\n")
    games.dice_function()
elif (userChoice == "c"):
    games.guessing_game()
else:
    print('''\n\tSorry, if you did not want to play any of our games
            \n\tPlease come back again!!!\n''')

