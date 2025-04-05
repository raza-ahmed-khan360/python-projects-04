import random

NUM_ROUNDS = 5

print("Welcome to the High-Low Game!")
print("--------------------------------")

score = 0

for round_num in range(1, NUM_ROUNDS + 1):
    print(f"Round {round_num}")
    player_num = random.randint(1, 100)
    computer_num = random.randint(1, 100)
    
    print(f"Your number is {player_num}")
    
    user_input = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
   
    while user_input not in ("higher", "lower"):
        user_input = input("Please enter either higher or lower: ").strip().lower()
    
  
    if player_num == computer_num:
       
        correct = False
    elif user_input == "higher" and player_num > computer_num:
        correct = True
    elif user_input == "lower" and player_num < computer_num:
        correct = True
    else:
        correct = False

    if correct:
        print(f"You were right! The computer's number was {computer_num}")
        score += 1
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_num}")

    print(f"Your score is now {score}")
    print("")  

print("Thanks for playing!")
print(f"You finished with a score of {score} out of {NUM_ROUNDS}")


if score == NUM_ROUNDS:
    print("Wow! You played perfectly!")
elif score >= NUM_ROUNDS // 2:
    print("Good job, you played really well!")
else:
    print("Better luck next time!")