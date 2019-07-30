#Anna Lieb
#Python Summer Work
#7/27/18
#al_priceIsRightFinalProject.py

ITEMS = ["vintage electric bass guitar", "diamond ring", "deluxe lawn tractor", "smart home device", "baseball signed by Babe Ruth", "first edition copy of Harry Potter and the Philosopher's Stone"]
PRICES = [999, 220000, 1999, 150, 124720, 80]

def playerInfo():
    #retrieves the number of players and the player names.
    #uses a dictionary to store player names.
    valid = False
    while valid == False: 
        numPlayers = int(input("How many players? "))
        if numPlayers <= 1:
            print("Sorry, there must be at least two players. Please try again. ")
        else:
            valid = True
    playerNames = {}
    for x in range(numPlayers):
        name = input("Enter the name of player " + str(x+1) + ": ")
        playerNames["player" + str(x+1)] = name
    return [numPlayers, playerNames]


def itemGuess(playerNames, numPlayers, itemNum):
    #asks the user to enter their price guess for a given item
    #stores the guesses in a list
    guesses = []
    for x in range(numPlayers):
        valid = False
        while valid == False:
            userGuess = int(input(playerNames["player" + str(x+1)] + ", please guess the price of a " + ITEMS[itemNum] + ": "))
            if userGuess in guesses:
                print("Sorry, that price has already been guessed. Please guess again." )
            elif userGuess < 0:
                print("Invalid syntax. Please guess again. ")
            else:
                valid = True
        guesses.append(userGuess)
    return guesses


def findWin(item, price, guesses, playerNames):
    #finds the winning player and returns the string of the winning player's name
    totalOverGuesses = 0
    for x in guesses:
        if x > price:
            guesses[guesses.index(x)] = 0
            totalOverGuesses += 1
            if totalOverGuesses == len(guesses):
                print("All of the guesses were too high! Please enter new guesses. ")
                return False
    winnerIndex = guesses.index(max(guesses))
    winnerName = playerNames["player" + str(winnerIndex + 1)]
    return winnerName


def playAgain():
    #asks if the user would like to play again 
    userInput = False
    while userInput == False: 
        repeat = input("Would you like to play again? y/n ")
        if repeat == "y":
            userInput = True
            return True
        elif repeat == "n":
            userInput = True
            return False
        else:
            print("Invalid input. Please try again. ")


def main():
    print('''Welcome to Price is Right!
In this game, you will be asked to guess the price of a given item.
The player that guesses the closest to the actual price without
going over the cost will win money. The player that has the most money
at the end of the game wins!
''')
    info = playerInfo()
    numPlayers = info[0]
    playerNames = info[1]
    print("OK! Let's start the game! \n")
    for x in range (len(ITEMS)):
        guesses = itemGuess(playerNames, numPlayers, x)
        item = ITEMS[x]
        price = PRICES[x]
        winner = findWin(item, price, guesses, playerNames)
        while winner == False:
            guesses = itemGuess(playerNames, numPlayers, x)
            winner = findWin(item, price, guesses, playerNames)
        print(winner, "is the winner! The actual value of the", item, "was $" + str(price) + ". \n")
        if playAgain() == False:
            break
        if x == len(ITEMS)-1:
            print("\nCongratulations! You have reached the end of the game. \nUnfortunately, there are no more items to guess. ")
    print("Game over. Goodbye!" )
    
    
main()
