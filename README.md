# Find mysterious word in five steps

## About the project:
If you enjoy solving mysteries, you're in the right place. Allow me to present a game where the main task is to uncover mysterious words. To succeed, a clue will be displayed on the screen. Enter your answer, and you'll either receive confirmation that your answer is correct, or you'll move on to the next clue. In case you don't succeed the first time, fear not — the correct answer will be revealed.
This game features a total of five mysterious words.

INSPIRATION FOR THIS GAME CAME FROM THE POPULAR SERBIAN QUIZ SCHOW "SLAGALICA"

![Terminal_photos](/assets/images/terminal_1.png)

## User Experience:
**Introduction**
The user familiarizes themselves with the project content in two ways:
- *Title:* Its significance is emphasized by using capital letters.
-  *Explanation*: A concise explanation guides the user into the essence of the project and explains how to use it.
**Demo or Game**

In the next step, the user has the option to choose between two possibilities:
- By typing **"d"** for Demo, they go to the page with a demo example. After becoming more familiar with the game rules, the user can start the actual game by typing **"g"** for "Game" or exit the program by typing **"e"** for "Exit."
- Alternatively, the user can directly initiate the game by typing **"g."**
**Game Flow**

The terminal displays the first clue to the mysterious concept and provides instructions to enter an answer.
- *Incorrect Answer:* The user receives a notification about the  incorrect answer and moves on to the next clue.
- *Correct Answer:* The user receives a notification about the correct answer.
The user can choose between:
1. Starting a new game by typing **"n"** for "New Game!"— a new set of questions appears on the screen.
2. Exiting the game by typing **"e"** for "Exit."
**End of Game**
At the end of the cycle of questions for the five mysterious concepts, the user exits the game by typing **"e."**

## Visual elements
in several ocasions the emoticons have been used
source code: David Gray: https://www.youtube.com/watch?v=qwAFL1597eM&t=23215sg

![Prototyp - Algorithm](/assets/images/algorithm.png)

## Further project´\*s development

#### Timer
- The user has a limited time to provide an answer to each of the offered clues. The remaining time is displayed through a countdown in the terminal.
- An even more advanced game has the feature that with each level of difficulty, the time for answering questions decreases.

#### Points
- At the end of each game, the user receives information about the number of **earned points** depending on their success in solving each set of five clues.
- At the end of the five-game set, the user receives information about the **total** number of earned points.

#### Stats
- At the end of a cycle of 5 games, the user receives statistics informing them of how many attempts were needed in each game.

#### Text Typer
- Introduce the option where the text is typed in gradually, instead of presenting the text in huge blocks. Inspiration comes from: [Text Typer Example](https://morgan-adventure-game-82970373e96f.herokuapp.com/)

#### Game Stages
- Our project comprises five distinct games. Keep the user informed with a notification indicating the current game out of the five, such as "Game 3 of 5."

## Software and learning materials used

-[Markdown - editor](https://markdown-editor.github.io/ "Markdown - editor") used for the creation of the Readme.md file

- [Python Checker](https://www.pythonchecker.com/ "Python Checker") used to style the code according to the [PEP 8](http:/https://peps.python.org/pep-0008// "PEP 8") standards
        Issue of 79 characters per line signaled
![Python Checker](/assets/images/pythonchecker.png)

[Python Tutor](https://pythontutor.com/render.html#mode=display "Python Tutor") used to monitor the execution of the python commands. See Debuging and Refactoring section bellow. 



- PowerPoint

- Tutorial no. 6 from [Python Full Course for free ](https://www.youtube.com/watch?v=XKHEtdqhLK8 "Python Full Course for free ") from Bro Code used for coding of input section.



## Product Testing

- The content of the terminal output has been checked constantly to find unwanted features. In this example, display_intro() function called two times:

   ![Display Intro](/assets/images/product_testing.PNG)

The issue resolved by deleting the nested display_intro() from the main().

   In the second case, the function was called two times, causing negative UX
   
   ![Display Intro](/assets/images/product_testing_2.PNG)

Comment: Vladimir to check p/g/n and similar in the algorithm, functions and game description.

## Debuging and Refactoring

- Exceptions raised in the Terminal used to locate the mistakes and refactor the code.
    For instance, scope issue solved by introducing "return choice" in users_input function and passing "choice" argument into the choose_step function

    
    ![Name Error](/assets/images/Name_Error.png)
    
    ![Type Error](/assets/images/Type_Error.png)

    Later, the same approach used to understand which funcion was missing to complete the workflow of the command lines

    ![Missing Function](/assets/images/name_error_click_g.PNG)

- Python Tutor used to monitor the execution of the python commands

    ![Python Tutor](/assets/images/python_tutor.PNG)

- teporarelly introduced print function used to control the flow of the command lines

     ![Print Function](/assets/images/using_print_function.PNG)

## Deployment


![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
