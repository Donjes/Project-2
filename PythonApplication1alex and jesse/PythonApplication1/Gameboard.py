import pygame
import time
from Dice import *
import os
from Character import *
from Node import *
from Playerscreen import *

#======================================= Variable die vanuit player screen moeten komen

size = width, height = 700, 650
white = (255, 255, 255)
gloveSmall2 = "images/red_handschoen.png"
gloveSmall2move = "images/red_handschoen1.png"
gloveSmall1 = "images/blue_handschoen.png"
gloveSmall1move = "images/blue_handschoen1.png"
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


#=================================================== NAVIGATIE FUNCTIE! ===========================================================================#
def BoardScreen(firstround, chooseChars,roll,p,screenlist, rectlist, crashed, menu_index, screen_index,last_page,letsSuperFight,letsFight,nextturn,tempTile,newLocation,dice_rolled):   
    save_game = False
    load_old_game = False
    if firstround:
        chooseChars[0].savePosition = 0
        chooseChars[1].savePosition = 10
        chooseChars[2].savePosition = 20
        chooseChars[3].savePosition = 30
        firstround = False
    corner = [0,10,20,30]
    player = chooseChars[p%4]
    tile = player.savePosition
# =========================================== Navigatie van de handschoenen bij elke dice throw optie om kant te kiezen
    event = pygame.event.poll()         
    if event.type == pygame.KEYDOWN: 
        if event.key == pygame.K_SPACE and newLocation == False and dice_rolled == False: 
            Sounds.Dice()
            roll = Trow_dice() 
            for i in range(15):
                rolling = Trow_dice()
                dice_img(rolling) 
                small_glove("images/DiceRolling.png",(300,300)) 
                pygame.display.update()
                time.sleep(0.1)
                if i == 14:
                    dice_img(roll)
            time.sleep(0.5)
            pygame.display.update()
            time.sleep(0.5)      
            dice_rolled = True
        if event.key == pygame.K_UP and dice_rolled == True:
            for i in range(roll[0]):                   
                tile += 1 
                small_glove(smallGlovemove[p%4],navigate[tile%40])    
                Sounds.Tile()
                pygame.display.update()
                time.sleep(0.1)
                print("plus")  
            tempTile = tile
            newLocation = True
        if event.key == pygame.K_DOWN and dice_rolled == True:
            for i in range(roll[0]):                   
                tile -= 1 
                small_glove(smallGlovemove[p%4],navigate[tile%40])    
                Sounds.Tile()
                pygame.display.update()
                time.sleep(0.1)
                print("plus")  
            tempTile = tile
            newLocation = True
# =========================================== Navigatie van de handschoenen bij enter kies je je lokatie en worden alle variable returned
        if event.key == pygame.K_RETURN and tempTile != chooseChars[p%4].savePosition and newLocation == True:
            chooseChars[p%4].savePosition = tempTile
                
            prevPositie = chooseChars[p%4].savePosition%40
            if prevPositie == 0 or prevPositie == 10 or prevPositie == 20 or prevPositie == 30 and prevPositie is not corner[p%4]:
                print(corner[p%4])
                print(prevPositie)
                time.sleep(10)
                letsSuperFight = 1
            for i in range(4):
                print(chooseChars[p%4])
                if prevPositie == chooseChars[i].savePosition and not chooseChars[p%4] == chooseChars[i]:
                    letsFight = 1
            if letsSuperFight == 0 and letsFight == 0:
                nextturn = 1
            p += 1
            newLocation = False
            dice_rolled = False
        elif event.key == pygame.K_ESCAPE:
            crashed = True
        elif event.key == pygame.K_o:
            screen_index = 4
            last_page = 3
        elif event.key == pygame.K_TAB:
            screen_index = 2


    return firstround,chooseChars,roll,p,screenlist, rectlist, crashed, menu_index, screen_index,last_page,letsSuperFight,letsFight,nextturn,tempTile,newLocation,dice_rolled

#===================================================== FIGHT FUNCTIES! =============================================================================#
# 1v1 fight
def fight(tempChar,i,roller1,roller2,roller_reset,roller1_img,roller2_img):

        event = pygame.event.poll()      
        if event.type == pygame.KEYDOWN:       
            if event.key == pygame.K_SPACE:     
                roll = Trow_dice()
                roller1_img = roll[1]
                roller1 = True
                #
                # hier komt de logica van hoeveel dmg1
                #
            if event.key == pygame.K_RETURN:   
                roll2 = Trow_dice()
                roller2_img = roll2[1]
                roller2 = True
                #
                # hier komt de logica van hoeveel dmg2
                #
        if roller1 and roller2:    
            #
            # hier komt de logica wie dmg doet aan wie en hoeveel conditie het kost (alle visuele cijfers worden in Game.py getekend
            #          
            roller_reset = True
            return roller1,roller2,roller_reset,roller1_img,roller2_img
        else:         
            return roller1,roller2,roller_reset,roller1_img,roller2_img    
        
# Corner fight
def superFight(tempChar,i,roller1,roller2,roller_reset,roller1_img,roller2_img):

        event = pygame.event.poll()      
        if event.type == pygame.KEYDOWN:       
            if event.key == pygame.K_SPACE:     
                roll = Trow_dice()                      
                roller1_img = roll[1]
                roller1 = True
                #
                # hier komt de logica van hoeveel dmg1
                #
            if event.key == pygame.K_RETURN:   
                roll2 = Trow_dice()
                roller2_img = roll2[1]
                roller2 = True
                #
                # hier komt de logica van hoeveel dmg2
                #
        if roller1 and roller2:   
            #
            # hier komt de zelfde logica als bij superfight (alle visuele cijfers worden in Game.py getekend)
            #                 
            roller_reset = True
            return roller1,roller2,roller_reset,roller1_img,roller2_img
        else:               
            return roller1,roller2,roller_reset,roller1_img,roller2_img     