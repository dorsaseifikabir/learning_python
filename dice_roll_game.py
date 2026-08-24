import random

roll_one = random.randint(1, 6)
roll_two = random.randint(1, 6)
player_one = roll_one + roll_two

roll_one = random.randint(1, 6)
roll_two = random.randint(1, 6)
player_two = roll_one + roll_two

print(player_one)
print(player_two)

if player_one > player_two:
    print('player one wins!')
elif player_one < player_two:
    print('player two wins!')
else:
    print("it's a tie!")
