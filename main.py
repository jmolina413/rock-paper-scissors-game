import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


# Function to display the ASCII art based on the choice
def display_choice(choice):
    if choice == 'rock':
        print(rock)
    elif choice == 'paper':
        print(paper)
    elif choice == 'scissors':
        print(scissors)


# Function to get the user's choice
def get_user_choice():
    user_choice = input("Enter Rock (r), Paper (p), or Scissors (s): ").strip().lower()
    while user_choice not in ['rock', 'paper', 'scissors', 'r', 'p', 's']:
        print("Invalid choice. Please enter Rock, Paper, or Scissors.")
        user_choice = input("Enter Rock (r), Paper (p), or Scissors (s): ").strip().lower()

    if user_choice == 'r':
        return 'rock'
    elif user_choice == 'p':
        return 'paper'
    elif user_choice == 's':
        return 'scissors'
    else:
        return user_choice


# Function to generate the computer's choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"


def ask_to_play_again():
    return input("Do you want to play again? (yes/no): ").strip().lower()


def main_screen():
    while True:
        mode = input("Choose a mode: 'best of three', 'tournament', or 'sudden death'\n").strip().lower()
        if mode in ['best of three', 'tournament', 'sudden death']:
            play_game(mode)
        else:
            print("Invalid mode. Please select a valid mode.")
            continue
        break


# Function to play the game
def play_game(mode):
    user_score = 0  # Initialize user's score
    computer_score = 0  # Initialize computer's score
    rounds = 0

    if mode == 'best of three':
        rounds_to_win = 2
    elif mode == 'tournament':
        rounds_to_win = 3
    else:
        rounds_to_win = 1

    while True:
        rounds += 1
        print(f"Round {rounds} - Let's play Rock, Paper, Scissors!")
        user_choice = get_user_choice()  # Get user's choice normally
        computer_choice = get_computer_choice()  # Get computer's choice

        print(f"You chose: {user_choice}")
        display_choice(user_choice)  # Display user's choice
        print(f"Computer chose: {computer_choice}")
        display_choice(computer_choice)  # Display computer's choice

        result = determine_winner(user_choice, computer_choice)  # Determine the winner
        print(result)  # Print the result

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Your score: {user_score} - Computer's score: {computer_score}")

        if user_score == rounds_to_win or computer_score == rounds_to_win:
            print(f"The game is over! {result}")
            play_again = ask_to_play_again()
            if play_again != 'yes':
                print("Thank you for playing")
                break
            else:
                main_screen()

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing")
            break


# Start the game
main_screen()
