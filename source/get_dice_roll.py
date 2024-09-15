from random import randint

def get_dice_roll():
    dice1 = randint(2, 6)
    dice2 = randint(2, 6)
    roll_ = dice1 + dice2
    return roll_