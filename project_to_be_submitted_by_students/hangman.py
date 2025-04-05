import random

def get_random_word():
    words = ["python", "css", "html", "javascript", "typescript", "php", "java", "c", "git"]
    return random.choice(words)

def display_current_state(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def play_hangman():
    word = get_random_word()
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("Welcome to Hangman!")
    while wrong_guesses < max_wrong_guesses:
        current_state = display_current_state(word, guessed_letters)
        print("Word: ", ' '.join(current_state))
        
        guess = input("Enter a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabet letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)
        
        if guess in word:
            print("Good guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess! Attempts remaining:", max_wrong_guesses - wrong_guesses)
        
        if set(word) <= guessed_letters:
            print("Congratulations! You guessed the word:", word)
            return

    print("Sorry, you ran out of guesses. The word was:", word)

if __name__ == "__main__":
    play_hangman()