import pygame
from Playerscreen import *
pygame.mixer.init()

def Mute():
    pygame.mixer.music.pause()
    punchsound.set_volume(0)
    dicesound.set_volume(0)
    introping.set_volume(0)
    mariosound.set_volume(0)
    tapsound.set_volume(0)
    tilesound.set_volume(0)
def Unmute():
    pygame.mixer.music.unpause()
    punchsound.set_volume(1)
    dicesound.set_volume(1)
    introping.set_volume(1)
    mariosound.set_volume(1)
    tapsound.set_volume(1)
    tilesound.set_volume(1)

def Options(screenlist, rectlist,crashed, menu_index, screen_index,character_index,b,save_game,load_old_game,last_page):


    resume = x, y = 25, 110 #coordinates glove --> resume
    save = x, y = 25, 220 #coordinates glove --> save
    load = x, y = 25, 335 #coordinates glove --> load
    rules = x, y = 25, 455 #coordinates glove --> rules
    exit = x, y = 350, 650 #coordinates glove --> exit
    menulist = [resume, save, load, rules, exit] #lijst van de buttons
    rect = rectlist[screen_index]
    screen = screenlist[screen_index]
    button = menulist[menu_index%5]
    size = width, height = 650, 746
    gameDisplay = pygame.display.set_mode(size)

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            crashed = True                  #programma sluit af met rode X

        if event.type == pygame.KEYDOWN:
            count = 0
            if event.key == pygame.K_SPACE:
                Sounds.Punch()
            if event.key == pygame.K_UP:
                Sounds.Tapsound()
                menu_index -= 1

            if event.key == pygame.K_DOWN:
                Sounds.Tapsound()
                menu_index += 1

            if menu_index == 0 and event.key == pygame.K_SPACE:
                Sounds.Punch()
                if last_page == 0:
                    screen_index = 0
                if last_page == 2:
                    screen_index = 2
                if last_page == 3:
                    screen_index = 3
            if menu_index == 1 and event.key == pygame.K_SPACE:
                Sounds.Punch()
                screen_index = 5
                save_game = True
            if menu_index == 2 and event.key == pygame.K_SPACE:
                Sounds.Punch()
                screen_index = 5
                load_old_game = True
            if menu_index == 3 and event.key == pygame.K_SPACE:
                Sounds.Punch()
                screen_index = 1
            if menu_index == 4 and event.key == pygame.K_SPACE:
                Sounds.Punch()
                crashed = True
            if event.key == pygame.K_m:
                    Mute()
            if event.key == pygame.K_u:
                    Unmute()








                

    b = 3
    return screen, rect, crashed, button, menu_index, screen_index, b,save_game,load_old_game,last_page

def RulesScreen(screenlist, rectlist, screen_index, menu_index, crashed, b):#b = ref van backspace screen
        
    rect = rectlist[screen_index]
    screen = screenlist[screen_index]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if b == 0:
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
        if b == 3:   #rules
            start = x, y = 0, 650
            rules = x, y = 225, 650
            exit = x, y = 450, 650
            menulist = [start, rules, exit]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    screen_index = 4
                    button = menulist[1]
    return screen, rect, screen_index, menu_index, crashed