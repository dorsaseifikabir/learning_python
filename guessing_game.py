import random
print("Let's ptry guessing a number between 1 to 50!")
print("easy = 10 guesses\nmedium = 5 guesses\nhard = 3 guesses")
while True:
    chosen_mode = input("Which mode will it be? ").strip().lower()
    max_guess = 0
    if chosen_mode == 'easy':
        max_guess = 10
        break
    elif chosen_mode == 'medium':
        max_guess = 5
        break
    elif chosen_mode == 'hard':
        max_guess = 3
        break
    else:
        print("You have to choose from the given options!")
        

computers_choice = random.randint(1, 50)
guess_count = 0

while True:
    try:
        player_choice = int(input("guess a number between 1 to 50: "))
        if player_choice not in range(1, 51):
            print("you must pick a number between 1 to 50!")
            continue  
        max_guess -= 1
        guess_count += 1
        if player_choice == computers_choice:                   
            print("you win!")  
            print(f"you got it on guess number {guess_count} ")                  
            break                    
        elif player_choice < computers_choice:                    
            print("Too low!")            
        else:                   
            print("Too high!") 
        if max_guess <= 0:
            print("You're out of guesses!")
            print(f"The chosen number was {computers_choice}.") 
            break                            
    except ValueError:
        print('You must enter a number!')
