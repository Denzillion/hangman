import random

word_list = ['apple', 'banana', 'orange', 'strawberry', 'mango']

word = random.choice(word_list)

print("Randomly chosen word:", word)

user_input = input("Enter a single alphabetical character: ")

if len(user_input) == 1 and user_input.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

