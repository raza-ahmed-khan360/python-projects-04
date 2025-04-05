PAKISTAN : int = 18
MALAYESYA : int = 14
INDONESHIA : int = 16

def main():
    user_age = int(input("Enter your age: "))
    if user_age >= PAKISTAN:
        print("You are eligible to vote in Pakistan")
    else:
        print("You are not eligible to vote in Pakistan")

    if user_age >= MALAYESYA:
        print("You are eligible to vote in Malayesya")
    else:
        print("You are not eligible to vote in Malayesya")
    if user_age >= INDONESHIA:
        print("You are eligible to vote in Indoneshia")
    else:
        print("You are not eligible to vote in Indoneshia") 

if __name__ == '__main__':
    main()