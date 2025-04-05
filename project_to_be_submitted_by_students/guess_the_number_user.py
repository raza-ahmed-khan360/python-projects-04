import random

def guess():
    playing = True
    print("Think of a number between 1 and 5, and I'll try to guess it!")
    
    while playing:
        low = 1
        high = 5
        attempts = 0
        
        while True:
            computer_guess = random.randint(low, high)
            attempts += 1
            response = input(f"Is your number {computer_guess}? (Enter 'c' for correct, 'l' if your number is lower, 'h' if it's higher): ").strip().lower()
            
            if response == 'c':
                print(f"I guessed your number in {attempts} attempts!")
                break
            elif response == 'l':
                high = computer_guess - 1
            elif response == 'h':
                low = computer_guess + 1
            else:
                print("Please enter a valid response: 'c', 'l', or 'h'.")
            
            if low > high:
                print("There seems to be a mistake. Let's restart this round!")
                break
        
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        playing = (play_again == 'y')

if __name__ == '__main__':
    guess()