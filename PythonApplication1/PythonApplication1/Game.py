﻿import pygame
import time
#from Node import *

pygame.init()

size = width, height = 700, 650
tile = 0
white = (255, 255, 255)

gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption('Survivor')
clock = pygame.time.Clock()

startup_screen = pygame.image.load("images/startscherm2.png")
startup_screen_rect = startup_screen.get_rect()                 #start at top left
rules_screen = pygame.image.load("images/rules.png")
rules_screen_rect = startup_screen.get_rect()
character_screen = pygame.image.load("images/playermenu.png")
character_screen_rect = character_screen.get_rect()
gloveImg = pygame.image.load("images/handschoen.png")
punch_sound = pygame.mixer.music.load("sounds/punch_sound.mp3")
# gloveSmall = pygame.image.load("images/red_handschoen.png")


screenlist = [startup_screen, rules_screen, character_screen]
m = 0


s_rect = startup_screen_rect
r_rect = rules_screen_rect
p_rect = character_screen_rect
rectlist = [s_rect, r_rect, p_rect]

remove = x, y = -100, - 100
start = x, y = 70, 150 #coordinates glove --> start
rules = x, y = 70, 250 #coordinates glove --> rules
exit = x, y = 350, 520 #coordinates glove --> exit
navi = (-100,-100) #1Ruben speler kleine handschoen word buiten beeld neer gezet

crashed = False

menulist = [start, rules, exit] #lijst van de buttons
i = 0                           #startwaarde = start
            #index van de lijst
            
#koffie logo bij het opstarten van het spel
#def Koffielogo():
#    size = width, height = 650, 650
#    gameDisplay = pygame.display.set_mode(size)
    
#    for i in range (9):
#        gameDisplay.blit(pygame.image.load("Koffielogo/Koffie"+ str(i) +".png"),(pygame.image.load("Koffielogo/Koffie"+ str(i) +".png").get_rect()))  
#        pygame.display.update()
#        if i == 0:
#            time.sleep(1)
#        elif i == 6:
#            Sounds.Introping()
#        time.sleep(0.08)
#    time.sleep(2)
    
#Koffielogo()

def glove_update(button,m):                   #geeft handschoen.png weer
    if m == 0:           #standard vector
        gameDisplay.blit(gloveImg,(button))

# def small_glove(navi):                  #3Ruben handschoen over board functie
#     gameDisplay.blit(gloveSmall,navi)

def screen_update(screen,rect):
    gameDisplay.blit(screen,(rect))

def sound_play(punch_sound):
    pygame.mixer.music.play(0)

def StartScreen(screenlist,rectlist,menulist,m,i,crashed,punch_sound):
    rect = rectlist[m]
    screen = screenlist[m]
    button = menulist[i]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True                  #programma sluit af met rode X

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sound_play(punch_sound)
        if m == 0:      #start
            screen = screenlist[m]
            rect = rectlist[m]
            if event.type == pygame.KEYDOWN:    #als er een key wordt ingedrukt
                if event.key == pygame.K_DOWN:  #key = down arrow
                    i += 1                      #index + 1
                    if i > 2:
                        i = 0                   #na exit button = start
                    button = menulist[i]        #button wordt plaats van de index
                if event.key == pygame.K_UP:    #key = up arrow
                    i -= 1                      #index - 1
                    if i < 0:
                        i = 2                   #na start button = exit
                    button = menulist[i]
                if event.key == pygame.K_SPACE and i == 2:
                    crashed = True
                if i == 1 and event.key == pygame.K_SPACE:
                    m = 1
                if i == 0 and event.key == pygame.K_SPACE:
                    m = 2

        if m == 1:   #rules
            size = width, height = 700, 650
            gameDisplay = pygame.display.set_mode(size)
            screen = screenlist[m]
            rect = rectlist[m]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    m = 0
                    button = menulist[1]
        if m == 2:   #rules
            size = width, height = 700, 750
            gameDisplay = pygame.display.set_mode(size)
            screen = screenlist[m]
            rect = rectlist[m]

    return screen,rect,button,m,i, crashed

while not crashed:

    gameDisplay.fill(white)  #startscherm.png linksboven weergegeven
    screen,rect,button,m,i, crashed= StartScreen(screenlist,rectlist,menulist,m,i,crashed,punch_sound)
    screen_update(screen, rect)
    glove_update(button,m)                                   #hier word button meegegeven aan glove_update

    # small_glove(navi)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
