import pygame
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
rules_screen = pygame.image.load("images/rules.png")
character_screen = pygame.image.load("images/playermenu.png")
punch_sound = pygame.mixer.music.load("sounds/punch_sound.mp3")
big_glove = pygame.image.load("images/handschoen.png")
red_glove = pygame.image.load("images/red_handschoen.png")
green_glove = pygame.image.load("images/green_handschoen.png")
yellow_glove = pygame.image.load("images/yellow_handschoen.png")
blue_glove = pygame.image.load("images/blue_handschoen.png")

startup_screen_rect = startup_screen.get_rect()                 #start at top left
rules_screen_rect = startup_screen.get_rect()
character_screen_rect = character_screen.get_rect()

screenlist = [startup_screen, rules_screen, character_screen]
screen_index = 0

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


menu_index = 0                           #startwaarde = start
            #index van de lijst


def glove_update(button, screen_index):                   #geeft handschoen.png weer
    if screen_index == 0:           #standard vector
        gameDisplay.blit(big_glove,(button))
    elif screen_index == 2:
        gameDisplay.blit(big_glove,(button))

# def small_glove(navi):                  #3Ruben handschoen over board functie
#     gameDisplay.blit(gloveSmall,navi)

def screen_update(screen,rect):
    gameDisplay.blit(screen,(rect))

def sound_play(punch_sound):
    pygame.mixer.music.play(0)

def StartScreen(screenlist, rectlist, screen_index, menu_index, crashed, punch_sound):

    start = x, y = 70, 150 #coordinates glove --> start
    rules = x, y = 70, 250 #coordinates glove --> rules
    exit = x, y = 350, 520 #coordinates glove --> exit
    menulist = [start, rules, exit] #lijst van de buttons
    rect = rectlist[screen_index]
    screen = screenlist[screen_index]
    button = menulist[menu_index]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True                  #programma sluit af met rode X

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sound_play(punch_sound)
        if screen_index == 0:      #start
            screen = screenlist[screen_index]
            rect = rectlist[screen_index]
            if event.type == pygame.KEYDOWN:    #als er een key wordt ingedrukt
                if event.key == pygame.K_DOWN:  #key = down arrow
                    menu_index += 1                      #index + 1
                    if menu_index > 2:
                        menu_index = 0                   #na exit button = start

                if event.key == pygame.K_UP:    #key = up arrow
                    menu_index -= 1                      #index - 1
                    if menu_index < 0:
                        menu_index = 2                   #na start button = exit
                
                if menu_index == 2 and event.key == pygame.K_SPACE:
                    crashed = True
                if menu_index == 1 and event.key == pygame.K_SPACE:
                    screen_index = 1
                if menu_index == 0 and event.key == pygame.K_SPACE:
                    screen_index = 2
    b = 0
    return screen, rect, button, screen_index, menu_index, crashed,b

def RulesScreen(screenlist, rectlist, screen_index, menu_index, crashed, b):#b = ref van backspace screen
        
    rect = rectlist[screen_index]
    screen = screenlist[screen_index]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if b == 0:
            remove = x, y = -100, - 100
            start = x, y = 70, 150 #coordinates glove --> start
            rules = x, y = 70, 250 #coordinates glove --> rules
            exit = x, y = 350, 520
            menulist = [start, rules, exit]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    screen_index = 0
                    button = menulist[1]     
        if b == 2:   #rules
            start = x, y = 0, 650
            rules = x, y = 225, 650
            exit = x, y = 450, 650
            menulist = [start, rules, exit]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    screen_index = 2
                    button = menulist[1]
    return screen, rect, screen_index, menu_index, crashed
        
def PlayerScreen(screenlist, rectlist,crashed, menu_index, screen_index):
    start = x, y = 0, 650
    rules = x, y = 225, 650
    exit = x, y = 450, 650
    menulist = [start, rules, exit] #lijst van de buttons
    button = menulist[menu_index]
    rect = rectlist[screen_index]
    screen = screenlist[screen_index]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True                  #programma sluit af met rode X

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sound_play(punch_sound)
            if event.key == pygame.K_RIGHT:
                menu_index += 1
                if menu_index > 2:
                    menu_index = 0
            if event.key == pygame.K_LEFT:
                menu_index -= 1
                if menu_index < 0:
                    menu_index = 2
            if menu_index == 2 and event.key == pygame.K_SPACE:
                crashed = True
            if menu_index == 1 and event.key == pygame.K_SPACE:
                screen_index = 1
            #if menu_index == 0 and event.key == pygame.K_SPACE:
                #screen_index == 0
    b = 2

    size = width, height = 750, 780
    gameDisplay = pygame.display.set_mode(size)

    return screen, rect, crashed, button, menu_index, screen_index, b


while not crashed:
    gameDisplay.fill(white)  #startscherm.png linksboven weergegeven
    if screen_index == 0:
        screen, rect, button, screen_index, menu_index, crashed, b = \
        StartScreen(screenlist, rectlist, screen_index, menu_index, crashed, punch_sound)
        screen_update(screen, rect)
        glove_update(button, screen_index)                         #hier word button meegegeven aan glove_update
    elif screen_index == 1:
        screen, rect,screen_index, menu_index, crashed = \
        RulesScreen(screenlist, rectlist, screen_index, menu_index, crashed, b)
        screen_update(screen, rect)
        glove_update(button, screen_index)
    elif screen_index == 2:
        screen, rect ,crashed, button, menu_index, screen_index, b = \
        PlayerScreen(screenlist, rectlist, crashed, menu_index, screen_index)
        screen_update(screen, rect)
        glove_update(button, screen_index)
    # small_glove(navi)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()