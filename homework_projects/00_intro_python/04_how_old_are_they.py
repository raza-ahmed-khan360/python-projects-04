def main():
    anton_age = 21

    beth_age = anton_age + 6

    chen_age = beth_age + 20

    drew_age = chen_age + anton_age

    ethan_age = chen_age

    print(f"Anton is \033[1m{anton_age}\033[0m years old.")
    print(f"Beth is \033[1m{beth_age}\033[0m years old.")
    print(f"Chen is \033[1m{chen_age}\033[0m years old.")
    print(f"Drew is \033[1m{drew_age}\033[0m years old.")
    print(f"Ethan is \033[1m{ethan_age}\033[0m years old.")

if __name__ == '__main__':
    main()