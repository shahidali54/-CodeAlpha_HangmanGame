import random

def hangman():
    # Predefined list of 5 words
    words = ['python', 'codeAlpha', 'hangMan', 'java', 'typescript']
    word = random.choice(words)
    # Letters in the chosen word
    word_letters = set(word) 
    # Letters guessed by player 
    guessed_letters = set()   
    incorrect_guesses = 0
    max_incorrect = 5

    print("Welcome to Hangman!")
    print(f"You have {max_incorrect} Attempts Remaining.")

    # Game loop
    while incorrect_guesses < max_incorrect and word_letters:
        # Display current state
        print("\nWord: ", end="")
        for letter in word:
            if letter in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print(f"\nAttempts left: {max_incorrect - incorrect_guesses}")
        print("Guessed letters:", " ".join(sorted(guessed_letters)))

        # Get player input
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            word_letters.remove(guess)
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! '{guess}' is not in the word.")

    # Game over
    if not word_letters:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame Over! The word was:", word)

# Run the game
if __name__ == "__main__":
    hangman()