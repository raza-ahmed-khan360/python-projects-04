ADULT_AGE: int = 18

def adult(age: int):
    if age >= ADULT_AGE:
        return True
    return False

def main():
    age: str = int(input("How old is this person?: "))
    print(adult(age))

if __name__ == "__main__":
    main()
