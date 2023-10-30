while True:
    guess = input("Guess a letter: ")

    if guess.isalpha() and len(guess) == 1:
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")


secret_word = "apple"  # Assign the secret word here or generate it using your existing logic

while True:
    guess = input("Guess a letter: ")

    if guess.isalpha() and len(guess) == 1:
        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word. Try again.")
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

def check_guess(guess, secret_word):
    guess = guess.lower()
    if guess.isalpha() and len(guess) == 1:
        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word. Try again.")
        return True
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
        return False

def ask_for_input(secret_word):
    while True:
        guess = input("Guess a letter: ")
        if check_guess(guess, secret_word):
            break

ask_for_input("apple")  # Change the secret word accordingly
