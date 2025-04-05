AFFIRMATION = "I am capable of achieving my goals."

def main():
    print("Please type the folowing affirmation: " + AFFIRMATION)

    user_feedback = input()
    while user_feedback != AFFIRMATION:
        print("Oops! Try again.")
        print("Please type the folowing affirmation: " + AFFIRMATION)
        user_feedback = input()

    print("Great job! You typed the affirmation correctly.")

if __name__ == "__main__":  
    main()