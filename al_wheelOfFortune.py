#Anna Lieb
#6/14/18
#CSP 2018
#al_wheelOfFortune.py

import random
def getRandomPhrase(phraseList):
    # This function returns a random string from the passed list of strings.
    phraseIndex = random.randint(0, len(phraseList) - 1)
    return phraseList[phraseIndex]

def displayBoard(missedLetters, correctLetters, secretPhrase):
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretPhrase)

    for i in range(len(secretPhrase)): # replace blanks with correctly guessed letters
        if secretPhrase[i] in correctLetters:
            blanks = blanks[:i] + secretPhrase[i] + blanks[i+1:]
        if secretPhrase [i] == " ":
            blanks = blanks[:i] + " " + blanks[i+1:]

    for letter in blanks: # show the secret phrase with spaces in between each letter
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def main():
    print('''Welcome to Wheel of Fortune!
A secret French phrase has been chosen. 
Please enter a letter. If the letter is in the secret phrase, it will appear in the secret phrase.
You can make 5 incorrect guesses before losing the game.''')
    phrases = ["cest la vie", "deja vu", "je ne sais quoi", "excusez moi", "bon appetit", "joie de vivre", "faux pas",]
    missedLetters = ''
    correctLetters = ''
    secretPhrase = getRandomPhrase(phrases)
    gameIsDone = False

    while True:
        displayBoard(missedLetters, correctLetters, secretPhrase)
        # Let the player type in a letter.
        guess = getGuess(missedLetters + correctLetters)

        if guess in secretPhrase:
            correctLetters = correctLetters + guess

            # Check if the player has won
            foundAllLetters = True
            for i in range(len(secretPhrase)):
                if secretPhrase[i] not in correctLetters and secretPhrase[i] != " ":
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('You win! The secret French phrase is "' + secretPhrase + '"! You won an all-inclusive getaway to the Bahamas!')
                gameIsDone = True
        else:
            missedLetters = missedLetters + guess

            # Check if player has guessed too many times and lost
            if len(missedLetters) == 5:
                displayBoard(missedLetters, correctLetters, secretPhrase)
                print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the phrase was "' + secretPhrase + '"')
                gameIsDone = True

        # Ask the player if they want to play again (but only if the game is done).
        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretPhrase = getRandomPhrase(phrases)
            else:
                break
main()
