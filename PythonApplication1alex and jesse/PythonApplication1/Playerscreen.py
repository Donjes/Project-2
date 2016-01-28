#from Game import *
import pygame
from character import *

def sound_play(punch_sound):
    pygame.mixer.music.play(0)

def PlayerScreen(screenlist, rectlist,crashed, menu_index, screen_index,character_index,punch_sound):
    start = x, y = 0, 650
    rules = x, y = 225, 650
    exit = x, y = 450, 650

    Jet = x,y = 450, 145
    Mario = x,y = 450, 235
    Chack = x,y = 450, 325
    Jackie = x,y = 450, 415
    Jason = x,y = 560, 145
    Steven = x,y = 560, 235
    Wesley = x,y = 560, 325
    Terry = x,y = 560, 415
    characterlist = [ Jet, Mario, Chack,  Jackie,  Jason, Steven, Wesley, Terry]

    char_button = characterlist[character_index]
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
            if menu_index == 0 and event.key == pygame.K_SPACE:
                screen_index = 3

            if event.key == pygame.K_DOWN:
                character_index += 1
                if character_index > 7:
                    character_index = 0
            if event.key == pygame.K_UP:
                character_index -= 1
                if character_index < 0:
                    character_index = 7

            for i in range(0,4):
                if event.key == pygame.K_RETURN and char_button == characterlist[0]:
                    name = characterlist[i]
                    JetRi = Player(name,"images/JetRi.png",10,30,12,25,10,23)
                    cnt += 1
                if event.key == pygame.K_RETURN and char_button == characterlist[1]:
                    name = characterlist[i]
                    SuperMario = Player(name,"images/SuperMario.png",10,10,30,30,15,15))
                    cnt += 1
                if event.key == pygame.K_RETURN and char_button == characterlist[2]:
                    name = characterlist[i]
                    ChackNorris = Player(name,"images/ChackNorris.png",10,26,25,24,24,1)
                    cnt += 1
                if event.key == pygame.K_RETURN and char_button == characterlist[3]:
                    name = characterlist[i]
                    JackieChan = Player(name,"images/JackieChan.png",20,25,5,25,20,15)
                    cnt += 1
                if event.key == pygame.K_RETURN and char_button == characterlist[4]:
                    name = characterlist[i]
                    JasonStatham = Player(name,"images/JasonStatham.png",10,11,19,21,23,26)
                    cnt += 1
                if event.key == pygame.K_RETURN and char_button == characterlist[5]:
                    name = characterlist[i]
                    StevenSeagal = Player(name,"images/StevenSeagal.png",27,15,12,11,25,20)
                    cnt += 1
                if event.key == pygame.K_RETURN and char_button == characterlist[6]:
                    name = characterlist[i]
                    WesleySniper = Player(name,"images/WesleySniper.png",30,14,14,20,18,14)
                    cnt += 1
                if event.key == pygame.K_RETURN and char_button == characterlist[7]:
                    name = characterlist[i]
                    TerryCrews = Player(name,"images/TerryCrews.png",10,15,25,30,20,10)
                    cnt += 1



    b = 2

    size = width, height = 750, 780
    gameDisplay = pygame.display.set_mode(size)

    return screen, rect, crashed, button, menu_index, screen_index, b, char_button, character_index