import random

ans = input('do you want to roll the dice? (y/n): ').lower()

while ans == 'y':
    dice_roll = random.randint(1, 6)
    print(f'You rolled a {dice_roll}')
    ans = input('roll again? (y/n): ').lower()


