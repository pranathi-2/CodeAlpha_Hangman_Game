import random
def hangman():
    #list of the words
    words_in_list = ["python", "hangman", "programming", "developer", "challenge", "enjoyment", "fun", "game",
                     "levelup", "winner", "coding", "team", "leader", "community", "crazymove", "interesting",
                     "amazing"]
    # to select a random word
    word_choice = random.choice(words_in_list)
    guessed_word = ["_"] * len(word_choice)
    attempts = 6 #attempts for word guess
    guessed_letters = set()
    #displaying the stages of stickman
    stickman = [
        """
           ------
           | |
                |
                |
                |
                |
        =========
        """,
        """
           ------
           | |
           O |
                |
                |
                |
        =========
        """,
        """
           ------
           | |
           O |
           | |
                |
                |
        =========
        """,
        """
           ------
           | |
           O |
          /| |
                |
                |
        =========
        """,
        """
           ------
           | |
           O |
          /|\\ |
                |
                |
        =========
        """,
        """
           ------
           | |
           O |
          /|\\ |
          / |
                |
        =========
        """,
        """
           ------
           | |
           O |
          /|\\ |
          / \\ |
                |
        =========
        """
    ]
    #statements to start the game
    print("Welcome to Hangman Game!")
    print("Try to guess the word")
    print("You need to guess one letter at a time")
    print("You have", attempts, "attempts remaining!")
    while attempts > 0:
        print(stickman[6 - attempts])  # it displays the current stickman based on remaining attempts left
        print("\nCurrent word:", " ".join(guessed_word))
        print("Guessed letters:", ", ".join(sorted(guessed_letters)))
        guess = input("Guess a letter: ").lower()
        #input validaation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        guessed_letters.add(guess)
        #checking for the correct guess
        if guess in word_choice:
            print(f"Good job! The letter '{guess}' is in the word.")
            for i, letter in enumerate(word_choice):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"Wrong guess! The letter '{guess}' is not in the word.")
            print(f"You have {attempts} attempts remaining.")
        # Check for the word is fully guessed or not
        if "_" not in guessed_word:
            print("\nCongratulations! You've guessed the word:", word_choice)
            break
    else:
        print(stickman[-1])  # Display final stickman
        print("\nGame over! You lost! The word was:", word_choice)
hangman()
