#---------------------------------------------------------
# Rock-Paper-Scissors Game
#---------------------------------------------------------

import random

def get_user_throw():
    choice_map = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    while True:
        user_input = input("Your choice: ").lower()
        if user_input in choice_map:
            return choice_map[user_input]
        elif user_input == 'q':
            return 'quit'
        else:
            print("Invalid input. Use 'r', 'p', 's', or 'q'.")

def get_computer_throw():
    return random.choice(['rock', 'paper', 'scissors'])

def compare_throws(user, computer):
    if user == computer:
        return "tie"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "win"
    else:
        return "lose"

def play_one_round():
    user_choice = get_user_throw()
    if user_choice == 'quit':
        return 'quit'

    computer_choice = get_computer_throw()

    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

    result = compare_throws(user_choice, computer_choice)

    if result == "tie":
        print(f"Both selected {user_choice}. It's a tie!")
    elif result == "win":
        if user_choice == "rock":
            print("Rock smashes scissors! You win!")
        elif user_choice == "paper":
            print("Paper covers rock! You win!")
        elif user_choice == "scissors":
            print("Scissors cuts paper! You win!")
    else:
        if computer_choice == "rock":
            print("Rock smashes scissors! You lose.")
        elif computer_choice == "paper":
            print("Paper covers rock! You lose.")
        elif computer_choice == "scissors":
            print("Scissors cuts paper! You lose.")

    return result

def ask_play_again():
    return input("Play another round? (y/n): ").lower() == "y"

def play_game():
    player_score = 0
    computer_score = 0
    tie_score = 0

    while True:
        result = play_one_round()

        if result == "quit":
            break
        elif result == "win":
            player_score += 1
        elif result == "lose":
            computer_score += 1
        elif result == "tie":
            tie_score += 1

        if not ask_play_again():
            break

    total_rounds = player_score + computer_score + tie_score

    print(f"\nRounds played: {total_rounds}")
    print(f"\nFinal Scores - You won: {player_score}, I won: {computer_score}")
    print("Thanks for playing! Goodbye!")
    return False

print("Welcome to Rock, Paper, Scissors!")
print("Do you want to play the game with me?")

while True:
    start = input('Enter "y" to play or replay, "n" to stop: ').lower()

    if start == "n":
        print("Okay, goodbye!")
        break
    elif start == "y":
        print("\nGreat! Ready to play!")
        print("Type: 'r' for rock, 'p' for paper, 's' for scissors, 'q' to quit\n")
        play_more = play_game()
        if not play_more:
            break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")