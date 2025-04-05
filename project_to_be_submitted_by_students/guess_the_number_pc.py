import random

def guess():
    print('Guess the number!')
    playing = True

    while playing:
        number = round(random.randint(1, 5))
        attempts = 0
        
        while True:
            try:
                user_guess = int(input('Guess a number between 1 to 5: '))
                attempts += 1
                if user_guess == number:
                    print(f'Congratulations! You guessed the number in {attempts} attempts!')
                    break
                else:
                    print('Nope! Try again!')
            except ValueError:
                print('Please enter a valid number!')
        
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        playing = (play_again == 'y')

if __name__ == '__main__':
    guess()