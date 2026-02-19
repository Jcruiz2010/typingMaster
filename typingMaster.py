import random
words = ["Accomplishments", "Benzodiazepines", "Cyclohexylamine", "Discombobulated", "Disenfranchised"]
random.shuffle(words)
try:
    numCorrect = 0
    numIncorrect = 0
    for word in words:
        print("Type each word correctly! (Case sensitive)")
        print(f"The word is {word}.")
        userInput = input("Type: ")
        # I don't do .lower() because you gotta write it perfectly
        if userInput == word:
            numCorrect += 1
            print("You typed it correctly!")
        else:
            numIncorrect += 1
            print("You typed it incorrectly...")
    print(f"\nTotal Correct: {numCorrect}")
    print(f"Total Incorrect: {numIncorrect}")
    print(f"Your correct percentage is {(numCorrect/5)*100}%.")
 
except Exception as e:
    print("An unexpected error occurred:", e)