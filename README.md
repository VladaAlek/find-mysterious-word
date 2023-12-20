https://markdown-editor.github.io/

# Find a mysterious word in five steps

## About the project:
If you enjoy solving mysteries, you're in the right place. Allow me to present a game where the main task is to uncover mysterious words. To succeed, a clue will be displayed on the screen. Enter your answer, and you'll either receive confirmation that your answer is correct, or you'll move on to the next clue. In case you don't succeed the first time, fear not — the correct answer will be revealed.
This game features a total of five mysterious words.

![Terminal_photos](/assets/images/terminal_1.png)

INSPIRATION FOR THIS GAME CAME FROM THE POPULAR SERBIAN QUIZ SHOW "SLAGALICA".

## User Experience:

 - See Prototype - Algorithm below

**Introduction**
The user familiarizes themselves with the project content in two ways:
- *Title:* Its significance is emphasized by using capital letters.
-  *Explanation*: A concise explanation guides the user into the essence of the project and explains how to use it. 
- The **typing-machine-effect** has ben introduced in this section to ensures the better readability. This is the feature where the text is typed in gradually, instead of being presented in huge text blocks. 

**Demo, Game or Exit**

In the next step, the user has the option to choose between three possibilities.

To indicate users' typo mistakes, the exception with the text "Type 'd' to see the demo, 'g' to play, or 'e' to exit!" 
will be raised when none of these three letters entered.
The three above mentioned letters are clearly visible to improve the text readibility and likebility of the project. 

- The user can directly initiate the game by typing **"g"**.
- Alternatively, it is possible to exit the game **"e"**.
- By typing **"d"** for Demo, they go to the page with a demo example. 
- Each question in the Demo is displayd individualy by introducing three second temporal delay to increasse the readibility. 
After becoming more familiar with the game rules, the user can start the actual game by typing **"g"** for "Game" or exit the program by **typing any other key** on the keyboard for **Exit**.

        ![Exceptions](/assets/images/wrong_value_input.png)

**Game Flow**

Before each game, the notification signals the game count.

![Game Count](/assets/images/...)

The terminal displays the first clue to the mysterious concept and provides instructions to enter an answer.
- *delayed action:* two messages display with a ten seconds brake between them: 
    1.  "You have 10 seconds to think about the answer!" 
    2.  "Please, type your answer here!"
- *Incorrect Answer:* The user receives a notification about the incorrect answer and moves on to the next clue.
- *Correct Answer:* The user receives a notification about the correct answer. In this stage, the new game segment starts or, if it was the last set of questions, the user can chose between several options.

- *explanation* the user is provided with the interpretation regarding the clues and answer after failing or succeeding to give the correct answer

The user can choose between:
1. Starting a new game by typing **"g"** for *New Game* — a new set of questions appears on the screen.
2. Exiting the game by typing **"e"** for *Exit*.

**Game Result**

- At the end of the five-game set, the user receives information about the **total** number of **wins** and **errors**.

**Reinitiation or End of the Game**

- At the end of the cycle of questions for the five mysterious concepts, the user is provided with the following two options:
"Type 🇬 to start the game, or any other key to exit!"

![Prototyp - Algorithm](/assets/images/algorithm.png)

