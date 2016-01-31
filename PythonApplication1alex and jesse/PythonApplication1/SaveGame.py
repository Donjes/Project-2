import pygame
import pickle #pythons save file dingetje

def saveGame(firstround,chooseChars,roll,p,screenlist, rectlist, crashed, menu_index, screen_index):
        saveAll = [] #we creeren een list met alle belangrijke variable
        saveAll.append(firstround)
        saveAll.append(chooseChars)
        saveAll.append(roll)
        saveAll.append(p)
        saveAll.append(screenlist)
        saveAll.append(rectlist)
        saveAll.append(crashed)
        saveAll.append(menu_index)
        saveAll.append(screen_index)
        saveFile = open('savedgame.txt', 'wb')#make een file
        pickle.dump(saveAll, saveFile) #slaan de list op in gemaakte file
        saveFile.close()#sluiten file

def loadGame():
        loadFile = open('savedgame.txt','rb') #openen file
        loadAll = pickle.load(loadFile) #laden de list uit de file
        firstround,chooseChars,roll,p,screenlist, rectlist, crashed, menu_index, screen_index = loadAll #halen variable uit de list
        return firstround,chooseChars,roll,p,screenlist, rectlist, crashed, menu_index, screen_index 
