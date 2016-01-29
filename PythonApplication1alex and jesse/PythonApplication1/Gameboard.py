import pygame
import time
from Dice import *
import os
from Character import *
from Node import *

#======================================= Variable die vanuit player screen moeten komen

size = width, height = 700, 650
white = (255, 255, 255)
gloveSmall1 = "images/red_handschoen.png"
gloveSmall1move = "images/red_handschoen1.png"
gloveSmall2 = "images/blue_handschoen.png"
gloveSmall2move = "images/blue_handschoen1.png"
gloveSmall3 = "images/green_handschoen.png"
gloveSmall3move = "images/green_handschoen1.png"
gloveSmall4 = "images/yellow_handschoen.png"
gloveSmall4move = "images/yellow_handschoen1.png"
smallGlove = [gloveSmall1,gloveSmall2,gloveSmall3,gloveSmall4]
smallGlovemove =[gloveSmall1move,gloveSmall2move,gloveSmall3move,gloveSmall4move]
#=======================================================================================

size = width, height = 750, 780
gameDisplay = pygame.display.set_mode(size)

roll = Trow_dice()

def small_glove(gloveSmall,navilist):                  #3Ruben handschoen over board functie    
        gameDisplay.blit(pygame.image.load(gloveSmall),navilist)
def dice_img(roll):
        gameDisplay.blit(pygame.image.load("images/" + roll[1]),(300,300))

# list van Tile lokaties
navigate = [(20,20),(80,20),(130,20),(180,20),(230,20),(300,20),(375,20),(425,20),(472,20),(520,20),(575,20),(575,85),(575,130),(575,180),(575,230),(575,300),(575,373),(575,425),(575,475),(575,525),(575,590),(520,590),(472,590),(425,590),(375,590),(300,590),(230,590),(180,590),(130,590),(80,590),(20,590),(20,525),(20,475),(20,425),(20,373),(20,300),(20,230),(20,180),(20,130),(20,85)]
# playerList 

p = 0

#gameboard
def BoardScreen(firstround, chooseChars,roll,p,screenlist, rectlist, crashed, menu_index, screen_index):   
    if firstround:
        chooseChars[0].savePosition = 10
        chooseChars[1].savePosition = 0
        chooseChars[2].savePosition = 20
        chooseChars[3].savePosition = 30
        firstround = False

    player = chooseChars[p%4]
    tile = player.savePosition
    for event in pygame.event.get():         # Navigatie van de handschoenen bij elke dice throw
        if event.type == pygame.KEYDOWN:         
            if event.key == pygame.K_SPACE: 
                roll = Trow_dice() 
                small_glove("images/DiceRolling.png",(300,300))  
                pygame.display.update()
                time.sleep(0.5)
                dice_img(roll)  
                pygame.display.update()
                time.sleep(0.5)           
                for i in range(roll[0]):                   
                    tile += 1 
                    small_glove(smallGlovemove[p%4],navigate[tile%40])    
                    pygame.display.update()
                    time.sleep(0.1)
                    print("plus")  
                chooseChars[p%4].savePosition = tile
                p += 1
                
    

    return firstround,chooseChars,roll,p,screenlist, rectlist, crashed, menu_index, screen_index