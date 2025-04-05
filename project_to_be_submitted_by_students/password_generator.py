import string
import random

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_punctuation=True):
    # Create a list of character sets based on preferences.
    char_sets = []
    if use_upper:
        char_sets.append(string.ascii_uppercase)
    if use_lower:
        char_sets.append(string.ascii_lowercase)
    if use_digits:
        char_sets.append(string.digits)
    if use_punctuation:
        char_sets.append(string.punctuation)

    if not char_sets:
        raise ValueError("At least one type of character must be selected to generate a password.")

    # Ensure that at least one character from each selected set is included.
    password_chars = [random.choice(chars) for chars in char_sets]

    # Validate requested length.
    if length < len(password_chars):
        raise ValueError("Password length is too short for the selected character sets.")

    # Fill the remaining password length with characters from all sets.
    all_chars = ''.join(char_sets)
    password_chars.extend(random.choices(all_chars, k=length - len(password_chars)))
    
    # Shuffle to distribute the guaranteed characters.
    random.shuffle(password_chars)
    return ''.join(password_chars)

def main():
    print("Modern Logic Password Generator")
    try:
        count = int(input("Enter the number of passwords to generate (enter numeric value): "))
        length = int(input("Enter password length (enter numeric value) (minimum {}): ".format(12)))
        passwords = []
        for _ in range(count):
            password = generate_password(length)
            passwords.append(password)
        print("\nGenerated Passwords:")
        for pwd in passwords:
            print(pwd)
    except ValueError as error:
        print("Error:", error)

if __name__ == "__main__":
    main()