# project2
Rock-Paper-Scissor Game

This is a terminal-based Rock-Paper-Scissors game implemented in Python. The user plays against the computer, which makes random choices. The game continues in rounds until the user decides to quit. 

Features implemented include the ability to play rock, paper, or scissors using the keys 'r', 'p', or 's'. The computer makes random choices using Python's `random` module. All user input is validated, and the game will prompt again for valid input if necessary. After each round, the player is asked whether they would like to play again. The game tracks the number of rounds played, the number of wins by the player, the number of wins by the computer, and the number of ties. When the user quits, the game displays a final summary of the scores and number of rounds played.


Here is an example of what the program looks like when run:

Welcome to Rock, Paper, Scissors!  
Do you want to play the game with me?  
Enter "y" to play or replay, "n" to stop: y

Great! Ready to play!  
Type: 'r' for rock, 'p' for paper, 's' for scissors, 'q' to quit

Your choice: p  
You chose paper, computer chose rock.  

Paper covers rock! You win!

Play another round? (y/n): n

Rounds played: 1  
Final Scores - You: 1, Computer: 0  
Thanks for playing! Goodbye!

The code is written in a modular structure using the following functions:
- get_user_throw(): prompts and validates user input
- get_computer_throw(): generates the computer’s throw
- compare_throws(): compares throws and determines round result
- play_one_round(): handles a full round of gameplay
- ask_play_again(): checks if the user wants to continue
- play_game(): main loop that runs the game and tracks scores
