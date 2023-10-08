# Python Function Puzzle Game

# Import the random library
import random

# Define a list of functions
functions = ["print", "len", "max", "min", "sum", "abs", "round", "type"]

# Start the game
while True:
    # Generate a random function
    function = random.choice(functions)

    # Generate a random input
    input_data = random.randint(1, 100)

    # Create a function call
    function_call = f"{function}({input_data})"

    # Ask the player to guess the output of the function call
    guess = input("What is the output of the function call? ")

    # Check if the player guessed correctly
    if guess == str(eval(function_call)):
        print("Correct!")
    else:
        print("Incorrect. The correct answer is", str(eval(function_call)))

    # Ask the player if they want to play again
    play_again = input("Do you want to play again? (y/n) ")

    if play_again != "y":
        break
