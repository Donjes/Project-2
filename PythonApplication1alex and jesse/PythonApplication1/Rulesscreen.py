import pygame

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
    return screen, rect, screen_index, menu_index, crashed