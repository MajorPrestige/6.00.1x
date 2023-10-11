# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words2.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    wordLettersList = list(secretWord)
    
    for wordLetter in wordLettersList:
        for letter in lettersGuessed:
            if wordLetter == letter:
                wordLettersList.remove(wordLetter)
                if len(wordLettersList) == 0:
                    return True
                return isWordGuessed(''.join(wordLettersList), lettersGuessed)  
            return False
    

def getGuessedWord(secretWord, lettersGuessed):
    ans = []
    specSymbol = '_'
    
    for wordLetter in secretWord:
        if wordLetter in lettersGuessed:
            ans.append(wordLetter)
        else:
            ans.append(specSymbol)
    
    return ' '.join(ans)

#'_ pp_ e'

def getAvailableLetters(lettersGuessed):
    alphabetList = list(string.ascii_lowercase)
    
    for letter in lettersGuessed:
        if letter in alphabetList:
            alphabetList.remove(letter)
        
    return "".join(alphabetList)
    

def hangman(secretWord):

    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')

    numberOfGueses = 8
    separator = "-" * 13
    proposal = 'Please guess a letter: '
    
    print(separator)
    
    userInputList = []
    guesedWord = "_" * len(secretWord)
    
    while numberOfGueses >= 0:
        
        if "_" not in guesedWord:
            print('Congratulations, you won!')
            break
        
        if numberOfGueses == 0:
            print('Sorry, you ran out of guesses. The word was a ' + secretWord + ".")
            break
        
        avalibleLetters = getAvailableLetters(userInputList)
        print('You have ' + str(numberOfGueses) + ' guesses left.')
        print('Available letters: ' + avalibleLetters)
        userInputLetter = input(proposal)
        inputLetterLowercase = userInputLetter.lower()
        userInputList.append(inputLetterLowercase)
        
        guesedWord = getGuessedWord(secretWord, userInputList)
        
        
        if inputLetterLowercase  not in avalibleLetters:
            print("Oops! You've already guessed that letter: " + guesedWord)
            print(separator)
        
        elif inputLetterLowercase in secretWord:
            print('Good guess: ' + guesedWord)
            print(separator)         
            
        else:
            numberOfGueses -= 1
            print("Oops! That letter is not in my word: " + guesedWord)
            print(separator)

        
        
    
    
    
    
    
    




hangman(chooseWord(wordlist))

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
