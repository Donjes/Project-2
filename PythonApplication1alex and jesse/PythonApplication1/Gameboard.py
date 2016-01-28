import pygame
import time
from Dice import *
import os
#from Character import *
from Node import *
class Player:
    def __init__(self,name,texture,attack1,attack2,attack3,attack4,attack5,attack6):
        self.playername = name

        self.texture = texture
        self.hitPoints = 100 #  change the hitpoints and conditionpoints !!!
        self.conditionPoints = 15
        self.savePosition = None #Optional for a saving option
        self.dice1 = attack1
        self.dice2 = attack2
        self.dice3 = attack3
        self.dice4 = attack4
        self.dice5 = attack5
        self.dice6 = attack6

TerryCrews = Player("name","images/TerryCrews.png",10,15,25,30,20,10)
JasonStatham = Player("name","images/JasonStatham.png",10,11,19,21,23,26)
WesleySniper = Player("name","images/WesleySniper.png",30,14,14,20,18,14)
JetRi = Player("name","images/JetRi.png",10,30,12,25,10,23)
StevenSeagal = Player("name","images/StevenSeagal.png",27,15,12,11,25,20)
SuperMario = Player("name","images/SuperMario.png",10,10,30,30,15,15)
JackieChan = Player("name","images/JackieChan.png",20,25,5,25,20,15)
ChackNorris = Player("name","images/ChackNorris.png",10,26,25,24,24,1)

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

def small_glove(gloveSmall,navilist):                  #3Ruben handschoen over board functie    
        gameDisplay.blit(pygame.image.load(gloveSmall),navilist)
def dice_img(roll):
        gameDisplay.blit(pygame.image.load("images/" + roll[1]),(300,300))

navigate = [(20,20),(80,20),(130,20),(180,20),(230,20),(300,20),(375,20),(425,20),(472,20),(520,20),(575,20),(575,85),(575,130),(575,180),(575,230),(575,300),(575,373),(575,425),(575,475),(575,525),(575,590),(520,590),(472,590),(425,590),(375,590),(300,590),(230,590),(180,590),(130,590),(80,590),(20,590),(20,525),(20,475),(20,425),(20,373),(20,300),(20,230),(20,180),(20,130),(20,85)]

playerList = [player1,player2,player3,player4]
p = 0

#gameboard
def BoardScreen(navi,roll,playerList,p,screenlist, rectlist, crashed, menu_index, screen_index):   

    player = playerList[p]
    if player == player1: #player 1 navigation
        tile1 = player1.savePosition
        for event in pygame.event.get():         
            if event.type == pygame.KEYDOWN:         
                if event.key == pygame.K_SPACE: 
                    roll = Trow_dice() 
                    for i in range(roll[0]):
                        tile1 += 1 
                        navi[0] = navigate[tile1%40]
                        small_glove(gloveSmall1move,navi[0])    
                        pygame.display.update()
                        #time.sleep(0.1)
                        print("plus")  
                    player1.savePosition = tile1
                    p = 1

    if player == player2: #player 2 navigation
        tile2 = player2.savePosition
        for event in pygame.event.get():         
            if event.type == pygame.KEYDOWN:         
                if event.key == pygame.K_SPACE: 
                    roll = Trow_dice() 
                    for i in range(roll[0]):
                        tile2 += 1 
                        navi[1] = navigate[tile2%40]
                        small_glove(gloveSmall2move,navi[1])    
                        pygame.display.update()
                        time.sleep(0.1)
                        print("plus")    
                    player2.savePosition = tile2                               
                    p = 2

    if player == player3: #player 3 navigation
        tile3 = player3.savePosition
        for event in pygame.event.get():         
            if event.type == pygame.KEYDOWN:         
                if event.key == pygame.K_SPACE: 
                    roll = Trow_dice() 
                    for i in range(roll[0]):
                        tile3 += 1 
                        navi[2] = navigate[tile3%40]
                        small_glove(gloveSmall3move,navi[2])    
                        pygame.display.update()
                        time.sleep(0.1)
                        print("plus")    
                    player3.savePosition = tile3                               
                    p = 3

    if player == player4: #player 4 navigation
        tile4 = player4.savePosition
        for event in pygame.event.get():         
            if event.type == pygame.KEYDOWN:         
                if event.key == pygame.K_SPACE: 
                    roll = Trow_dice() 
                    for i in range(roll[0]):
                        tile4 += 1 
                        navi[3] = navigate[tile4%40]
                        small_glove(gloveSmall4move,navi[3])    
                        pygame.display.update()
                        time.sleep(0.1)
                        print("plus")    
                    player4.savePosition = tile4                               
                    p = 0
    size = width, height = 650, 746
    gameDisplay = pygame.display.set_mode(size)
    gameDisplay.blit(pygame.image.load("images/speelveld.png"),(pygame.image.load("images/speelveld.png").get_rect()))
    small_glove(gloveSmall1,navi[0])
    small_glove(gloveSmall2,navi[1])
    small_glove(gloveSmall3,navi[2])
    small_glove(gloveSmall4,navi[3])
    dice_img(roll)
    #pygame.display.update()

    return navi,p,playerList,screenlist, rectlist, crashed, menu_index, screen_index