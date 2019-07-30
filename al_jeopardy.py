#Anna Lieb
#CSP 2018
#6/27/18
#al_jeopardy.py

PROMPTS = [["This common pet's sense of smell is 40x better than a human's",
            "This pet is famous for always landing on its feet",
            "This pet's shell grows with it as it ages",
            "Although this animal is a pet to some, others in South America consider it a delicacy"],
           ["Queen Elizabeth II represents this country's royal family",
            "This Pixar animated film follows the life of a superhero family",
            "This TV show first became popular in 1964, and depicted a famously spooky family",
            "When this arctic bird has chicks, both parents share responsibility for raising the young"],
           ["This yellow vehicle transports children to and from school",
            "This meal is thought to be most important in starting a school day off right",
            "School teachers are often associated with this red fruit",
            "This holiday typically marks the start of the school year"],
           ["This summer holiday celebrates the anniversary of the Declaration of Independence",
            "This TV and movie streaming service is a popular summer pick for bored kids",
            "Hot dogs and hamburgers are common at this summer get-together",
            "This celestial event occurs each year around June 21st in the northern hemisphere"]]

RESPONSES = [["what is a dog?", "what is a cat?", "what is a turtle?", "what is a guinea pig?"],
             ["what is the united kingdom?", "what is incredibles?", "what is the addams family?", "what is a penguin?"],
             ["what is a school bus?", "what is breakfast?", "what is an apple?", "what is labor day?"],
             ["what is july 4th?", "what is netflix?", "what is a barbecue?", "what is the summer solstice?"]]


def drawBoard(board):
    # This function prints out the updated board.
    # "board" is a list of 16 strings representing the board.
    print('-'*28)
    print("  1   |  2   |  3   |  4   |")
    print(" Pets |Family|School|Summer|")
    print("      |      |      | Fun  |")
    print('-'*28)
    print('      |      |      |      |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' | ')
    print('      |      |      |      |')
    print('-'*28)
    print('      |      |      |      |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' | ' + board[7] + ' | ')
    print('      |      |      |      |')
    print('-'*28)
    print('      |      |      |      |')
    print(' ' + board[8] + ' | ' + board[9] + ' | ' + board[10] + ' | ' + board[11] + ' | ')
    print('      |      |      |      |')
    print('-'*28)
    print('      |      |      |      |')
    print(' ' + board[12] + ' | ' + board[13] + ' | ' + board[14] + ' | ' + board[15] + ' | ')
    print('      |      |      |      |')
    print('-'*28)

def chooseQuestion():
    #The user chooses which question to play
    #This function returns a list that contains the chosen board position and the correct answer to that board position. 
    category = int(input("Which category do you want to play? (1-4) "))
    amount = int(input("Which dollar amount do you want to play? (1-4) "))
    boardPosition = PROMPTS[category - 1][amount - 1]
    correctAnswer = RESPONSES[category - 1][amount - 1]
    amtWon = amount*100
    return [boardPosition, correctAnswer, category, amount, amtWon]

def getUserResponse():
    #The user enters their response and checks that syntax is valid
    question = True
    while question == True: 
        response = input("What is your guess? ").lower()
        respList = response.split()
        lastWord = respList[len(respList)-1]
        lastCharacter = lastWord[len(lastWord)-1]
        if respList[0] != "what" or respList[1] != "is" or lastCharacter != "?":
            print('Error: please enter your response in the form, "What is..." and ending with a "?"')
        else:
            question = False 
    return response

def checkUserResponse(userResponse, correctAnswer):
    #Checks if the user response is correct
    if userResponse == correctAnswer:
        return True
    else:
        return False

def assignBoardPosition(chosenPrompt):
    #This function takes the user input category and dollar amount and converts it to a board position
    category = chosenPrompt[2]
    amount = chosenPrompt[3]
    if category == 1 and amount == 1:
        box = 0
    elif category == 2 and amount == 1:
        box = 1
    elif category == 3 and amount == 1:
        box = 2
    elif category == 4 and amount == 1:
        box = 3
    elif category == 1 and amount == 2:
        box = 4
    elif category == 2 and amount == 2:
        box = 5
    elif category == 3 and amount == 2:
        box = 6
    elif category == 4 and amount == 2:
        box = 7
    elif category == 1 and amount == 3:
        box = 8
    elif category == 2 and amount == 3:
        box = 9
    elif category == 3 and amount == 3:
        box = 10
    elif category == 4 and amount == 3:
        box = 11
    elif category == 1 and amount == 4:
        box = 12
    elif category == 2 and amount == 4:
        box = 13
    elif category == 3 and amount == 4:
        box = 14
    elif category == 4 and amount == 4:
        box = 15
    return box

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def main():
    print('Welcome to Jeopardy!')
    print('You will be given a prompt, and you must provide an answer to the prompt in the form of a question.')
    print('A response will only be accepted in the form, "What is..." and ending with a "?"')
    print()

    while True:
        # Reset the game
        theBoard = (('$100 ')*4 + ('$200 ')*4 + ('$300 ')*4 + ('$400 ')*4).split()
        usedBoxes = []
        gameIsPlaying = True
        winnings = 0

        while gameIsPlaying:
            drawBoard(theBoard)
            print("Your total winnings: $" + str(winnings))
            print()
            chosenPrompt = chooseQuestion()
            box = assignBoardPosition(chosenPrompt)
            while box in usedBoxes:
                #Makes sure that the user doesn't enter a box that is already answered. 
                print("That box is already used. Please choose another box. ")
                chosenPrompt = chooseQuestion()
                box = assignBoardPosition(chosenPrompt)
            print("Here is the prompt: ", chosenPrompt[0])
            userResponse = getUserResponse()
            check = checkUserResponse(userResponse, chosenPrompt[1])
            theBoard[box] = '    ' #When a box is blank, that indicates that the box has been used. 
            usedBoxes.append(box)
            if check == True:
                print("That is the correct response!")
                winnings += chosenPrompt[4]
            else:
                print("Sorry, that is incorrect.")
                print("You have won $" + str(winnings))
                gameIsPlaying = False
            print()

            #Ends game if all prompts have been answered
            if len(usedBoxes) == 16:
                print("Congratulations! You have correctly answered all of the prompts!")
                print("You have won $" + str(winnings))
                gameIsPlaying = False

        if not playAgain():
            print("Game over. ")
            break

main()


