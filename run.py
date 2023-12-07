# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide
# and 24 rows high

import sys
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


def main():
    """
    Run all program functions
    """
    display_welcome_messages()
    
    

# print the title of the game in capital letters
text = "Find a mysterious word in five steps"
print(text.upper())
print("")
print("")
print("")

main()

# sys.exit()