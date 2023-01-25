import random
import math

maximum = 100
secret_number = random.randint(1, maximum)
guessed = False
attempts = 0
player_wants_to_play = True
best_result = math.inf

while player_wants_to_play:

    while not guessed:
        attempts += 1
        guess = int(input("Try to guess a secret number! "))
        
        if guess == secret_number:
            guessed = True
            print("Congratulations! You win! It took you " + str(attempts) + " attempts to guess a secret number.")
            
            if attempts < best_result:
                print("It's your best result!")
                best_result = attempts
            
        elif guess > secret_number:
            print("Less.")
        else:
            print("More.")
        
    guessed = False    
    print("Your best result is " + str(best_result) + ".")
    player_wants_to_play = str(input("Do you want to play again? yes/no ")) == "yes"
    
    if player_wants_to_play:
        secret_number = random.randint(1, maximum)
        attempts = 0
    else: 
        print("Game is over. Your best result is " + str(best_result) + ".") 
    
        
    