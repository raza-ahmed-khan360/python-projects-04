import random
NUM_SIDES = 6

def main():
    die_one: int = random.randint(1, NUM_SIDES)
    die_two: int = random.randint(1, NUM_SIDES)
    total: int = die_one + die_two
    
    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die_one)
    print("Second die:", die_two)
    print("Total of two dice:", total)

if __name__ == "__main__":
    main()    
