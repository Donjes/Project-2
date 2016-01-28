import pygame
import time
from Dice import *
import os
from character import *
from Node import *
playerList = Empty
player1 = TerryCrews
player2 = JasonStatham
player3 = WesleySniper
player4 = JetRi
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
gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption('Survivor')
clock = pygame.time.Clock()
roll = Trow_dice()
board_screen = pygame.image.load("images/speelveld.png")
board_screen_rect = board_screen.get_rect()
def small_glove(gloveSmall,navi):                  #3Ruben handschoen over board functie    
        gameDisplay.blit(pygame.image.load(gloveSmall),navi)
def dice_img(roll):
        gameDisplay.blit(pygame.image.load("images/" + roll[1]),(300,300))

navigate = [(20,20),(80,20),(130,20),(180,20),(230,20),(300,20),(375,20),(425,20),(472,20),(520,20),(575,20),(575,85),(575,130),(575,180),(575,230),(575,300),(575,373),(575,425),(575,475),(575,525),(575,590),(520,590),(472,590),(425,590),(375,590),(300,590),(230,590),(180,590),(130,590),(80,590),(20,590),(20,525),(20,475),(20,425),(20,373),(20,300),(20,230),(20,180),(20,130),(20,85)]

playerList = [player1,player2,player3,player4]
p = 0
player1Loc = 11
player2Loc = 0
player3Loc = 21
player4Loc = 32
#gameboard
def BoardScreen(roll,player1Loc,player2Loc,player3Loc,player4Loc,p,screenlist, rectlist, crashed, menu_index, screen_index):   
    navi1 = (575,20)
    navi2 = (20,20)
    navi3 = (575,590)
    navi4 = (20,590)
    player = playerList[p]
    if player == player1: #player 1 navigation
        tile1 = player1Loc
        for event in pygame.event.get():         
            if event.type == pygame.KEYDOWN:         
                if event.key == pygame.K_SPACE: 
                    roll = Trow_dice() 
                    for i in range(roll[0]):
                        tile1 += 1 
                        navi1 = navigate[tile1%40]
                        small_glove(gloveSmall1move,navi1)    
                        pygame.display.update()
                        time.sleep(0.1)
                        print("plus")  
                    player1Loc = tile1
                    p = 1

    if player == player2: #player 2 navigation
        tile2 = player2Loc
        for event in pygame.event.get():         
            if event.type == pygame.KEYDOWN:         
                if event.key == pygame.K_SPACE: 
                    roll = Trow_dice() 
                    for i in range(roll[0]):
                        tile2 += 1 
                        navi2 = navigate[tile2%40]
                        small_glove(gloveSmall2move,navi2)    
                        pygame.display.update()
                        time.sleep(0.1)
                        print("plus")    
                    player2Loc = tile2                               
                    p = 2

    if player == player3: #player 3 navigation
        tile3 = player3Loc
        for event in pygame.event.get():         
            if event.type == pygame.KEYDOWN:         
                if event.key == pygame.K_SPACE: 
                    roll = Trow_dice() 
                    for i in range(roll[0]):
                        tile3 += 1 
                        navi3 = navigate[tile3%40]
                        small_glove(gloveSmall3move,navi3)    
                        pygame.display.update()
                        time.sleep(0.1)
                        print("plus")    
                    player3Loc = tile3                               
                    p = 3

    if player == player4: #player 4 navigation
        tile4 = player4Loc
        for event in pygame.event.get():         
            if event.type == pygame.KEYDOWN:         
                if event.key == pygame.K_SPACE: 
                    roll = Trow_dice() 
                    for i in range(roll[0]):
                        tile4 += 1 
                        navi4 = navigate[tile4%40]
                        small_glove(gloveSmall4move,navi4)    
                        pygame.display.update()
                        time.sleep(0.1)
                        print("plus")    
                    player4Loc = tile4                               
                    p = 0
       
    gameDisplay.blit(pygame.image.load("images/speelveld.png"),board_screen.get_rect()) 
    small_glove(gloveSmall1,navi1)
    small_glove(gloveSmall2,navi2)
    small_glove(gloveSmall3,navi3)
    small_glove(gloveSmall4,navi4)
    dice_img(roll)
    pygame.display.update()
    clock.tick(60)
    return player1Loc,player2Loc,player3Loc,player4Loc,screenlist, rectlist, crashed, menu_index, screen_index