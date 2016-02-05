import random
import pygame

diceIMG1 = pygame.image.load("images/Dice1.png")
diceIMG2 = pygame.image.load("images/Dice2.png")
diceIMG3 = pygame.image.load("images/Dice3.png")
diceIMG4 = pygame.image.load("images/Dice4.png")
diceIMG5 = pygame.image.load("images/Dice5.png")
diceIMG6 = pygame.image.load("images/Dice6.png")


def Throw_dice():
    diceList = [1,2,3,4,5,6]
    dice = random.choice(diceList)
    diceImglist = [diceIMG1,diceIMG2,diceIMG3,diceIMG4,diceIMG5,diceIMG6]
    diceImg = diceImglist[dice-1]
    return dice,diceImg