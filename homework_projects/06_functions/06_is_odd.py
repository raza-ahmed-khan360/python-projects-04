def main():
    for i in range(10):
        if odd(i):
            print(f"{i} is odd")
        else:
            print(f"{i} is even")

def odd(value: int):
    remainder = value % 2
    return remainder == 1

if __name__ == "__main__":
    main()