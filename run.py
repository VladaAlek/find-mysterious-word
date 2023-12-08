# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide
# and 24 rows high

#import sys
""" 
import exit system function to be used the user chose to exit the game

"""


def display_welcome_messages():
    """
    Welcoming message function
    """
    print("Welcome to our guessing the mysterious word game!")
    print("Follow 5 clues by filling up the input fields one after another")
    print("to find out the mysterious term.")
    print("Don't worry if you don't guess from the first attempt;")
    print("you will get more signs to guide you to the victory.")

# User input


def users_input():
    print("")
    choice = input("Type 'd' to see the demo or type 'p' to play the game!\n").lower()
    print("")
    return choice


# add option where the user get the notification that she/he used the wrong data type

# Start game function
def game_start():
    print("Usually, it is all around us!")

def choose_step(choice):
    """
    Function to choose between demo and play
    """
    if choice == 'd':
        display_intro()
    else:
        print("Let's start the game!")
        game_start()


# Intro display function


def display_intro():
    print("It is a fruit!")
    print()
    print("Answer: mango")
    print("Sorry, mango is not the correct answer!")
    print()
    
    print("It is a very common fruit!")
    print()
    print("Answer: apple")
    print("Sorry, apple is not the correct answer!")
    print()
    
    print("It takes a lot of sun to raise this fruit.")
    print()
    print("Answer: orange")
    print("Sorry, orange is not the correct answer!")
    print()
    
    print("This fruit is slippery.")
    print()
    print("Answer: kiwi")
    print("Sorry, kiwi is not the correct answer!")
    print()
    
    print("When ripe, it is yellow and curved.")
    print()
    print("Answer: banana")
    print("")
    print("")
    banana_text = "Congratulations, banana is the correct answer!"
    print(banana_text.upper())
    print("")
    print("")


# Function to print "Click g to start the game!" text if the user does not choose "g"
def click_g():
    print("Click g to start the game!")

# Store user's choice to start the game

def users_input_start_game(): 
    start_game_choice = input("Click g to start the game!\n").lower()
    return start_game_choice


# Function to start the game from the demo field
def click_game(start_game_choice):
    if start_game_choice == "g":
        game_start()
    else:
        click_g()


def main():
    """
    Run all program functions
    """
    display_welcome_messages()
    choice = users_input()
    choose_step(choice)
    start_game_choice = users_input_start_game()  # Get user input for starting the game
    click_game(start_game_choice)    
    

print("")
print("")
# print the title of the game in capital letters
text = "Find a mysterious word in five steps"
print(text.upper())
print("")
print("")


main()

# sys.exit()