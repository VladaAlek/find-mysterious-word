import sys
""" 
import exit system func. to be used when 
the user chose to exit the game

"""


def display_welcome_messages():
    """
    Welcoming message function
    """
    print("\nWelcome to our guessing the mysterious word game! \U0001F60E")
    print("\nFollow 5 clues by filling up the input fields one after another")
    print("\nto find out the mysterious term.")
    print("\nDon't worry if you don't guess from the first attempt;")
    print("\nyou will get more signs to guide you to the victory.")

# User input


def users_input():
    """
    Function to allow the demo-game-exit navigation and to raise an exception if a typo occurs.
    """
    try:
        print("")
        choice = input("Type 'd' to see the demo, 'g' to play, or 'e' to exit!\n").lower()
        if choice not in ["g", "d", "e"]:
            raise ValueError("Invalid input. Please enter 'g', 'd', or 'e'.")
        return choice  # Return the choice if it's valid
    except ValueError as e:
        print(f"Error: {e}")
        return users_input()


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
    print("\nThank you for playing!\n")
    sys.exit("\nBye! 👋")


def choose_step(choice):
    """
    Function to choose between demo and play
    """
    if choice == 'd':
        display_intro()
    elif choice == "e":
        exit_game()
    else:
        print("Let's start the game!".upper())
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
    demo_text = "Game Demonstration"
    print(demo_text.upper())
    print("\nIt is a fruit!\n")
    print()
    print("Answer: mango\n")
    print("Sorry, mango is not the correct answer!🤨")
    print()
    
    print("\nIt is a very common fruit!")
    print()
    print("Answer: apple\n")
    print("Sorry, apple is not the correct answer!🤨")
    print()
    
    print("\nIt takes a lot of sun to raise this fruit.")
    print()
    print("\nAnswer: orange")
    print("\nSorry, orange is not the correct answer!🤨")
    print()
    
    print("\nThis fruit is slippery.")
    print()
    print("\nAnswer: kiwi")
    print("\nSorry, kiwi is not the correct answer!🤨")
    print()
    
    print("\nWhen ripe, it is yellow and curved.")
    print()
    print("\nAnswer: banana")
    print("")
    print("")
    banana_text = "🙌 Congratulations, banana is the correct answer!"
    print(banana_text.upper())
    print("")
    print("")

    start_game_choice = input("Type 'g' to play, or any button to exit!\n").lower()
    click_game(start_game_choice)
    
    print("")
    print("")


def click_g():
    """
    Function to print "Click g to start the game!" text if the user 
    does not choose "g"
    """
    #print("Click g to start the game!")


def users_input_start_game():
    """
    Store user's choice to start the game
    """
    try:
        start_game_choice = input("Click g to start the game!\n").lower()
        if start_game_choice == "g":
            return start_game_choice
        else:
            raise ValueError("Invalid input. Please enter 'g'.")
    except ValueError as e:
        print(f"Error: {e}")

# each list of strings contains the clues and answers for one game

clues_1 = ['It is a city.', 'It is a capital city!', 
'It is somewhere in Europe.', 'It has Spanish Steps.', 'Colosseum too.']

clues_2 = ['It is a tool.', 'It is a very common tool in many trades.',
           'Typically, it is made of wood and steel.', 
           'It is present in comic books too!', 'You have nailed it!']


# create the dictionary containing list of strings as a values for the clues 
# and correct answers values

clue_sets = [
    {'clues': clues_1,
    'correct_answer': 'rome',
    'explanation': 'Rome is the capital city of Italy (Europe), famous for its beautiful historical architecture (https://en.wikipedia.org/wiki/Spanish_Steps). Probably the most famous building is the Roman Colosseum.'},
    {'clues': clues_2,
    'correct_answer': 'hammer',
    'explanation': 'A hammer is a tool used for driving nails, breaking objects, or forging metal. It is a versatile tool with a wide range of applications.'}
]


def play_game():
    """Function to execute the game."""
    # For loop to iterate through the dictionary and return clues 
    # and correct answers
    game_count = 0  # Initialize the game count
    for game_data in clue_sets:
        # Variables to store the values for clues, correct answers, 
        # and explanation from the dictionary
        game_count += 1  # Increment the game count
        print(f"\n--- Game {game_count} ---")
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
                # Print "Congratulations" message and 
                # capitalize the first letter
                print(f"Congratulations, {clue_answer.capitalize()}")
                print(f" is the correct answer!")
                # Print the custom explanation for the correct answer
                print(explanation)

                # Stop further iteration as the correct answer 
                # has been provided
                break
            # Else statement for the if statement
            else:
                Print("Turn back the original message later") 
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

