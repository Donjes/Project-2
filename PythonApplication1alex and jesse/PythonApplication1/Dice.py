import random

def Throw_dice():
    diceList = [1,2,3,4,5,6]
    dice = random.choice(diceList)
    diceImglist = ["Dice1.png","Dice2.png","Dice3.png","Dice4.png","Dice5.png","Dice6.png"]
    diceImg = diceImglist[dice-1]
    return dice,diceImg