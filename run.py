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

# each list of strings contains the clues and answers for one game
clues_1 = ['It is a city.', 'It is a capital city!', '…somewhere in Europe.', 
'It has Spanish Steps.', '...and Colosseum.']

clues_2=[ 'It is a tool.', 'It is a very common tool in many trades.',
'Typically, it is made of wood and steel.', 'It is present in comic books too!',
'You have nailed it!']

# create the dictionary containing list of strings as a values for the clues and 
# correct answers values

clue_sets = [
    {'clues': clues_1, 'correct_answer': 'rome', 'explanation': 'Rome is the capital city of Italy (Europe), famous for its beautiful historical architecture (https://en.wikipedia.org/wiki/Spanish_Steps). Probably the most famous building is the Roman Colosseum.'},
    {'clues': clues_2, 'correct_answer': 'hammer', 'explanation': 'A hammer is a tool used for driving nails, breaking objects, or forging metal. It is a versatile tool with a wide range of applications.'}
]

def play_game():
    """Function to execute the game."""
    # For loop to iterate through the dictionary and return clues 
    # and correct answers
    for game_data in clue_sets:
        # Variables to store the values for clues, correct answers, 
        # and explanation from the dictionary
        clues = game_data['clues']
        correct_answer = game_data['correct_answer']
        explanation = game_data.get('explanation', 'No explanation available.')

        # Nested loop to iterate and print the clues
        for clue in clues:
            print(clue)
            # Creates a variable to store the input values and transform them
            # into lowercase letters
            clue_answer = input("Please, type your answer here!\n").lower()

            # If statement to compare the user's input with the correct answer
            if clue_answer == correct_answer:
                # Print "Congratulations" message and capitalize the first letter
                print(f"Congratulations, {clue_answer.capitalize()} is the correct answer!")
                # Print the custom explanation for the correct answer
                print(explanation)

                # Stop further iteration as the correct answer 
                # has been provided
                break
            # Else statement for the if statement
            else:
                print(f"Sorry, {clue_answer.capitalize()} is the wrong answer. Keep trying!")

        # Else statement for the for loop activated when the correct answer has not been provided
        else:
            print(f"Sorry, {correct_answer.capitalize()} was the correct answer.")
            # Print the default explanation for the correct answer
            print(explanation)


def main():
    """
    Run all program functions
    """
    display_welcome_messages()
    choice = users_input()
    choose_step(choice)
    # Get user input for starting the game
    start_game_choice = users_input_start_game()  
    play_game()
    

print("")
print("")
# print the title of the game in capital letters
text = "Find a mysterious word in five steps"
print(text.upper())
print("")
print("")


main()

