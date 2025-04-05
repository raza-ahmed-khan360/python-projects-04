import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "Tie"
    if ((user == 'rock' and computer == 'scissors') or
        (user == 'paper' and computer == 'rock') or
        (user == 'scissors' and computer == 'paper')):
        return "User wins"
    return "Computer wins"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        try:
            user_choice = input("Enter rock, paper, scissors or 'quit' to exit: ").lower()
            if user_choice == 'quit':
                print("Thanks for playing!")
                break
            if user_choice not in ['rock', 'paper', 'scissors']:
                print("Invalid input. Try again.")
                continue

            computer_choice = get_computer_choice()
            print(f"Computer chose: {computer_choice}")

            result = determine_winner(user_choice, computer_choice)
            print(f"Result: {result}\n")
        except Exception as e:
            print(f"An error occurred: {e}")
            continue

if __name__ == "__main__":
    main()