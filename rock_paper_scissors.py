import random

player_wins = 0
computer_wins = 0
rps = ['rock', 'paper', 'scissors']

choices = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissors'
}

for i in range(3):

    while True:
        player_choice = input(
            "rock, paper or scissors? "
        ).lower().strip()

        # Convert first letters to full words
        if player_choice in choices:
            player_choice = choices[player_choice]

        if player_choice in rps:
            break

        print("Please choose rock, paper, scissors, or r/p/s.")

    pc_choice = random.choice(rps)

    if player_choice == pc_choice:
        print("It's a tie!")

    elif (
        (player_choice == 'rock' and pc_choice == 'scissors') or
        (player_choice == 'paper' and pc_choice == 'rock') or
        (player_choice == 'scissors' and pc_choice == 'paper')
    ):
        print("You win!")
        player_wins += 1

    else:
        print("You lose!")
        computer_wins +=1

    print(f"Computer chose: {pc_choice}")
    print(f"Your total wins: {player_wins}")
    print()

if player_wins > computer_wins:
    print("The player is the winner!")
elif computer_wins > player_wins:
    print("The computer wins!")
else:
    print("it's a tie!")