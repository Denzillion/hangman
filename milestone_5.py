import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess.isalpha() and len(guess) == 1:
            if guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                if guess in self.word:
                    print(f"Good guess! {guess} is in the word.")
                    for i, letter in enumerate(self.word):
                        if letter == guess:
                            self.word_guessed[i] = guess
                    self.num_letters -= 1
                else:
                    self.num_lives -= 1
                    print(f"Sorry, {guess} is not in the word.")
                    print(f"You have {self.num_lives} lives left.")
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

    def ask_for_input(self):
        while self.num_lives > 0 and self.num_letters > 0:
            guess = input("Guess a letter: ")
            self.check_guess(guess)
            if self.num_letters == 0:
                print("Congratulations! You guessed the word.")
            elif self.num_lives == 0:
                print(f"Sorry, you ran out of lives. The word was '{self.word}'.")

# Testing the Hangman class
hangman = Hangman(["apple", "orange", "banana"])  # Pass the word list to the class
hangman.ask_for_input()  # Start the game

