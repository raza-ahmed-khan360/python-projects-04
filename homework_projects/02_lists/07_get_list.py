def main():
    lst = []

    val = input("Enter a value: ")
    while val:
        lst.append(val)
        val = input("Enter a value: ")
    print(lst)

if __name__ == "__main__":
    main()