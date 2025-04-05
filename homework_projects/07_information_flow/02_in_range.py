def in_range(n, low, high):
    return low <= n <= high

def main():
    n = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))

    if in_range(n, low, high):
        print(n, "is within the range [", low, ",", high, "].")
    else:
        print(n, "is not within the range [", low, ",", high, "].")

if __name__ == '__main__':
    main()
