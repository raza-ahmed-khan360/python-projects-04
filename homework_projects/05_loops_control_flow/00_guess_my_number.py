import random

def main():
    secret_number = random.randint(1, 99)
    print("I am thinking of a number between 1 and 99....")

    guess = int(input("Enter a guess: "))

    while guess != secret_number:
        if guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

        print()
        guess = int(input("Enter a guess: "))
    print("Congratulations! You guessed it!")

if __name__ == "__main__":
    main()