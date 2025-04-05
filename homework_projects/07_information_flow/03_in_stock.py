def main():
    fruit: str = input("Enter a fruit: ")
    stock = num_in_stock(fruit)
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)

def num_in_stock(fruit):
    if fruit == "apple":
        return 2
    if fruit == "orange":
        return 5
    if fruit == "mango":
        return 20
    else:
        return 0 
    
if __name__ == "__main__":
    main()