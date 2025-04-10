import random
import time
DONE_LIKELIHOOD = 0.2  # Probability of stopping at each count
def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        time.sleep(1)
        if done():
            return
        print(curr_num)

def done():
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("Done counting!")

if __name__ == "__main__":
    main()