## Visual Elements
EMOTICONS
 - Inspiration for the introduction of emoticons came from [Python Tutorial for Beginners (with mini-projects)](https://www.youtube.com/watch?v=qwAFL1597eM "Python Tutorial for Beginners (with mini-projects)")
 - The source for the visual mateerial is from: [Emoticons](https://beta.emojipedia.org/ "Emoticons") and [Number Emoji](https://emojicombos.com/g "Number Emoji")

## Further Project´s Development

 #### Game Duration
 - provide the user with how many tries are left before the game conclusion

#### Timer

- The user has a limited time to provide an answer to each of the offered clues. The remaining time is displayed through a countdown in the terminal.
- An even more advanced game has the feature that with each level of difficulty, the time for answering questions decreases.
- The inspiraton for this concept came from [Count-Down_Timer](https://www.askpython.com/python/examples/countdown-with-for-loops "Count-Down_Timer")
and *CI Python Essentials - For Loop*.

#### Points
- As a continuation of the previously introduced **Correct** or **Wrong** Games counter, the user may receive information about the number of points won, depending on which stage of each game the correct answer was successfully guessed. For instance, after the first clue, the user gets 50 points, while in the fifth clue stage, the user earns only 10 points. Failing to solve this game segment results in no points being won.

#### Stats
- At the end of a cycle of 5 games, the user receives statistics informing them of how many attempts were needed in each game.

#### Game Stages
- Our project comprises five distinct games. Keep the user informed with a notification indicating the current game out of the five, such as "Game 3 of 5."

## Software and learning materials used

- Python

- cloud IDE [codeanywhere.com](https://codeanywhere.com/ "codeanywhere.com")

- Code editor [Visual Studio Code](https://code.visualstudio.com/ "Visual Studio Code") for writing and testing code externaly.

- [Markdown - editor](https://markdown-editor.github.io/ "Markdown - editor") used for the creation of the Readme.md file.

- [Python Checker](https://www.pythonchecker.com/ "Python Checker") used to style the code according to the [PEP 8](http:/https://peps.python.org/pep-0008// "PEP 8") standards.

    The issue of 79 characters per line signalled

![Python Checker](/assets/images/pythonchecker.png)

[Python Tutor](https://pythontutor.com/render.html#mode=display "Python Tutor") is used to monitor the execution of the Python commands. See the Debugging and Refactoring section below.

[Grammarly](https://app.grammarly.com "Grammarly") is used to correct grammar and spelling mistakes


- [Powerpoint](https://www.microsoft.com/de-de/microsoft-365/powerpoint "Powerpoint") is used for the creation of the Algorithm.

- Tutorial no. 6 from [Python Full Course for free ](https://www.youtube.com/watch?v=XKHEtdqhLK8 "Python Full Course for free ") from Bro Code used for coding of the input section.

- typing Instruction effect inspiration came from [Text Typer Example](https://morgan-adventure-game-82970373e96f.herokuapp.com/), 
[Slack Community](https://app.slack.com/client/T0L30B202/search "Slack Community") and [Flush Function in Python Blog](https://pythonhow.com/how/flush-the-output-of-the-print-function/ "Flush Function in Python Blog")

- [Python Time Sleep](https://www.digitalocean.com/community/tutorials/python-time-sleep "Python Time Sleep")

- [Exit Game Function](https://github.com/gitdagray/python-course/blob/main/lesson12/rps5.py "Exit Game Function"), lines 78-80.

- inspiration and sourcecode for the Game Counter: [Inspiration](https://www.youtube.com/watch?v=qwAFL1597eM "Inspiration") and [sourcecode](https://github.com/gitdagray/python-course/blob/main/lesson12/rps5.py "Game Counter") 


## Product Testing

- The content of the terminal output has been checked constantly to find unwanted features. Here are some of the most distinct examples.
In this case, display_intro() function called two times:

   ![Display Intro](/assets/images/product_testing.PNG)

The issue was resolved by deleting the nested display_intro() from the main().

In the second case, the function was called two times, causing a negative UX.
   
   ![Display Intro](/assets/images/product_testing_2.PNG)

The same as here:
   
   ![wrong Function Called](/assets/images/product_testing_3.PNG)


Confusing instructions noticed in the first version of the play_game function.

    ![Confusing Instruction](/assets/images/confusing_aswers.PNG)

Confusing answers noticed in the last step of the play_game function.

    ![Confusing Last Answer](/assets/images/wrong_final_answer.PNG)

The observation that the letters of the cities in the answers should be capitalized.

    ![Capitalized Names](/assets/images/capitalize.PNG)

A mistake in clues_1 list causes the inconsistency when print function activated

    ![Mistake in clues_1 List](/assets/images/string_list_mistake.png).

Game initiation is possible not only by typing the "g" key on the keyboard.
  
    ![Unprecise Game Initiation](/assets/images/game_initiation.png).

Problematic return to the game when exception raised.

    ![Unprecise Game Initiation](/assets/images/command_not_found.png)

Conflicting instruction and final result at the end of the final game.
    
    ![Conflicting instructions](/assets/images/g_key_start_game.PNG)

An overlapping answer occures when the user enters the input before the ten seconds period expires.

    ![Overlapping Answer](/assets/images/overlapping_anwers.PNG)

Incorrect Correct Wrong Count in the initial code version.

    ![Incorrect Correct Wrong Count](/assets/images/incorect_correct_wrong_count.PNG)

    ![Correct Correct Wrong Count](/assets/images/corect_correct_wrong_count.PNG)

The game promtly ends after the total correct/wrong answer has been printed. Solution: introduction of the users_input_start_game function.

    ![Game Promtly Ends](/assets/images/deadend.PNG)



## Debugging and Refactoring

- **Exceptions raised** in the Terminal are used frequently to locate the mistakes and refactor the code.
    For instance, the scope issue was solved by introducing "return choice" in the users_input function and passing the "choice" argument into the choose_step function.

    ![Name Error](/assets/images/Name_Error.png)
    
    ![Type Error](/assets/images/Type_Error.png)

    Later, the same approach was used to understand which function was missing to complete the workflow of the command lines.

    ![Missing Function](/assets/images/name_error_click_g.PNG)

    The same tool is an efficient syntax error indicator.

    ![Synthax Errors](/assets/images/synthax_error.png)


- **Python Tutor** used to monitor the execution of the Python commands.

    ![Python Tutor](/assets/images/python_tutor.PNG)

- temporarily introduced *print function* used to control the flow of the command lines.

     ![Print Function](/assets/images/using_print_function.PNG)

- **Problems indicator**, built-in function of Codeanywhere used. 

    ![Problem Indicator](/assets/images/problems.PNG.jpg)

- Staging and Pushing Issues in [Git](https://github.com/git-guides) 

    -  ![Staging and Pushing Issues](/assets/images/codeanywhere_unreliability%20.jpg)
    -  ![Staging and Pushing Solution](/assets/images/tutor_support.png)

- **Blame** option in the GitHub used to access and examine the deployment history.

    - [Blame](/assets/images/blame_github.png)

- **Commit** option in the GitHub used to access and examine the previous code versions.

- Issue that the time_counter function was called before all other functions or in the wrong place of the play_game function disrupting the desired line of commands.

    ![Count Down Issue](/assets/images/count_down_issue.PNG)

    ![Count Down Issue](/assets/images/count_down_issue_1.PNG)

- *Infinite Loop* in users_input_start_game() if the user does not input "g." Issue solved by introducing **sys.exit**. 

     ![Loop](/assets/images/loop.PNG)

## Testing User Stories from the UX Section

#### First-Time Visitor Goals

As a first-time visitor, clarity and quick understanding are paramount. Right off the bat, the project contains several features to make the positive UX.
- **Title with capital letters**: For better readibility.
- Clear **Introduction**: To inform the user of the main goal of the product and game rules.
- **Demo Section** To increase the understanding of the game. 
- **Dynamic features** such as *typing-machine-effect* and *temporal* elements to make the game more appealing. Additionall, *typing-machine-effect* aims to ensure that the users are familiar with the rules of the game.
- **Visual effects**: To increase readability and the likability factor.
- Multiple measures to improve the **navigation**. Beside multiple options when the user can chose its next step, the **game count** ensures better avarenes of the game navigation.

-  ![Game Counter](/assets/images/game_counter.png)

**Issues noticed:** Capitalization of the first letter in the answers, for instance, "Rome" is not required in all games. It causes situations in which some words start with the capital letter unnecessarily. Hence, the user can expect the results like "Hammer", instead of "hammer".

#### Returning and Frequent Visitor Goals

 - **Second-time users** may find this product not interesting to play again since they already know the correct answers. 
 
 - Nevertheless, **users who return multiple times** have the option to reconfigure and repurpose this product as an educational resource. This is particularly applicable in lower-grade levels of elementary schools, especially when all sets of questions are closely linked to a specific subject, such as geography or history.


## Deployment

- Readme.md file deploied in [GitHub](https://github.com/ "GitHub").
- Python code from the run.py file deployed in [Heroku](https://www.heroku.com/)
    1. problems to log in to Heroku
     - this, seemingly simple step, required the action of the CI Tutor Team and repeated intervention of the Heroku Support team.

- run.py file imported python-built-in modules **"import sys"** and **"import time"**. Hence, the project runs without any additional packages in the requirements.txt file. 

![Heroku Deployment Problems](/assets/images/heroku_deployment_problems.png)

- **Codeanywhere** - frequent failures when trying to upload captures to the image folder which caused the disruption of the workflow and delays in deployment.
- This project contains no *credentials*.
- The project is released under the **Common Creatives license**, allowing for its unrestricted and free use by individuals and entities.

### Acknowledgments

- Mentor Narender Singh
- Sarah, Rebecca, Roman, John and Oisin from the CI Tutor Team :-)
- Heroku Support Team

 


