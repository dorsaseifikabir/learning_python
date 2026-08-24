import random

player_wins = 0
computer_wins = 0

RPS = ('rock', 'paper', 'scissors')

choices = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissors'
}

round_number = 1

while round_number <= 3 or player_wins == computer_wins:

    while True:
        player_choice = input(
            "rock, paper or scissors? "
        ).lower().strip()

        if player_choice in choices:
            player_choice = choices[player_choice]

        if player_choice in RPS:
            break

        print("Please choose rock, paper, scissors, or r/p/s.")

    pc_choice = random.choice(RPS)

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
        computer_wins += 1

    print(f"Computer chose: {pc_choice}")
    print(f"Your total wins: {player_wins}")
    print(f"Computer total wins: {computer_wins}")
    print()

    round_number += 1


if player_wins > computer_wins:
    print("The player is the winner!")
else:
    print("The computer wins!")