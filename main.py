import nltk 
import random 


nltk.download('words')
from nltk.corpus import words


validList = [word.lower() for word in words.words() if word.isalpha() and len(word) == 5]



def guess_word():
    wordToGuess = random.choice(validList)
    attempts = 6

    for i in range(attempts):
        inputWord = input(f"Attempt {i + 1}/{attempts}: Guess the 5-letter word: ").lower()
        result = ["_"] * 5

        if len(inputWord) != 5 or not inputWord.isalpha():
            print("Invalid input. Please enter a 5-letter word.")
            if i == attempts - 1:
                print(f"Sorry, you've used all attempts. The word was: {wordToGuess}")
                return
            continue
        elif inputWord not in words.words():
            print("Word not in the valid list. Please try again.")
            if i == attempts - 1:
                print(f"Sorry, you've used all attempts. The word was: {wordToGuess}")
                return
            continue
        for j in range(5):
            if inputWord[j] == wordToGuess[j]:
                result[j] = inputWord[j].upper()
            elif inputWord[j] in wordToGuess:
                result[j] = inputWord[j].lower()

        print("Result:", " ".join(result), "\n")
        if inputWord == wordToGuess:
            print("Congratulations! You've guessed the word!")
            return
        
        elif i == attempts - 1:
            print(f"Sorry, you've used all attempts. The word was: {wordToGuess}")