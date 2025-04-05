def main():
    fruits = {'apple': 1.5,
              'banana': 0.5,
              'orange': 0.75,
              'grape': 2.0,}
    
    total_cost = 0.0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount_bought = int(input("How many (" + fruit_name + ") do you want to buy? "))
        total_cost += price * amount_bought
    print("Total cost: $", str(total_cost))

if __name__ == "__main__":
    main()