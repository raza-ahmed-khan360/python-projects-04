import random
NUM_SIDES = 6
print("This is a Dice Simulator")
def roll_dice():
    die_one: int = random.randint(1, NUM_SIDES)
    die_two: int = random.randint(1, NUM_SIDES)
    total: int = die_one + die_two
    print("Total of two dice is: ", total)

def main():
    die_one: int = 10
    print("die_one in main() start as:" + str(die_one))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die_one in main() is:" + str(die_one))

if __name__ == "__main__":
    main()    
