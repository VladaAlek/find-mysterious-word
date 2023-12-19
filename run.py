import sys
import time

""" 
import exit system func. to be used when 
the user chose to exit the game

"""

def print_title():
    """
    # print the title of the game in capital letters
    """
    print("")
    print("")
    text = "Find a mysterious word in five steps"
    print(text.upper())
    print("")
    print("")
    
def typing_greeting_message(text):
    """ causes the letters to be presented one by one
    """
    for char in text:
        #time.sleep(0.1)
        print(char, end='', flush=True)
        

def display_welcome_messages():
    """
    Welcoming message function
    """
    greeting_message = "\nWelcome to our guessing the mysterious word game! \U0001F60E\n"
    typing_greeting_message(greeting_message)
    greeting_message = "\nFollow 5 clues by filling up the input fields one after another\n"
    typing_greeting_message(greeting_message)
    greeting_message = "\nto find out the mysterious term.\n"
    typing_greeting_message(greeting_message)
    greeting_message = "\nDon't worry if you don't guess from the first attempt.\n"
    typing_greeting_message(greeting_message)
    greeting_message = "\nyou will get more signs to guide you to the victory.\n"
    typing_greeting_message(greeting_message)
    

# User input


def users_input():
    """
    Function to allow the demo-game-exit navigation and to raise an exception if a typo occurs.
    """
    try:
        print("")
        choice = input("Type 🇩 to see the demo,\n🇬 to play,\nor 🇪 to exit!\n").lower()
        if choice not in ["g", "d", "e"]:
            raise ValueError("Invalid input. Please enter 🇬, 🇩, or 🇪.")
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
    else:play_game()


def click_game(start_game_choice):
        """
        Function to start the game from the demo field
        """
        print("Type 🇬 to play, or any button to exit!\n")
        if start_game_choice == "g":
            play_game()
        elif start_game_choice != "g":
            exit_game()
    

def display_intro():
    """
    Intro display function
    """
    demo_text = "\nGame Demonstration"
    print(demo_text.upper())
    print("\nIt is a fruit!\n")
    time.sleep(2)
    print()
    print("Answer: mango\n")
    time.sleep(2)
    print("Sorry, mango is not the correct answer!🤨")
    print()
    
    print("\nIt is a very common fruit!")
    time.sleep(2)
    print()
    print("Answer: apple\n")
    time.sleep(2)
    print("Sorry, apple is not the correct answer!🤨")
    print()
    
    print("\nIt takes a lot of sun to raise this fruit.")
    time.sleep(2)
    print()
    print("\nAnswer: orange")
    time.sleep(2)
    print("\nSorry, orange is not the correct answer!🤨")
    print()
    
    print("\nThis fruit is slippery.")
    time.sleep(2)
    print()
    print("\nAnswer: kiwi")
    time.sleep(2)
    print("\nSorry, kiwi is not the correct answer!🤨")
    print()
    
    print("\nWhen ripe, it is yellow and curved.")
    time.sleep(2)
    print()
    print("\nAnswer: banana")
    print("")
    print("")
    time.sleep(2)
    banana_text = "🙌 Congratulations, banana is the correct answer!"
    print(banana_text.upper())
    print("")
    print("")

    start_game_choice = input("Type 🇬 to play, or any button to exit!\n\n").lower()
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
        start_game_choice = input("Click 🇬 to start the game, or any other key to exit!\n").lower()
        if start_game_choice == "g":
            return start_game_choice
        else:
            exit_game()          
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
    correct_count = 0  # Initialize the correct answer count
    fail_count = 0  # Initialize the wrong answer count
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
            print(f"You have 10 seconds to think about the answer!")          
            #time.sleep(10)
            # Creates a variable to store the input values and transform them
            # into lowercase letters
            clue_answer = input("Please, type your answer here!\n").lower()

            # If statement to compare the user's input with the correct answer
            if clue_answer == correct_answer:
                # Print "Congratulations" message and 
                # capitalize the first letter
                # Increment the correct answer count

                print(f"Congratulations, {clue_answer.capitalize()}")
                print(f" is the correct answer!")
                # Print the custom explanation for the correct answer
                print(explanation)
                correct_count += 1
                # Stop further iteration as the correct answer 
                # has been provided
                break
            # Else statement for the if statement
            else:
                print(f"Sorry, {clue_answer.capitalize()} is the wrong answer.")# Else 
                #statement for the for loop activated when the correct answer
                # has not been provided
        else:
            # Increment the wrong answer count
            fail_count += 1
            print(f"Almost, {correct_answer.capitalize()}") 
            print(f"was the correct answer.")
            #Print the default explanation for the correct answer
            print(explanation)
    # Print the final results after all games
    print(f"\nTotal Correct Answers: {correct_count}")
    print(f"Total Wrong Answers: {fail_count}")


def main():
    """
    Run all program functions
    """
    print_title()
    display_welcome_messages()
    choice = users_input()
    choose_step(choice)
    # Get user input for starting the game
    start_game_choice = users_input_start_game()  
    play_game()
    

main()

