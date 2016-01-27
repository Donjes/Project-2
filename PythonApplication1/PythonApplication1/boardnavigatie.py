import pygame
import time
from Dice import *
import os
from character import *
from Node import *

pygame.init()
playerList = Empty
player1 = TerryCrews
player2 = JasonStatham
size = width, height = 700, 650
tile = 0
white = (255, 255, 255)
navi = (-100,-100)
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

playerList = Node(player1,Node(player2,Empty))

while True:
        player = playerList.Value
        navigate = [(20,20),(80,20),(130,20),(180,20),(230,20),(300,20),(375,20),(425,20),(472,20),(520,20),(575,20),(575,85),(575,130),(575,180),(575,230),(575,300),(575,373),(575,425),(575,475),(575,525),(575,590)]
        if player == player1:
            gloveSmall = "images/red_handschoen.png"
            for event in pygame.event.get():         
                if event.type == pygame.KEYDOWN:         
                    if event.key == pygame.K_SPACE: 
                        roll = Trow_dice() 
                        for i in range(roll[0]):
                            tile += 1 
                            navi = navigate[tile%21]
                            small_glove(gloveSmall,navi)    
                            pygame.display.update()
                            time.sleep(0.1)
                            print("plus")  
                        player.Position = navi
                        playerList = playerList.Tail
        if player == player2:
            gloveSmall = "images/blue_handschoen.png"
            for event in pygame.event.get():         
                if event.type == pygame.KEYDOWN:         
                    if event.key == pygame.K_SPACE: 
                        roll = Trow_dice() 
                        for i in range(roll[0]):
                            tile += 1 
                            navi = navigate[tile%21]
                            small_glove(gloveSmall,navi)    
                            pygame.display.update()
                            time.sleep(0.1)
                            print("plus")    
                        player.Position = navi                                
                        playerList = playerList.Tail
        print(navi)

        gameDisplay.blit(pygame.image.load("images/speelveld.png"),board_screen.get_rect()) 
        small_glove(gloveSmall,navi)
        dice_img(roll)
        pygame.display.update()
        clock.tick(60)

pygame.quit()
quit()