def count_even(lst):
    count = 0 
    for num in lst:
        if num % 2 == 0:
            count += 1
    print(count)


def list():
    lst = []
    while True:
        user_input = input("Enter an integer or press Enter to stop: ")
        while user_input != "":
            lst.append(int(user_input))
            user_input = input("Enter an integer or press Enter to stop: ")
        
        return lst

def main():
    lst = list()
    count_even(lst)

if __name__ == "__main__":
    main()