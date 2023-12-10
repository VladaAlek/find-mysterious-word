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
    print("Welcome to our guessing the mysterious word game! \U0001F60E")
    print("Follow 5 clues by filling up the input fields one after another")
    print("to find out the mysterious term.")
    print("Don't worry if you don't guess from the first attempt;")
    print("you will get more signs to guide you to the victory.")

# User input


def users_input():
    print("")
    choice = input("Type 'd' to see the demo, 'g' to play, or 'e' to exit!\n").lower()
    print("")
    return choice


# add option where the user get the notification that she/he used the wrong data type

# Start game function
#def game_start():
    # Call the function to start the game
    #play_game()

def exit_game():
    """
    function to exit the game while thanking the user
    code origin: 
    https://github.com/gitdagray/python-course/blob/main/lesson12/rps5.py
    lines 78-80
    """
    print("\n🎉🎉🎉🎉")
    print("Thank you for playing!\n")
    sys.exit("Bye! 👋")

def choose_step(choice):
    """
    Function to choose between demo and play
    """
    if choice == 'd':
        display_intro()
    elif choice == "e":
        exit_game()
    else:
        print("Let's start the game!".upper()) # check this code, use python tutor
        print("")
        play_game()


def click_game(start_game_choice):
        """
        Function to start the game from the demo field
        """
        print("Type 'g' to play, or any button to exit!\n")
        if start_game_choice == "g":
            play_game()
        elif start_game_choice != "g":
            exit_game()
    

def display_intro():
    """
    Intro display function
    """
    print("It is a fruit!")
    print()
    print("Answer: mango")
    print("Sorry, mango is not the correct answer!🤨")
    print()
    
    print("It is a very common fruit!")
    print()
    print("Answer: apple")
    print("Sorry, apple is not the correct answer!🤨")
    print()
    
    print("It takes a lot of sun to raise this fruit.")
    print()
    print("Answer: orange")
    print("Sorry, orange is not the correct answer!🤨")
    print()
    
    print("This fruit is slippery.")
    print()
    print("Answer: kiwi")
    print("Sorry, kiwi is not the correct answer!🤨")
    print()
    
    print("When ripe, it is yellow and curved.")
    print()
    print("Answer: banana")
    print("")
    print("")
    banana_text = " 🙌 Congratulations, banana is the correct answer!"
    print(banana_text.upper())
    print("")
    print("")

    start_game_choice = input("Type 'g' to play, or any button to exit!\n").lower()
    click_game(start_game_choice)
    
    print("")
    print("")


def click_g():
    """
    Function to print "Click g to start the game!" text if the user does not choose "g"
    """
    #print("Click g to start the game!")


def users_input_start_game():
    """
    Store user's choice to start the game
    """ 
    start_game_choice = input("Click g to start the game!\n").lower()
    return start_game_choice

clues_1 = ['It is a city.', 'It is a capital city!', '…somewhere in Europe.', 'It has Spanish Steps.', '...and Colosseum.', 'Rome']

def play_game():
    for clue in clues_1:
        print(clue)
        clue_answer = input("Please, type your answer here!\n").lower()
        
        if clue_answer == 'rome':
            print("Congratulations, " + clue_answer.capitalize() + " is the correct answer!")
            # Here you can call the function for the next game or perform any other action
            break
        else:
            print("Sorry, " + clue_answer.capitalize() + " is the wrong answer. Keep trying!")

    # If the loop completes without a correct answer, provide the correct answer
    else:
        print("Sorry, Rome was the correct answer.")


def main():
    """
    Run all program functions
    """
    display_welcome_messages()
    choice = users_input()
    choose_step(choice)
    start_game_choice = users_input_start_game()  # Get user input for starting the game
    

print("")
print("")
# print the title of the game in capital letters
text = "Find a mysterious word in five steps"
print(text.upper())
print("")
print("")


main()

