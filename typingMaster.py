words = ["Accomplishments", "Benzodiazepines", "Cyclohexylamine", "Discombobulated", "Disenfranchised"]
try:
    numCorrect = 0
    numIncorrect = 0
    for word in words:
        print("Type each word correctly! (Case sensitive)")
        print(f"The word is {word}.")
        userInput = input("Type: ")
        # I don't do .lower() because you gotta write it perfectly
except Exception as e:
    print("An unexpected error occurred:", e)